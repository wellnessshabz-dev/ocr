---
title: "Why I Switched from OpenClaw to Hermes — 5 Reasons (NetworkChuck)"
source_type: "youtube"
channel: "NetworkChuck"
speaker: "NetworkChuck, Jeff Quesnelle (Nous Research cofounder)"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "NetworkChuck's YouTube channel. Detailed comparison of Hermes vs OpenClaw after 1 month of Hermes usage. Features an interview with Jeff Quesnelle (cofounder, Nous Research). Covers memory architecture, self-improving skills, philosophy, and practical deployment."
tags: ["hermes", "openclaw", "comparison", "memory", "self-improvement", "skills", "nous-research", "curator", "honcho", "harness-philosophy"]
---

# Why I Switched from OpenClaw to Hermes — 5 Reasons

Source: NetworkChuck YouTube channel. After 1 month using Hermes, compares it
to OpenClaw across 5 dimensions. Includes interview with Jeff Quesnelle
(cofounder, Nous Research).

## Context

Hermes was an **internal tool at Nous Research** for 6-7 months before
OpenClaw launched. When they tried OpenClaw, they found it "clunkier" and
decided to release their own. Hermes has since topped OpenClaw on OpenRouter
token usage and is the fastest growing GitHub project.

## 5 Reasons Hermes > OpenClaw

### #1: Vibe & Mission
Nous Research is "humanistic, censorship free, and democratic AI." The
aesthetic and terminal experience are intentionally fun and polished. "It's
not just the vibe — it's who these people are."

### #2: Memory Architecture (Key Differentiator)

| Aspect | Hermes | OpenClaw |
|--------|--------|----------|
| USER.md | 1,375 char hard limit | No hard limit |
| MEMORY.md | 2,200 char hard limit | No hard limit |
| Update frequency | Nudges every ~10 turns (during session) | Only on compaction/session start |
| Curated by | Agent itself (forced to distill) | Agent (tends to bloat) |

**Two files**:
- **USER.md**: about the person (preferences, habits, context)
- **MEMORY.md**: about the environment (technical setup, connections, tools)

**Hard limits force the agent to curate** — what's actually important to keep
vs discard. This prevents bloat that makes OpenClaw "feel clunky on day 30."

**Honcho plugin**: External peer service that builds a personality profile over
time. Every message is analyzed to build a "peer card" — conclusions about the
user (traits, preferences, habits). Fed into the system prompt at query time.
"High friction technical procrastination" is the kind of insight it generates.

### #3: The People
Nous Research is a group of AI researchers who met on Discord building their
own models (the Hermes models). They're not a tool company — they're
researchers who built a tool for themselves. "When we saw what OpenClaw did,
we were like, we can give this out because we have our own version."

> "I think who's making the tools, why they're making the tools, and what
> they're gonna do going forward is really important."

### #4: Self-Improvement Loop (Crystallized Skills)

**This is the headline feature** — "Better on day 30 than day one."

Agent **creates its own skills** by crystallizing workflows from your
interactions. Example: agent set up Twingate VPN, then automatically created
a "Twingate client operations" skill for reuse.

> "We modeled it after how we ourselves work — we struggle through things.
> When we figure out ways that solve hard problems, we note that down, and
> then we iterate on those successes." — Jeff Quesnelle

**Curator agent**: Runs in the background, periodically reviews skills.
Moves skills through **active → stale → archive** states. Removes irrelevant
skills, improves existing ones. Prevents skill pileup.

**Pre-packaged skills** are curated by the Hermes team (e.g., GitHub PR review
is the actual review process used internally by Nous Research).

**Contrast with OpenClaw**: Marketplace model (download skills, malware CVEs).
Hermes model: build skills from your own usage, zero trust built-in.

### #5: Doesn't Break
> "OpenClaw feels like a project. Hermes feels like a product."

NetworkChuck's wife uses Hermes (named "Honey") for homeschool, diet planning,
house management with 6 kids. "I haven't had one issue — nothing I didn't
cause myself."

## Key Philosophy

> "The harness is the haptic feedback to the model of the world."

> "Get out of the way of the models. The models are smart. We just need to
> give them the hands, the feet, the fingers to touch the world in an
> appropriate way."

## Feature Updates

- **Dashboard**: web UI for managing skills, plugins, agents, models
- **Kanban**: task board with progress tracking, comments, human input blocks
- **Auxiliary models**: one big model for main thinking, others for research/delegation
- **Computer use**: preview (controlling the computer)
- **Achievements**: gamification

## Relevance to OCR

### Direct Architecture Parallels

| Hermes Feature | OCR Equivalent |
|----------------|----------------|
| USER.md (hard-limited, curated) | Per-user context in governance layer |
| MEMORY.md (hard-limited, curated) | GBrain episodic memory with compaction |
| Self-improving skills (crystallized from usage) | Skill registry — evolved from governance outcomes |
| Curator agent (active/stale/archive) | Ontology Manager + skill lifecycle |
| Honcho (external peer modeling) | Trajectory Modeler — builds user/system profile |
| Auxiliary models | Multi-model routing per perspective agent |
| Kanban with human input blocks | Shipment lifecycle + HumanReview gates |

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Get out of the model's way** | Harness is haptic feedback — same as Pi's 300-token philosophy |
| **Curated memory with bounds** | Hard limits force distillation — OCR must bound context |
| **Self-improving loop** | Skills emerge from usage, not marketplace — matches OCR's audit→improve |
| **Product over project** | OCR must feel like a product, not a research prototype |
| **Feature parity without bloat** | OCR should match Claude Code/Hermes on core, not on surface features |
| **Human-in-loop gates** | Kanban stops for human input — matches governance layer |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **Hard limits force curation** | USER.md/MEMORY.md size caps prevent context bloat — OCR should bound every memory file |
| **Active/stale/archive skill lifecycle** | OCR's skill registry needs automatic archival of unused skills |
| **Honcho peer modeling** | External reasoning over user data builds richer profiles — OCR should support pluggable profile builders |
| **Skills crystallized from usage, not downloaded** | OCR skills come from governance outcomes, not a marketplace — zero-trust by design |
| **Auxiliary models for sub-tasks** | One model for reasoning, another for research, another for delegation — OCR's multi-model routing |
| **Harness = haptic feedback** | The harness gives the model sensory feedback about the world — OCR's ontology + audit data is the haptic feedback |
| **OpenClaw feels like a project** | Risk of over-engineering. OCR must prioritize the product experience. |
