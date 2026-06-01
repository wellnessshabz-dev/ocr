---
title: "Hermes Agent — Backup, Memory, Cron, Goals, Pantheon, OS Guide"
source: "YouTube"
url: ""
speaker: "Jack Roberts"
channel: "Jack Roberts"
date: ""
bronze_status: "reasoned"
tags:
  - hermes
  - agent-framework
  - memory
  - cron
  - goals
  - supergoal
  - pantheon
  - anti-gravity
  - github-backup
  - firecrawl
  - soul.md
  - obsidian
  - mcp
  - model-agnostic
  - mission-control
district: "raw/bronze-docs/youtube/Jack_Roberts"
parent: "raw/bronze-docs/youtube/Jack_Roberts/_index.md"
---

# Hermes Agent — Backup, Memory, Cron, Goals, Pantheon, OS Guide

> Reasoned analysis of a Jack Roberts video covering Hermes agent's memory system, scheduling, goal framework, multi-model strategy, Pantheon personas, anti-gravity CLI, GitHub backup, and mission control dashboard.

## Memory System

Hermes has a layered memory architecture:

- **MEMORY.md** — Central markdown memory file
- **Peer cards** — One per person, stores tone, preferences, relationship context
- **Fuzzy index** — Semantic-ish retrieval without full vector DB
- **1-hour prompt cache** — Keeps token limits lower by caching recent context
- **soul.md** — Core context manual describing the user's life. "Explain who you are, where you live. Do you want it to look around corners? Challenge your thinking?" Functions as the agent's understanding of the user's identity and preferences
- **Obsidian integration** — Connects to Obsidian vault for persistent notes
- **AI meeting notetaker integration** — Granola, Fireflies, Fathom
- **Email integration** — Via Zapium MCP for reading/searching emails

## Background Tasks

- `/background` command runs multiple concurrent thoughts without collision
- Agent can reason about multiple topics simultaneously in isolated contexts

## Cron Scheduling

- Schedule tasks with `/cron`
- Example: Morning brief at 8am with a **dream sequence** — agent proactively considers history, reflects on past patterns, and gives 3 recommendations + 1 non-negotiable daily action
- Heartbeat system for 24/7 zombie detection and recovery

## Goal / Super Goal Framework

- `/goal` — Sets a northstar for the current session
- **Super goal** — Extends goal with a human-AI handshake protocol:
  - Breaks the goal into bite-sized chunks
  - Assigns each chunk to either the human or the agent
  - Creates structured collaboration with clear ownership
- Turn budgets control depth of pursuit

## Model Strategy

- **OpenRouter** — Primary gateway for every model
- **Grok via OAuth** — X/Twitter access, 100K context window
- **Opus 4.7** — Deep reasoning tasks
- **Gemini (via anti-gravity CLI)** — Multimodal capabilities
- **DeepSeek V4** — Cheap research delegation
- **Pantheon** — Create different personas, each backed by a different model, each with different skills and context

## Anti-Gravity CLI

- Replaces the deprecated Gemini CLI
- Provides Gemini multimodality including video analysis
- CLI-based access to Gemini capabilities

## Mission Control / Operating System

- Dashboard interface showing:
  - Usage tracking
  - Memory state
  - Model monitoring
  - Global connections status
  - Goals and progress
  - Skills inventory
  - Personas (Pantheon)

## GitHub Backup

- Daily automated snapshot of entire Hermes configuration to a private GitHub repo
- Version control for agent state and memory

## 10 Key Commands

| Command | Purpose |
|---------|---------|
| `/goal` | Set session northstar |
| `/model` | Switch active model |
| `/cron` | Schedule recurring tasks |
| `/clear` | Reset context |
| `/steer` | Redirect agent focus |
| `/resume` | Resume interrupted session |
| `/background` | Parallel thought execution |
| `/kanban` | Visual task management |
| `/curator` | Content curation agent |
| `/stop` | Halt execution |

## Deployment Recommendation

- Recommends **local computer** over VPS for simplicity and security
- Docker for isolation when needed
- Avoids VPS complexity for single-user setups

## Firecrawl for Web Search

- Firecrawl integration for web search
- Claims **80% cost reduction** compared to direct browsing approaches
- Aligns with OCR's existing Firecrawl usage in the scraper router

## Relevance to OCR

| OCR Concept | Hermes Parallel | Notes |
|-------------|-----------------|-------|
| Shipments | Goals / Super goals | Structured task decomposition with ownership |
| GBrain memory | MEMORY.md + soul.md | Both use layered memory with markdown as substrate |
| Council orchestration | Pantheon personas | Multiple model-backed personas with different perspectives |
| Governance & audit | GitHub backup | Daily state snapshots for rollback and audit |
| Web scraper | Firecrawl | 80% cost reduction using Firecrawl for web content |
| Skill runtime | Skills system | Reusable capability packages |
| MCP | MCP integration | Model Context Protocol for tool connectivity |
