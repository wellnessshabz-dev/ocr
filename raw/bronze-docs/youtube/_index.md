---
title: "YouTube — Raw Video Transcripts & Reasoning"
description: "Bronze layer: raw YouTube transcripts and reasoned analyses from videos relevant to OCR. Organized by topic."
status: "active"
district: "raw/bronze-docs/youtube"
type: "neighborhood"
parent: "raw/bronze-docs"
neighbors: ["raw/bronze-docs/documentation", "raw/bronze-docs"]
traffic:
  reads: ["Architecture synthesis agents", "raw/bronze-docs/ (cross-reference)"]
  writes: ["Cron job (YouTube scrape → transcript → reason → store)"]
blast_radius:
  services: ["None directly"]
  data: ["Raw video transcripts, reasoned analyses"]
  depends_on_accuracy: "low (Bronze layer — append-only, never edit)"
---

# YouTube — Raw Video Transcripts & Reasoning

Bronze layer for YouTube content. Each video gets a file with the reasoned
analysis of its content. Directory structure is **channel-based**: the
directory name is the YouTube channel name, not a topic category.

## Ingestion Pipeline (Future Cron Job)

1. **Search** — Cron job searches YouTube for relevant videos by keyword/topic
2. **Scrape** — Get transcript via YouTube API or whisper
3. **Store raw** — Save raw transcript to a `raw/` subfile
4. **Reason** — Run through LLM to extract key concepts, connections to OCR
5. **Store reasoned** — Save reasoned analysis as the main file in the channel dir

## Channel Directories

- **AI_Engineer/** — Videos from the AI Engineer channel (workflow, tools, patterns)
- **Sequoia_Capital/** — Videos from Sequoia Capital's channel (founder interviews, strategy)
- **Matt_Pocock/** — Videos from Matt Pocock's personal channel (skills, workflows, agent handoffs)
- **mastra/** — Videos from the mastra channel (coding agents, harnesses, context engineering)
- **Chai_Aur_Code/** — Videos from the Chai Aur Code channel (MCP, AI protocols, developer tools)
- **Nate_Herk/** — Videos from Nate Herk's channel (AI industry analysis, Anthropic, Karpathy, Claude Code strategy, context engineering)
- **IBM_Technology/** — Videos from the IBM Technology channel (AI agent memory, CoALA framework, enterprise AI patterns)
- **VS_Code/** — Videos from the VS Code channel (VS Code Insiders Podcast, agents window, agentic development evolution)
- **Damian_Galzara/** — Videos from Damian Galzara's channel (harness engineering, four levers of agent design, production AI systems)
- **Brandon_Melville/** — Videos from Brandon Melville's channel (Pi harness, AI coding tools, developer workflows)
- **DIY_Smart_Code/** — Videos from DIY Smart Code channel (Pi vs Claude Code vs OpenCode, multi-agent architectures, state-driven agents, platform capabilities)
- **Better_Stack/** — Videos from Better Stack channel (Dogra voice AI platform, self-hosted alternatives, developer tooling)
- **Product_Faculty/** — Videos from Product Faculty channel (AI product management, Featured Five series, product discovery coaching)
- **Jack_Roberts/** — Videos from Jack Roberts' channel (Hermes AI agent framework, multi-platform agent OS, entrepreneurship)
- **ZazenCodes/** — Videos from ZazenCodes channel (Hermes agent, VPS deployment, Telegram mobile coding, GitHub Actions, practical agent workflows)
- **Mansel_Scheffel/** — Videos from Mansel Scheffel channel (Claude Code Workflows, sub-agent orchestration via workflow.js, deep research)
- **NetworkChuck/** — Videos from NetworkChuck channel (Hermes vs OpenClaw, memory architecture, self-improving skills, harness philosophy)
- **Alex_Finn/** — Videos from Alex Finn channel (Hermes use cases, slashgoal metaprompting, Kanban, memory wiki, Tailscale cross-device)
- **Simon_Scrapes/** — Videos from Simon Scrapes channel (Hermes critique, self-validation loop, skill bloat, multi-client limits, modular skill systems)
- **Lewis_Jackson/** — Videos from Lewis Jackson channel (self-improving trading agent, Markov hedge fund method, quant trading, goal-driven AI loops)
- **WorkOS/** — Videos from WorkOS channel (MCP Night events, Auth.md agentic registration, IDJAG, agent economy, enterprise agent infrastructure)
- **Peter_Yang/** — Videos from Peter Yang channel (AI tutorials, solo founder interviews, Conductor build skills, multi-model adversarial review, practical AI product workflows)
- **David_Ondrej/** — Videos from David Ondrej podcast (agentic engineering interviews, developer AI stacks, harness configurations, context engineering)

## Status Convention

Each video file has a `status` field in YAML frontmatter:
- `raw` — transcript only, no reasoning applied
- `reasoned` — processed with analysis and OCR connections
- `stale` — superseded by newer content on the same topic

## Related Directories

- `raw/bronze-docs/youtube/AI_Engineer/`
- `raw/bronze-docs/youtube/Sequoia_Capital/`
- `raw/bronze-docs/documentation/`
- `raw/bronze-docs/`
