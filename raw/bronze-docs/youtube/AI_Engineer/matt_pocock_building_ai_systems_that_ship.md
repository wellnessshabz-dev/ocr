---
title: "Building AI Systems That Ship — Matt Pocock Workshop"
source_type: "youtube"
channel: "Matt Pocock"
date: "2026-06"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Live workshop transcript, reasoned and structured by OCR system."
tags: ["ai-agents", "workflow", "tdd", "vertical-slices", "deep-modules", "kanban-dag", "grill-me", "sandcastle", "ubiquitous-language", "code-is-not-cheap", "design-interface-delegate-implementation"]
---

# Building AI Systems That Ship — Matt Pocock

Sources:
- Main conference talk at AI Engineer, June 2026 — "Code is Not Cheap" thesis,
  Ubiquitous Language skill, specs-to-code critique
- Workshop at AI Engineer, June 2026 — Live demo with TypeScript toolchain
  (Sandcastle, Grill Me, once.sh patterns)

## What Matt Builds

Matt's stack:
- **Grill Me**: A skill/agent pattern that interviews the AI on an idea until "shared
  understanding" (Frederick Brooks' "design concept") is reached. Not a spec — an
  alignment ritual. The output is a PRD that summarizes the alignment, not a
  requirements document to be read cover-to-cover.
- **PRD → Kanban board**: The PRD is decomposed into issues arranged in a DAG
  (directed acyclic graph) with blocking relationships. NOT a sequential plan.
- **AFK Agent**: After planning, implementation runs autonomously using
  Sandcastle (a TypeScript library for running parallel AI agents with Docker
  sandboxing, automated review, and merge).
- **once.sh**: Shell scripts for one-shot bootstrapping (e.g., `init-repo.sh`
  that sets up a new project skeleton). He has many of these.

## Core Concepts

### 1. Smart Zone / Dumb Zone

LLMs have a ~100K token "smart zone." Beyond that, performance degrades. This
directly confirms Nick Nisi's observation about context dropping and Dex Hardy's
observation about context limits. The implication for OCR: **shipments must be
sized to fit in the smart zone.** A council deliberation that exceeds the smart
zone produces worse outcomes, not better.

### 2. Memento Memory

LLMs forget everything when context is cleared. Matt frames this as a *feature*,
not a bug: don't try to compact context (repeating/summarizing for continuation),
because a fresh start is always a clean state. The starting state is deterministic.
This means **OCR's council orchestrator should prefer fresh invocations with
tight context slices over long-running conversations with context compaction.**

### 3. Shared Understanding > Plan Reading

The Grill Me skill doesn't produce a plan for humans to read. It produces
alignment — the AI and the builder reach a shared understanding of the design
concept. The PRD is a summary artifact, not a reference document. Nick Nisi
would agree: he said "skills should be gotchas, not comprehensive references,"
because comprehensive docs degrade agent performance. Matt extends this to
PRDs: don't keep them in the repo after implementation because agents find stale
docs and get confused (doc rot).

**OCR Connection**: `cognition/councils/` should implement the Grill Me pattern.
When a shipment arrives, the council shouldn't just produce a position — it should
grill the shipment: ask hard questions, test assumptions, reach shared understanding.
The chairman's synthesis is the PRD equivalent: a summary of the alignment, not
the truth itself.

### 4. Ubiquitous Language (DDD Shared Vocabulary)

Matt introduces a **Ubiquitous Language skill** based on Domain-Driven Design.
The skill scans the codebase, extracts domain terminology, and creates a shared
vocabulary markdown file — tables of terms with precise definitions that both
the human and the AI agree on.

Why it matters:
- Without shared vocabulary, the AI talks in verbose approximations
- With shared vocabulary, the AI's thinking traces become shorter and more precise
- The human keeps the markdown file open during planning to stay aligned
- Both code and conversation derive from the same domain model

Matt's observation from reading thinking traces: the Ubiquitous Language file
not only improves planning quality but also reduces verbosity in the AI's
reasoning and aligns implementation with the original plan.

