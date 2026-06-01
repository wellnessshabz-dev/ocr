---
title: "Hermes — 21 Concepts Tutorial for the Open-Source AI Agent Framework (Jack Roberts)"
source_type: "youtube"
channel: "Jack Roberts"
speaker: "Jack Roberts"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Jack Roberts' YouTube channel. Comprehensive beginner-to-advanced tutorial on Hermes — an open-source AI agent framework with multi-platform support, memory, sub-agents, cron jobs, model agnosticism, and a dashboard operating system. 271B tokens used across 22 messaging platforms."
tags: ["hermes", "agent-framework", "multi-platform", "memory", "sub-agents", "cron", "heartbeat", "mcp", "model-agnostic", "goal-function", "operating-system", "one-brain", "skills"]
---

# Hermes — 21 Concepts Tutorial for the Open-Source AI Agent Framework

Source: Jack Roberts' YouTube channel. A comprehensive beginner-to-advanced
tutorial on the Hermes open-source AI agent framework.

## Hermes Stats
- **271 billion tokens** used (~240 billion words)
- **22 messaging platforms** supported
- Open-source, self-hosted (local or VPS)

## 21 Concepts (Summarized)

### 1. Agent vs Chatbot
Chatbot tells you how to book a flight. Agent books it. "Smart friend vs
personal assistant." Hermes has tools and takes actions.

### 2. When to Use Hermes vs Other Tools
Framework: Hermes = dog (lives with you, knows you, gets smarter year over
year). Claude Code = contractor (brilliant for specific job, doesn't remember
you). OpenClaw = roommate. IDE = buddy you work with.

> "The more you use Hermes, the better it understands you."

Mobile-first agent. Claude Code at desktop, Hermes everywhere else.

### 3. One Brain, 22 Mouths
Same intelligence accessible from Telegram, Discord, WhatsApp, browser OS,
and 18+ other interfaces. Not locked into one software.

### 4. Where It Lives
- **Local computer** — free, runs while computer is on
- **VPS** — runs remotely, paid monthly, needs security hardening

### 5. OAuth vs API Key
| Method | How | Providers |
|--------|-----|-----------|
| OAuth | Browser sign-in | Groq, ChatGPT (uses $20 subscription) |
| API key | String of characters | Everything else (Anthropic, OpenAI, OpenRouter) |

ChatGPT subscription works via OAuth. Claude requires API credits.

### 6. Choosing the Right Model (Multi-Brain Strategy)
Model agnosticism: use the right tool for the right job.

| Task | Model |
|------|-------|
| Deep reasoning | Opus 4.7 |
| Generalist | GPT |
| Volume + Twitter search | Grok |
| Free / low-cost | DeepSeek |

Use **OpenRouter** as one connection for hundreds of models. Set $10/month
cap per API key. `/model` to switch mid-session.

> "To a hammer, everything is a nail. Your brain is a toolbox, not a
> one-size-fits-all."

### 7. Local Hosted Models
Run models on own computer via Ollama. Trade-off: limited to smaller models
(32B params on MacBook). 100% private, works anywhere (underground, flying,
space).

### 8. Memory — Never Starting from Zero
Three memory systems:
- **memory.md** — markdown file on laptop
- **SQLite full-text search** — over every message in every session
- **Compound memory** — gets better over time (~2 weeks to feel magical)

Can connect to Obsidian, Pinecone, Claude Code memory for cross-platform
awareness.

### 9. Character Bible (soul.md)
File that defines agent's personality, values, communication style. What
makes your Hermes different from everyone else's.

### 10. Integrations
Off-the-shelf API key integrations: text-to-speech, image generation, vision,
web search, Granola (meeting notes), and anything with an API key.

### 11. Computer Actions
When running locally: browser vision, bash, file operations, native Chrome
dev tools, cursor movements. Can take actions while you're away.

### 12. MCP (Model Context Protocol)
> "API is the wiring. MCP is the instruction manual."

MCP = standardized connection package. More token-efficient than raw APIs
because it explains exactly how the tool works — no costly checking needed.

