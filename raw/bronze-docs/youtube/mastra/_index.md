---
title: "mastra — YouTube Videos"
description: "Videos from the mastra YouTube channel about coding agents, agent harnesses, and agentic workflows."
status: "active"
district: "raw/bronze-docs/youtube/mastra"
type: "neighborhood"
parent: "raw/bronze-docs/youtube"
neighbors: ["raw/bronze-docs/youtube/AI_Engineer", "raw/bronze-docs/youtube/Sequoia_Capital", "raw/bronze-docs/youtube/Matt_Pocock"]
traffic:
  reads: ["Architecture synthesis", "Harness designers"]
  writes: ["Manual ingestion"]
blast_radius:
  services: ["None directly"]
  data: ["Video transcripts and reasoned analyses"]
  depends_on_accuracy: "low (Bronze layer)"
---

# mastra — YouTube Videos

Collection of reasoned analyses from the mastra channel about coding agents,
agent harnesses, and context engineering.

## Contents

| File | Speaker | Topic | Status |
|------|---------|-------|--------|
| `mario_building_pi_minimal_extensible_coding_harness.md` | Mario (Pi) | Minimal extensible coding harness, custom compaction, tree sessions, extensibility > built-in, OSS clanker protection | reasoned |

## Topic Tags

- `minimalism` — Strip away features, build extensible core
- `extensibility` — Custom tools, hot reload, npm bundling
- `custom-compaction` — Pluggable compaction strategies
- `terminal-bench` — Agent evaluation benchmark
- `terminus` — tmux-only agent that tops Terminal Bench
- `approval-fatigue` — Dialog-based approval fails
- `tree-sessions` — Session as tree, not linear chat
- `oss-protection` — Vouch system against AI-generated contributions
- `hot-reload` — Edit extensions while agent runs
- `containerization` — Sandbox execution > approval gates

## Naming Convention

`<speaker>_<topic>.md` — snake_case, descriptive of content.

## Related Directories

- `raw/bronze-docs/youtube/AI_Engineer/`
- `raw/bronze-docs/youtube/Sequoia_Capital/`
- `raw/bronze-docs/youtube/Matt_Pocock/`
- `docs/adrs/`
