---
title: "Hermes as Lead Developer — VPS Setup, Telegram Mobile Coding, GitHub Deployment (ZazenCodes)"
source_type: "youtube"
channel: "ZazenCodes"
speaker: "ZazenCodes"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "ZazenCodes YouTube channel. Practical tutorial on setting up Hermes agent on a Hostinger VPS with Telegram for mobile coding. Demonstrates full workflow from phone → Telegram → VPS → Docker → Hermes → GitHub → GitHub Actions → live site deployment."
tags: ["hermes", "vps", "telegram", "mobile-coding", "github-actions", "docker", "self-healing", "token-usage", "approval-gates", "hostinger"]
---

# Hermes as Lead Developer — VPS Setup, Telegram Mobile Coding, GitHub Deployment

Source: ZazenCodes YouTube channel. Practical tutorial on using Hermes as a
lead developer — deployed on a VPS, accessible from Telegram on mobile, coding
on real projects.

## Architecture

```
Phone (Telegram) → VPS (Hostinger) → Docker → Hermes Agent → GitHub → GitHub Actions → Live Site
```

## VPS Deployment (Hostinger)

- One-click Hermes deploy from Hostinger dashboard
- KVM 2 (8GB RAM, 2 vCPUs) recommended for parallel tasks
- Password saved during setup used for web UI login
- Docker volumes mount the agent's brain (`data/`) for persistence

## Three Layers of Access

| Layer | Access Method | What You See |
|-------|--------------|--------------|
| VPS | SSH root@IP | Docker compose, .env credentials, volumes |
| Docker container | `docker exec -it <name> /bin/bash` | `opt/hermes/`, mounted `opt/data/` (the brain) |
| Hermes agent | Run `./hermes` inside container | Interactive chat with the agent |

## Telegram Bot Setup

1. **BotFather** on Telegram → `/newbot` → get token
2. **User ID** via user-info bot → restrict bot to only your ID
3. Paste token into Hermes setup
4. **Self-healing** — if Telegram doesn't connect, ask Hermes to fix itself

> "When Hermes isn't working, just get it to fix itself."

## GitHub Integration

- Hermes ships with `ghcli` and `github-auth` skills built-in
- OAuth-based authentication (no token management needed)
- Separate agent GitHub account for scoped repo access (not your personal)
- Used `git clone` to pull target repo
- Codebase inspection via `gh` CLI + file reading + browser

## Secure Deployment Pattern

**Important**: Hermes pushes to GitHub (staging branch), **not** directly to the
live server. GitHub Actions handles the actual deployment.

> "It's more secure to get GitHub to manage deployment secrets than to show
> those things to Hermes."

## Mobile Workflow Demo

1. "Deploy to prod" command in Telegram
2. "Add a blog to my website" — Hermes loads front-end design skill
3. Generates blog post + image (via Codex)
4. Pushes to staging branch
5. GitHub Action deploys to live site
6. **Approval gate**: high-risk commands prompt for approval in Telegram
7. **Visibility**: all commands visible in chat — "this is what got me addicted"

## Token Usage Concern

> "Hermes has this issue of using a lot of tokens. All these commands running,
> all this stuff it was doing. I want to get Hermes doing the work I want it to
> do without all this extra stuff costing so many tokens."

Verbose thinking and tool calls burn context. The visibility into what it's
doing is valuable but expensive.

## Comparison to OpenClaw

| Aspect | Hermes | OpenClaw |
|--------|--------|----------|
| CLI feel | Snappier, more responsive | — |
| Slash commands | More comprehensive | — |
| Self-healing | Built-in | Not built-in |
| Visibility | Shows all commands in chat | Hides internals |
| Token efficiency | Wastes tokens on verbose thinking | More efficient? |
| Developer | AI researchers (Nexus Research) | — |

## Relevance to OCR

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **VPS deployment** | Hermes on Hostinger VPS = same as OCR's single-node VPS bootstrap |
| **Docker volumes for persistence** | `data/` folder = the agent's brain — matches OCR's persistent volumes |
| **Docker compose** | Same pattern as OCR |
| **GitHub Actions for secure deployment** | Matches OCR's CI/CD pattern — don't give agent deployment secrets |
| **Approval gates for high-risk ops** | Matches OCR's governance (Validated / HumanReview / Rejected) |
| **Scoped access** | Separate agent GitHub account = OCR's access control |
| **Multi-platform** | Telegram as interface = OCR should support messaging platforms |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **Self-healing as built-in pattern** | OCR agent should be able to diagnose and fix its own connection/infrastructure issues |
| **Visibility is addictive but expensive** | Show what the agent is doing (transparency) but make it optional / configurable |
| **Token waste from verbose tool use** | OCR must optimize context burn — compact tool output, summarize intermediate steps |
| **Three-layer mental model** (VPS → Docker → Agent) | OCR documentation should explain deployment layers clearly |
| **Mobile approval of high-risk commands** | OCR governance should support mobile approval for HumanReview decisions |
| **Agent needs own GitHub account** | OCR should recommend/automate scoped service accounts |
| **Staging branch pattern** | OCR governance should support staged deployment (staging → prod gates) |
