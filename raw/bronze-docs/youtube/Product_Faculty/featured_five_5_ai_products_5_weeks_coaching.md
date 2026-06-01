---
title: "Featured Five — 5 AI Products in 5 Weeks with Roger Jinn (Product Faculty)"
source_type: "youtube"
channel: "Product Faculty"
speaker: "Mo Ali, Roger Jinn, Eric Manrique, Samantha Hur, Rahul, Namita, Deon"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Product Faculty channel. Series where 5 students build AI products over 5 weeks with coaching from Roger Jinn (ex-Head of Product, Google DeepMind). Episode covers discovery phase — problem definition, ICP identification, MVP scope, positioning. Hosted by Mo Ali (CEO)."
tags: ["product-faculty", "ai-product-management", "discovery", "contextual-layer", "meridian", "organizational-intelligence", "mvp-scoping", "eval-framework", "human-in-loop"]
---

# Featured Five — 5 AI Products in 5 Weeks with Roger Jinn

Source: Product Faculty YouTube channel. Mo Ali (CEO) hosts Roger Jinn
(ex-Head of Product, Google DeepMind) coaching 5 students through AI product
discovery.

## The 5 Products

### 1. Meridian (Eric Manrique — VP Product, JP Morgan)
**Tagline**: "Passive organizational intelligence"

Processes messages, emails, meeting transcripts, event agendas across channels
— relates them to topics, projects, people. If two meetings are about the same
project, Meridian connects them, extracts outcomes and decisions, and makes
them retrievable without notepads or sticky notes.

**Key realization from coaching**: Eric shifted from thinking of this as an
**intelligence layer** to a **contextual layer**. "Its specialty is not
creating or establishing intelligence. It's to digest, synthesize, and relate
across different topics, people, projects."

> "I'm not building a model from scratch. I'm building a universal, easily
> distributable company brain that can be shared with either AI agents or
> human beings."

**MVP scope** (per Roger's coaching):
1. Ingestion layer — integrate with Slack, email, meetings
2. Vector database with MCP server wrapper
3. Knowledge worker UI — visualize relationships between projects, tasks, people

**Agent ICP deferred** — knowledge worker first because human-in-loop feedback
is easier; agent use case is theoretical until workloads are at scale.

### 2. Sammy (Samantha Hur)
**Tagline**: "Execution lighter for the modern kitchen"

Solves the **"mustard finger problem"** — constant scrolling between recipe
ingredients and instructions on recipe sites. Ingests unstructured recipe data,
refactors it into cook-mode format where each instruction block has embedded
ingredients, amounts, and tools.

**Key coaching insight**: The real differentiation is **prep mode** (preparing/
planning the recipe), not cook mode (execution). Roger (ex-Alexa PM lead at
Amazon) highlighted that Alexa already has the cooking execution layer — Sammy
needs unique intelligence capabilities Alexa doesn't have.

### 3. Tenet (Rahul — Senior PM, Sixt)
**Tagline**: "Rule articulation framework for prop traders"

Closes the **discipline gap** between knowing trading rules and actually
following them under pressure (revenge trading, emotional decisions).

**Two AI capabilities**:
- **Gap detection** — evaluate rule book against completeness baseline, prompt for missing areas
- **Nuance extraction** — capture the trader's subjective mental process at the moment of entry (why they entered, why they deviated)

AI acts as **accountability partner** — not a generic chatbot.

### 4. Skillana (Namita)
**Tagline**: "Plan-mode workspace for decisions"

Helps product leaders pressure-test decisions with incomplete information.
Started broad, narrowed to **prioritization** as the first use case (roadmap
decisions, launch decisions, resource allocation).

**Key coaching insight**: "Do one thing exceptionally well" — capture the mind
space of "this is the best tool for prioritization" rather than doing 10 things
adequately.

### 5. Deon (Mark — Federal Government)
**Tagline**: "FIDIC contract Q&A for nation-state infrastructure"

Nation states as buyers, US government employees as users. Indexed version of
official 1999 FIDIC code + 90 gold standard test questions. Human-in-loop
evals with domain experts.

## Recurring Coaching Themes (Roger Jinn)

| Theme | Quote |
|-------|-------|
| **Contextual ≠ Intelligence** | "You're building a contextual layer for knowledge workers and AI agents" — the moat is integrating user's existing data, not the LLM |
| **Prep > Exec** | The differentiation is often hidden *before* the obvious workflow moment |
| **Narrow MVP** | "Do one thing exceptionally well" — focus on one use case, capture mindspace |
| **Why not ChatGPT?** | Contextual data integration is the answer. Generic tools lack user-specific context, repositories, strategy documents |
| **Evals early** | Build eval sets, cross-model validation, human-in-loop for ground truth |
| **ICP clarity** | Distinguish between the buyer (nation state) and the user (US government employee) |

## Relevance to OCR

### Meridian ≈ OCR/GBrain

Meridian's pivot from "intelligence layer" to "contextual layer" is exactly
the GBrain design philosophy:

| Aspect | Meridian | OCR GBrain |
|--------|----------|------------|
| Purpose | Passive organizational intelligence | Cognitive state engine |
| Inputs | Messages, emails, meetings | Shipments, ontology nodes, trajectories |
| Outputs | Related topics, projects, people | Decision graphs, contradiction surfaces |
| Architecture | Ingestion → Vector DB + MCP → Knowledge worker UI | Ingestion → Shipment compiler → Council → GBrain → Executive surfaces |
| Differentiation | Not intelligence — contextual synthesis | Not just memory — cognitive state with lineage |

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Contextual layer design** | Meridian's pivot confirms GBrain should be context substrate, not intelligence layer |
| **Knowledge worker first, then agents** | Meridian defers agent ICP — same reasoning as OCR's human-in-loop governance |
| **Narrow MVP** | Matches Pi's minimal core philosophy |
| **Eval framework with human-in-loop** | Matches OCR's governance layer (Validated / HumanReview / Rejected) |
| **Ingestion → Memory → Surface** | Meridian's architecture mirrors OCR's pipeline |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **"Universal company brain" positioning** | OCR is a "universal organizational brain" for decisions — not just memory |
| **Prep mode vs execution mode** | OCR should separate preparation (ontology extraction, shipment compilation) from execution (council deliberation, governance) |
| **Why not ChatGPT/Claude Code framing** | OCR's answer: contextual data integration. The moat is the ingested ontology, not the LLM. |
| **Agent use case is theoretical until scale** | Defer fully autonomous agent workflows until the knowledge worker loop is validated |
| **Passive vs active cognition** | OCR should passively ingest (like Meridian) and only actively deliberate when a shipment triggers council |
