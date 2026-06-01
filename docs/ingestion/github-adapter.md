# GitHub MCP Adapter — Implementation Guide

## What We Built

We built the code that connects OCR to GitHub. It runs the official `github-mcp-server`
Go program as a child process, talks to it over stdin/stdout, and turns commits into
structured data that OCR can use.

The code lives in `ingestion/github/` and has three files:

```
ingestion/github/
├── client.py       # Low-level connection to the Go program
├── adapter.py      # High-level API: "give me the latest commits"
├── types.py        # Data containers: commit, author, event
└── __init__.py     # Exports the public API
```

---

## How It Works (Simple Version)

```
Your Code on GitHub
        │
        ▼
github-mcp-server (Go program)
   │  Reads commits from GitHub API
   │  Speaks MCP protocol over stdio
        ▼
client.py (persistent connection)
   │  Keeps one connection alive for many calls
        ▼
adapter.py (friendly API)
   │  get_latest_commits(5) → list of commits
   │  get_commit("abc123") → one commit
   │  poll() → keep watching for new stuff
        ▼
types.py (clean data)
   │  GitHubEvent → to_shipment() → OCR-ready dict
```

## How It Works (Technical)

### client.py — The Transport Layer

This is the low-level part. It:

1. Finds your GitHub token (checks env var `GITHUB_PERSONAL_ACCESS_TOKEN`, then `GITHUB_TOKEN`, then runs `gh auth token`)
2. Starts the `github-mcp-server` Go binary as a subprocess
3. Opens an MCP session (JSON-RPC over stdin/stdout)
4. Keeps the session alive until you're done

**Key class: `GitHubMCPClient`**

```python
async with GitHubMCPClient() as client:
    tools = await client.list_tools()
    commits = await client.call_tool("get_commit", {...})
```

- **Enter**: starts the Go binary, opens session
- **Exit**: closes session, kills the binary
- **Persistent**: one session handles many calls (see "The Fix" below)

### adapter.py — The High-Level API

Builds on client.py. You give it a repo name and ask for commits:

```python
adapter = GitHubAdapter("wellnessshabz-dev/ocr")
events = await adapter.get_latest_commits(5)
for e in events:
    print(e.payload.message)          # the commit message
    print(e.payload.author.name)      # who wrote it
    print(e.payload.stats)            # +45 -12 = 57 changes
    print(e.payload.files)            # list of files changed
```

**Methods:**

| Method | What it does | When to use |
|--------|-------------|-------------|
| `get_latest_commits(n)` | Gets the last `n` commits with full diffs | Initial sync, periodic polling |
| `get_commit(sha)` | Gets one commit by its SHA | On-demand lookups |
| `check_connection()` | Tests if the Go binary and token work | Startup health check |
| `get_me()` | Returns your GitHub profile | Identifying the watcher |
| `poll(interval, on_event)` | Watches for new commits forever | Production: set it and forget it |

### types.py — The Data Model

Three data containers:

```python
@dataclass
class GitHubAuthor:
    name: str          # "Jane Doe"
    email: str         # "jane@example.com"
    username: str      # "janedoe"

@dataclass
class GitHubCommit:
    sha: str           # "abc123def456"
    message: str       # "Fix login timeout bug"
    author: GitHubAuthor
    date: datetime
    stats: dict        # {"additions": 45, "deletions": 12, "total": 57}
    files: list[dict]  # [{"filename": "src/auth.ts", "status": "modified", "patch": "@@ -42..."}]

@dataclass
class GitHubEvent:
    event_type: str    # "commit"
    repo: str          # "owner/repo"
    payload: GitHubCommit
    raw: dict          # original response from GitHub MCP
```

The `to_shipment()` method converts an event into the format OCR needs:

```python
{
    "type": "commit",
    "repo": "wellnessshabz-dev/ocr",
    "trajectory": {
        "sha": "abc123",
        "message": "Fix login timeout bug",
        "author": "Jane Doe <jane@example.com>",
        "date": "2026-06-01T12:00:00Z",
        "stats": {"additions": 45, "deletions": 12, "total": 57}
    },
    "entities": ["src/auth.ts", "Jane Doe"],
    "evidence": {"files": [...], "diff": "..."}
}
```

---

## The One-Big-Problem We Fixed

### Before: 31 Connections for 30 Commits

When you asked for "the latest 30 commits", the original code did this:

```
Connection 1:  "list me the latest 30 commits"    → gets a list with 30 SHAs
Connection 2:  "give me details on commit #1"      → gets details
Connection 3:  "give me details on commit #2"      → gets details
...
Connection 31: "give me details on commit #30"     → gets details
```

Every connection starts the Go binary, initializes the session, makes one call, and shuts down. For 30 commits: **31 connections**. Slow, wasteful, unnecessary.

### After: 1 Connection for 30 Commits

Now it does:

```
One Connection:
    "list me the latest 30 commits"
    "give me details on commit #1"
    "give me details on commit #2"
    ...
    "give me details on commit #30"
    (close connection)
```

**1 connection, 31 calls inside it.** Much faster.

### What Changed

The old code had a function `call_tool()` that opened a new session every single time:

```python
# Old: one connection per call
async def call_tool(name, args):
    async with open_session() as session:
        return await session.call_tool(name, args)

# To get 30 commits:
for sha in shas:          # Loop opens 30 connections
    detail = await call_tool("get_commit", {"sha": sha})
```

The new code has `GitHubMCPClient` that keeps the session alive:

```python
# New: one connection for many calls
async with GitHubMCPClient() as client:
    for sha in shas:      # Same session for all 30
        detail = await client.call_tool("get_commit", {"sha": sha})
```

### Why the Fix Was Tricky

The `github-mcp-server` Go program communicates over stdin/stdout using
the MCP protocol. The MCP library uses async generators internally.
Opening/closing them directly with `__aenter__()` caused a bug where
cleanup ran in the wrong task (Python error: "Attempted to exit cancel
scope in a different task").

The fix uses `AsyncExitStack` — a Python standard library tool that
properly manages nested async contexts:

```python
async def __aenter__(self):
    self._stack = AsyncExitStack()
    read, write = await self._stack.enter_async_context(stdio_client(params))
    self._session = await self._stack.enter_async_context(ClientSession(read, write))
    await self._session.initialize()
    return self

async def __aexit__(self, *args):
    await self._stack.__aexit__(*args)  # cleans up everything in reverse order
```

---

## Current Status

| Aspect | Status |
|--------|--------|
| Connection to GitHub | ✅ Working (tested against `github/github-mcp-server` and `wellnessshabz-dev/ocr`) |
| Fetch commits | ✅ Working — returns full diff, author, stats, files |
| Persistent sessions | ✅ Working — 1 session per batch |
| Single commit fetch | ✅ Working |
| Connection check | ✅ Working |
| Poll loop | ✅ Written, not tested in production (no webhook trigger yet) |
| Error handling | ⚠️ Basic — retries and reconnection not built yet |
| Rate limiting | ⚠️ Not handled — assumes GitHub token has sufficient quota |
| Write operations | ❌ Blocked by design — OCR is read-only |

---

## Configuration

| Setting | How to set | Default |
|---------|-----------|---------|
| GitHub token | `GITHUB_PERSONAL_ACCESS_TOKEN` env var, or `gh auth login` | Auto-detect via `gh auth token` |
| Go binary path | `GITHUB_MCP_SERVER_PATH` env var | `~/go/bin/github-mcp-server` |
| Toolsets | `GitHubMCPClient(toolsets="...")` | `repos,context` |

---

## Requirements

- Go binary installed: `go install github.com/github/github-mcp-server/cmd/github-mcp-server@latest`
- `gh auth login` or `GITHUB_PERSONAL_ACCESS_TOKEN` env var
- Python 3.10+ (uses `mcp` SDK)
- Binary at `~/go/bin/github-mcp-server` (or set `GITHUB_MCP_SERVER_PATH`)

---

## Testing

```bash
# Quick test
/opt/homebrew/bin/python3.11 -c "
import asyncio
from ingestion.github import GitHubAdapter

async def main():
    adapter = GitHubAdapter('wellnessshabz-dev/ocr')
    events = await adapter.get_latest_commits(3)
    for e in events:
        print(e.payload.sha[:8], e.payload.message[:60])

asyncio.run(main())
"
```

---

## Related Docs

- [`github-mcp.md`](github-mcp.md) — What GitHub MCP is and how OCR uses it (not how we built it)
- `ingestion/github/_index.md` — Contract and blast radius for this directory
- `docs/build/v1_plan.md` — Where this fits in the OCR build plan
