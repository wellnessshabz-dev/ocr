---
title: "How a Solo Founder Ships 5 AI Products in Parallel — Josh (shpigford) Interview"
source: "YouTube"
url: ""
speaker: "Peter Yang"
channel: "Peter Yang"
date: ""
bronze_status: "reasoned"
tags:
  - solo-founder
  - conductor
  - build-skill
  - worktrees
  - adversarial-review
  - but-for-real
  - learnings-skill
  - claude.md
  - shipping-fast
  - multi-product
  - baremetrics
  - shpigford
  - vibe-coding
  - chops
  - opus
  - gpt-review
district: "raw/bronze-docs/youtube/Peter_Yang"
parent: "raw/bronze-docs/youtube/Peter_Yang/_index.md"
---

# How a Solo Founder Ships 5 AI Products in Parallel — Josh (shpigford) Interview

> Reasoned analysis of Peter Yang's interview with Josh (shpigford), a solo founder who sold Baremetrics for $4M and now builds 5+ AI products simultaneously using Conductor, a multi-model skill-based build system.

## Background

- **Josh (shpigford)**: Sold Baremetrics (business analytics SaaS) for $4M after 7 years
- Now runs **5+ AI products**: Proxy User (synthetic QA users), Rumored (LLM hallucination monitoring), Reply Social (social media reply management), Clearly (open source markdown editor), a cancer care coordination tool for his mom
- Typical launch cadence: **24 hours to same day** from idea to ship
- ADHD — uses context-switching across products as a feature, not a bug

## The Build System

Josh uses **Conductor** (not Claude Code directly) for its:
- Multi-model switching (Opus for bulk, GPT 3.5 for review)
- Automated worktree management (unique ports, env vars, iOS setup per tree)
- Built-in review model support

### Build Skill Pipeline

```
Research → Implementation Document → N Phases → Each Phase = Worktree → PR
```

**Step 1: Research**
- Takes existing codebase + new feature requirements
- Generates a research document: API calls, pros/cons, architecture decisions, what to keep/discard
- Does web searching for competitor implementations, latest docs

**Step 2: Implementation Document**
- A product + technical spec
- Broken into **phases** (typically 3-4, sometimes 30+)
- Each phase is **user-testable** — Josh must be able to personally play with it

**Step 3: Build Phase**
- Each phase runs in a new **git worktree** (separate branch, separate PR)
- Benefits: self-contained context, rollback checkpoints, prevents context rot
- Does deeper research per phase: web search, UI.sh design pass, competitor analysis
- After each phase, updates a **progress file** with decisions made and system learnings

### Review Flow (Adversarial)

```
Opus (bulk coding) → GPT 3.5 (review pass) → "But for Real" skill → Merge
```

**GPT 3.5 Review**
- Set as review model in Conductor
- Invariably finds 3-5 bugs that Opus overlooked
- Analogous to a human code review partner

**"But for Real" Skill**
- After implementation, Josh runs a separate skill that **bullies the AI** into rechecking
- Prompt: "You almost certainly screwed some stuff up. Go back over it again."
- Catches additional bugs beyond the GPT review pass
- Iterated using **Chops** (Josh's open source Mac app for skill management)

### Learnings Skill

After each phase ships:
- Reviews the entire worktree, all conversations, all corrections
- "Look at the stuff I had to tell you over and over — no, that didn't work, try this"
- Distills into updates for the **CLAUDE.md** file
- CLAUDE.md auto-evolves: each project becomes less likely to repeat past mistakes

### CLAUDE.md Structure

- **About the product**: What it does, user personas, marketing voice
- **Stack**: Rails + Inertia + Postgres (Josh's stack)
- **Commands**: What to use, when to use (prevents AI from guessing wrong commands)
- **Testing**: Uses agent browser to open things up and verify
- **Conductor-specific vars**: Unique ports etc.
- Generated per-project from a template, then continuously updated by learnings skill

## Design Process

1. **Name first** — Must have a name before anything else
2. **Logo** — 99% done in Adobe Illustrator (pen tool, fonts, colors)
3. **Brand identity** — Fonts, color schemes, textures, favicons
4. **Build the app** — Code the actual product
5. **Marketing page** — Generated after the app is built (not before)

> "I'll build the whole thing first, then generate marketing copy by looking through the entire feature set."

## Shipping Philosophy

- **Ships within 24 hours, sometimes same day**
- Builds product before landing page (reverse of typical MVP advice)
- "Spending months working on something before you put it out for other people to use is a real bad idea"
- **Demand validation**: Launch first, see what happens. Landing page email collection is a distraction.
- Distribution: Twitter following (~60K), social media

## Business Model

- **Always a paid version** for hosted products with infrastructure costs
- Open source products (Clearly) stay free
- **Pricing**: Avoids low-cost plans ($5-20) due to high support overhead
- If a product doesn't cover its server costs → shut it down
- If shutting down with paying customers → refund last few months

## Support

- Central inbox for all products
- AI-generated **in-app chat support system** (Intercom replacement)
- Has account context inside the chat
- Compartmentalizes support by product

## Advice for New Builders

- "Make mistakes as fast as you can and recognize what the mistake was so you don't repeat it"
- Vibe coding is fantastic — "anybody building anything is a win"
- "There's no replacement for just jumping in there and doing it"
- "Put stuff out there. The idea of spending months working on something before you put it out is a real bad idea."
- AI-assisted coding reduces mistakes but doesn't eliminate them
- You can't know what the problem looks like for others until they're using it

## Key Takeaway: Multi-Model Adversarial Review

The most interesting pattern: **Opus builds, GPT reviews, a bullying skill rechecks, and learnings get baked into CLAUDE.md**. This creates a closed loop where:
1. The strong model generates
2. A different model catches blind spots
3. A meta-skill forces one more pass
4. Lessons persist across sessions via evolving context

## Relevance to OCR

| OCR Concept | This Video | Notes |
|-------------|-----------|-------|
| Skill runtime | Josh's build skill + phases | Modular, reusable capability packages exactly like OCR skills |
| Governance | Worktree per phase + PR | Checkpoints, rollback, audit trail per shipped unit |
| Council deliberation | Multi-model review (Opus → GPT → But for Real) | Different models as different perspectives, similar to council roles |
| GBrain memory | Learnings skill → CLAUDE.md updates | Continuous memory consolidation, lessons persist across sessions |
| Trajectory | Progress file per phase | Decision history that future phases reference |
| Chairman synthesis | Adversarial review | A "devil's advocate" pass that catches blind spots |
| Shipments | Research → spec → phases → PRs | Structured decomposition of work into shippable units |
| Ontology | CLAUDE.md with user personas, stack, commands | Shared context that the agent understands about the project |
