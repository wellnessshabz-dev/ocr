---
title: "Eval Maturity for AI Agents — Phil Hetzel (BrainTrust)"
source_type: "youtube"
channel: "AI Engineer"
speaker: "Phil Hetzel"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "AI Engineer conference talk. Phil Hetzel leads solutions engineering at BrainTrust, an agent quality company. Prior: Slalom Consulting (global Databricks lead), KPMG."
tags: ["evals", "eval-maturity", "llm-as-judge", "observability", "production-traces", "eval-flywheel", "braintrust"]
---

# Eval Maturity for AI Agents — Phil Hetzel, BrainTrust

Source: AI Engineer conference. Phil Hetzel, BrainTrust (agent quality platform).

## Core Thesis

Eval maturity is a continuum that grows with agent complexity. Start with
human annotation (vibes + justification), then automate with LLM-as-judge,
then handle multi-step tool calls, then discover failure modes at scale.
The goal: **evals are not tests — they're production replayed in a safe
environment.**

## Eval Primitives

Every eval has three components:

1. **Task** — The agent or prompt under test
2. **Dataset** — Examples that initiate the task (edge cases, production traces)
3. **Scoring functions** — How you judge quality (LLM-as-judge, deterministic code, human annotation)

## Four Maturity Levels

### Level 1: Just Getting Started — Human Annotation

**What**: Run agent against ~10 example inputs, human annotator gives thumbs
up/down + justification.

**Key insight**: The justification matters more than the score. Extract domain
knowledge from the human's head so it can be scaled via LLM-as-judge later.

**Don't give users a generic annotation platform** — customize the view to
match how they think about agent traces. This encourages adoption.

### Level 2: Measuring to Manage — LLM-as-Judge

**What**: Use the human justifications to derive failure modes, then automate
scoring with LLM-as-judge or deterministic checks.

**Critical warning**: "Putting a robe and a cloak on an LLM doesn't make it
inherently more trustworthy." **Eval your eval** — create a ground truth
dataset for the judge and verify alignment with human decisions.

**The Eval Flywheel**:
```
Production traces → identify failures → offline eval → improve agent → repeat
```

Also: **use production traces in your eval dataset.** Don't write synthetic
tests — replay real production inputs.

Deterministic scoring is valid too: token count, tool call frequency, latency
— anything measurable in code.

### Level 3: Accounting for Complexity — Multi-Step Agents

**What**: Agents that make tool calls (context-gathering or CRUD). Now you
need to evaluate entire traces, not just final outputs.

**Two types of tool calls:**
- **Context-gathering**: Read-only (search, lookup, query)
- **CRUD**: Create, Read, Update, Delete (side effects)

**Two hard problems:**
1. Representing external system state at eval time (what was the DB state when
   this input was recorded?)
2. Preventing CRUD operations from mutating production data during eval

**Solutions:**
- **Inject state into traces**: Captured system state is part of the eval context
- **Timestamp queries**: For vector DBs and versioned systems, query "as of" timestamp
- **Mock APIs**: Approximate production environment without side effects

### Level 4: Advanced — Automated Failure Mode Discovery

**What**: Topic modeling at scale to automatically surface failure modes from
production traces. CI/CD integration via eval provider CLI.

**Emerging patterns:**
- Automated topic clustering of failed traces → identify new failure modes
- Eval-as-code: CLI-driven eval pipelines in CI/CD
- Continuous eval: production traces automatically feed eval datasets

## Key Principles

1. **Evals are not unit tests** — don't try to exhaustively cover everything.
   Start high-level with failure modes, not edge cases.

2. **Eval results don't need to be perfect** — directional trending is fine.
   Non-deterministic scoring (LLM-as-judge) is okay if trending correct.

3. **Production traces > synthetic tests** — the best eval dataset is replaying
   real production inputs. "Evals are rerunning production in a safe environment."

4. **Eval your eval** — LLM-as-judge needs its own ground truth dataset.
   Judge alignment can be measured deterministically because judge outputs are
   discrete (pass/fail).

5. **State is the hardest problem** — representing external system state at
   eval time is not fully solved. Use trace injection + timestamp queries as
   practical approximations.

## Relevance to OCR

### The Eval Flywheel is OCR's Learning Loop

Phil's flywheel maps directly to OCR's architecture:

| Flywheel Step | OCR Component |
|--------------|---------------|
| Capture production traces | replay/ + observability/traces |
| Identify failures | observability/ + human review (governance) |
| Offline eval | shipments/replay/ — replay past shipments through current pipeline |
| Improve agent | ontology/ + gbrain/ — update based on failures |
| Repeat | The continuous pipeline |

### Eval Maturity Maps to OCR's Build Order

Phil's four levels describe exactly the progression OCR should follow:

1. **Human annotation** (Level 1) — Start with human review of scrape results
   from ingestion/web/. Thumbs up/down with justification.

2. **LLM-as-judge** (Level 2) — Scale with automated scoring once failure modes
   are understood. Build the ground truth dataset from Level 1 annotations.

3. **Multi-step traces** (Level 3) — Full shipment pipeline (compile → council →
   chairman → governance). Each stage is a tool call that needs evaluation.

4. **Automated discovery** (Level 4) — Topic modeling of failed shipments to
   automatically surface new failure modes. Continuous eval in CI/CD.

### Confirms Existing Decisions

- **Evals as ETL** (architecture synthesis): Phil's flywheel is ETL —
  Extract (production traces) → Transform (eval pipeline) → Load (improvements)
- **Evals as precondition** (ADR-0006): Phil starts Level 1 with human
  annotation — not automated evals. Start humble.
- **Golden dataset needed**: Level 2 requires a ground truth dataset for judge
  alignment — same as our golden eval dataset.
- **Observability = evals**: Phil says evals and observability are "the same
  problem from a systems perspective" — validates putting them in the same
  architectural layer.

### What Phil Adds That No One Else Does

| Insight | OCR Application |
|---------|-----------------|
| **Eval maturity as a continuum** | Don't try to build Level 4 immediately. Start with human annotation. |
| **Justification > score** | When humans evaluate, capture WHY not just pass/fail. This builds the ground truth for automation. |
| **Stateful evals** | The hardest problem in eval is representing external state. OCR's shipment pipeline is stateful — each shipment depends on ontology/ + gbrain/ state at the time. |
| **Eval your eval** | Don't trust LLM-as-judge blindly. Build a meta-eval dataset to verify judge alignment. |
| **Production traces as dataset** | The eval dataset should be replayed production, not synthetic tests. OCR's replay/ directory is the eval dataset. |
| **Tool call : context-gathering vs CRUD** | OCR's pipeline has both: context-gathering (ontology lookups, memory queries) and CRUD (writing to ledger, gbrain). Each needs different eval approaches. |
