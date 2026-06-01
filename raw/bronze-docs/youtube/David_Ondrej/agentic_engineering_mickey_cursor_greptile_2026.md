---
title: "Agentic Engineering in 2026 — Mickey (resmic) on Cursor, Open Source, Greptile, and the $200/mo Mindset"
source: "YouTube"
url: ""
speaker: "David Ondrej"
channel: "David Ondrej"
date: ""
bronze_status: "reasoned"
tags:
  - agentic-engineering
  - cursor
  - gpt-5.5
  - opus-4.7
  - open-source-tool
  - vercel
  - greptile
  - grep-loop
  - context-engineering
  - service-layer
  - svelte
  - convex
  - launch-early
  - security
  - knowledge-work
  - harness
  - resmic
district: "raw/bronze-docs/youtube/David_Ondrej"
parent: "raw/bronze-docs/youtube/David_Ondrej/_index.md"
---

# Agentic Engineering in 2026 — Mickey (resmic) on Cursor, Open Source, Greptile, and the $200/mo Mindset

> Reasoned analysis of David Ondrej's podcast interview with Mickey (resmic), a senior developer who has AI write 95% of his code. Covers harness selection, context engineering, the Open Source tool, service layer patterns, Greptile auto-review loops, and the launch-fast mindset.

## Background

- **Mickey (resmic)**: Senior developer, says 95% of code in last 3 months was AI-generated
- Still writes code manually on weekends for fun, but professionally leans fully into AI
- Hosted on **David Ondrej** podcast (David Andre channel)

## Core Philosophy: Harness Over Model

> "The model is just a predictor of next text. It doesn't think. It doesn't do. The harness — APIs, tools, system prompt, markdown files — guides it to perform a specific action."

### Model Strategy

| Task | Model | Harness |
|------|-------|---------|
| Back-end, large codebases | **GPT 5.5** (extra high) | Cursor Agent |
| UI / frontend changes | **Opus 4.7** (max) | Cursor Agent |
| Code review | GPT 5.5 | Greptile |

Cursor as the harness because:
- Best model switching
- New agentic view
- Outperforms Claude Code and Codex on benchmarks for the same models

### The Model is Just a Harness Component

The model converts English → tokens → graph prediction → next token → English. It cannot read files, search code, or run commands. The harness provides those capabilities as **tool calls**.

## Tool 1: Open Source (by Vercel)

Fetches the source code of any package/library and dumps it into the codebase as a local folder.

### Why Code Over Docs

> "The code is the single best source of truth. Human-written docs are the worst."

- No translation layer, no stale docs
- Agent references exact function implementations
- 8/10 times gets it spot on with precise context
- Example workflow: `npx open-source <repo-url>` → folder appears in codebase → agent references it

### How It's Used

- **agents.md** tells the agent: "To understand a package, fetch its source code using open source"
- In prompts: "Reference the Svelte codebase in the open-source folder to understand how this component should work"
- Works for frameworks (Svelte, React), libraries (Effect), tools (Daytona, Browser Use)

## agents.md: Keep It Thin

> "The harnesses are getting lighter and lighter. Pi is winning because you don't need much. Models are so good they'll read your codebase and know the stack."

- Don't put obvious stuff ("this is a React codebase") — models already infer this
- Only put non-obvious context: vision, project structure preferences, specific rules
- AI-generated the agents.md — don't hand-write it

## Context Engineering as the Key Differentiator

### The Context Window Budget

Agents have a finite context window (~227K tokens). Within that budget:
- Bloat → agent gets dumber
- Precise → agent performs at peak

Strategy: **Agentic Engineering > Vibe Coding**
- Vibe coding = offloading thinking to the agent
- Agentic engineering = you do the thinking, agent does the work

### Feature Planning

1. Generate a plan first (for the human to review, not for the agent)
2. If the plan requires too much context → break into smaller PRs
3. Each PR = minimal, focused chunk
4. Only then let the agent implement

> "The model doesn't think about its context window when generating a plan. If the plan needs this much context, it will never execute it right."

### Codex Context Meter

Codex shows a context usage percentage. At ~77%+, start a new thread rather than compacting. Even Claude Code's lead dev doesn't use `/compact` — starts a fresh session.

## Tool 2: Service Layer Skill

### Problem

AI agents tend to **rewrite duplicate code** rather than reuse existing functions. Adding Telegram integration? The agent writes a new streaming function instead of reusing the one that already exists.

### Solution

After building a feature:
1. Run the service layer skill
2. Agent scans the codebase for duplicated code
3. Restructures into reusable service layer functions
4. Cleans up code smell proactively

