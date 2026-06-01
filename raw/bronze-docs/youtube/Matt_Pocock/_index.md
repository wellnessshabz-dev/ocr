---
title: "Matt Pocock (Channel) — YouTube Videos"
description: "Videos from Matt Pocock's personal YouTube channel. Channel-based directory: the channel name is the directory name."
status: "active"
district: "raw/bronze-docs/youtube/Matt_Pocock"
type: "neighborhood"
parent: "raw/bronze-docs/youtube"
neighbors: ["raw/bronze-docs/youtube/AI_Engineer", "raw/bronze-docs/youtube/Sequoia_Capital"]
traffic:
  reads: ["Architecture synthesis", "Skill authors"]
  writes: ["Manual ingestion"]
blast_radius:
  services: ["None directly"]
  data: ["Video transcripts and reasoned analyses"]
  depends_on_accuracy: "low (Bronze layer)"
---

# Matt Pocock — YouTube Videos

Collection of reasoned analyses from Matt Pocock's personal YouTube channel
about AI coding tools, skills, and workflows.

## Contents

| File | Speaker | Topic | Status |
|------|---------|-------|--------|
| `matt_pocock_handoff_skill_agent_handoffs.md` | Matt Pocock | Handoff skill, compact vs handoff, DIY sub-agents via context handoff documents, parallel decomposition | reasoned |
| `matt_pocock_grill_with_docs_from_grill_me_to_ubiquitous_language.md` | Matt Pocock | Grill with Docs, Grill Me → ubiquitous language (DDD), context.md, ADRs, DDD for AI alignment | reasoned |
| `matt_pocock_reviewing_thermonuclear_code_quality_review_skill.md` | Matt Pocock | Reviewing Cursor's Thermonuclear review skill, ambitious review, code judo, file size as agent tax, false positives > missed regressions | reasoned |
| `matt_pocock_nine_things_wrong_grill_me_grill_with_docs.md` | Matt Pocock | Advanced usage guide — high/low fidelity questions, handoff to prototype, scope management, active vs passive, parametric vs contextual knowledge, parallel sessions | reasoned |

## Topic Tags

- `handoff` — Markdown-based context handoff between agent sessions
- `compact` — Inline context summarization for single-session continuation
- `context-window` — Smart zone vs dumb zone budget management
- `intentional-compaction` — Purpose-driven compression, not blind summarization
- `sub-agents` — DIY sub-agent pattern via handoff documents
- `parallel-decomposition` — Splitting tasks across parallel agent sessions
- `temp-directory` — Disposable transient artifacts in temp storage
- `cross-agent` — Plain markdown handoff works with any coding agent
- `grilling` — Matt's grill-me skill for structured planning sessions
- `prototype` — Handoff to prototype session, return learnings to planner
- `grill-with-docs` — Grill Me + context.md + ADRs, evolution of grilling skill
- `grill-me` — Original skill: LLM interviews you relentlessly about design
- `ubiquitous-language` — DDD shared language between code, devs, domain experts
- `ddd` — Domain-Driven Design for AI alignment
- `adr` — Architectural Decision Records for hard-to-reverse decisions
- `context-md` — Lightweight glossary at repo root as thinnest documentation layer
- `shared-language` — Pre-constrained interpretation for agents
- `alignment` — Language alignment produces aligned reasoning and code
- `thermonuclear` — Ambitious code review with code judo thinking
- `code-review` — Agent-driven code quality review
- `ambitious-review` — Look beyond the diff, restructure aggressively
- `code-judo` — Reframe to delete complexity instead of polishing it
- `file-size` — 1000-line rule as agent context efficiency optimization
- `agent-navigation` — Agents navigate by file name, not by scanning contents
- `false-positives` — Acceptable tradeoff for catching regressions you'd miss

## Naming Convention

`<speaker>_<topic>.md` — snake_case, descriptive of content.

## Related Directories

- `raw/bronze-docs/youtube/AI_Engineer/`
- `raw/bronze-docs/youtube/Sequoia_Capital/`
- `docs/adrs/`
