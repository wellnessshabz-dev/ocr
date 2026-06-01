---
title: "The Handoff Skill — Agent-to-Agent Context Handoff (Matt Pocock)"
source_type: "youtube"
channel: "Matt Pocock"
speaker: "Matt Pocock"
date: "2026-05"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Matt Pocock's personal YouTube channel. This video shows his handoff skill for passing context between AI coding sessions."
tags: ["handoff", "compact", "context-window", "intentional-compaction", "sub-agents", "parallel-decomposition", "temp-directory", "cross-agent", "grilling", "prototype"]
---

# The Handoff Skill — Agent-to-Agent Context Handoff (Matt Pocock)

Source: Matt Pocock's personal YouTube channel. Deep dive into his "handoff"
skill for passing compressed context between independent agent sessions.

## Core Thesis

**Handoff is the natural evolution of compact.** Compact helps you continue a
single session past the dumb zone. Handoff helps you decompose a single session
into parallel independent sessions. Both manage context window growth, but they
serve different purposes and produce different topologies of work.

## Smart Zone vs Dumb Zone

Even with 1M token context windows, performance degrades after ~120k tokens:
- **Smart zone** (~0–120k tokens): Agent can focus, attention relationships are
  not strained, responses are high quality
- **Dumb zone** (~120k+): Attention is too diffuse, agent gets progressively
  dumber
- **Practical limit**: ~120k tokens before the agent noticeably degrades

The implication: you need to budget context even with large windows. This
confirms Dex Horthy's smart/dumb zone model with a concrete ceiling.

## Compact: Single-Session Continuation

Compact summarizes a large conversation into a smaller artifact:
- Input: Large conversation near dumb zone
- Output: Summary (files referenced, things said, conversation tone)
- Result: Back to smart zone, but with sediment (layers of past compactions)
- Use case: Long-running single sessions, especially debugging (save state,
  try things, compact again)

**Matt still uses compact** and considers it useful. But it creates "sediment"
(compacted layers) that accumulates and is somewhat inefficient.

## Handoff: Multi-Session Parallel Decomposition

Handoff compresses the current context into a markdown file for another session:
- Input: Current session context + a specific purpose/focus
- Output: `handoff.md` file saved to OS temp directory
- Result: Two independent sessions running in parallel

**Primary use case**: During a session, notice something out-of-scope but
important → hand it off to another session instead of extending current one.

## Key Design Decisions of the Handoff Skill

### 1. Save to OS temp directory (disposable)

Handoff files go to the OS temp directory, NOT the workspace. They are
**transient artifacts** — not documentation. They should not rot in the
codebase. This is the same principle as ephemeral storage: if it's meant
to be consumed by another agent, don't commit it.

### 2. Include suggested skills

The handoff document includes a `suggested skills` section so the next
session knows which skills to invoke (grill with docs, diagnose, prototype).
This means the handoff carries not just context but also **session flavor** —
the receiving agent knows how to approach the work.

### 3. Don't duplicate content already in artifacts

If the context is already captured in a GitHub issue, markdown file, or code
comment, just use a pointer instead of repeating it. This keeps handoff
documents lean and self-referencing.

### 4. Redact sensitive information

API keys, passwords, PII must be stripped. Handoff files in temp directories
should not leak secrets.

### 5. Tailor the document to the purpose

If the user provides arguments describing what the next session will focus on,
the handoff document is tailored accordingly. The agent needs to know the
purpose of the next session to write a good handoff.

## Usage Patterns

### Pattern 1: Out-of-Scope Task (Spawning)

```
Session A (main task)
  → notices refactoring opportunity (out of scope)
  → handoff: create handoff.md for Session B
  → Session B (refactoring) runs independently
  → Session A stays pure (focus intact)
```

This is the simplest pattern. Session A defines the scope boundary explicitly
by handing off. The act of declaring the handoff sharpens the current session.

### Pattern 2: Grilling → Prototype → Grilling (Return)

```
Session A (grilling/planning)
  → hits question that needs prototype
  → handoff: create handoff.md for prototype session
  → Session B (prototype) implements UI/logic prototype
  → Session B handoff: create handoff.md returning learnings to Session A
  → Session A resumes with prototype insights
```

