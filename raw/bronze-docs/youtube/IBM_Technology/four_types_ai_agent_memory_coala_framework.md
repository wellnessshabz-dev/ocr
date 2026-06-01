---
title: "Four Types of AI Agent Memory — CoALA Framework (IBM Technology)"
source_type: "youtube"
channel: "IBM Technology"
speaker: "IBM Technology"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "IBM Technology YouTube channel. Overview of the CoALA (Cognitive Architectures for Language Agents) framework from Princeton, mapping four types of agent memory to production implementations."
tags: ["memory", "coala", "working-memory", "semantic-memory", "procedural-memory", "episodic-memory", "skill-md", "progressive-disclosure", "agent-architecture"]
---

# Four Types of AI Agent Memory — CoALA Framework (IBM Technology)

Source: IBM Technology YouTube channel. Breakdown of the CoALA framework's
four memory types for AI agents, mapped to real production implementations.

## The Four Memory Types

### 1. Working Memory (Context Window)

The agent's current context — everything it can see right now:
- Current conversation
- System instructions
- Loaded files and data

Analogy: **RAM** — fast, immediately accessible, volatile. Session ends, it's
gone. Limited size (even 1M tokens has a ceiling; performance degrades before
reaching it).

Every agent and every chatbot has working memory. It's not what makes an agent.

### 2. Semantic Memory (Knowledge Base)

Facts, rules, conventions, documentation — what the agent needs to know in
general.

Academic literature describes this as vector databases or knowledge graphs. In
production systems, it's much simpler: **markdown files**. Claude Code's
`CLAUDE.md` at the root of a project is semantic memory — project architecture,
coding conventions, build commands, frameworks to use, what NOT to do.

Loaded into context at the start of every session. Without it, the agent makes
the same mistakes repeatedly — no persistent knowledge.

### 3. Procedural Memory (Skills)

How the agent knows how to do things. Open standard: **agent skills** using
`skill.md` files. A skill is a folder with a markdown file describing what it
does and step-by-step instructions.

Uses **progressive disclosure**:
- Agent sees only a lightweight index — name + description (~100 tokens per
  skill)
- When a task matches a skill description, agent loads the full instructions
- References (templates, scripts) pulled in during execution only
- Prevents blowing through the working memory budget

This differs from semantic memory: semantic knowledge is always present in
context; procedural knowledge is loaded on demand.

### 4. Episodic Memory (Past Experience)

Record of past interactions, decisions, and learnings. Not full transcripts —
**distilled/compressed experience**.

Examples:
- "Last time we debugged the auth module, the issue was in the middleware"
- Accumulated notes across sessions deciding what's worth remembering

This is where agents start to genuinely **learn** — getting better over time.
But it's the hardest type to get right:
- What do you delete?
- When does information become obsolete?
- If a user changes jobs, do you keep old project memories?
- **Forgetting is an engineering problem**

## Which Agents Need Which Memory

| Agent Type | Working | Semantic | Procedural | Episodic |
|-----------|---------|----------|------------|----------|
| Simple reflex (thermostat, routing bot) | ✅ | ❌ | ❌ | ❌ |
| Narrow customer support (password reset) | ✅ | ❌ | ✅ | ❌ |
| Full coding agent | ✅ | ✅ | ✅ | ✅ |

## Core Thesis

> "Memory is what separates a chatbot from an agent. A chatbot gives a
> response. An agent gives a response shaped by persistent knowledge,
> accumulated experience, project memory, preferences, and remembered
> mistakes so we're not destined to repeat them."

## Relevance to OCR

### CoALA = GBrain's Architecture

| CoALA Memory Type | OCR GBrain Equivalent | Implementation |
|-------------------|----------------------|----------------|
| **Working** | Context window per shipment | Each gate receives a context slice |
| **Semantic** | Ontology graph | Neo4j + `_index.md` documentation |
| **Procedural** | Skill registry | `skill.md` files, perspective agent definitions |
| **Episodic** | Trajectory modeler + replay manager | Decision history, past councils, governance audit |

### Progressive Disclosure = OCR's Activation Engine

Procedural memory's progressive disclosure (lightweight index → load on match
→ pull resources on demand) is exactly how OCR's activation engine should work:
- Activation computes scores from lightweight skill metadata (~100 tokens each)
- Only matching skills load full instructions
- Resources load during execution, not before

### Forgetting = Governance Policy

OCR needs a formal forgetting policy for episodic memory:
- When does a trajectory become obsolete?
- How long do governance records persist?
- Shipment history: append-only (audit) vs pruned (working memory)
- Human analog: forgetting is useful — OCR should intentionally prune

### Semantic Memory as Markdown Files

The insight that production semantic memory is often just markdown files
validates OCR's approach: `_index.md` files, `SKILL.md` files, `context.md`
(Matt Pocock). The ontology (Neo4j) is the structured semantic memory, but
markdown files are the human-readable complement.

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Ontology as semantic memory** | CoALA framework names semantic memory as agent knowledge base |
| **Skills as procedural memory** | CoALA names skill.md as procedural memory standard |
| **Trajectory modeler** | Episodic memory = past decisions + learnings |
| **Progressive disclosure** (Nick Nisi) | Skills loaded on demand, not all at once |
| **Forgetting as design concern** | Episodic memory hardest to get right — needs explicit policy |
| **Context window = working memory** | Each shipment needs a bounded context slice |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **CoALA framework** | Shared vocabulary for memory architecture design |
| **Four distinct memory types** | Clear separation of concerns for GBrain |
| **Progressive disclosure pattern** | Index → load on match → pull resources |
| **Forgetting is engineering** | OCR needs explicit archival/dormancy policies |
| **Memory = agent differentiation** | Memory architecture is what separates from chatbot |
| **Markdown as semantic memory** | Files as knowledge base — validated production pattern |
