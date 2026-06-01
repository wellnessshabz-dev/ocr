---
title: "Building Pi — A Minimal Extensible Coding Harness (Mario)"
source_type: "youtube"
channel: "mastra"
speaker: "Mario"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Talk on mastra channel. Mario, Austrian, game dev background, 17 years in open source. Built Pi (pi.dev) as his own coding agent harness after souring on existing ones."
tags: ["pi", "minimalism", "extensibility", "custom-compaction", "terminal-bench", "terminus", "approval-fatigue", "oss-protection", "vouch", "tree-sessions", "hot-reload"]
---

# Building Pi — A Minimal Extensible Coding Harness (Mario)

Source: Tessel conference. Mario shares his journey building Pi, a minimal
extensible coding harness, after souring on Claude Code and other tools.

## The Journey

Mario's history with coding agents:
1. **Copy-paste from ChatGPT** (2023) — single functions, mostly broken
2. **GitHub Copilot** — tap to happiness, sometimes worked, sometimes recited
   GPL code verbatim
3. **Aider / Auto-GPT** — precursors, limited
4. **Claude Code** (Feb 2025) — the breakthrough. RL-trained models using file
   tools and bash ad-hoc instead of AST indexing. "They created the entire
   genre."

**Souring on Claude Code**: It became a "spaceship" — 90% dark matter features
nobody uses, flickering terminal UI (React in terminal = 12ms re-layout),
unstable API changes breaking workflows, zero model choice, zero extensibility,
hooks system expensive (spawns process per event), no observability into
context management.

## Survey of Existing Harnesses

| Harness | Good | Bad |
|---------|------|-----|
| **Claude Code** | Created the genre, good models | Spaceship, unstable, no extensibility |
| **Codex CLI** | Model improved a lot | Bad UI initially |
| **Amp** | Takes away features instead of adding them, grounded decisions | Limited model choice |
| **Factory (Troy)** | Solid | Not experimental enough, no big advantage over Claude Code |
| **Open Code** | Good team, pragmatic, stable | LSP injection too early (model gives up), compaction destroys prompt cache, every message = JSON file on disk, security RCE vulnerability with default server, no context management |

## Key Thesis: Minimalism

**Terminal Bench** is a coding/agent evaluation harness with ~82 diverse tasks.
**Terminus** tops the leaderboard. What does Terminus use? Only a `tmux`
session — the model sends keystrokes and reads back VT code sequences. No file
tools, no sub-agents, no web search, no planning.

**If the simplest interface tops the benchmark, what are all the features for?**

Two conclusions:
1. **We're in the "messing around and finding out" stage** — nobody knows what
   the perfect coding harness looks like. Minimalism and spaceship are both
   being tried.
2. **We need better ways to mess around** — harnesses need to be self-modifying
   and malleable for rapid experimentation.

## Pi's Design

### Core Philosophy

> "Adapt your coding agent to your needs instead of the other way around."

Strip away everything. Build a minimal extensible core.

### Tiny System Prompt

Pi's system prompt is tiny compared to every other harness. Frontier models are
heavily RL-trained to know what a coding agent is. **Why keep telling them?**

### YOLO by Default (with Containerization)

Mario rejects the approval dialog model:
- **YOLO mode**: Dangerous, agent does whatever
- **Approval mode**: Fatigue — people either turn it off or press enter blindly
- **Containerization**: The real solution. Sandbox execution, not approval gates.

### 4 Tools Only

1. **read** — file
2. **write** — file
3. **edit** — file
4. **bash** — shell

**Not included**: MCP, sub-agents, plan load, background bash, built-in todos.

| Feature | Pi's Approach |
|---------|--------------|
| MCP | CLI tools + skills, or build an extension |
| Sub-agents | tmux + spawn agent again (fully observable) |
| Plan load | Write `plan.md` — persistent artifact, reusable across sessions |
| Background bash | tmux — same thing |
| Todos | Write `todo.md` |

### Extensibility (The Real Innovation)

Pi is extensible at every layer:

1. **Custom tools** — write a TypeScript file, loaded automatically
2. **Custom UI** — full tree access for entirely custom interfaces
3. **Skills** — prompt templates, bundled on npm/git
4. **Custom compaction** — Mario thinks all current compaction impls are bad
5. **Permission gates** — implement in 50 lines if you want them
6. **Custom providers** — register proxies, self-hosted models
7. **Override built-in tools** — e.g., read/write/edit/bash via SSH (5 min impl)
8. **Hot reload** — edit extensions while agent runs, reload instantly
9. **Themes** — UI theming
10. **Bundling** — package everything on npm, install with one command