**OCR Connection**: This is exactly what `ontology/extraction/` should produce.
Every shipment carries entities; the ontology should maintain a persistent,
evolving vocabulary that both the system and its consumers use. The Ubiquitous
Language is the ontology's human-readable surface — the shared vocabulary
between the cognitive runtime and the organization it serves.

### 5. Kanban DAG > Sequential Plans

Sequential plans can only be worked on by one agent at a time. A Kanban board
with blocking relationships (DAG) allows multiple agents to pick up independent
parallelizable issues simultaneously. Matt's Sandcastle library runs agents in
parallel on these DAGs.

**OCR Connection**: `ontology/graph/` already models relationships between
decisions. The DAG pattern from Matt's Kanban board maps directly to ontology
edge types like `blocks`, `enables`, `contradicts`, `supersedes`. OCR's ontology
should model which shipments/tasks can proceed in parallel and which are blocking.

### 6. Vertical Slices (Traceable Bullets)

Matt's most important operational insight: **AI naturally codes horizontally.**
It builds all the database models first, then all the API endpoints, then all the
frontend. This delays full-stack feedback to the very end. The fix is to explicitly
instruct vertical slices — thin traces that cross every layer (DB → API → frontend)
in a single shot.

Example: for a notification feature, the vertical slice is:
```
1. Add notification model          (DB)
2. Add notification endpoint        (API)
3. Add notification component       (Frontend)
4. Add notification tests           (Tests)
```

Each slice is a "traceable bullet" — you can verify it end-to-end immediately.

**OCR Connection**: This is the Medallion Architecture applied at the feature
level. A shipment should be a vertical slice that crosses Bronze (raw data) →
Silver (structured cognition) → Gold (governed decision) in a single flow.
OCR's current scaffold organizes by layer (ingestion/ separate from cognition/
separate from surfaces/), which is horizontal organization. The challenge is
to make *shipments* vertical while keeping the *codebase* organized by layer.

### 7. TDD is Essential

TDD is not optional when building with AI. The feedback loop (test fails → fix →
test passes) is the only mechanism that prevents the AI from cheating.

**Rate of feedback is your speed limit** (The Pragmatic Programmer):
Matt describes this as "outrunning your headlights" — the AI produces too much
code too fast, doesn't test until the end, and then debug cycles explode. The
fix is to force small deliberate steps with immediate feedback. TDD enforces
this: test → implement → verify → refactor. Each cycle is small enough that
the AI cannot outrun its headlights.

Two specific failure modes TDD prevents:
- **Cheating prevention**: Without a pre-written failing test, the AI will write
  a test that passes trivially (empty implementation, wrong assertions, tautologies).
- **Feedback ceiling**: AI output quality is bounded by the quality of its feedback
  loops. Tests and types provide deterministic feedback. If the feedback loop is
  slow (manual review), the AI outputs will plateau.

Matt's workflow: write the failing test first, commit it, *then* tell the agent
to make it pass. The failing test is a contract.

**OCR Connection**: This is the eval pipeline. OCR's `observability/` layer
should hold the golden eval dataset (failing tests = known outcomes). When a
shipment arrives, run it through the eval pipeline before committing. If pass
rate drops, the gate rejects. This is exactly the Medallion Bronze→Silver gate:
a test to normalize raw shipments.

### 8. Deep Modules > Shallow Modules

Reference: John Ousterhout, "A Philosophy of Software Design."

- **Deep module**: Small interface (few functions, few arguments), lots of
  functionality inside. Easy to test, easy for AI to understand and use.
- **Shallow module**: Large interface (many functions, many arguments, complex
  dependency graph), little functionality per file. Hard for AI to navigate.

Matt's observation: **AI agents naturally produce shallow modules.** They create
many small files with complex cross-references because the AI doesn't feel the
pain of that complexity — the human does, during review. The builder must actively
prevent this by designing module interfaces first and delegating implementation.

**OCR Connection**: How the OCR codebase itself is organized determines how well
AI agents can work on it. Deep modules mean:
- Fewer files per module (not micro-file architecture)
- Clear public interfaces with minimal surface area
- Implementation details hidden inside
- Testability as a first-class design constraint

This should be a code review standard for OCR: reject shallow modules during PR review.

