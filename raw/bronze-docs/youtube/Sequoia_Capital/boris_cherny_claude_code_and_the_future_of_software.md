---
title: "Claude Code and the Future of Software — Boris Cherny (Anthropic)"
source_type: "youtube"
channel: "Sequoia Capital"
speaker: "Boris Cherny"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Interview on Sequoia Capital's channel. Boris Cherny is the creator of Claude Code and MCP at Anthropic. He designed and built the first version of Claude Code in late 2024."
tags: ["claude-code", "loop", "routines", "product-overhang", "agents-everywhere", "democratization", "organizational-process", "boris-cherny"]
---

# Claude Code and the Future of Software — Boris Cherny, Anthropic

Source: Sequoia Capital YouTube channel. Interview with Boris Cherny, creator of
Claude Code and MCP at Anthropic.

## Core Thesis

**Coding is solved.** The creator of Claude Code writes 100% of his code through
agents, does dozens of PRs daily, and has teams of thousands of agents running
around the clock. The question is no longer "can agents write code" but "how do
organizations adapt to a world where they do."

## Claude Code Origin Story

- Started accidentally in late 2024 as part of Anthropic Labs (incubator)
- Built for the **next model**, not the current one — pre-PMF for 6 months
- Early versions were "barely usable" — Boris used it for ~10% of his code
- Exponential growth started with **Opus 4 in May**, inflected with every model release (4.5, 4.6, 4.7)
- The team: small (few people), disbanded after launch, now back together led by Mike Krieger (ex-Instagram CTO)

The thesis: **product overhang** — the model can do things that no product has
yet captured. In late 2024, the state of the art was type-ahead (one line at a
time). The bet was that the next model could handle full agentic coding.

## Personal Setup

Boris's personal workflow (what's possible today):

- **100% of code through agents**: Claude Code codebase is 100% written by Claude. Boris writes "somewhere between a few dozen and 150 PRs per day."
- **Primarily works from his phone**: 5-10 Claude sessions, each with multiple sub-agents. Hundreds of agents during the day, thousands at night.
- **`/loop` as the killer primitive**: Claude uses cron to schedule recurring jobs. Dozens of loops running at any time:
  - One babysits PRs (fix CI, auto-rebase)
  - One keeps CI healthy (fixes flaky tests)
  - One grabs Twitter feedback and clusters it every 30 minutes
- **Routines** (server-side loops): persist even when laptop is closed

Boris's key insight: **"Loops are the future."** The most powerful pattern is not
a single agent invocation — it's agents that wake up on a schedule, do work,
and go back to sleep.

## Product vs Model

| Timeframe | Ratio | Reason |
|-----------|-------|--------|
| 1 year ago | 50/50 | Harness (product) mattered as much as model capability |
| Today | Weighted to model | Models are good enough that harness is less critical |
| 2 years | Heavily to model | Better alignment will make safety mechanisms less necessary |

Boris's YC lesson applies: **"Build something people love."** Even with great
models, product details matter. But the investment profile changes: invest in
harness early to capture the overhang, then let the model catch up.

## Future of Teams

- **More cross-disciplinary generalists**: Engineers who are also good at
  product, design, data science — all in one person
- **Everyone codes**: On the Claude Code team, every single person writes code
  — engineering manager, product manager, designers, data scientist, finance,
  user researcher
- **Organizational process is the differentiator**, not technology: "The same
  technology is available to everyone. The bigger lead is organizational
  structure and process." This confirms Dex's mental alignment thesis and
  Patrick's organizational loop.

## Anthropic's Internal Practices

Most advanced AI company's actual workflow:
- **All code is written by models** — zero manually written code
- **All SQL is written by models**
- **Claudes talk to each other over Slack** — agents negotiate, ask questions,
  resolve unknowns through natural language over standard communication protocols
- **Thousands of agents running continuously** — loops, routines, sub-agents
- **No human-in-the-loop for most operations** — agents handle CI, PR review,
  data queries autonomously

## Democratization of Software

The printing press analogy:
- Before printing press: ~10% literacy (professional scribes)
- After printing press: literacy rose to ~70% over centuries
- Parallel: software is becoming a universal literacy

The best person to write accounting software is not an engineer — it's an
accountant who knows the domain. Coding is the easy part. Domain knowledge is
the hard part.

