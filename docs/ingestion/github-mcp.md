# GitHub MCP — How OCR Reads Your Code

## The Big Idea

OCR needs to know what's happening in your GitHub repositories to build an
organizational brain. GitHub MCP is the bridge that lets OCR ask GitHub questions
and get structured answers — no manual API calls, no web scraping.

Think of it as: OCR talks to GitHub MCP, GitHub MCP talks to GitHub's API,
GitHub MCP brings the answer back to OCR in a clean format.

---

## What Is GitHub MCP?

MCP stands for Model Context Protocol. GitHub MCP Server is an official tool
published by GitHub (`github/github-mcp-server`) that wraps the entire GitHub
API into ~79 question-and-answer tools organized into 19 groups (called
"toolsets"). It runs as a Go binary and needs a GitHub token to authenticate.

Two ways to run it:

| Mode | How | When to use |
|------|-----|-------------|
| **Local** | `github-mcp-server stdio --toolsets repos,issues` | Development, private repos |
| **Remote** | Point to `https://api.githubcopilot.com/mcp/` | When you don't want to install anything |

The remote server is GitHub's hosted version — you just need a GitHub token and
you're done.

---

## How OCR Uses It

OCR ingests signals (like a code commit) and processes them into organizational
cognition. GitHub MCP is the first link in that chain:

```
GitHub Commit happens
       ↓
Webhook fires → n8n wakes up
       ↓
n8n asks GitHub MCP: "get_commit(sha=abc123, include_diff=true)"
       ↓
GitHub MCP fetches from GitHub API
       ↓
Returns: message, author, files changed, diff, stats
       ↓
OCR Shipment Compiler receives the commit data
       ↓
OCR Ontology Extractor reads the diff and finds:
  - Which files changed → component nodes
  - Who wrote it → person node
  - What was said in the message → shipment classification
       ↓
Shipment enters cognition loop → council → memory → surface
```

---

## The 19 Toolsets — What Each Group Does

A toolset is a bundle of related questions OCR can ask GitHub. You don't need
all of them — OCR only needs a handful.

### The 4 OCR Needs (the important ones)

**1. `repos` — Repository operations (15 tools)**
The most important toolset for OCR. Lets you read commits, files, branches,
releases, tags.

| Tool | What it returns | Why OCR needs it |
|------|----------------|------------------|
| `get_commit` | Commit SHA, message, author, date, stats, files changed with **patch/diff** | **THE primary signal** — feeds the Shipment Compiler |
| `get_file_contents` | Raw file content at any commit/branch | Deep-dive into specific files during ontology extraction |
| `get_repository_tree` | Full directory tree | Maps the repo structure into component ontology |
| `list_commits` | Commit history on a branch | Trajectory/replay — rebuilds org state over time |
| `list_branches` | All branch names | Tracks parallel work streams |
| `create_branch`, `create_or_update_file`, `push_files` | Write operations | OCR never writes — we read only |

**2. `pull_requests` — Pull request operations (10 tools)**
Adds the "why" behind commits.

| Tool | What it returns | Why OCR needs it |
|------|----------------|------------------|
| `pull_request_read` | PR title, body, diff, files, reviews, comments | The **reason** behind code changes → ontology Decision nodes |
| `list_pull_requests` | Filtered PR list (open/closed, by branch) | Discovers active/inactive work |
| `search_pull_requests` | Cross-repo PR search | Finds related decisions across repos |

**3. `context` — User and team context (3 tools)**
Who is doing the work.

| Tool | What it returns | Why OCR needs it |
|------|----------------|------------------|
| `get_me` | Your GitHub profile: login, name, email, company, orgs | Seeds the Person ontology |
| `get_team_members` | All members of a team | Maps team structures |
| `get_teams` | Teams you belong to | Org chart for governance |

**4. `search` — Cross-repository search (4 tools)**
Connects dots across the entire organization.

| Tool | What it returns | Why OCR needs it |
|------|----------------|------------------|
| `search_code` | Code search across ALL repos | Finds all references to a concept → ontology consolidation |
| `search_issues` | Issue search | Finds related decisions, risks, blockers |
| `search_repositories` | Repo search | Discovers new repos to monitor |
| `search_users` | User search | Finds people by role or expertise |

### The 15 OCR Doesn't Need (yet)

These exist in the GitHub MCP but OCR doesn't need them for V1. They're listed
for completeness.

**5. `issues` (7 tools)** — Read and manage issues. OCR may use `search_issues`
(from the search toolset) but doesn't need the full issues toolset.

**6. `actions` (4 tools)** — CI/CD workflows. Useful later for deployment
ontology (tracking what shipped when).

**7. `discussions` (4 tools)** — GitHub Discussions. Could feed the "strategic
question" surface in Phase 3.

**8. `projects` (3 tools)** — GitHub Projects (the new project management
tables). Could feed Objective/Risk ontology nodes.

**9. `code_security` (2 tools)** — Code scanning alerts. Security risk ontology.

**10. `dependabot` (2 tools)** — Dependency alerts. Dependency risk ontology.

**11. `secret_protection` (2 tools)** — Secret scanning alerts. Security ontology.

**12. `security_advisories` (3 tools)** — Global and repo security advisories.

**13. `labels` (3 tools)** — Repository labels. Lightweight taxonomy.

**14. `gists` (4 tools)** — Gist operations. Not relevant for organizational
cognition.

**15. `notifications` (6 tools)** — Notification management. Not relevant.

**16. `stargazers` (3 tools)** — Star/unstar repos. Community metrics (Phase 3).

**17. `orgs` (1 tool)** — Org-level security advisories.