### 9. Design Interface, Delegate Implementation

From deep modules comes a practical workflow: **the human designs the interface,
the AI handles the implementation inside.** The module becomes a "gray box" —
the human doesn't need to review every line of internal code as long as:
1. The interface is well-designed (controlled by the human)
2. The module has a testable boundary at the interface
3. The module is not in a critical path (finance, security, compliance)

This is what makes deep modules powerful for AI-assisted development. You
design the shape of the module, define the contract at the boundary, and let
the AI fill in the internals. The human's brain is preserved for strategic
thinking.

Matt's framing: **AI is a tactical programmer (the sergeant on the ground).
The human is the strategic thinker (the general).** The AI makes the code
changes; the human designs the modules that those changes live inside.

**OCR Connection**: This is the council/worker division. The council (general)
designs the deliberation shape. The skills (sergeants) execute within that
shape. The governance layer tests at the module boundary, not the internals.

### 10. Push vs Pull for Coding Standards

- **Push**: reviewer enforces standards by rejecting bad code. Scales with review
  capacity.
- **Pull**: implementer retrieves standards via skills/agents when they need
  guidance. Scales with agent adoption.

Matt's insight: **push to the reviewer, pull for the implementer.** The reviewer
(the human) sets the bar and enforces it. The implementer (the AI) retrieves
standards on demand. Don't put all coding standards in a document that agents
must read — they won't. Put them in review checklists, skill descriptions, and
automated linters.

**OCR Connection**: Skills should be designed for pull. A skill file is a
reference the AI pulls when it encounters a gotcha situation. The governance
layer (review) enforces via push. This is exactly Nick Nisi's "skills as gotchas"
pattern — the skill is a pull artifact (3-5 failure modes), not a push document
(comprehensive reference).

### 11. Doc Rot

PRDs and architecture docs that stay in the repo after implementation confuse
agents. The PRD describes the *intended* state, but the code *is* the actual state.
When an agent reads both, it resolves the inconsistency by averaging — producing
worse results than reading either in isolation.

Matt's solution: **close issues on GitHub.** Don't keep markdown PRDs in the repo.
The issue tracker is the source of truth for what was done and what is blocked.
Agents should read issues, not docs, to understand current state.

**OCR Connection**: This is a strong design constraint on OCR's documentation
strategy. The `_index.md` system must be a map (directory shapes, connections,
gotchas), not an encyclopedia (detailed summaries of what each file does). The
code is the source of truth. Documentation is a map, not a plan.

### 12. Code is Not Cheap — The Overarching Thesis

Matt's most important message: **bad code is the most expensive it's ever been.**
A codebase that's hard to change cannot take advantage of AI's speed. Every
undisciplined AI change adds entropy. If you don't actively invest in design,
the system degrades with every iteration.

**Specs-to-code movement critique**: Matt tried specs-to-code (write spec → AI
generates code → never touch code, just change spec). Each iteration produced
*worse* code. The compiler analogy breaks because code quality doesn't
deterministically follow from spec quality — the AI makes tactical decisions
that accumulate entropy.

**Software entropy** (The Pragmatic Programmer): Every change to a system,
if you only think about that change and not the system's design, makes the
system worse. AI agents amplify this because they make changes faster than
humans can review. The only countermeasure is conscious design investment
every day.

**Kent Beck**: "Invest in the design of the system every day." This is the
antidote to specs-to-code. Design is not a phase — it's a daily practice.

**OCR Connection**: This is the strongest argument for why OCR needs gates
before agents. The gates are the design investment — the place where entropy
is checked and reversed. Without gates, OCR's cognition pipeline would
accumulate contradictory decisions, orphaned ontology nodes, and degraded
trajectory quality. Every shipment that passes through governance is a
daily design investment.

## Connections to the Eight Threads

