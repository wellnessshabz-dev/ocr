---
title: "GitHub — GitHub MCP Integration"
description: "GitHub MCP adapter that watches repos and emits shipment-ready events for GStack skill activation."
status: "active"
district: "ingestion/github"
type: "neighborhood"
parent: "ingestion"
neighbors: ["ingestion/web", "shipments/compiler", "cognition/skills"]
traffic:
  reads: ["GitHub API (via github-mcp-server Go binary)"]
  writes: ["GStack skill activation (via shipments)"]
blast_radius:
  services: ["GitHub event processing", "GStack skill activation pipeline"]
  data: ["GitHub commit state", "Polling cursor (known SHAs)"]
  depends_on_accuracy: "critical (commits are high-priority signals for ontology extraction)"
contract:
  upstream: "github-mcp-server Go binary (stdio transport) — speaks MCP protocol over stdin/stdout"
  downstream: "GStack skill activation — receives shipments with entities, people, trajectory"
    token: "GITHUB_PERSONAL_ACCESS_TOKEN env var, or auto-detected via `gh auth token`"
    binary: "$HOME/go/bin/github-mcp-server (can override with GITHUB_MCP_SERVER_PATH env var)"
  mode: "read-only — only calls get/list tools, never create/edit"
  session: "persistent — `GitHubMCPClient` keeps one session for batch calls (was 31 sessions/run, now 1)"
---

# GitHub — GitHub MCP Integration

Watches a GitHub repository via the official `github/github-mcp-server` Go binary
over MCP stdio transport. Fetches commits with diffs, normalizes them into typed
events, and emits shipment-ready dicts for GStack skill activation.

## How It Works

```
GitHub Repo
    │
    ▼
github-mcp-server (Go binary, stdio transport)
    │  MCP protocol (JSON-RPC over stdin/stdout)
    │  Tools: get_commit, list_commits, get_me, list_branches
    ▼
ingestion/github/client.py
    │  Spawns/manages the Go binary
    │  Returns structured JSON dicts
    ▼
ingestion/github/adapter.py (GitHubAdapter)
    │  get_latest_commits() → list[GitHubEvent]
    │  get_commit(sha) → GitHubEvent
    │  poll(interval) → continuous event loop
    │  Each event → to_shipment() for GStack
    ▼
GStack Skill Activation
```

## Files

| File | Purpose |
|------|---------|
| `__init__.py` | Package exports: `GitHubAdapter`, `GitHubMCPClient`, types |
| `types.py` | Dataclasses: `GitHubAuthor`, `GitHubCommit`, `GitHubEvent` |
| `client.py` | MCP transport: `GitHubMCPClient` class (persistent session for batch calls), `resolve_token()` |
| `adapter.py` | `GitHubAdapter`: high-level API, `poll()`, `get_latest_commits()`, `to_shipment()` |

## Usage

```python
from ingestion.github import GitHubAdapter

adapter = GitHubAdapter("owner/repo")
events = await adapter.get_latest_commits(5)
for e in events:
    shipment = e.to_shipment()
    print(shipment["trajectory"]["message"].split("\n")[0])
```

## Requirements

- `github-mcp-server` Go binary in PATH (install: `go install github.com/github/github-mcp-server/cmd/github-mcp-server@latest`)
- `GITHUB_PERSONAL_ACCESS_TOKEN` env var, or `gh auth login` completed

## Related Directories

- `ingestion/web/` — Web scraping engine (sister ingestion module)
- `shipments/compiler/` — Receives GitHub events as shipments
- `cognition/skills/` — GStack skill runtime (activated by shipments)

---

*GitHub — GitHub MCP Integration — part of the OCR system. See `_index.md` in this directory for orientation.*