**18. `experiments` (3 tools)** — Meta-tools for managing MCP itself. Useful for
development/debugging.

**19. `users` (0 tools)** — Empty placeholder. No tools exist yet.

### Remote-only toolsets

| Toolset | Purpose |
|---------|---------|
| `copilot` | GitHub Copilot Coding Agent integration |
| `copilot_spaces` | Copilot Spaces |
| `github_support_docs_search` | Search GitHub product documentation |

---

## What One Call Tells OCR About the Organization

Imagine OCR calls `get_commit(owner="my-org", repo="my-app", sha="abc123",
include_diff=true)`. Here is exactly what it gets back and what OCR does with
each piece:

```
┌─────────────────────────────────────────────────────┐
│              get_commit response                     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  sha: "abc123"          ──→  Trajectory ID           │
│                                                      │
│  message: "Fix login    ──→  Shipment type:          │
│  timeout bug (#456)"         "tactical" (bug fix)    │
│                              Links to issue #456     │
│                              → Decision ontology     │
│                                                      │
│  author:                ──→  Person node:            │
│    login: "jane"              name: Jane             │
│    name: "Jane Doe"           role: developer        │
│                              Edge: Jane `owns` this   │
│                                    shipment          │
│                                                      │
│  date: "2026-05-30"     ──→  Trajectory timing       │
│                              → Memory decay weight   │
│                                                      │
│  stats:                 ──→  Shipment magnitude      │
│    additions: 45              Small/Medium/Large     │
│    deletions: 12                                    │
│    total: 57                                        │
│                                                      │
│  files: [               ──→  For EACH file:          │
│    {                        ─→ Component node:       │
│      filename:                "src/auth/login.ts"    │
│        "src/auth/login.ts"                          │
│      status: "modified"     → Edge:                  │
│                                "evolved_from"        │
│                                (previous version)    │
│      patch: "@@ -42,6      → Ontology Extractor      │
│        +42,15 @@ ..."           input:                │
│                                - function names      │
│                                - library imports     │
│                                - config changes      │
│                                - API endpoints       │
│    },                                              │
│    {                        ─→ Component node:       │
│      filename:                "src/auth/session.ts"  │
│        "src/auth/session.ts"                        │
│      status: "renamed"      → Edge: "renamed_from"  │
│      previous_filename:       previous path          │
│        "src/session.ts"                             │
│    },                                              │
│    {                        ─→ Dependency node:      │
│      filename:                package.json change    │
│        "package.json"                               │
│      status: "modified"     → Edge: "depends_on"    │
│      patch: "express:         library dependency    │
│        4.18→4.19"                                   │
│    }                                               │
│  ]                                                  │
│                                                      │
└─────────────────────────────────────────────────────┘
```

## The Ontology Graph This Single Call Seeds

```
[Person: Jane Doe]             [Component: login.ts]
     │                                │
     │ owns                           │ evolved_from
     ▼                                ▼
[Shipment: Commit abc123] ──── modifies ────→ [Component: login.ts (v2)]
     │                                │
     │ links_to                       │ relates_to
     ▼                                ▼
[Decision: Issue #456]         [Component: session.ts]
                                        │
                                        │ renamed_from
                                        ▼
                                   [Component: session.ts (old)]
                                        │
                                        │ depends_on
                                        ▼
                                   [Dependency: express@4.19]
```

OCR builds this picture from a single `get_commit` call. No additional API
calls needed for the initial ontology seed.

---

## What a Second Call Adds

If the commit is linked to a PR, OCR can call `pull_request_read`:

```
pull_request_read response adds:
├── title: "Fix login timeout"       →  Objective node
├── body: "Users were getting 408    →  Decision rationale
│   errors when token expired..."       (why was this done?)
├── reviewers: ["alice", "bob"]      →  2 more Person nodes
├── labels: ["bug", "auth"]          →  2 taxonomy nodes
├── linked issues: ["#456"]          →  Issue → Risk node
│                                          (what problem?)
└── reviews:                         →  Governance trace
    └── alice approved                  (who validated?)
```

---

## What a Third Call Connects

`search_code(query="login timeout", ...)` finds every file across every
repository that mentions "login timeout" — letting OCR discover related
components, identify dependencies, and surface contradictions (e.g., two
teams fixing the same bug independently).

---

## OCR's Configuration

OCR is read-only. It never creates, edits, or deletes anything on GitHub. The
recommended configuration:

```
--toolsets=repos,pull_requests,context,search
```

Or even tighter — just the 5 tools OCR actually calls:

```
--tools=get_commit,pull_request_read,search_issues,search_code,get_me
```

This keeps the tool list small (saves LLM context tokens) and guarantees
OCR cannot accidentally write to GitHub.

---

## Summary

GitHub MCP gives OCR a window into your codebase. One `get_commit` call returns
the diff, message, author, and files — everything the Shipment Compiler needs
to build a shipment and seed the ontology graph. A second call (`pull_request_read`)
adds the "why." A third (`search_code`) connects related concepts across the org.

OCR runs these calls through n8n when it receives a webhook (commit pushed, PR
opened, etc.). The entire pipeline is read-only, agent-agnostic, and maps
directly to the architecture documented in `raw/bronze-docs/`.

---

## Reference

- GitHub MCP Server: https://github.com/github/github-mcp-server
- Remote MCP docs: https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md
- Config guide: https://github.com/github/github-mcp-server/blob/main/docs/server-configuration.md
- Architecture context: `raw/bronze-docs/ocr_kimi_2.6_raw_1/16_mcp_ingestion_security.md`
- Build plan: `docs/build/v1_plan.md`