### Why It Matters

Clean code structure = easier for agents in future sessions. If it's hard for a human to read, it's hard for an agent.

> "Old engineering practices that engineers shunned (well-structured code, defined tests) are actually great for agents."

## Tool 3: Greptile + Grep Loop (Auto Research)

### Greptile

Code review tool that gives confidence scores (1-5) on PRs with specific feedback on what's wrong.

### Grep Loop Skill

```
/grep-loop → agent reads PR + Greptile feedback → fixes issues → waits for new review → repeats until 5/5
```

**This is Karpathy's auto research loop applied to code review:**
- Agent keeps iterating autonomously
- Does not stop until the objective metric (5/5) is hit
- If PR is >9,000 lines, context window limits effectiveness — keep PRs small

### Practical Outcome

In the last 3 months, Mickey built a large app entirely agent-engineered using this formula. Grep Loop runs for 20-30 minutes autonomously, pushing fixes until 5/5.

## Stack Choices for Agentic Engineering

### Svelte over React

- Simpler — closer to HTML + TypeScript
- React has "footguns" (hooks, newer API surface)
- Agent is well-trained on HTML + TS, less so on React-specific patterns
- Can reference Svelte source code via Open Source tool

### Convex Backend

- All features are TypeScript code (scheduled functions, APIs, everything)
- No dashboard screenshots needed — agent has full context on backend
- Schema, queries, mutations all in code that agent can read and edit
- Compare to Supabase — requires dashboard context that agent can't access

## Launch Philosophy

### The SF Delusion

> "In San Francisco, the level at which people believe they will succeed is so high. They launch with a semi-functional MVP — auth might break at 100 users — they launch anyway. They get hype. They raise money."

### Key Principles

- Launch before it's ready — animated demo videos = product barely works
- "Build in public" — don't hide until perfect
- People love the underdog — get hate only after success
- External pressure = faster iterations
- "If you have competition, they're going to move fast and burn more tokens. It might as well be you."

### Counteracting Perfectionism

- Full-time job + building means sacrificing sleep and social events
- If you're not that committed, competition will win
- User feedback early is better than no feedback at all

## Security in the Agent Era

### Package Supply Chain

> "The most dangerous attack vector is packages. Tell your agent: never install a package younger than 14 days."

- By day 14, vulnerabilities are usually caught
- Hugging Face has distilled models with guardrails removed — capable of nefarious tasks
- Be part of discourse on X — when a breach happens, you know within minutes

### Personal Security

- **Pass phrases** — family members verify identity before sending money
- **2FA** via authenticator app (not SMS — SIM swapping is real)
- **Password manager** (1Password, etc.)
- Share half the master key with a trusted person
- Educate older family members about voice cloning, AI-generated images

### Incident Response

When a breach is reported on X:
1. Paste tweet into Claude
2. "Am I cooked?"
3. Claude scans system directories
4. Confirms clean or identifies exposure

## Predictions

### Knowledge Work Will Boom

> "I'm more bullish on knowledge work than agentic engineering. Models are already smart enough for knowledge work. We just don't have the tooling around it."

- OpenAI and Anthropic launching consulting companies to deploy into businesses
- Contracts, accounting, legal work — already being transformed
- Entry point for non-technical people to demonstrate value with AI

### Models Will Specialize

- GPT 5.5: smarter for architecture, back-end
- Opus 4.7: better at UI
- Question: single monolithic model vs. smaller specialized models?

### Mindset

> "I'm not technical = I'm not future."

- Tools change every 6 months (context stuffing → minimal context in 1 year)
- Being on X and following the cutting edge puts you ahead of 95% of people
- $200/month subscription is an investment, not an expense

## Relevance to OCR

| OCR Concept | This Video | Notes |
|-------------|-----------|-------|
| Harness | Cursor + tools + context | Everything around the model is the harness — maps to OCR's runtime |
| Council orchestration | Grep Loop (auto research) | Autonomous loop until objective metric is met — same as council deliberation |
| GBrain memory | agents.md + codebase as source of truth | Context that persists and evolves |
| Shipments | Minimal PRs per feature | Structured decomposition into shippable units |
| Governance | Greptile review scores | Objective quality metric, audit trail |
| Ontology | Open Source tool (code as truth) | Direct source instead of interpreted docs |
| Skills | Service layer skill | Reusable, modular capability |
| Context engineering | Keep context low, precise | Core OCR principle for memory activation |
| Ingestion | Open Source fetches code | Automated context gathering from external sources |
