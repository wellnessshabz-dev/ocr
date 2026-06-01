---
title: "Advanced Context Engineering for Coding Agents — Dex Horthy (HumanLayer)"
source_type: "youtube"
channel: "AI Engineer"
speaker: "Dex Horthy (Dexter Horthy)"
date: "2026-06"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "AI Engineer conference, June 2026. Dex Horthy is founder of HumanLayer, author of the viral 14K★ '12 Factor Agents' methodology. This talk is a follow-up focused on context engineering and the Research→Plan→Implement (RPI) framework."
tags: ["context-engineering", "rpi", "research-plan-implement", "dumb-zone", "intentional-compaction", "sub-agents", "mental-alignment", "12-factor-agents", "harness-engineering", "don't-outsource-the-thinking"]
---

# Advanced Context Engineering for Coding Agents — Dex Horthy, HumanLayer

Source: AI Engineer conference, June 2026. Follow-up to "12 Factor Agents" (top 8 talk of all time).

## Core Thesis

Code quality drops when agents leave the "smart zone" of their context window. The solution is **intentional compaction** at every stage of a three-phase workflow: **Research → Plan → Implement (RPI)**. This is not a new framework — it's a technical discipline for managing context windows.

The RPI workflow is a direct consequence of a fundamental property of LLMs: **they are stateless, non-deterministic functions.** The only thing that influences what comes out next is what's in the conversation so far. Every turn of the tool-calling loop is influenced exclusively by the preceding tokens. So "better tokens in = better tokens out" is the only lever you have.

## The Dumb Zone

Confirmed with a specific threshold:

- Context window: ~168K tokens (Claude), some reserved for output
- **~40% utilization** is where diminishing returns start
- Too many MCPs, too much file content, too many conversation turns → all work happens in the dumb zone
- The more you use the context window, the worse outcomes get (Jeff Huntley's research)

This is the same "smart zone" concept Matt Pocock discussed. Dex frames it as the engineering constraint that drives everything else.

## Intentional Compaction

The naive loop: ask → wrong → correct → wrong → correct → run out of context → cry.

The smarter approach: proactively compress the context window **before** it fills up. Take the current conversation, ask the agent to compress everything relevant into a markdown file. Review it, tag it. When a new agent starts, it reads the compressed artifact instead of re-searching the codebase.

What takes up space:
- Reading/searching files
- Understanding code flow
- Editing files
- Test and build output
- MCP JSON dumps with UUIDs ("God help you")

What should be compacted: **only the exact files and line numbers that matter** to the problem.

### Compression of Truth

Research compresses the codebase into a research document — a snapshot of what's actually true based on the code itself, not stale documentation. The research is generated **on demand** (sub-agents fork fresh context windows), not from static onboarding docs that rot.

### Compression of Intent

The plan compresses the research + PRD/bug ticket into a set of exact steps with file names, line snippets, and test strategy. The plan includes **actual code snippets** of what will change — so the human can verify intent before execution.

### Reliability vs Readability Trade-off

As plans get longer, reliability goes up and readability goes down. There's a sweet spot per team and codebase. Plans with code snippets reach that sweet spot faster because the dumbest model possible can follow them.

## RPI: Research → Plan → Implement

### 1. Research
- Understand how the system works
- Find the right files
- Stay objective — do NOT propose solutions yet
- Output: research document (compressed truth)

### 2. Plan
- Outline exact steps with file names and line snippets
- Include how to test after every change
- Include actual code snippets of what will change
- Human reviews the plan before any code is written
- Output: plan file (compressed intent)

### 3. Implement
- Run the plan step by step
- Keep context low — each step is small
- The plan is explicit enough that the dumbest model can follow it

## Sub-Agents: For Context, Not Roles

Dex's strongest opinion: **sub-agents are for controlling context, not anthropomorphizing roles.**

"Please stop assigning frontend/backend/QA/data scientist sub-agents."

The correct use: spawn a sub-agent to fork a new context window, do all the reading/searching/understanding, and return a succinct result. The parent agent gets the answer without consuming smart zone tokens on reading files.

```
Parent (low context consumption)
  │
  ├── Research sub-agent (forked context, reads everything, returns succinct)
  ├── Plan sub-agent (forked context, produces plan)
  └── Implement sub-agent (forked context, runs plan steps)
```

## Mental Alignment

Code review's true purpose: **mental alignment** — keeping everybody on the same page about how the codebase is changing and why. In a world where AI ships 2-3x more code, reviewing plans is more scalable than reviewing code.

- A human can read and understand a plan faster than reviewing the resulting diff
- Plans include code snippets — the reviewer can see exactly what will change
- The plan enables the reviewer to catch problems early, before code exists
- The AMP thread on the PR gives the reviewer the full journey (prompts → steps → build output)

Mental alignment prevents the rift: staff engineers don't adopt AI (doesn't help them), juniors use it heavily (produces slop), seniors clean up slop. Cultural change must come from the top.