**Real extensions built by the community**:
- `/slash` — replicated Claude Code's slash in 5 minutes with more features
- Pi Messenger — chat room for multiple Pi agents with custom UI
- Pi Mess — play a game while agent runs
- Pi Annotate — annotate websites inline, feed back into context
- File Switch — quickly view modified files

### Session as Tree

Pi sessions are trees, not linear chat logs. You can:
- Create branches for sub-agents
- Read all files in a branch, summarize, go back to root
- Take summary into main branch and continue work
- Nothing injected behind your back

### Cost Tracking

Full cost tracking per session (many harnesses don't do this well).

## OSS Protection: "Rage Against the Clankers"

Mario's problem: Open source projects getting flooded with AI-generated PRs
and issues ("clanker slop"). Solutions:

1. **OSS Vacation** — Close issues/PRs for a few weeks. Important things get
   re-reported.
2. **Vouch System** — A markdown file in the repo with approved human
   contributors. PRs from unlisted accounts auto-close.
3. **Human Verification** — First, introduce yourself in a human voice via an
   issue. Get added to the vouch list.
4. **Mitchell from Ghostty** turned this into **Vouch** — a reusable project.

## Relevance to OCR

### Minimalism vs Spaceship

Mario's thesis directly challenges the approach of most other talks. Where
others add features (sub-agents, MCP, planning, etc.), Pi subtracts. This is a
valid alternative hypothesis:

| Spaceship Approach (most tools) | Minimalist Approach (Pi) |
|--------------------------------|-------------------------|
| Many built-in features | 4 tools, everything else is extension |
| Linear chat | Tree sessions |
| Approval gates | Containerization |
| Sub-agents as black boxes | tmux for full observability |
| System prompt engineering | Tiny system prompt (models already trained) |
| Compaction is built-in | Custom compaction via extensions |

### Custom Compaction Thesis

Mario: "All current compaction implementations are not good." This suggests
OCR should NOT bake compaction into the pipeline as a fixed strategy. Instead,
compaction should be swappable — different strategies for different shipment
types (research compaction vs code compaction vs governance compaction).

### Tree Sessions = GPSDI

Pi's tree-structured sessions (branch → explore → summarize → return to root)
is exactly what OCR's gates already do — each gate branch processes a shipment,
produces output, and returns to the main pipeline.

### Extensibility > Built-in

Pi's extension model (custom tools, hot reload, npm bundling) is more
sophisticated than any other harness. OCR should consider a similar approach
for its skills and perspective agents — pluggable, hot-reloadable, and
bundlable.

### Containerization > Approval Gates

Mario argues containerization is the only real safety mechanism. OCR's
governance layer should consider this: sandboxed execution (container) +
deterministic verification (governance) > prompt-based guardrails.

### OSS Vouch System

OCR is open source. If it gets popular, it will face the same clanker slop
problem. The vouch system (human-first contribution) is a pattern to adopt.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Observability** (OC missing it) | Mario: sub-agents must be observable (tmux > black box) |
| **Approval fatigue** | Mario: approval dialogs don't work → containerization instead |
| **Compact is imperfect** | Mario: all current compaction impls are bad |
| **Gates > agents** (Nick) | Mario: permission gates in 50 lines as extension, not core |
| **Don't outsource understanding** (Dex/Karpathy) | Mario: tree sessions keep you in control, nothing hidden |
| **Serial execution** (Luke) | Pi's tree is serial — branch, explore, return |
| **Skills as packages** (Patrick) | Pi extensions are npm packages — same model |
| **Minimal tool surface** (Tejas) | Pi: 4 tools + harness, Tejas: harness > tools |

### What Mario Adds

| Insight | OCR Application |
|---------|-----------------|
| **Minimalism hypothesis** | Not all features are needed — experiment with stripping down |
| **Custom compaction** | Compaction should be pluggable, not hardcoded |
| **Tree sessions** | Session structure matters — GPSDI should use tree topology |
| **Containerization > approval** | Safety at infrastructure level, not prompt level |
| **Hot-reloadable extensions** | Skills and perspective agents should hot-reload |
| **Tiny system prompt** | Don't over-prompt — models already know their role |
| **OSS clanker protection** | Vouch system for OCR's own repo |
| **Terminal Bench / Terminus** | Strongest empirical argument for minimal tool surface |
