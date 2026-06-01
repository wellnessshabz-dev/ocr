---
title: "Pi: Claude Code Competitor — Extensions, Multi-Agent Teams, Any Model (DIY Smart Code)"
source_type: "youtube"
channel: "DIY Smart Code"
speaker: "DIY Smart Code"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "DIY Smart Code channel. Comparison/review video positioning Pi against Claude Code and OpenCode. Frames Pi as the Neovim of coding agents — minimal core, infinite extensibility. Introduces state-driven agent pattern and meta-agent orchestration. Uses OpenClaw (145K stars) and T (51 extensions, 95% Claude Code parity) as proof points."
tags: ["pi", "claude-code", "open-code", "comparison", "state-driven-agents", "meta-agent", "multi-agent", "extensions", "headless-mode", "rpc-protocol", "sdk-mode"]
---

# Pi: Claude Code Competitor — Extensions, Multi-Agent Teams, Any Model

Source: DIY Smart Code YouTube channel. Positions Pi against Claude Code and
OpenCode. Frames Pi as the Neovim of coding agents.

## The Trio

| Tool | Analogy | Philosophy |
|------|---------|------------|
| Claude Code | VS Code | Polished, opinionated, works for everyone |
| OpenCode | Linux (Ubuntu) | Batteries included, works on day one |
| Pi | Neovim | Minimal core, infinite extensibility |

## System Prompt Impact

| Tool | System Prompt Size | Context Burn |
|------|-------------------|--------------|
| Claude Code | ~10,000 tokens | Up to 9% of context before you start |
| Pi | ~300 tokens | Minimal — lets the model cook |

> "Every token in the system prompt is a token stolen from your context window."

Pi's philosophy: modern LLMs are smart enough to figure out file operations,
error handling, and planning on their own.

## 15+ LLM Providers with Mid-Session Switching

Providers: Claude, GPT, Gemini, Grok, Groq, Cerebras, DeepSeek, OpenRouter,
and more.

Workflow: Start with Opus for deep reasoning → switch to GPT-4o for fast
iteration → drop to Haiku for quick file edits.

> Model freedom = cost freedom. DeepSeek for heavy reasoning at half the cost.

## Extension Ecosystem (Ready to Install)

Extensions are TypeScript packages — install via npm or git repos. Can add:
tools, commands, keyboard shortcuts, hooks, widgets, themes.

**T** (built by one developer on Pi): 51 extensions, 34 themes, ephemeral
agents, multi-model routing teams, CLI + ST key — 95% feature parity with
Claude Code.

## Multi-Agent Architectures on Pi

| Pattern | Description |
|---------|-------------|
| Sub-agents | Isolated contexts — no information bleeding |
| Agent teams | Specialized roles: scout → plan → code → review |
| Agent chains | Sequential pipeline: schema → validate → implement → test |
| Meta agent | Orchestrator that builds agents, assigns tasks, monitors, synthesizes — doesn't write code itself |

> "You're not just using an AI coding tool. You're building an AI coding
> organization."

## State-Driven Agents ("Till Done")

An agent that works until an objective is met, not until context fills up:

- Define a state machine: Research → Plan → Implement → Test → Refine
- Define transitions between states
- Agent moves through each state
- **Persists progress across sessions**
- Only stops when the goal is achieved

> "You define an objective Monday morning. The agent works through it across
> multiple sessions, picking up exactly where it left off. Context resets
> don't matter because the state machine tracks progress independently."

### OCR Relevance

This is the most directly relevant concept in the video for OCR. The "till done"
state machine is exactly what OCR's Trajectory Modeler + Episodic Memory should
support — shipment progress persists across context resets.

| Pi State Machine | OCR Equivalent |
|-----------------|----------------|
| Research | Ingest + ontology extraction |
| Plan | Shipment compilation |
| Implement | Council deliberation |
| Test | Governance validation |
| Refine | Feedback loop back to council |

## Platform Capabilities

| Mode | Use Case |
|------|----------|
| **Headless** | CI/CD pipelines, automated code review, batch processing |
| **RPC** | Control Pi from any language (Python, Go, Rust) |
| **SDK** | Embed Pi in custom applications |

OpenClaw proof point: 145,000 GitHub stars in a single week.

## Terminal Bench 2.0

Pi + Opus competed against Codex, Cursor, and Windsurf using their native
models — competitive results despite just 4 tools and a 300-token system
prompt.

## Verdict: 80/20

> "For 80% of your work, Claude Code is probably the right choice. But that
> other 20% — specific models, multi-agent orchestration, embedding, full
> observability — that's where Pi lives."

## Relevance to OCR

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| Minimal core (300 tokens) | Matches OCR's 5 primitive layers |
| Multi-agent architectures | Confirms council + perspective agent design |
| Extension ecosystem | Confirms skills + package design |
| Headless / RPC / SDK modes | Confirms OCR's executive surfaces design |
| Model diversity | Confirms Ollama + multi-provider approach |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **State-driven "till done" agent** | Shipments should persist across context resets via state machine |
| **Meta-agent pattern (orchestrator builds agents)** | Chairman could dynamically assemble perspective agents per shipment |
| **80/20 heuristic** | OCR should do 20% of things well with primitives, not 80% of things okay with bloat |
| **Model freedom = cost freedom** | Route shipment types to cheapest adequate model |
| **Context burn as metric** | Track system prompt % as a KPI |
| **Pi as platform, not tool** | OCR should expose SDK + RPC, not just API |