## Don't Outsource the Thinking

Dex's most important message: **AI cannot replace thinking. It can only amplify the thinking you have done — or the lack of thinking you have done.**

- A bad line of code is a bad line of code
- A bad part of a plan could be 100 bad lines of code
- A bad line of research (misunderstanding the system) hoses the entire thing
- Human effort should move to the highest-leverage part of the pipeline: **plan review** and **intent verification**

## Specs-Driven Development is Broken

Semantic diffusion (Martin Fowler, 2006): a good term gets defined, everyone gets excited, it means 100 different things to 100 different people, becomes useless. This is happening to "spec-driven development."

"Spec" now means:
- A better prompt
- A product requirements document
- Verifiable feedback loops with back pressure
- Treating code as assembly (Sean's version)
- A bunch of markdown files while coding
- Documentation for an open source library

The term is semantically diffused. RPI is not spec-driven development. RPI is **context engineering** — a technical practice, not a philosophy.

## Trajectory Matters

Negative trajectory (human corrects → AI fails again → human corrects again) trains the AI that "I do something wrong, human yells at me" is the pattern. The next most likely token becomes "do something wrong so the human yells at me again."

**Positive trajectory is essential.** Set the agent up for success with good research, good plans, and small verification loops. The conversation's trajectory influences every subsequent tool choice.

## The Growing Rift

Current state of AI adoption in engineering:
- **Staff engineers**: don't adopt AI — doesn't make them much faster
- **Junior/mid-level**: use AI heavily — fills skill gaps but produces slop
- **Senior engineers**: hate AI more every week — cleaning up cursor-generated slop

This is AI's fault? No. Mid-level engineer's fault? No. Cultural change must come from the top. This is what context engineering solves: it raises the quality floor so that AI-generated code doesn't become tech debt.

## Relevance to OCR

### RPI Maps to the Shipment Pipeline

| RPI Phase | OCR Stage | Artifact |
|-----------|-----------|----------|
| Research | shipments/compiler/ + ontology/extraction/ | context.json (compressed truth) |
| Plan | cognition/councils/ → cognition/chairman/ | positions.json + synthesis.json (compressed intent) |
| Implement | cognition/governance/ → commit | governance.json + gbrain/ledger updates |

### Key Insights

1. **Intentional compaction = gates**: Each gate in OCR's shipment pipeline is a compaction point. The signal compacts into context. Context compacts into positions. Positions compact into synthesis. Synthesis compacts into governance. Each compaction keeps the system in the smart zone.

2. **Sub-agents validate our council/skills split**: Council orchestrator spawns skills as sub-agents with isolated context slices. The skills return succinct position summaries. The chairman reads summaries, not raw reasoning. This is Dex's sub-agent pattern exactly.

3. **Plan review = chairman synthesis review**: The human (or governance gate) reviews the plan (synthesis) before execution. This is the "don't outsource the thinking" principle. The most leverage point is verifying the intent.

4. **Trajectory matters for council deliberation**: Negative trajectories compound. If early positions are contradictory, the council spirals. Design the deliberation to start with successes, not failures.

5. **Mental alignment through gates**: OCR's governance gate enables mental alignment at the organizational level — every committed decision has a reviewed plan. Leaders can read plans instead of code.

6. **Specs-driven dev is broken for OCR too**: Don't call OCR's ontology "specs." It's context. The ontology is a living vocabulary, not a specification. Semantic diffusion applies.

7. **Don't outsource the thinking applies to councils**: The council does the thinking (research → plan). The skills implement within the council's bounds. The governance gate verifies. The human never reviews raw skill execution — they review the plan and the outcome.

### Confirms Existing Decisions

- **Gates > agents** (Nick Nisi): Confirmed from the compaction angle — gates are where compaction happens
- **Smart zone limits** (Matt Pocock): Specific 40% threshold provided
- **Fresh context > accumulated** (Matt, Luke): Sub-agents fork new context windows
- **Serial > parallel** (Luke): RPI is inherently serial; each phase produces a compaction artifact for the next
- **Evals as precondition** (Patrick Debois): Research → Plan requires verification at each transition

### What Dex Adds That Others Don't

| Insight | Unique to Dex | OCR Application |
|---------|---------------|-----------------|
| Dumb zone at 40% | Specific threshold | Context budget for each pipeline stage |
| Intentional compaction | Compaction as a verb, as a practice | Gates are compression points |
| Sub-agents are for context, not roles | Correct use of sub-agents | Council skills are context-isolated sub-agents |
| Trajectory matters | Conversation trajectory influences next tokens | Design council deliberation for positive trajectory |
| Mental alignment through plan review | Plan review scales better than code review | Governance gate enables org-scale alignment |
| Semantic diffusion warning | Spec-driven dev is already useless as a term | OCR does "context engineering," not "spec-driven dev" |
| Compression of truth vs intent | Two distinct compression types | Research (truth) vs Plan (intent) in pipeline |
