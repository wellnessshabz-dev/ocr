---
title: "Grill With Docs — From Grill Me to Ubiquitous Language (Matt Pocock)"
source_type: "youtube"
channel: "Matt Pocock"
speaker: "Matt Pocock"
date: "2026-05"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Matt Pocock's personal YouTube channel. Evolution of his Grill Me skill into Grill with Docs, adding ubiquitous language (DDD) and ADRs."
tags: ["grill-with-docs", "grill-me", "ubiquitous-language", "ddd", "domain-driven-design", "adr", "shared-language", "context-md", "alignment", "ontology"]
---

# Grill With Docs — From Grill Me to Ubiquitous Language (Matt Pocock)

Source: Matt Pocock's personal YouTube channel. The evolution of Grill Me into
Grill with Docs — adding DDD's ubiquitous language and ADRs.

## The Backstory

Matt's **Grill Me** skill (4 sentences, the most influential he's ever written)
has the LLM interview you relentlessly, walking down each branch of the design
tree, resolving dependencies between decisions one by one. It's wildly popular
("goated," "game-changer," "saves time" — users report one-shotting everything
after grilling).

But Matt felt dissatisfaction: the agent doesn't know your domain's shared
language. Every session you re-explain terms of art. Fuzzy language goes
unchallenged. Good shared language discovered during a session isn't documented
anywhere.

## The Solution: Three Layers

### Layer 1: context.md (Ubiquitous Language)

Based on Domain-Driven Design (Eric Evans, the "big blue book"). A single
markdown file at repo root documenting:

- What the repo is (top-level description)
- All entities and their relationships
- Terms of art (e.g., "standalone video = a video with lesson_id = null")
- Domain-specific jargon

The file is called `context.md` and lives at the repo root. For monorepos with
multiple bounded contexts, you'd have `context.md` per context directory.

**Key:** This is NOT comprehensive documentation. It's the thinnest layer of
documentation to give the AI a leg up — a glossary of non-obvious terms.

### Layer 2: Grill with Docs skill

Combines Grill Me + context.md awareness. Additional instructions to:

1. Look for existing `context.md` and pull in the shared language
2. **Challenge language usage** against the existing glossary
3. **Sharpen fuzzy language** — when terms are ambiguous, drill until precise
4. **Discuss concrete scenarios** — use the shared language in context
5. **Cross-reference with code** — ensure language matches implementation
6. **Update context.md** as you go — language is never frozen

### Layer 3: ADRs (Architectural Decision Records)

For decisions that are hard to reverse and surprising without context. ADRs sit
in the repo and document:

- The decision itself
- The trade-offs considered
- Why this path was chosen
- Consequences down the line

**Rule:** Only create an ADR when the decision is hard to reverse. Swappable
libraries don't need ADRs. Complex architectural trade-offs do.

## Grill with Docs in Action

The transcript shows a live session adding a "pitch" entity (Mr. Beast-style
video packaging). The agent:

1. **Surface attention with glossary**: "Standalone video is already defined as
   a video with lesson_id = null. Before going further, let's clarify..."
2. **Resolve cardinality**: One pitch to many standalone videos? Or one-to-one?
3. **Detect terminology collision**: "Standalone video" could mean pitched or
   unpitched — let's resolve the collision
4. **Define status semantics**: Pitch statuses — idle, scheduled, shipped (user
   chooses free-form transitions)
5. **Determine deletion cascades**: On delete restrict (archive instead of
   delete)
6. **Save to context.md**: Updates the glossary with all new pitch-related terms

The user notices "pitched standalone video" is awkward (double "standalone") and
can refine before code is generated.

## The Payoff

1. **Concise replies** — AI uses fewer tokens because shared language is
   pre-defined. Doesn't need to re-describe everything.
2. **Concise thinking traces** — AI thinks in language. Better language = better
   thinking. Fewer tokens spent thinking too.
3. **Aligned code** — Variable names, file names, and database schemas all
   derive from the same shared language. Code is easier to navigate.
