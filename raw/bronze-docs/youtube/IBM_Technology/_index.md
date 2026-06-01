---
title: "IBM Technology — YouTube Videos"
description: "Videos from the IBM Technology YouTube channel about AI architecture, memory systems, and enterprise AI patterns."
status: "active"
district: "raw/bronze-docs/youtube/IBM_Technology"
type: "neighborhood"
parent: "raw/bronze-docs/youtube"
neighbors: ["raw/bronze-docs/youtube/AI_Engineer", "raw/bronze-docs/youtube/mastra", "raw/bronze-docs/youtube/Nate_Herk"]
traffic:
  reads: ["Architecture synthesis", "Memory substrate designers"]
  writes: ["Manual ingestion"]
blast_radius:
  services: ["None directly"]
  data: ["Video transcripts and reasoned analyses"]
  depends_on_accuracy: "low (Bronze layer)"
---

# IBM Technology — YouTube Videos

Collection of reasoned analyses from the IBM Technology channel about AI agent
architecture, memory systems, and enterprise AI patterns.

## Contents

| File | Speaker | Topic | Status |
|------|---------|-------|--------|
| `four_types_ai_agent_memory_coala_framework.md` | IBM Technology | CoALA framework — working, semantic, procedural, episodic memory; progressive disclosure for skills; forgetting as engineering; memory separates agents from chatbots | reasoned |

## Topic Tags

- `memory` — AI agent memory architecture
- `coala` — Cognitive Architectures for Language Agents (Princeton)
- `working-memory` — Context window, volatile, limited
- `semantic-memory` — Knowledge base (facts, rules, conventions)
- `procedural-memory` — Skills, how-to knowledge
- `episodic-memory` — Past experiences, distilled learnings
- `progressive-disclosure` — Load on demand, not all at once
- `skill-md` — Open standard for procedural memory
- `forgetting` — Intentional memory pruning as engineering

## Naming Convention

`<topic>_<description>.md` — snake_case, descriptive of content.

## Related Directories

- `raw/bronze-docs/youtube/AI_Engineer/`
- `raw/bronze-docs/youtube/mastra/`
- `raw/bronze-docs/youtube/Nate_Herk/`
- `docs/adrs/`
