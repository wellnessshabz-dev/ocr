---
title: "Nine Things People Get Wrong With Grill Me / Grill With Docs (Matt Pocock)"
source_type: "youtube"
channel: "Matt Pocock"
speaker: "Matt Pocock"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Matt Pocock's personal YouTube channel. Advanced usage guide for Grill Me/Grill with Docs — failure modes, high/low fidelity questions, scope management, active vs passive, model selection, parallel sessions."
tags: ["grill-me", "grill-with-docs", "planning", "high-fidelity", "low-fidelity", "scope", "active-vs-passive", "parametric-knowledge", "contextual-knowledge", "parallel-sessions", "shape-up"]
---

# Nine Things People Get Wrong With Grill Me / Grill With Docs (Matt Pocock)

Source: Matt Pocock's personal channel. Advanced guide to using planning
skills effectively — the failure modes and how to fix them.

## The Core Problem

Grill Me and Grill with Docs are popular as replacements for plan mode in
agents. But people report "it asked me 200 questions" — because the skills
rely on the **skill of the person answering**. The user needs to be good at
planning, scope, and knowing what questions need what fidelity.

## Key Lenses

### 1. High-Fidelity vs Low-Fidelity Questions (from Ryan Singer's Shape Up)

| Type | Definition | Example | Grillable? |
|------|-----------|---------|-----------|
| **Low-fidelity** | Answerable with Q&A | URL routes, basic decisions | ✅ Yes |
| **High-fidelity** | Needs a zoomed-in, detailed image | UI feel, form layout across pages | ❌ Ungrillable |

**Failure mode**: Trying to answer high-fidelity questions during a grilling
session. You can't plan your way to a feeling. You need to see it.

**Fix**: **Prototyping handoff** pattern:
```
Grill session → hits ungrillable question → handoff → prototype session
  → prototype learns → handoff back → grill session continues
```

This is the same pattern as Matt's earlier handoff video (grilling →
prototype → grilling) but framed specifically around question fidelity.

### 2. Scope Management

**Failure mode**: Grilling too large a scope. Two problems:
- Hidden high-fidelity questions emerge
- Hit the dumb zone (~120k tokens for frontier models) before answering half
  the questions

**Fix**: Ask the agent to decompose large scope into smaller scopes upfront.
Grill each sub-scope individually. Each stays within the smart zone.

### 3. Active vs Passive

| Mode | Symptom | Cause |
|------|---------|-------|
| **Too passive** | Agent asks 540 questions, scope explodes | Letting agent lead the interview |
| **Too active** | Endless grilling, never getting to code | Never hitting the "ungrillable → build" transition |

**Fix**: "It's a conversation, not an interview." Take an active hand in
leading the direction, but know when to stop planning and start building.

### 4. Valuing the Grilling Artifact

**Failure mode**: People clear the context and start a new session before
creating a PRD/handoff. They discard 100k tokens of valuable design decisions.

**Fix**: The grilling session IS the artifact. Preserve decisions by:
- Implementing directly from the session (if enough budget remains)
- Creating a handoff document (PRD) from the session before closing
- Never clearing context without capturing the decisions

### 5. Model Selection for Grilling vs Implementation

| Phase | Knowledge Source Needed | Model Required |
|-------|------------------------|----------------|
| **Grilling** | Parametric knowledge (model's innate understanding of systems, off-the-wall suggestions) | **Smart model** (lots of parameters, frontier) |
| **Implementation** | Contextual knowledge (files, plan, codebase) | **Can use dumber model** |

Parametric knowledge is what makes grilling work — the model's training on
thousands of systems gives it the ability to suggest things you haven't
considered. Dumber models don't have this.

**Fix**: Use a smart model for grilling/planning, a cheaper model for
implementation (where context dominates).

### 6. Parallel Grilling Sessions

Run 2 grilling sessions simultaneously. Flip between them like Slack threads.

- Max 2-3 sessions (2 comfortable, 3 if one is doing long research)
- Doubles throughput
- Gets more planning done in less time
- Requires mental capacity — gets easier with practice

## Summary of the Nine

1. Trying to answer high-fidelity (ungrillable) questions in a grilling session
2. Grilling too large a scope (hidden high-fidelity + dumb zone)
3. Being too passive (agent leads, scope explodes)
4. Being too active (never getting to code)
5. Discarding the grilling session context (clearing without capturing)
6. Using too dumb a model for grilling (needs parametric knowledge)
7. Not using parallel sessions (leaving throughput on the table)
8. (Implicit) Not knowing the smart zone ceiling (~120k tokens)
9. (Implicit) Not understanding when to handoff vs implement directly

## Relevance to OCR

### Grilling = Council Deliberation

The high/low fidelity distinction maps to OCR's council structure:

| Grill Phase | OCR Equivalent |
|-------------|----------------|
| Low-fidelity (grillable) | Council positions on known entities |
| High-fidelity (ungrillable) | Requires prototype → HumanReview or executive surface |
| Prototyping handoff | Shipment sent to specialized council (deeper expertise) |
| Handoff return | Synthesis from sub-council feeds back to main council |

### Scope Decomposition = Shipment Bounding

Large scopes must be decomposed before grilling. OCR's context bounding engine
does exactly this — it takes a large signal and bounds it to a manageable
shipment scope. If the shipment is too large, it should be split.

### Active vs Passive = Chairman's Role

The chairman must be **active** in council deliberation — leading the
conversation, keeping scope tight, knowing when to push for synthesis. A
passive chairman lets perspectives explode in scope. An overly active chairman
never gets to synthesis.

### Parametric vs Contextual Knowledge

This distinction has implications for OCR's model selection strategy:
- **Council deliberation** (grilling phase) → needs frontier model (parametric
  knowledge for creative challenge, contradiction detection)
- **Governance** (verification phase) → can use cheaper model (contextual
  knowledge dominates — checking against known rules and ontology)

### Parallel Councils

Matt runs parallel grilling sessions. OCR should support parallel council
deliberations for independent shipments. Each shipment has its own council
with its own context window.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Prototyping handoff pattern** | Ungrillable questions → handoff → prototype → return |
| **Context bounding** | Large scope must be decomposed before processing |
| **Chairman as active leader** | Active vs passive — chairman must lead deliberation |
| **120k smart zone** (Dex Horthy) | Confirmed: frontier models degrade beyond ~120k |
| **Model tiering** (Nate Herk) | Smart model for planning, cheap for implementation |
| **Handoff as primitive** (Matt) | Handoff is the mechanism for both parallel and sequential work |
| **Design decisions as artifacts** | Grilling context must be preserved — don't clear |

### What Matt Adds

| Insight | OCR Application |
|---------|-----------------|
| **High/low fidelity framework** | Determines when to deliberate vs when to prototype |
| **Ungrillable as a concept** | Some questions can't be planned — must be built |
| **Parametric vs contextual knowledge** | Drives model selection strategy per pipeline stage |
| **Parallel sessions** | OCR should support parallel council deliberation |
| **Scope decomposition upfront** | Bounding engine must decompose, not just bound |
| **Grilling context is the artifact** | GPSDI phases should accumulate, not discard |
| **Shape Up language for planning** | Borrowed from Ryan Singer — useful shared vocabulary |