### 13. Skills (Muscle Memory)
Reusable capability packages. Build on agent-skills.io. Can assign specific
models to specific skills (deep reasoning → Opus, autopilot → cheap model).

### 14. Six Power Keys
| Command | Function |
|---------|----------|
| `/q` | Queue next prompt (doesn't interrupt current) |
| `/background` | Run task concurrently |
| `/kanban` | Task board visualization |
| `/reset` | Clear session |
| `/compress` | Summarize session to reduce context |
| `/model` | Switch model mid-session |

One session = one goal. Compress and reset frequently.

### 15. Safety — Principle of Least Access
Never give the keys to the kingdom. Only minimal access needed. API keys
never in chat — use environment variables. Rotate keys via OAuth.

### 16. Northstar / Goal Function
- **Goal**: single session objective with turn budget (e.g., 20 turns)
- **Super goal**: medium-term objective → agent asks questions → generates
  4-10 actions (some for agent, some for human) → progress bar

> "Every hero needs a great goal."

### 17. Sub-Agents (Team)
Spin up parallel sub-agents with fresh contexts. Each researches independently,
reports back. Hermes co-founder runs 12 parallel instances daily.

### 18. Heartbeat / Cron (24/7 Agent)
Scheduled tasks: morning briefings, reminders, periodic check-ins. Zombie
detection, hallucination recovery. Feels alive — proactively reaches out.

### 19. Token Budget
73% of every request is fixed overhead. 10 tokens ≈ 7 words. 4M tokens in 2
hours mistake example. Best practices: clear sessions, right model for right
job, one conversation one goal, keep system prompts clean.

### 20. Operating System
Dashboard for managing everything: AI spend, usage in real-time, skills,
memory, connections, model used, pantheon (persona library), mission control
(goals/plans), GitHub backup, Obsidian brain.

### 21. One Brain
Connect Hermes + Claude Code with shared memory. Hermes knows projects,
customers, decisions. Claude Code is precision building tool. One says
something to Hermes, another to Claude Code — they connect because of shared
memory and understanding.

## Relevance to OCR

### Direct Architecture Parallels

| Hermes Concept | OCR Equivalent |
|----------------|----------------|
| One brain, 22 mouths | GBrain accessible from multiple executive surfaces |
| Memory systems (memory.md + SQLite) | GBrain's layered memory (working, episodic, semantic) |
| soul.md (character bible) | System prompt for council + chairman |
| Skills with model routing | Skill registry with per-skill model assignment |
| Sub-agents (parallel, fresh context) | Council perspective agents (parallel reasoning, no cross-contamination) |
| Heartbeat / cron | Scheduled governance + trajectory modeling |
| Goal function with turn budget | Shipment with bounded deliberation |
| Super goals (multi-step, agent+human actions) | Shipment lifecycle with gates + governance checkpoints |
| Principle of least access | OCR's access control tied to permissions/tenants |
| Compress / reset | Context compaction (like Pi's auto compact) |
| Model agnosticism (OpenRouter) | Ollama + multi-provider routing |
| Operating system dashboard | Executive dashboard |
| GitHub backup | Persistent volumes + S3 backups |
| MCP protocol support | OCR should support MCP for tool integration |
| /q + /background (concurrent tasks) | Parallel council deliberation + background processes |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **~2 weeks to feel magical** | Memory systems need time to compound — set deployment expectations |
| **One session = one goal** | One shipment = one bounded deliberation — clear when done |
| **73% fixed overhead per request** | Token efficiency is a design constraint — keep system prompts minimal |
| **Super goal pattern** | Shipments should decompose into sub-shipments with human and agent actions |
| **Zombie detection / hallucination recovery** | Heartbeat monitoring needs anomaly detection |
| **Pantheon (persona library)** | OCR should have a library of perspective agent archetypes |
| **soul.md as separate from skills** | Character/personality is distinct from capability — OCR should separate governance personality from skill logic |
| **Multi-platform from day one** | OCR should be accessible from Telegram, web, Slack — not just API |
| **OS dashboard as control center** | Executive dashboard should show live state of all subsystems |
