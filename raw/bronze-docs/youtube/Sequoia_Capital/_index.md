---
title: "Sequoia Capital (Channel) — YouTube Videos"
description: "Videos from Sequoia Capital's YouTube channel. Sequoia is a venture capital firm; their channel features founder interviews, technical conversations, and strategy discussions."
status: "active"
district: "raw/bronze-docs/youtube/Sequoia_Capital"
type: "neighborhood"
parent: "raw/bronze-docs/youtube"
neighbors: ["raw/bronze-docs", "raw/bronze-docs/youtube/AI_Engineer"]
traffic:
  reads: ["Architecture synthesis agents looking for strategic/theoretical content"]
  writes: ["YouTube ingestion cron job"]
blast_radius:
  services: ["None directly"]
  data: ["Video transcripts and reasoned analyses"]
  depends_on_accuracy: "low (Bronze layer)"
---

# Sequoia Capital — YouTube Videos

Collection of reasoned analyses from Sequoia Capital's YouTube channel.
Sequoia videos tend to be strategic and theoretical — founders and technical
leaders discussing the big picture of AI, software, and systems.

## Contents

| File | Speaker | Topic | Status |
|------|---------|-------|--------|
| `andrej_karpathy_vibe_coding_to_agentic_engineering.md` | Andrej Karpathy | Software 3.0, vibe coding vs agentic engineering, jagged intelligence, LLM Wiki, verifiability | reasoned |
| `boris_cherny_claude_code_and_the_future_of_software.md` | Boris Cherny (Anthropic) | Claude Code origin, coding is solved, loops/routines, product overhang, org process as differentiator | reasoned |

## Naming Convention

`<speaker>_<topic>.md` — snake_case, descriptive of content. Speaker name first for attribution.

## Related Directories

- `raw/bronze-docs/youtube/`
- `raw/bronze-docs/youtube/AI_Engineer/`
- `docs/adrs/`
