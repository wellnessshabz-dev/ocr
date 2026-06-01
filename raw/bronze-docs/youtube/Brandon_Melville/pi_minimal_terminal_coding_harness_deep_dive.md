---
title: "Pi — Minimal Terminal Coding Harness Deep Dive (Brandon Melville)"
source_type: "youtube"
channel: "Brandon Melville"
speaker: "Brandon Melville"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Brandon Melville's YouTube channel. Comprehensive tutorial on Pi — the minimal terminal coding harness. Covers philosophy, setup, navigation, branching, extension system, and seven layers of customization."
tags: ["pi", "minimalism", "extensibility", "branching", "sessions-as-trees", "skills", "prompt-templates", "packages", "customization-layers"]
---

# Pi — Minimal Terminal Coding Harness Deep Dive (Brandon Melville)

Source: Brandon Melville's YouTube channel. A comprehensive walkthrough of
Pi: philosophy, setup, navigation, branching, and extension system.

## Pi's Stats
- **45.5k+ GitHub stars**
- **2.5M+ weekly NPM downloads**
- **OpenClaw** has integrated with Pi to power its AI agent capabilities

## Philosophy: Small Core with Programmable Edges

**Core** (5 things): read, bash, edit, write, sessions
- No built-in plan mode (intentional — can be added via extension)

**Edges** (everything else): models, agents.md, skills, prompts, extensions
- User builds what they need, shapes the tool, shares with others

> "Pi expects you to adapt it to your workflows, not the other way around."

## Setup

Install: `pi.dev` → shell command (Linux/Mac/WSL)

Model connections:
- **Subscriptions**: Claude Pro Max, ChatGPT Plus/Pro, GitHub Copilot
- **API keys**: Anthropic, OpenAI, Grok, Mistral, xAI, Azure, Bedrock, custom
- **`/login`**: OAuth flow for subscription providers

## Navigation

| Shortcut | Function |
|----------|----------|
| Control + L | Choose model |
| Control + P | Cycle model |
| Shift + Tab | Change thinking level |
| Control + G | Open external editor (VS Code) |
| Control + C (×2) | Stop session |

**`/settings`**: 21 settings including auto compact, auto resize images, block
images, scale commands, theme.

## Four Modes

| Mode | Flag | Use Case |
|------|------|----------|
| Interactive | (default) | Full TUI experience |
| JSON | `--json` | Scripts |
| Event stream | `--json-mode` | Event streams |
| RPC | — | Non-Node integration |
| SDK | — | Embed Pi in apps (OpenClaw) |

## Branching and Recovery (Sessions as Trees)

Sessions are **trees**, not linear chat logs.

| Command | Function |
|---------|----------|
| `/tree` | Branch from earlier message, edit and resubmit. Keeps alternate path in same session file. |
| `/fork` | Go back to an earlier message, change the prompt. Keeps both paths. File changes NOT undone — only conversation history is forked. |
| `/clone` | Duplicate current session at current point |
| `-c` flag | Resume previous session |
| `-r` flag | List all sessions (sort by threaded/recent/fuzzy, delete with Control+D) |

**Undo has two meanings:**
- **Prompt undo** → branching (tree/fork)
- **File undo** → git (not built into Pi — use git or checkpoint extensions)

## Extending Pi

### Context Modification (Priority Order)
| Layer | File | Purpose |
|-------|------|---------|
| 1 | `settings.json` | Change defaults |
| 2 | `agents.md` (or `claude.md`) | Project rules / instructions |
| 3 | `system.md` | Replace default system prompt |
| 4 | `append-system.md` | Add to default system prompt |
| 5 | Prompt templates (`~/.pi/prompts/`) | Repeat a prompt with slash command |
| 6 | Skills (`~/.pi/agents/`) | Reusable capability packaging |
| 7 | Extensions | Change behavior |
| 8 | Packages | Share what you made |

### Skills
- Each skill is a folder with a required `skill.md`
- Front matter: name + description (minimum)
- Body: step-by-step prompt
- Skills are loaded on demand (progressive disclosure)

### Prompt Templates
- Files in `~/.pi/prompts/` become slash commands
- `/hello` → expands the full prompt text into the conversation

### Packages (`pi.dev/packages`)
Official package library with extensions like:
- **Context mode** — MCP plugin that saves 98% of context window
- **Pi subagents**
- **Pi MCP adapter**
- **Pi web search**

## What Pi Deliberately Leaves Out

| Feature | Pi's Approach |
|---------|--------------|
| MCP | Not built-in — use CLI tools + skills or extension |
| Subagents | Not built-in — use tmux + spawn agent again |
| Permission pop-ups | Not built-in — containerization instead |
| Background bash | Not built-in — tmux |
| Todos | Not built-in — write todo.md |
| Plan mode | Not built-in — install extension |

> "If you need a workflow every day, make it a template, a skill, an extension,
> or a package."

## Relevance to OCR

### Seven Layers of Customization = OCR's Pluggable Architecture

| Pi Layer | OCR Equivalent |
|----------|----------------|
| `settings.json` | Infrastructure config (PostgreSQL, Neo4j, Redis) |
| `agents.md` / project rules | Per-district `_index.md` conventions |
| `system.md` | Default system prompt for council / chairman |
| `append-system.md` | Per-shipment context additions |
| Prompt templates (`/commands`) | Pre-defined council templates |
| Skills | Perspective agents, skill registry |
| Extensions | Custom tools, custom providers |
| Packages | Skill packages on npm/Git |

### Sessions as Trees = GPSDI Branching

Pi's session tree (branch from any message, keep alternate paths) confirms
OCR's pipeline should support branching — e.g., a governance rejection could
branch back to a specific gate with refined context rather than restarting.

### Deliberate Missing Features = OCR's Design Choices

Pi deliberately leaves out features to keep the core minimal. OCR should adopt
the same principle: the core pipeline (ingest → compile → deliberate →
govern → surface) is minimal. Everything else (MCP, sub-agents, permissions)
is an extension.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Minimal core** (Mario's thesis) | Pi's core is 5 primitives — everything else is extension |
| **Sessions as trees** (Mario) | Tree branching confirmed in practice |
| **Skills with progressive disclosure** | skill.md front matter = name + description, loaded on demand |
| **No built-in permissions** (Mario) | Permissions = containerization, not pop-ups |
| **Compact as setting** | Auto compact in settings — configurable |
| **Extensibility > built-in** | Seven layers of customization |
| **Package ecosystem** | pi.dev/packages = model for OCR skill marketplace |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **Seven layers of customization** | Architecture template for OCR pluggability |
| **Fork vs clone distinction** | Undo = prompt undo (branch) vs file undo (git) — OCR needs both |
| **Subscriptions as model access** | OCR can use subscription plans, not just API keys |
| **45.5k stars validation** | Minimal extensible approach is validated at scale |
| **OpenClaw integration** | Pi's SDK enables other harnesses to use its capabilities — OCR should expose SDK |
| **Packages as distribution** | OCR skills should be installable from a registry |
