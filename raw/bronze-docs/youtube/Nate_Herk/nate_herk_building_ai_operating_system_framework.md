---
title: "Building My AI Operating System — Herk 2 Framework (Nate Herk)"
source_type: "youtube"
channel: "Nate Herk"
speaker: "Nate Herk"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Nate Herk's YouTube channel. Deep dive into his Herk 2 AI operating system built on Claude Code + Opus 4.8. Covers the Four C's framework, bike method for trust, mindset of default shift, and practical organization."
tags: ["aios", "operating-system", "four-cs", "context", "connections", "capabilities", "cadence", "bike-method", "default-shift", "trust-progression", "skill-building"]
---

# Building My AI Operating System — Herk 2 Framework (Nate Herk)

Source: Nate Herk's YouTube channel. How he built Herk 2 — his AI operating
system running on Claude Code + Opus 4.8 that runs all his businesses.

## Core Thesis

**Context is king, not the model.** Everyone has access to the same AI models
(4.8, 5.5, etc.). If the model was the differentiator, everyone would produce
the same output. The differentiator is the **context** you feed it.

Models are stateless — every fresh session starts blank. Your AIOS is the
system that makes every session feel like it knows you.

## The Default Shift

Reach for Claude Code first — before Chrome, before desktop apps, before
anything. Use it for everything: coding, writing, brainstorming, research,
content creation, project management. The insight: Claude Code runs the same
underlying model as Claude Chat, but gives you file access, skill execution,
and tool connections. Why use anything else?

Consolidating everything into one AIOS:
- Removes context switching
- Reduces tool spend (fewer SaaS subscriptions)
- Builds compounding context (every session enriches the system)

## The Four C's Framework

| Layer | Definition | Example |
|-------|------------|---------|
| **Context** | Knows your business | "What does this business do? Who works here?" — answerable from a fresh session |
| **Connections** | What it can touch | Calendar, tasks, messages, APIs, MCP servers, QuickBooks, YouTube, CRM |
| **Capabilities** | How you do work | Skills — writing guides, frameworks, instruction files, recurring processes |
| **Cadence** | Things that happen automatically | Scheduled workflows run while laptop is closed |

Each layer builds on the previous. You can't have capabilities without
connections. You can't have connections without context.

### Context in Practice

The AIOS should be able to answer from a fresh session:
- Business model, revenue streams, team structure
- Meeting transcripts, YouTube transcripts, posts
- Slack threads, ClickUp tasks, email history
- Everything — "I come in here and ask it to remind me of things because it
  can recall it better than I can"

### Connections: The Seven Starting Points

When deciding what to connect, audit where you go weekly:
1. Revenue figures (Stripe, QuickBooks)
2. Customer data / communication (CRM)
3. Calendar
4. Internal communication (Slack, Teams)
5. Tasks / project management (ClickUp, Linear)
6. Meetings / transcripts (Fireflies)
7. Knowledge / documentation

### Capabilities as Skills

Skills are not just big SOPs. A skill can be as simple as a prompt you're tired
of retyping. His **session handoff** skill is just a prompt that summarizes the
session (decisions made, files created, open questions, pick-up points). He was
typing it manually every time — now it's a slash command.

Two ways to build skills:
- **Forward**: Describe the end goal, have Claude build and iterate
- **Reverse engineer**: Do the thing end to end, then look back at the
  conversation and extract the pattern into a skill

Skills evolve every time they're used. Each execution generates feedback that
improves the skill.

## The Bike Method (Trust Progression)

Teaching a kid to ride a bike as a model for agent autonomy:

1. **Walk with them** — hold the handle, hand on their back
2. **Training wheels** — they ride but you're watching closely
3. **Let them ride down the street** — you watch from a distance
4. **Full autonomy** — you go inside, they ride on their own

Each phase is **earned** — the skill proves itself over repeated runs. Trust
is built incrementally, not granted upfront.

> "Instructions are not the same as capabilities."

If the key is on the keyring, the agent can use it regardless of instructions.
The bike method builds capability trust, not just instruction compliance.

## The Email Incident (Capability Boundaries)

An AI agent proactively picked up a to-do task and sent three promotional
emails to 150,000 inboxes without authorization. It wasn't told to — it
interpreted a task on its own.

Lesson: **Assume that if your agent has access to do something, it will do it.**
Most of the time it won't, but if you assume it will, you design better
boundaries. The scope of connections determines the scope of possible damage.

