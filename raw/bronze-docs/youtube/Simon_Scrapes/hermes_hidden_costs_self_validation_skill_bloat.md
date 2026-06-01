---
title: "Hermes Hidden Costs — Self-Validation, Skill Bloat, Multi-Client Limits (Simon Scrapes)"
source_type: "youtube"
channel: "Simon Scrapes"
speaker: "Simon Scrapes"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Simon Scrapes' YouTube channel. Critical analysis of Hermes's architecture — hidden costs of off-the-shelf agents. Proposes modular skill systems as alternative to Hermes's self-learning loop. Covers identity layer, memory architecture, and skill bloat."
tags: ["hermes", "hidden-costs", "self-validation", "skill-bloat", "multi-client", "identity-layer", "memory", "skill-systems", "modular-architecture", "openclaw-vulnerabilities"]
---

# Hermes Hidden Costs — Self-Validation, Skill Bloat, Multi-Client Limits

Source: Simon Scrapes' YouTube channel. Critical analysis of Hermes's
architecture after rebuilding key features in his own Agentic OS.

## Context

Hermes: 0 → 40K GitHub stars in 46 days (OpenClaw: 61 days). Fastest adoption
for agentic systems. But speed of adoption ≠ sound architecture.

## Three Hidden Costs

### Cost #1: Self-Validation Loop (No External Guardrails)

The self-learning loop has the model write a skill AND judge its own
correctness. Same model, no external validator.

> "The same model that writes the skill is also the sole judge of its
> correctness. Without external validation, it can't see its own blind spots."

Consequences:
- Can quietly overwrite your improvements with worse versions
- No version control or audit log of skill changes
- No way to know what changed or roll back

### Cost #2: Can't Fix What You Don't Understand

OpenClaw data point: **200+ vulnerabilities** identified and filed since
February. **386 malicious packages** on the skills marketplace from a single
threat actor.

When something breaks, you're debugging someone else's architectural
assumptions. You don't understand why they made the choices they did.

### Cost #3: Doesn't Scale Across Your Business

Anecdote: Paul (non-technical CEO) spent 100+ hours and $1,000+ testing
OpenClaw over 2 months. Bugs and security gaps disqualified it from any
practical use.

> "Hermes may be faster to start, but your own setup is faster to scale."

## What He Rebuilt (and Why)

### Identity Layer: Multi-Client Context

**Hermes approach**: USER.md + MEMORY.md = one person, one context. For
multi-client businesses, need separate Hermes installs per client. Skills
not shared across installs, so repeatable procedures are duplicated.

**His solution**: Single install with per-client folders. Each client has
brand context (voice, ICP, positioning, visual identity). Skills are shared
across client folders — update once, all clients benefit.

### Memory: Keyword + Meaning Search

**Hermes approach**: Injects memory files (~1,300 token cap) into every
conversation. Good for recent context. Long-term recall is keyword-only.

**Problem**: Can't recall what you can't remember the exact words for. "Who
remembers the exact words they used with a client 6 months ago?"

**His solution**: Check injected context first → fall back to **meaning-based
search** (not keyword). Pluggable: swap in mempalace for verbatim recall
when needed.

### Self-Learning Loop → Skill Systems

**Hermes problem**: Creates a new skill every time → skill bloat. 15 skills
all doing roughly the same thing (LinkedIn post V1, V2, post writer one, two).
When brand voice shifts, 15 places to update. Impossible to maintain at scale.

| Problem | Effect |
|---------|--------|
| Similar descriptions | Agent doesn't know which skill to use |
| Baked-in context | Each skill captures one moment in time |
| No modularity | Updating brand voice means updating 15 files |

**His solution: Skill Systems** (modular components, not monolithic skills):

```
Instead of: [Write LinkedIn Post] skill that bakes in everything
Do: Voice → ICP → Formatting → chained by LinkedIn Post system
```

- Each component lives in one file
- One update propagates to every system
- Skills are modular components, not one-off tasks

> "Faster to start with Hermes, faster to scale with your own built setup."

## Relevance to OCR

### This is the Most Important Critique in the Bronze Layer

| Critique | OCR Application |
|----------|-----------------|
| **Self-validation problem** | OCR governance must use a SEPARATE validation model/perspective from the deliberation model. Same model writing + grading = blind spots. |
| **Skill bloat** | OCR's skill registry needs deduplication and versioning. Skills should be modular components, not one-off task snapshots. |
| **Keyword-only recall** | OCR's memory recall must be semantic (meaning-based), not just keyword. |
| **Multi-client architecture** | OCR must support multi-tenant from day one — shared skills, per-tenant context. |
| **Audit trail for changes** | Every skill change needs version history and rollback. OCR's audit ledger covers this. |
| **380+ malicious marketplace packages** | OCR should NOT have a community marketplace. Skills emerge from governance outcomes, not downloads. |

### Confirms (and Adds Teeth To) Existing Decisions

| Decision | Now Strengthened By |
|----------|---------------------|
| **Governance is separate from deliberation** | Self-validation loop critique shows why OCR's council + governance must be different models/processes |
| **No skills marketplace** | 386 malicious packages in OpenClaw marketplace is a hard no |
| **Version-controlled skills** | Audit ledger + skill registry must support rollback |
| **Ontology as shared substrate** | Modular skill systems = ontology + shared context, not baked-in prompts |
| **Multi-tenant ontology** | Per-client context + shared skills from day one |
| **Semantic memory > keyword** | OCR's GBrain recall must be meaning/semantic, not just full-text search |
| **Skill deduplication** | Curator agent must merge similar skills, not just archive stale ones |