**For OCR**: Organizational cognition is the next domain-specific literacy.
The best person to make organizational decisions is someone who understands
the organization, not the agent wrangler.

## SaaS Apocalypse?

Boris's take (from the Acquired podcast's "Seven Powers" framework):

**Powers that get less important with AI:**
- **Switching costs**: AI can port from one system to another easily
- **Process power**: AI (especially 4.7) can hill-climb any process — give it
  a target and it iterates until done

**Powers that still matter:**
- Network effects
- Scale economies
- Cornered resources

**Result**: 10x more disruptive startups. Tiny startups can compete with large
companies because large companies face internal resistance to change and
process evolution. Startups build with AI natively from day one.

## Multi-Agent Parallelism

- `/loop` emerged naturally with 4.7 — the model suggests it without prompting
- `4.7"just starts doing"` parallel work, scheduling, agent delegation
- As models improve, users don't need to figure out how to hold the tools
- It's a product design problem: make parallelism natural, not something users
  have to orchestrate manually

## Computer Use and MCP

- MCP is the answer for knowledge work tools (Salesforce, Google Docs, Calendar)
- **Computer Use is the catchall** for systems without MCPs — slow but effective
- For the model, it's all tokens — MCP, APIs, computer use are all interfaces
  to the same underlying capability

## Product Overhang Thesis (Building for Tomorrow)

Boris's framework for deciding what to build:
1. Find what the current model can almost do but no product captures
2. Build for that — it will be pre-PMF for 6 months
3. When the next model ships, you have PMF

Current candidates for the next overhang:
- **Claude Design** — pretty good today, will get much better
- **Loop/batch parallelism** — massively parallel agents
- **Computer Use** — catchall for non-MCP systems

## Relevance to OCR

### Loops = Shipment Pipeline

Boris's `/loop` is exactly what OCR's pipeline runner does — continuous
processing of shipments with cron-like schedules. The difference: OCR's
pipeline is deliberately serial with structured handoffs (per Luke's
correction), not massively parallel. OCR should implement loops as the
**orchestration mechanism** for the pipeline.

### Product Overhang Thesis Confirms ADR-0006

The architecture is built for the **next** model, not the current one. Just
as Claude Code was pre-PMF for 6 months, OCR's current state (85% scaffold)
is pre-PMF. The bet is that the model will catch up to the architecture.

### Organizational Process > Technology

Boris's strongest message for OCR: **"The same technology is available to
everyone. The biggest lead is organizational structure and process."** This
is the entire rationale for OCR — not a better model, but a better
organizational cognition infrastructure.

### Claude-to-Claude Communication

Agents negotiating over Slack validates the council pattern. The chairman's
synthesis is the structured output of agent-to-agent deliberation. OCR should
design for agent-to-agent communication as a first-class primitive.

### Cross-Disciplinary Generalists

Everyone on the Claude Code team codes. For OCR, this means every role
(product, design, strategy) should be able to read and write shipments.
The ontology is the shared language.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| Gates > agents | Harness investment is front-loaded, diminishing as models improve — build gates now |
| Serial processing | Claude Code's loops are serial per loop iteration — one task per wake cycle |
| Organizational focus | "Org process is the differentiator" |
| Eval pipeline | Boris's "babysitting PRs" loop is an eval pipeline — detect CI failures, fix them |
| Cross-referenced architecture | Everyone on team codes → ontology is shared language for all roles |

### What Boris Adds That No One Else Does

| Insight | Unique to Boris | OCR Application |
|---------|----------------|-----------------|
| **Product overhang** | Build for the model that will exist in 6 months | The architecture is forward-looking; invest in harness now |
| **Loops as first-class primitive** | Cron-like recurring agent tasks | Pipeline runner should support scheduled processing |
| **Routines (server-side loops)** | Agents persist when laptop closes | Shipment pipeline runs on the VPS, not the developer's machine |
| **Claude-to-Claude over Slack** | Agents communicate through standard channels | Council/chairman pattern: structured agent-to-agent output |
| **Harness importance diminishes** | Product matters now, less over time | Build governance gates early; they will need less enforcement later |
| **All SQL written by models** | Even data operations are agent-native | OCR should be agent-native end to end |
| **100% AI generated codebase** | Real, not aspirational — Claude Code itself | Proof that the future already works at scale |
