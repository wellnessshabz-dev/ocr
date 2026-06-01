---
title: "Harness Engineering — The Four Levers of Agent Design (Damian Galzara)"
source_type: "youtube"
channel: "Damian Galzara"
speaker: "Damian Galzara"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Damian Galzara's YouTube channel. Framework for diagnosing agent failures through four levers: context, tools, loop, and governance. Harness engineering as the system around the model."
tags: ["harness-engineering", "four-levers", "context", "tools", "loop", "governance", "diagnostic", "agent-failures", "harness-over-model"]
---

# Harness Engineering — The Four Levers of Agent Design (Damian Galzara)

Source: Damian Galzara's YouTube channel. A diagnostic framework for agent
failures: context, tools, loop, and governance — the four levers of the
harness.

## The Evolution

| Stage | Model Role | Path Owner |
|-------|-----------|------------|
| **LLM Features** | Perform transformation (summarize, classify, rewrite) | App/code |
| **Workflows** | Multiple LLM calls coordinated by code | Mostly code |
| **Agents** | Decide what to inspect, which tool, whether result is enough | Model owns part of the path |

The more control you give the model, the more the surrounding system (the
harness) matters.

## The Four Levers

### 1. Context — What the Model Can See

Everything the model sees at the moment it needs to make a decision:
- System prompt, conversation history, retrieved documents
- Memory files, codebase docs, screenshots, logs
- Tool descriptions (model can only choose tools it understands)
- State accumulated while working

**Failure modes**:
- Information exists somewhere but not surfaced where model decides
- Too much information — signal gets buried. More context ≠ better context.

**Diagnostic**: Did the model have the right information in the right shape
at the right moment?

### 2. Tools — What the Model Can Do

How the model affects the outside world:

| Tool Type | Tradeoff |
|-----------|----------|
| **Local functions** | Controlled, domain-specific |
| **MCP** | Portable, reusable |
| **CLI/shell** | Extremely flexible, harder to govern |

**Diagnostic**: Does the agent have the right action surface exposed in a way
the model can understand and use effectively?

### 3. Loop — How the Agent Keeps Moving

Typical agent loop:
1. Model receives prompt + current context
2. Looks at available tools, decides if action needed
3. Requests tool call → harness runs it → returns result
4. Model interprets result: answered? failed? new problem? need another call?
5. Repeat until done, blocked, or harness stops

**Failure modes**: No clear stopping conditions → runaway agents (keep calling
tools, searching, retrying, checking one more thing).

**Controls needed**: Max steps, time limits, no-progress detection, explicit
completion criteria.

**Diagnostic**: Did the agent know what to do next, when to continue, and when
to stop?

### 4. Governance — What Keeps Autonomy in Check

The lever that separates demo from production:
- Permissions, approval gates, sandboxing
- Audit logs, rate limits, environment boundaries
- Blast radius design

**Failure modes**:
- Too constrained → agent can't finish the task
- Too unconstrained → agent takes unintended action

**Diagnostic**: What can the agent do automatically? What requires approval?
What should be out of bounds entirely?

## The Diagnostic

> When an agent fails, the useful question is not "why is the model bad?"
> It's **which lever broke?**

1. **Context** — Did the model have the right information in the right shape
   at the right moment?
2. **Tools** — Did it have the right action surface exposed clearly and safely?
3. **Loop** — Did it know what to do next, when to continue, and when to stop?
4. **Governance** — Did it have the right permissions, approval gates, and
   boundaries?

## Core Thesis

> "The model sets the ceiling, but the harness determines how much of that
> capability you actually get to use."

A better harness makes a smaller model look smarter. A frontier model in a
bad harness looks dumb. Model choice is only part of the story.

## Relevance to OCR

### The Four Levers = OCR's Architecture Layers

| Lever | OCR Component |
|-------|--------------|
| **Context** | Ontology (semantic memory), GBrain (working + episodic), shipment context slice |
| **Tools** | MCP servers, skill registry, perspective agent tool access |
| **Loop** | Shipment pipeline (GPSDI gates), council deliberation loop, governance retry |
| **Governance** | Policy engine, audit ledger, approval gates, blast radius controls |

### Diagnostic Framework for OCR Shipments

When a shipment fails governance or produces poor output, ask which lever
broke:
- **Context**: Was the ontology incomplete? Was the context slice too large
  (signal buried)?
- **Tools**: Did the council have the right perspective agents? Were MCP
  connections working?
- **Loop**: Did the pipeline loop without clear stopping conditions? No-progress
  detection?
- **Governance**: Too constrained (false rejection)? Too unconstrained (bad
  decision committed)?

### Model Sets Ceiling, Harness Determines Delivery

This directly validates OCR's architecture: OCR doesn't depend on frontier
models. The harness (ontology + pipeline + governance + gates) determines what
fraction of any model's capability actually reaches the organizational
decision. A better OCR harness makes a cheaper model produce better decisions.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Harness > prompts** (Tejas) | Four levers = harness levers |
| **Gates > agents** (Nick Nisi) | Governance = the lever that separates demo from production |
| **Deterministic guardrails** (Daniel/Tejas) | Governance should be deterministic gates, not prompts |
| **Context bounding** (Dex/Patrick) | More context ≠ better context |
| **Loop controls** | Max steps, time limits, no-progress detection |
| **Blast radius design** | OCR's blast_radius in _index.md files |
| **Model tiering** | Harness determines delivery, not model ceiling |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **Diagnostic framework** | When a shipment fails, ask which lever — not "why is the model bad" |
| **Four lever model** | Shared vocabulary for harness architecture review |
| **Context can be too much** | "More context is not automatically better" — bounding is essential |
| **Tool surface tradeoffs** | Local vs MCP vs CLI — each has different governance properties |
| **Loop design = stopping conditions** | Pipeline needs explicit done criteria per gate |
| **Governance as the production lever** | Without it, cool demo never becomes trusted system |