4. **One-shot implementation** — After grilling, the implementation is
   straightforward because all ambiguity was resolved during language alignment.

## Grill Me vs Grill with Docs

| Dimension | Grill Me | Grill with Docs |
|-----------|----------|-----------------|
| **Codebase needed?** | No | Yes (context.md required) |
| **Use case** | General brainstorming, eulogies, early ideation | Production codebases with established domain language |
| **When to use** | No codebase, new projects (early), non-engineering | Codebase exists, even early in a project |
| **Language** | Discovered during session | Pre-existing + discovered, saved to context.md |
| **Output** | Shared understanding (transient) | context.md updated (persistent) |

Matt's recommendation: "When you have a codebase, use Grill with Docs. When you
don't have a codebase, use Grill Me." Even very early projects benefit from
Grill with Docs because establishing shared language early is where DDD pays
off most.

## Broader Insight: DDD Works with AI

**The same techniques that work with humans also work with AI.** DDD's
ubiquitous language was designed for human-to-human communication on complex
domains. It turns out AI agents benefit from the same rigor because:

- AI uses language to think (chain-of-thought, reasoning traces)
- Ambiguous language produces ambiguous reasoning
- Precise shared language produces aligned reasoning
- The glossary constrains interpretation

This is the conceptual bridge between software architecture and AI alignment.

## Relevance to OCR

### context.md = OCR's Ontology

OCR's entire ontology is a `context.md` at organizational scale. It defines:

| context.md Concept | OCR Equivalent |
|--------------------|----------------|
| Entity definitions | Ontology nodes (Products, People, Components, Decisions) |
| Relationships | Graph edges (owns, blocks, enables, contradicts) |
| Terms of art | Ontology labels with temporal versions |
| Bounded contexts | Ontology subgraphs per domain area |
| Updates | Shipment-driven promotion of candidate nodes |

### Grill with Docs = Council Deliberation

The grilling process maps directly to OCR's council protocol:
1. **Surface attention** → Chairman identifies entities in the shipment
2. **Sharpen fuzzy language** → Perspective agents challenge fuzzy concepts
3. **Resolve collisions** → Contradiction detection (semantic diff)
4. **Determine relationships** → Ontology edge resolution
5. **Save to glossary** → Commit to ontology after governance

### ADRs = Governance Records

ADRs in OCR are the decisions committed to the audit ledger:
- Non-obvious decisions with hard-to-reverse consequences
- Trade-offs and rationale
- Source attribution and lineage

### DDD as AI Alignment Strategy

This is a major conceptual addition: DDD isn't just for human teams. It's an
AI alignment technique. A shared language file (`context.md`) pre-constrains
the agent's interpretation of the domain, which reduces ambiguity in both
communication and reasoning traces.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Ontology as shared substrate** | context.md = lightweight ontology |
| **Chairman as synthesizer** | Grill with Docs = chairman grilling perspective agents |
| **ADRs for governance** | Hard-to-reverse decisions need ADRs |
| **Shipment-driven ontology evolution** | context.md updated during grilling session |
| **Don't outsource understanding** (Dex/Karpathy) | Language alignment IS understanding — you must participate |
| **Intentional compaction** (Dex) | context.md is compressed shared understanding |
| **Gates > agents** (Nick) | Language acts as a gate — constrains what the agent can misinterpret |

### What Matt Adds

| Insight | OCR Application |
|---------|-----------------|
| **DDD for AI alignment** | Ontology isn't just data modeling — it's an alignment mechanism |
| **context.md as thinnest layer** | Minimal viable glossary, not comprehensive docs |
| **Grill with Docs as council template** | The exact protocol (surface → sharpen → resolve → save) |
| **ADRs only for hard-to-reverse** | Not every decision needs governance — only costly reversals |
| **Language → thinking quality** | Better language produces better reasoning traces |
| **Grill Me vs Grill with Docs** | Framework for deciding when ontology is needed vs not |
| **DDD doesn't need AI-specific tools** | Existing software engineering patterns solve alignment |