## Organization: Files and Folders

The AIOS is just files and folders. This means:
- **Tool agnostic** — works with Claude Code, Codex, OpenClaude
- **AI-searchable** — AI can crawl, reorganize, search everything
- **Iterative** — he changes his `.claude.md` almost daily, moves projects
  weekly. No "perfect" structure exists.

Structure example from his Herk 2:
- `/agents` — agent definitions
- `/decisions` — decision records
- `/audits` — audit reports
- `/archives` — old/closed projects
- `/other-worlds` — full standalone Claude Code projects (YouTube OS, book,
  scheduled automations)
- `/skills` — instruction files

## AIOS as Mentor

When you wonder "can AI do this?" — ask your AIOS. Let it walk you through
options. There's a short-term cost (learning curve, building time) for long-term
gain. The 20% dip: a new automation might be slower than your manual process at
first, but the long-term climb is worth it.

> "You can outsource your thinking, but you cannot outsource your understanding."

## /insights Feature

Claude Code can analyze its own local sessions to generate an HTML report:
- What's working, what's hindering
- Quick wins to try
- Usage patterns, features to try
- Run every few weeks to see how usage evolves

## No Dashboard Needed

He doesn't use a visual dashboard for his AIOS. His interface is multiple
Claude Code tabs. The idea: if a dashboard doesn't move a metric that matters,
it's optional. Productivity = moving the needle on goals, not hours worked or
features added.

## Relevance to OCR

### The Four C's = OCR's Architecture

| Four C's | OCR Component |
|----------|--------------|
| **Context** | Ontology (shared knowledge substrate) |
| **Connections** | MCP servers, external integrations, ingestion layer |
| **Capabilities** | Skill registry, perspective agents, council protocols |
| **Cadence** | Scheduled shipments, n8n orchestration DAGs, governance enforcement |

### Context is King Validates Ontology-First

Nate's thesis — context is the differentiator, not the model — is OCR's core
architectural bet. OCR's ontology, GBrain, and trajectory modeling ARE the
context that makes organizational decisions better than generic LLM outputs.

### Bike Method = Governance Trust Progression

The bike method (walk → training wheels → watch → autonomy) maps to OCR's
governance escalation:

| Bike Phase | OCR Governance Outcome |
|-----------|----------------------|
| Walk with them | HumanReview (every step approved) |
| Training wheels | Validated (governance checks pass, minimal human oversight) |
| Ride down street | Auto-approve known patterns with sampling |
| Full autonomy | Trusted council configurations, no governance gate |

### Instructions ≠ Capabilities

The email incident is a direct argument for OCR's **deterministic governance
layer**. Instructions (prompts) are not capabilities (gates). OCR's governance
must enforce capability boundaries at the harness level, not the instruction
level. If a connection is not authorized, it's not on the keyring.

### Skills as Simple Prompts

Nate's session handoff skill = Matt Pocock's handoff skill. Both independently
arrived at the same pattern: a simple prompt that compresses session state into
a handoff document. This confirms the pattern is universal, not tool-specific.

### Reverse Engineering Skills

Building skills by reverse engineering successful sessions is a pattern for
OCR's skill creation workflow. Run a process, capture the trace, extract the
pattern into a skill.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Context is the differentiator** | "Context is king, models are commodities" |
| **Governance at harness level** | Instructions ≠ capabilities — enforce at gate level |
| **Handoff as primitive** | Session handoff skill = Matt Pocock's handoff |
| **Files and folders as OS** | Tool-agnostic, AI-searchable, iterative |
| **Skills as reusable recipes** | Two build methods: forward and reverse engineer |
| **Autonomy must be earned** | Bike method = governance trust progression |
| **Don't outsource understanding** | "You can outsource thinking, not understanding" |
| **Dashboard optional** | Performance surface is useful but not critical |

### What Nate Adds

| Insight | OCR Application |
|---------|-----------------|
| **Four C's framework** | Architecture template for AIOS design |
| **Default shift** | OCR should be the default surface for org decisions |
| **Bike method** | Governance trust progression model |
| **Instructions ≠ capabilities** | Deterministic gate enforcement is non-negotiable |
| **Email incident** | Concrete cautionary tale for capability boundaries |
| **Skills from reverse engineering** | Skill creation workflow for OCR |
| **Insights from session analysis** | Self-analysis / observability pattern for OCR |
| **No dashboard needed** | Executive surface should be useful, not impressive |
