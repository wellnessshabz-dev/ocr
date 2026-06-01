---
title: "The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory"
source_type: "youtube"
channel: "AI Engineer"
speaker: "Luke Alvoeiro"
date: "2026-05"
url: "https://www.youtube.com/watch?v=ow1we5PzK-o"
status: "reasoned"
processed_by: "human + claude"
source_notes: "AI Engineer YouTube channel. Luke leads core agent harness at Factory, previously created Goose (now under AI Agentic AI Foundation)."
tags: ["multi-agent", "orchestrator-worker-validator", "validation-contract", "serial-execution", "factory", "missions", "structured-handoffs", "model-agnostic"]
---

# The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory

Source: AI Engineer YouTube channel. Luke Alvoeiro, Factory — leads core agent harness.
Previously created Goose (open-source coding agent, now at AI Agentic AI Foundation).

## Core Thesis

The bottleneck in software engineering is not intelligence — it's human attention.
A human can only drive a few tasks per day. The goal: **human decides what to build,
system figures out how.** Agents work for hours/days, human comes back to finished work.

## Five Multi-Agent Strategies (Taxonomy)

1. **Delegation** — One agent spawns another. Parent says "go figure out DB schema,"
   gets response. Simplest form, most common (sub-agents, coding tools).

2. **Creator-Verifier** — One agent builds, another checks. Separation of concerns.
   Implementer has cost bias (wants code to work). Fresh agent with fresh context
   finds more issues. Same reason humans do code review.

3. **Direct Communication** — Agents DM each other without central coordinator.
   Hard to get right — state fragments across conversations, no single source of truth.

4. **Negotiation** — Agents communicate over shared resource (same API, same code).
   Best when net positive sum trading — agents have win-win potential.

5. **Broadcast** — One agent sends info to many. Status updates, new context, shared
   constraints. Less flashy but critical for long-running coherence.

## Missions Architecture (Combines 1, 2, 4, 5)

### Three-Role Architecture

#### Orchestrator (Planning)
- Acts as sounding board, asks strategic questions, probes unclear requirements
- Produces: **features**, **milestones**, and a **validation contract**
- The validation contract defines "done" *before any code is written*
- Orchestrator never accumulates granular context — delegates investigation to sub-agents

#### Workers (Implementation)
- Each worker gets **clean context** — no accumulated baggage, no degraded attention
- Reads spec, implements feature, commits via git
- Next worker inherits clean slate + working codebase
- Writes tests BEFORE code (tests reflect intended behavior, not implementation details)

#### Validators (Verification)
Two types that run at each milestone boundary:

1. **Scrutiny Validator** — Runs test suite, type checking, lint. Spawns dedicated code
   review agents for each completed feature. More traditional.

2. **User Testing Validator** — Acts like QA engineer. Spawns the application, interacts
   via computer use, fills forms, checks pages render, clicks buttons. Ensures functional
   flows work holistically. **Takes longer than scrutiny — most mission wall clock time
   is spent here, not generating tokens.**

**Critical: Validators have never seen the code before.** They're adversarial by design.
No investment in the implementation. Tests written after implementation don't catch bugs —
they confirm decisions. Pre-code validation contract prevents drift.

### Validation Contract

Written during planning, before any feature is defined. Defines correctness independently
of implementation. For complex projects, hundreds of assertions. Each feature is assigned
one or more assertions it must satisfy. Sum of all features = every assertion covered.

This prevents the "tests shaped by the code, not by what the code was attempting to do" problem.

### Serial Execution (CRITICAL DESIGN POINT)

**Parallelism doesn't work for software dev.** Factory tried parallel agents:
- Agents conflict, step on each other's changes
- Duplicate work
- Inconsistent architectural decisions
- Coordination overhead eats speed gains AND burns tokens

**Missions runs features serially.** One worker or validator at any point in time.
Within a feature, parallelization on **read-only operations** (searching codebase,
researching APIs). Within validators, parallelize read-only code review.

"Seems slower on paper, but error rate drops dramatically. When tasks run many days,
correctness compounds."

### Model Selection Per Role ("Droid Whispering")
- **Planning**: benefits from slow, careful reasoning
- **Implementation**: benefits from fast code fluency and creativity
- **Validation**: benefits from precise instruction following

No single model or provider excels at all three. Model-agnostic architecture =
structural advantage. Different model providers for validation prevents bias from
shared training data.

**Inverse also true**: structure can compensate for weaker models. Validation contracts
and milestone checkpoints allow successful missions even with open-weight models.

### Structured Handoffs

When a worker finishes, it fills out a structured handoff detailing:
- What was completed
- What was left undone
- What commands were run + exit codes
- What issues were discovered
- Did it abide by orchestrator-defined procedures

Errors caught at milestone boundaries. Corrective work scoped. System self-heals
by forcing agents to write down what happened, then addressing issues.

### Thin Deterministic Logic

Almost all orchestration logic is in prompts and skills, not a hard-coded state machine.
~700 lines of text. Four sentences can alter execution strategy. Worker behavior driven
by skills the orchestrator defines per mission.

The only deterministic logic is very thin: running validation, ensuring progress blocks
when handoff issues are not addressed. "Missions ensures discipline, models provide
intelligence."

### Bitter Lesson Awareness

System designed to improve with every model improvement, not be made obsolete.
Because orchestration is prompt/skill-based (not hard-coded), model improvements
compound through the architecture. As models get better at reasoning, planning,
execution, and computer use, each improvement compounds: better planners produce
tighter specs, better workers make fewer mistakes, better validators judge more
reliably.

## Production Data

From building a Slack clone as a benchmark:
- **60% of time spent on implementation, 60% of tokens on implementation**
- **Validation never succeeds on first go** — always creates follow-up features
- **50% of final code is tests, 90% test coverage**
- 81 issues surfaced by validators → 21 targeted fix features (34.4% of implementation work)
- Longest mission: **16 days** (believe can go to 30)
- 37% of missions run longer than 4 hours
- 14% run longer than 24 hours

## OCR Connections

| Factory Missions | OCR Equivalent |
|---|---|
| Orchestrator | Council Orchestrator (`cognition/councils/`) |
| Workers | Skills (`cognition/skills/`) |
| Validators (Scrutiny + User Testing) | Governance (`cognition/governance/`) |
| Validation Contract (pre-code) | Eval pipeline (`observability/`) |
| Structured handoffs | Trajectory modeler (`gbrain/temporal/`) |
| Serial features | Serial shipment processing (design correction) |
| Clean context per worker | Fresh context per skill invocation |
| Model-agnostic architecture | ActivationScore selects skills |
| Thin deterministic logic (~700 lines) | `_index.md` + skills pattern |
| "Droid whispering" | Skill of modeling LLM interactions across roles |

### Critical Design Correction

**Matt Pocock's Kanban DAG** (multiple parallel agents) applies at the *task management*
level but NOT at the *execution* level. Luke's production data shows parallel agents
conflict and burn tokens. **Shipments should be processed serially** with parallelism
only on read-only operations (research, code review during validation).

This validates the Medallion gate pattern: serialize at the gate (one shipment at a time
through governance), parallelize only within read-only scopes.