This is the **parent-child-return** pattern. Session B creates a handoff
document that captures learnings (non-obvious things not captured in the
prototype itself) and passes it back to Session A. The prototype session
was 169k tokens (wouldn't have fit in the grilling session).

**This is a DIY sub-agent.** Two complete sessions communicating via
handoff documents. No shared context, no cross-contamination.

### Pattern 3: Cross-Agent Handoff

The handoff is a plain markdown file — not tied to any specific coding agent.
You can create a handoff in Claude Code and pass it to Cursor, Copilot CLI,
Codex, or any other agent. This enables:
- Adversarial review (one agent reviews another agent's work)
- Cross-platform pipelines
- Best-tool-for-the-job composition

## How Handoff Differs from Compact

| Property | Compact | Handoff |
|----------|---------|---------|
| **Purpose** | Continue same session | Start a new session |
| **Output** | Session summary (same session) | Markdown file (separate session) |
| **Parallelism** | No — linear continuation | Yes — independent parallel sessions |
| **Sediment** | Yes — layers accumulate | No — each handoff is standalone |
| **Scope** | Same scope, deeper | Out-of-scope tasks |
| **Cross-agent** | No (harness-specific) | Yes (plain markdown) |
| **Lifespan** | Session lifespan | Transient (temp dir) |

## Relevance to OCR

### Handoff = Shipment Pipeline

OCR's shipment pipeline is a series of handoffs:
1. **Ingestion** → compiles raw signal into a shipment
2. **Compiler** → enriches with ontology context
3. **Council** → deliberates, creates positions
4. **Chairman** → synthesizes positions
5. **Governance** → validates and commits

Each gate receives a context slice (handoff), processes it, and produces a
denser context slice for the next gate. Matt's handoff shows the concrete
primitive: a context slice + purpose description + suggested next steps.

### Handoff vs RPI (Dex Horthy)

Dex's RPI (Research→Plan→Implement) describes the lifecycle. Matt's handoff
is the **Plan artifact** — the compressed output of Research that feeds into
Implement. The handoff document IS the Plan:

| RPI Stage | Output | Handoff Equivalent |
|-----------|--------|-------------------|
| Research | Notes, findings | Current session context |
| Plan | Plan artifact | handoff.md (compressed intent) |
| Implement | Code/files | Receiving session execution |

### Suggested Skills = Activation Engine

The handoff document's "suggested skills" section maps to OCR's activation
engine, which determines which perspective agents to include in a council.
The handoff carries routing information: "next session should use these skills."

### Disposability Confirms Architecture

Handoff files are disposable (temp directory). This confirms that OCR's
intermediate artifacts (between gates) should be transient. What persists
is the governance record (audit ledger, lineage index) — not the intermediate
context slices.

### Pattern 2 (Parent-Child-Return) = Council Deliberation

The grilling → prototype → grilling pattern is exactly how OCR councils work:
- Chairman sends context slice to each perspective agent
- Each agent returns a position (like prototype returns learnings)
- Chairman synthesizes positions into consensus

Matt's "DIY sub-agent" pattern confirms that structured handoffs between
independent agents produce better results than a single monolithic session.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Intentional compaction** (Dex) | Handoff is intentional compaction with a purpose |
| **Smart zone ceiling** (Dex) | ~120k tokens concrete ceiling confirmed |
| **Don't outsource understanding** (Dex/Karpathy) | Handoff includes purpose — the user must define the "why" |
| **Gates > agents** (Nick) | Handoff defines scope boundaries — gates in practice |
| **Serial gates** (Luke) | Handoff creates serial dependency: A→B→A |
| **Temp/transient storage** | Handoff files go to temp dir, not workspace |
| **Skill routing** (Nick) | Suggested skills = skill activation |
| **Compact as debugging tool** | Long sessions for debugging, handoff for parallel work |

### What Matt Adds That No One Else Does

| Insight | OCR Application |
|---------|-----------------|
| **Handoff as explicit primitive** | GPSDI needs a handoff artifact between gates |
| **DIY sub-agents via handoff** | Sub-agent topology without explicit framework support |
| **Cross-agent portability** | Shipments should be plain markdown, not API-specific |
| **Purpose-driven compaction** | Compaction without purpose is just summarization |
| **Handoff sharpens current session** | Defining scope boundaries improves focus |
| **Return handoff (parent-child-return)** | Pattern for bidirectional sub-agent communication |
| **Temp dir for transient artifacts** | Policy: intermediate artifacts go to temp, not workspace |
