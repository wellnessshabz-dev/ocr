---
title: "6 Hermes Use Cases That Transformed My Workflow (Alex Finn)"
source_type: "youtube"
channel: "Alex Finn"
speaker: "Alex Finn"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Alex Finn's YouTube channel. Practical Hermes agent use cases after months of usage. Covers slashgoal metaprompting, Kanban triage, competitor research, memory wiki, Tailscale cross-device admin, morning priority cron."
tags: ["hermes", "use-cases", "slashgoal", "metaprompting", "kanban", "competitor-research", "memory-wiki", "tailscale", "cross-device", "morning-priority", "cron"]
---

# 6 Hermes Use Cases That Transformed My Workflow

Source: Alex Finn's YouTube channel. Practical Hermes agent use cases after
months of usage with 5 parallel Hermes agents.

## 1. Slashgoal with Metaprompting

**Problem**: `/goal` is powerful but underused — most prompts are too vague.

**Solution**: **Metaprompting** — ask another AI to write the goal prompt.

```
"Build a /goal prompt for: [describe task with all details]"
```

The metaprompt generates a detailed prompt with constraints, scope, and
deliverables. Hermes then asks clarifying questions before running for hours.

> "I've had /goal run for over 24 hours straight working on a task."

Use for: building complex apps, long documents, detailed code changes.
Output files from /goal can be fed to Claude Code/Codex for finishing work.

## 2. Kanban Board (Morning Routine)

Hermes built-in Kanban. Auto-assigns tasks to agents from **triage**.

**Morning routine**:
1. Write full todo list on paper
2. Put everything Hermes can do into Kanban triage
3. Do human-only work (pay bills, meetings)
4. Return to completed tasks

> "It's like having an employee. You start your day, give Hermes everything
> it needs to do, go do your human work, and by the time you're done, Hermes
> took care of all the work it can do."

## 3. Competitor Technical Research

Hermes opens a browser, navigates to competitor sites, examines:
- Tech stack (via console, network tab)
- Features
- Pricing
- Analytics events collected
- All tools and libraries

Generates a full markdown report. Feed the report to Claude Code/Codex to
emulate features.

> "If you're vibe coding an app, have Hermes go research competitors and
> build you a full research breakdown."

## 4. Memory Wiki

Prompt Hermes to build a website that serves as:
- **Subject index**: topics discussed
- **Daily logs**: what was worked on each day
- **Clickable**: drill into any entry for details

**Dual purpose**:
- Human-readable diary of all agent interactions
- Memory reinforcement — Hermes can browse its own logs to recall past context

> "The more your agent has context about you, the better work it can do."

Setup prompt: "I want to build a memory wiki. This should be a site I can
visit that has a list of all the subjects we've talked about and the daily
logs of what we've done together."

## 5. General Computer Administrator (Tailscale)

Install **Tailscale** (free) on all devices → creates a private network.

**Capabilities unlocked**:
- Access files across devices from anywhere
- Run local LLM on one device, use it from another
- Test localhost apps across all devices
- Cross-device file transfer via agent

> "It basically gives Hermes agent superpowers. Every device becomes one
> network accessible from anywhere."

## 6. Morning Priority Prompt (Self-Improvement Loop)

Cron/heartbeat: every morning at 9am, Hermes proactively messages asking
for the #1 priority of the day. Then:
1. Comes up with tasks it can do to help
2. Updates memories about the user

> "The better the context your agent has about you, the better work it can
> recommend, the more custom it can be."

Setup prompt: "Every morning at 9am, ask me what my #1 priority is for that
day. Come up with tasks you can do to help. Update your memories about me."

## Relevance to OCR

### Patterns by OCR Component

| Use Case | Pattern | OCR Application |
|----------|---------|-----------------|
| Metaprompting for /goal | Prompt generation → human review → execution | Governance: generate council prompt from shipment metadata, review before deliberation |
| Kanban triage | Queue management → auto-assignment → execution | Shipment lifecycle: queued → assigned → in progress → completed |
| Competitor research | Browser automation → analysis → structured report | Ingestion: web scraping → ontology extraction → structured document |
| Memory wiki | Continuous log → searchable memory reinforcement | GBrain episodic memory + replay for context |
| Tailscale admin | Cross-device orchestration | Distributed agent execution across infrastructure |
| Morning priority | Proactive cron → learn → improve | Heartbeat monitoring + trajectory modeling + self-improvement |

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Metaprompting for /goal** | OCR governance should generate prompts from shipment metadata |
| **Kanban as lifecycle** | Shipment states map to Kanban columns |
| **Memory wiki as diary** | GBrain needs human-readable access surface |
| **Cross-device access** | OCR agents should work across distributed infrastructure |
| **Proactive cron for improvement** | Self-improvement loop must be scheduled, not reactive |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **Metaprompt for complex tasks** | When a shipment is complex, use metaprompting to generate the council prompt from the shipment spec |
| **Kanban triage as pattern** | OCR needs a triage queue before shipment compilation — filter what the system should handle |
| **Memory wiki is dual-use** | Human diary + agent memory reinforcement. OCR's cognition log should serve both humans (executive dashboard) and agents (replay). |
| **Tailscale for cross-device** | OCR should support mesh networking for distributed execution |
| **Morning priority = daily trajectory** | OCR should have a daily trajectory check-in — what's the org's #1 priority today, how does it affect the decision graph |