| Thread | Connection to Matt Pocock |
|--------|--------------------------|
| **Nick Nisi** | Both emphasize gates, feedback loops, and skills-as-gotchas. Matt adds the *workflow* that Nick's philosophy needs: Grill Me → PRD → Kanban → AFK → QA. Nick provides the *why* (gates over agents), Matt provides the *how* (vertical slices, TDD, deep modules). |
| **Medallion Architecture** | Matt's flow is a Medallion pipeline: Raw idea (Bronze) → Grill Me alignment (Silver) → AFK implementation (Silver→Gold) → Human review (Gold). Each transition has a gate (PRD review, test pass, code review). |
| **Evals as ETL** | TDD maps to evals: write the fail case first (Extract), run the agent (Transform), check pass/fail (Load). Matt's TDD-first workflow is eval-first by another name. |
| **CDLC (Patrick Debois)** | Matt's workflow fits inside Patrick's organizational loop: Generate (Grill Me → PRD) → Evaluate (TDD, code review) → Distribute (skills, once.sh) → Observe (agent logs, production feedback) → Adapt (improve context). Matt provides the *tactical* workflow that Patrick's *strategic* lifecycle orchestrates. |
| **Context Engineering (Dex Horthy)** | Matt's smart zone (100K tokens) gets a specific threshold (40%) and a cure (intentional compaction + RPI). Matt's Grill Me aligns design concept; Dex's Research aligns understanding of the codebase. Matt's TDD provides deterministic feedback; Dex's plan review provides organizational alignment. Both say: don't outsource the thinking. |
| **Karpathy / Software 3.0** | Matt's "Code is NOT cheap" thesis confirmed by Karpathy himself — models produce bloated code. Matt's TDD + deep modules are the answer to Karpathy's jagged intelligence problem: structure and verification compensate for model valleys. Matt's "design interface, delegate implementation" is how Software 3.0 feels in practice. |
| **Boris Cherny / Claude Code** | Boris proves Matt's thesis works at scale — 100% AI-generated codebase, dozens of PRs per day. But Boris agrees with Matt: harness matters now (even if it diminishes later). Matt's deep modules are the code quality discipline that makes Boris's "loops" viable — loops that fix broken things only work if the system is well-structured. |
| **Eval Maturity (Phil Hetzel)** | Matt's TDD-first workflow maps to Phil's eval maturity continuum. Matt writes the test first (failing test = contract); Phil's Level 1 starts with human annotation of outputs. Matt's "rate of feedback = speed limit" means you need evals to bound iteration speed. Phil tells you how to build those evals incrementally. |

## What This Changes for OCR

1. **Council deliberation should follow the Grill Me pattern**: When a shipment
   arrives, the council's first job is alignment — grill the shipment, reach
   shared understanding. The chairman's synthesis is a PRD equivalent, not a
   position paper.

2. **Shipments should be vertical slices**: A shipment crosses
   ingestion → cognition → memory → surfaces in a single trace. If it doesn't
   produce end-to-end feedback, it's not ready for review.

3. **Ontology should model blocking relationships (DAG)**:
   `blocks`, `enables`, `contradicts`, `supersedes` edges determine parallel
   execution order. The trajectory modeler depends on this to determine what
   can run concurrently.

4. **Eval pipeline is TDD**: Every shipment arrives with a test case. The eval
   pipeline is the Bronze→Silver gate. If the shipment doesn't pass its own
   test, it doesn't enter cognition.

5. **Codebase should favor deep modules**: Design module interfaces with minimal
   surface area. Hide implementation. Test through the interface, not the
   internals. Reject shallow modules in code review.

6. **Documentation is a map, not an encyclopedia**:
   `_index.md` files should be thin signposts, not comprehensive summaries.
   Stale docs degrade agent performance more than missing docs.

7. **AFK agent loop as a goal state**: OCR's ideal runtime is a Matt-style
   nightshift/day shift loop: human plans, shipment enters pipeline, agents
   deliberate AFK, human reviews the result in the morning. This is the natural

8. **Ubiquitous Language from ontology**: `ontology/extraction/` should produce
   a persistent shared vocabulary that both the system and the organization use.
   Every shipment enriches the vocabulary. This is the human-readable surface
   of the ontology graph.

9. **Design investment is a gate condition**: Every shipment through governance
   must check: does this improve or degrade system design? If the decision
   adds complexity without offsetting benefit, the gate rejects it. This is
   how gates reverse software entropy.
   end state of the Medallion architecture with gates.
