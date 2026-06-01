---
title: "Claude Code Dynamic Workflows — The Ladder of Complexity (Nate Herk)"
source_type: "youtube"
channel: "Nate Herk"
speaker: "Nate Herk"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Nate Herk's YouTube channel. Deep dive into Claude Code's dynamic workflows feature, comparing skills, sub-agents, agent teams, /goal, and workflows across a complexity/expense ladder."
tags: ["dynamic-workflows", "claude-code", "sub-agents", "agent-teams", "skills", "parallel-execution", "synthesis", "ultra-code", "deep-research"]
---

# Claude Code Dynamic Workflows — The Ladder of Complexity (Nate Herk)

Source: Nate Herk's YouTube channel. Breakdown of Claude Code's dynamic
workflows feature — how it differs from skills, sub-agents, agent teams, and
/goal, and when to use each.

## The Feature: Dynamic Workflows

Claude Code writes a **JavaScript file** that orchestrates many parallel agents.
Each agent is a full Claude call with its own context window. Results from all
agents are merged and sent back to the main Claude session for synthesis.

**Demo**: Analyzed 41 skills using 41 Haiku scoring agents + 1 Opus synthesis
agent. 5M input tokens consumed, produced a ranked HTML report with fix
suggestions and patterns.

## The Ladder of Complexity (Expense Increases Upward)

| Level | Name | Model | Communication | Best For |
|-------|------|-------|---------------|----------|
| 0 | **Chat** | Single session | Human ↔ Agent | Quick questions, single edits |
| 1 | **Skill** | Reusable recipe | Automated recipe | Repeatable processes |
| 2 | **Sub-agent** | 1+ parallel agents | Agent ↔ Main session only | Messy side tasks, parallel research |
| 3 | **Agent Team** | Small crew | Agents talk to each other | War rooms, councils, debates |
| 4 | **Workflow** | JS-orchestrated swarm | Agents → Synthesis (no agent-to-agent) | Giant parallel jobs |
| ∞ | **/goal** | Loop until done | Agent keeps retrying until criteria met | Long-running autonomous tasks |

### Key Distinctions

**Skill vs Workflow**: Skill is the "how" (reusable recipe). Workflow is the
"how many" (width/depth of parallel execution).

**Goal vs Workflow**: Goal is **depth** — a loop that keeps going until
`done == true` (can run 24h+). Workflow is **width** — many parallel agents
that execute once, results synthesized.

**Agent Teams vs Workflow**: Teams have agents that **talk to each other**
(group chat model). Workflows have agents that work **independently** and only
return results to the main session for synthesis.

## When to Use a Workflow

> "Does this break into many pieces that can run independently in parallel?"

Good candidates:
- Reviewing every file in a codebase (400-file migration)
- High-risk work needing maximum compute per piece
- Bulk analysis (audit all skills, rank features)
- Deep research (built-in `/deep research` — agents vote on each claim)

Bad candidates:
- Single edits, quick questions
- General knowledge work
- Tasks that are already fast with a single agent

## Cost Characteristics

- One workflow burned through 50% of a $200/month plan in one prompt
- 30+ minutes runtime for a 41-agent audit
- 5M input tokens consumed (mostly input, less expensive than output)
- Each agent = full Claude call with its own context window
- Can reduce cost by putting workers on **Haiku** (cheaper) and only synthesis
  on **Opus**
- **Ultra Code mode** = X-high effort reasoning + default workflows + bypassed
  permissions — most expensive

## Hidden Features & Caveats

1. **Confirmation required** — Workflows always confirm before running. Won't
   accidentally invoke.
2. **Save location** — By default, workflows save to Claude's global working
   directory, not your project. Must explicitly tell it to save in-project.
3. **`/workflows`** — View all running workflows, check token usage, tools,
   duration per agent.
4. **`/deep research`** — Built-in workflow that spins up research agents,
   they vote on each claim, produces a cited report.
5. **Workflows are JavaScript files** — Can be saved, rerun, edited. Live in
   `.claude/workflows/`.
6. **Agents in workflows can use skills, MCP servers, API keys** — All
   configured tooling is available to each worker agent.
7. **Nesting possible** — Workflow inside a /goal (but very expensive).
8. **Explicit invocation best** — "Set up a dynamic workflow to do this" works
   better than just saying "workflow" (which might not trigger the feature).

## The Ultimate Decision Matrix

| If you have this... | Use this... |
|--------------------|-------------|
| Quick thing | Chat (just ask) |
| Thing you repeat | Skill |
| Messy side task | Sub-agent |
| Small crew that talks | Agent Team |
| Keep going until done | /goal |
| Giant parallel job | Dynamic Workflow |

## Relevance to OCR

### Workflow = Shipment Pipeline Orchestrator

Claude Code's dynamic workflow is a **horizontal parallel decomposition** —
exactly what OCR needs for batch processing. The workflow is a JS file that
orchestrates agents; OCR's pipeline is a DAG that orchestrates gates.

### The Ladder = OCR's Processing Modes

| Claude Feature | OCR Equivalent |
|----------------|----------------|
| Chat (single session) | Single shipment processing |
| Skill (reusable recipe) | Skill registry / activated skill |
| Sub-agent (parallel, no cross-talk) | Perspective agents in council |
| Agent Team (crew, cross-talk) | Council deliberation with debate rounds |
| Workflow (JS orchestrated parallel) | Batch shipment processing DAG |
| Synthesis agent | Chairman synthesizer |

### Parallel Agent Pattern

The demo (41 Haiku workers + 1 Opus synthesis) is a **map-reduce** pattern:
- Map: each agent scores one skill independently
- Reduce: synthesis agent ranks all results

This confirms the pattern for OCR's batch decisions: map ontology entities
across perspective agents, reduce through the chairman.

### Cost Scaling Awareness

Nate's cost warning (50% of $200 plan in one prompt) is a direct caution for
OCR's design: parallel agent orchestration is expensive. OCR must:
- Use cheaper models for worker perspective agents (Haiku-level) and reserve
  expensive models for synthesis (Opus-level)
- Bound scope explicitly in every shipment
- Name deliverables clearly so agents know when done
- Monitor token burn per shipment

### /goal vs Workflow = Depth vs Width

This distinction maps to OCR's two processing modes:
- **Depth mode** (serial): A shipment loops through refinement until governance
  validates it. Each retry is a deeper pass.
- **Width mode** (parallel): A batch of independent shipments processed
  simultaneously, each through its own gate.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Parallel perspective agents** | Workflow = horizontal parallelism |
| **Chairman synthesis** | Opus synthesis agent merging Haiku workers |
| **Council independence** (no cross-talk) | Workflow agents don't talk to each other |
| **Serial processing** (Luke Alvoeiro) | /goal = depth loop, workflow = width |
| **Skills as building blocks** | Skills nest inside workflows |
| **Expense awareness** | Each agent = full call, workers should be cheap models |
| **Handoff pattern** (Matt Pocock) | Workflow = handoff at harness level |
| **Map-reduce for evaluation** (Phil Hetzel) | 41 workers + 1 synthesis = eval pipeline |

### What Nate Adds

| Insight | OCR Application |
|---------|-----------------|
| **The ladder framework** | Clear decision tree for which execution mode to use |
| **Depth vs width** | /goal (depth) vs workflow (width) — OCR needs both modes |
| **Workflow = JS file** | Pipeline definition as executable artifact (not runtime state) |
| **Ultra Code mode** | Most expensive mode: X-high + default workflows — a caution |
| **Save location gotcha** | Artifacts go to global dir by default — explicit path needed |
| **Cost tracking per agent** | `/workflows` shows per-agent token/tool/duration |
