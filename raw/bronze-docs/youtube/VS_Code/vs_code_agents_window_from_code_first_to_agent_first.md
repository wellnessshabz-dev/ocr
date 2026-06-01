---
title: "VS Code Agents Window — From Code-First to Agent-First (VS Code Insiders Podcast)"
source_type: "youtube"
channel: "VS Code"
speaker: "Bridget Merton (VS Code team)"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "VS Code Insiders Podcast (VS Code YouTube channel). Bridget Merton returns to discuss the evolution of agentic development in VS Code since September 2025 and the new dedicated Agents Window."
tags: ["vs-code", "agents-window", "agent-first", "multi-agent", "work-trees", "sub-sessions", "code-first", "harness", "custom-agents"]
---

# VS Code Agents Window — From Code-First to Agent-First (VS Code Insiders Podcast)

Source: VS Code YouTube channel. VS Code Insiders Podcast with Bridget Merton
on the evolution from sessions view to the dedicated Agents Window.

## The Evolution (Sept 2025 → 2026)

VS Code invested in multiple agent harnesses within the editor:
- **Copilot CLI** (background agent)
- **Copilot Cloud agent**
- **Claude agent**
- **Local agent mode** (VS Code's own harness)

Sessions management evolved from separate sidebar views to being integrated
into the chat panel — users expected to find sessions where they type messages.

Users became more **multi-agent and multi-project** — working across repos,
projects, and harnesses simultaneously. But VS Code was still scoped to one
workspace at a time.

## The Agents Window: Agent-First Development

A dedicated VS Code window designed for **agent-first** (not code-first) work.
Familiar to VS Code users (theme, keybindings, settings, auth transfer) but
redesigned for task-oriented multi-agent workflows.

### Layout

| Zone | Content |
|------|---------|
| **Left sidebar** | Session list organized by workspace/project |
| **Center** | Agent chat, streaming output, review |
| **Right panel** | Changes (diffs), Files (file tree), integrated browser |
| **Bottom left** | Customizations (custom agents, MCP servers) — always visible |
| **Top right** | Actions — Run Task, Open in VS Code, etc. |

### Key Features

1. **Multiple harnesses per session** — Pick Copilot CLI, Claude agent, or
   cloud agent per session
2. **Work trees as default** — Each session isolated in its own work tree
   (can override to folder)
3. **Multi-project** — Sessions span different repos, workspaces, machines
4. **SSH/dev tunnels** — Agents on remote machines
5. **Integrated browser** — Preview apps without leaving the window
6. **Changes panel** — Review diffs, add line comments, iterate with agent
7. **PR creation** — Create/draft PRs directly from changes panel
8. **Sync changes** — Pull upstream changes, handle merge conflicts
9. **Sub-sessions** — Create additional sessions on the same work tree for
   related work (code review, exploration)
10. **Permission approvals from sidebar** — Approve/deny without opening
    session
11. **Customizations elevated** — Custom agents and MCP servers visible and
    editable by default

### Code-First vs Agent-First

| Mode | When to Use |
|------|-------------|
| **VS Code editor** (code-first) | Extensive code editing, fine-tuning wording, debugging |
| **Agents window** (agent-first) | Kick off multi-project explorations, review outputs, monitor sessions |

The windows are **seamlessly connected**:
- "Open in Agents" button in VS Code → opens Agents window
- "Open in VS Code" button in Agents window → opens the work tree in VS Code
- Theme, keybindings, auth, settings transfer between them

### Extensibility

- **Top 100 marketplace extensions** auto-activate in Agents window (themes,
  grammars, languages, keybindings)
- **`extensions.supportAgentsWindow`** setting — allows specific extensions
- Looking for extension author feedback on what makes sense in agent-first
  environment

## Relevance to OCR

### Agent-First = OCR's Design Philosophy

VS Code's shift from code-first to agent-first mirrors OCR's shift from
application-first to cognition-first. OCR is an agent-first operating system
for organizational decisions — the agents window is the primary interface,
not a code editor.

### Agents Window = OCR's Executive Surface

| Agents Window Feature | OCR Executive Surface Equivalent |
|----------------------|----------------------------------|
| Session list by workspace | Shipment queue by domain/priority |
| Multi-harness per session | Multi-council per shipment |
| Work tree isolation | Shipment isolation (each gets own context slice) |
| Changes panel | Governance verification output |
| Integrated browser | Executive dashboard live preview |
| PR creation | Decision commit + audit record |
| Sub-sessions | Sub-councils on specific facets |
| Customizations | Skill registry + perspective agent config |

### Multi-Agent, Multi-Project

OCR must support multiple concurrent shipments across different organizational
domains, just as VS Code's Agents window supports multiple projects. Each
shipment is isolated (work tree equivalent) and can use different council
compositions (harness equivalent).

### Sub-Sessions = Sub-Councils

The sub-session pattern (additional sessions on the same work tree) maps to
sub-councils: a main council spins off specialized sub-councils for specific
facets of a decision, results feed back to the main council.

### Code-First ↔ Agent-First Switching

OCR should support seamless switching between:
- **Cognition-first** (executive surface — monitor shipments, review decisions)
- **Code-first** (implementation — the code that the decision produced)

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Multi-agent by design** | VS Code's entire agents window is multi-agent |
| **Isolated context per shipment** | Work tree isolation per session |
| **Sub-councils** | Sub-sessions on same work tree |
| **Executive surface** | Dedicated agent-first window with dashboard-like features |
| **Swappable harnesses** (Mario/Pi) | VS Code supports multiple agent harnesses per session |
| **Permission gates** | Approval from sidebar without opening session |
| **Workspace/project organization** | Sessions organized by workspace |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **Agent-first window as primary interface** | OCR's executive surface should be the default view |
| **Code-first ↔ agent-first switching** | Seamless mode switching for OCR operators |
| **Sub-sessions pattern** | Sub-councils on same shipment |
| **SSH/dev tunnels for remote agents** | OCR agents on remote machines |
| **Customizations always visible** | Skill registry and perspective agents should be front-and-center |
| **Top 100 extension strategy** | Which integrations auto-load in OCR |
| **Work trees for isolation** | Shipment isolation strategy confirmed |
| **Integrated browser for preview** | OCR preview of decision outcomes |
