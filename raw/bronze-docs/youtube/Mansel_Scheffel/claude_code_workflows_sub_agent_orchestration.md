---
title: "Claude Code Workflows — Sub-Agent Orchestration via workflow.js (Mansel Scheffel)"
source_type: "youtube"
channel: "Mansel Scheffel"
speaker: "Mansel Scheffel"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Mansel Scheffel's YouTube channel. Deep dive on Claude Code's new Workflows feature — moves sub-agent orchestration from the LLM's context window to a deterministic JavaScript script (workflow.js). Covers architecture, deep research demo, multi-model per phase, limitations, and use cases."
tags: ["claude-code", "workflows", "sub-agents", "orchestration", "workflow.js", "deep-research", "multi-model", "deterministic-loops", "journal", "state-management"]
---

# Claude Code Workflows — Sub-Agent Orchestration via workflow.js

Source: Mansel Scheffel's YouTube channel. Deep dive on Claude Code's new
Workflows feature — script-based sub-agent orchestration.

## The Sub-Agent Problem (Old Way)

Main Claude Code session spawns sub-agents with isolated context windows. Each
sub-agent performs a task and returns only the answer (~500 tokens) instead of
all intermediate bloat (could be 60,000 tokens).

**Old problem**: Claude as orchestrator manages all sub-agents in its context
window. At scale, the manager loses track because it holds intermediate states
in context. Must track who runs next, what they're running, how to manage
results.

> "We have our manager who loses track of everything because it has to hold
> intermediate states within its context."

## The Solution: Workflow Script (workflow.js)

Move the manager from the LLM's context window to a **deterministic script**.

| Aspect | Old Way | New Way (Workflows) |
|--------|---------|---------------------|
| Orchestrator | Claude (in context) | workflow.js (separate process) |
| State | Held in LLM context | Held in JavaScript variables |
| Loops | LLM-driven | Deterministic loops in script |
| Scale | Limited by context | Massive (1,000 agents per run) |
| Resume | No | Yes (via journal) |

### Runtime Architecture

```
Main Claude Code session
  → Process: workflow.js (separate process, loaded at runtime)
    → Spawns sub-agents (agents 1..N)
    → Journal manages state (pause/resume)
    → Only final answers return to main context
```

## Limitations

| Constraint | Value |
|------------|-------|
| Concurrent agents | 16 max |
| Total agents per run | 1,000 max |
| Direct FS/shell from script | No (agents can do it) |
| Works in | Desktop app, IDE (terminal mode) |
| Not in | VS Code extension (currently) |
| Default for Max/Team | On |
| Default for Pro | Off (will nuke budget) |
| Research preview | Yes |

## Deep Research Demo

5-stage pipeline for researching "vitamin C benefits":

| Stage | Parallelism | Tokens | Agents |
|-------|-------------|--------|--------|
| Scope | Break into 5 angles | 31K | 1 |
| Search | 5 parallel web searches | — | 5 |
| Fetch | Dedupe URLs, pull 15 sources | — | — |
| Verify | Adversarial 3-vote fact-check per claim (2/3 refutes kills) | — | ~75 |
| Synthesize | Write final answer | — | — |

**Totals**: 105 agents, 3.1M tokens, 15 minutes for one question.

> "Just because you can doesn't mean you should."

### Startup Forge Demo (Self-Created)

4 agents invent startups from different angles (consumer, B2B, climate, AI).
Each scored by VC judge the moment ready. Top idea attacked by 3 parallel
skeptics (persona prompting — distinct lens each). Final honest investor pitch
must confront every objection.

## Multi-Model Per Phase

Each phase can specify a different model:

| Phase | Model | Task |
|-------|-------|------|
| Generate | Haiku (cheap) | Brainstorm name/tagline candidates |
| Critique | Sonnet (medium) | Score each candidate |
| Synthesize | Opus (expensive) | Write final brand brief |

Configured in the workflow.js file:
```javascript
{ phase: "generate", model: "haiku", agents: 6, prompt: "..." }
{ phase: "critique", model: "sonnet", agents: 1, prompt: "..." }
{ phase: "synthesize", model: "opus", agents: 1, prompt: "..." }
```

## Three Levels of Control

| Level | How | What You Can Change |
|-------|-----|---------------------|
| 1 | Natural language prompt | Be specific upfront |
| 2 | Inspect file before running | Agent count, parallelism, prompts, models, budget guards |
| 3 | Edit workflow.js directly | Full control over JavaScript logic |

## When to Use Workflows vs Skills

| Use | Skills | Workflows |
|-----|--------|-----------|
| Daily deterministic tasks | ✅ | ❌ (too expensive) |
| Complex fan-out tasks | ❌ | ✅ |
| Deterministic loops | ❌ | ✅ |
| Resume mid-run | ❌ | ✅ |
| Business operations | ✅ | ❌ |
| Deep research | ❌ | ✅ |
| Massive bug sweeps | ❌ | ✅ |

## Relevance to OCR

### This is the Closest Pattern to OCR's Council Architecture

| Claude Code Workflows | OCR Equivalent |
|-----------------------|----------------|
| workflow.js (deterministic orchestrator) | n8n DAGs + Council Orchestrator |
| Sub-agents with isolated contexts | Perspective agents (parallel, no cross-contamination) |
| Journal (pause/resume state) | Episodic Memory + Trajectory Modeler |
| Multi-model per phase | Skill registry with per-model assignment |
| 16 concurrent agents | Council size + parallel deliberation |
| Verify stage (adversarial 3-vote) | Governance check (Validated / HumanReview / Rejected) |
| Startup Forge (judge + skeptics) | Chairman + Devil Advocate perspective |
| Deterministic loops | Bounded deliberation with turn budget |
| Only final answers return to main | Chairman receives only position summaries |

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Deterministic orchestration** (script over LLM) | Moving manager from context to script is the key architectural insight |
| **Isolated contexts for parallel agents** | Sub-agents with no cross-contamination |
| **Multi-model routing** | Different models per phase = different skills per perspective |
| **State persistence for resume** | Journal enables pause/resume — OCR needs trajectory + episodic memory |
| **Token budget awareness** | 3.1M tokens for 15 min research — context burn is real |
| **Human-in-loop for approval** | Level 2 control: inspect before run |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **Orchestrator in script, not context** | OCR's Council Orchestrator should be a deterministic script (or n8n DAG), not an LLM managing state in its context |
| **Journal for state management** | Separates orchestration state from LLM context — this is the key pattern for resume and reliability |
| **Adversarial validation pattern** | 3-vote fact-checking, 2/3 kills. OCR's governance should use similar adversarial verification |
| **16 concurrent agents as practical max** | OCR can benchmark council size against 16 concurrent agents |
| **Deep research is 3M tokens per use** | OCR should budget for heavy governance checks vs lightweight ones |
| **Skills for daily, Workflows for complex** | OCR should distinguish between routine shipments (skills) and complex investigations (councils) |
| **Persona prompting for multi-lens review** | Each skeptic has a distinct lens — confirms OCR's perspective agent design |
