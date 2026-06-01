---
title: "Simon Scrapes — YouTube Videos"
description: "Videos from Simon Scrapes' YouTube channel about agentic systems, Hermes architecture, custom agentic OS, and modular skill design."
status: "active"
district: "raw/bronze-docs/youtube/Simon_Scrapes"
type: "neighborhood"
parent: "raw/bronze-docs/youtube"
neighbors: ["raw/bronze-docs/youtube/NetworkChuck", "raw/bronze-docs/youtube/mastra", "raw/bronze-docs/youtube/AI_Engineer"]
traffic:
  reads: ["Architecture synthesis", "Agent system critique", "Multi-tenant design"]
  writes: ["Manual ingestion"]
blast_radius:
  services: ["None directly"]
  data: ["Video transcripts and reasoned analyses"]
  depends_on_accuracy: "low (Bronze layer)"
---

# Simon Scrapes — YouTube Videos

Collection of reasoned analyses from Simon Scrapes' YouTube channel about
agentic systems, Hermes architecture, and modular skill design.

## Contents

| File | Speaker | Topic | Status |
|------|---------|-------|--------|
| `hermes_hidden_costs_self_validation_skill_bloat.md` | Simon Scrapes | Hermes hidden costs — self-validation loop, skill bloat, multi-client limits, memory recall limits, modular skill systems as alternative | reasoned |

## Topic Tags

- `hermes` — Open-source AI agent framework
- `hidden-costs` — Architectural trade-offs of off-the-shelf agents
- `self-validation` — Same model writes and judges skills
- `skill-bloat` — Proliferation of near-identical skills
- `multi-client` — Single-person context vs multi-tenant needs
- `identity-layer` — USER.md, MEMORY.md, brand context
- `memory` — Keyword vs meaning-based recall
- `skill-systems` — Modular components over monolithic skills
- `modular-architecture` — Pluggable, composable agent design
- `openclaw-vulnerabilities` — 200+ CVEs, 386 malicious packages

## Naming Convention

`<framework>_<critique>.md` — descriptive of content.

## Related Directories

- `raw/bronze-docs/youtube/`
- `raw/bronze-docs/youtube/NetworkChuck/`
- `raw/bronze-docs/youtube/AI_Engineer/`
- `docs/adrs/`
