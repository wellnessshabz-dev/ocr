---
title: "Box AI Strategy — Context Layer, Unstructured Data, and the Agentic Enterprise (Product Faculty)"
source_type: "youtube"
channel: "Product Faculty"
speaker: "Sachin (host), Yosheb Bhavnani (Head of AI Strategy, Box)"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Product Faculty channel interview about Box's AI strategy. Yosheb Bhavnani discusses the context layer for unstructured enterprise data, building agents into the product stack, model neutrality, and the future of knowledge work."
tags: ["box", "unstructured-data", "context-layer", "enterprise-ai", "knowledge-work", "model-neutrality", "agentic-enterprise", "human-in-loop", "content-explosion", "governance", "ai-strategy"]
---

# Box AI Strategy — Context Layer, Unstructured Data, and the Agentic Enterprise

Source: Product Faculty YouTube channel. Sachin interviews Yosheb Bhavnani,
Head of AI Strategy at Box, about enterprise AI, unstructured data, and
building the Box Agent.

## The Unstructured Data Problem

> "90% of knowledge is stuck in unstructured content."

Unstructured = anything you can't table or query easily: Word docs, PowerPoints,
PDFs, manufacturing records, lease agreements, financial statements, PRDs,
product timelines with every version over time.

Before AI: impossible to access at scale — required humans to read meticulously.
After AI: a "complete unlock of knowledge" for burdensome content problems.

## Context Layer > Model

> "The right model doesn't really matter if the AI can't see your data or use
> it the way you want."

Box CEO Aaron Levy calls this **"the era of context."** AI without context is
like hiring a super smart PhD who knows nothing about your organization.

What context means in practice:
- **File tree structure** — a file in 2026 folder vs 2024 folder
- **Versioning** — which version of the product timeline is current
- **Recency** — sick leave policy just changed, AI needs the official file
- **Metadata** — signals about what is the authoritative source
- **Permissions** — AI should only access files the user has access to

## Security & Governance (Two Layers)

| Layer | Concern |
|-------|---------|
| **Hard security** | No prompt injection, no data leakage back into model training |
| **Nuanced governance** | Every customer has different appetite. Permissions-tied access. Tool-level control: can AI create files? move folders? varies by industry (legal ≠ tech) |

## Three Paradigms for the Future of Work

1. **Agents doing more work** → humans do higher value work
2. **More agents than humans accessing content** → need headless product (MCP, CLI, API) alongside UX
3. **Human-agent collaboration** → transparency is key: know what agents are doing, control, feedback, metrics, improvement

> "The future of teams is people + agent collaboration."

## Content Explosion

> "Every session is content. The AI outputs are content. Now everything becomes
> content. That 90% number may stay at 90% — but the volume of that 90% just
> exploded."

AI creates more unstructured data than it ingests. The unstructured data
problem doesn't go away — it compounds.

## Key Strategic Decisions at Box

### 1. Build the Agent INTO the Product Stack

> "One of the most strategic decisions we made: we were not going to build it
> as an add-on."

Many companies build AI as a separate experiment (go here for agent, go here
for your work). Box deliberately did not do this — they built the agent into
the stack so it works with existing permissions, security, and production
infrastructure. It was painful, took longer, required rework. But it was
foundational.

### 2. Model Neutrality / Optionality

> "We've bet pretty hard on model neutrality."

Models are getting better but diverging in capabilities. Box benchmarks every
model release. The pace is accelerating. Building a platform that can swap in
the latest model (e.g., 4.7 Opus) is a strategic advantage.

### 3. Products Must Serve Both Audiences

Every product with a UX also needs: MCP, CLI, API. Agents are a new customer.

> "You have to think through: am I providing this experience as well as through
> an API, CLI, and in an agent-friendly way?"

## Three Principles for Enterprise AI Strategy

1. **AI with purpose** — Don't sprinkle an LLM on top. Look at your customers:
   how can they grow, have higher ROI, reduce burden? What AI stack do you need
   to add to deliver that value?

2. **Neutrality / optionality** — Don't lock into one model provider.

3. **Willingness to throw things away** — The agentic stack changes underneath
   you. You'll be ready to release and the world changed. "Whoops, didn't work
   out. Starting again."

## J-Curve: Slower Before Faster

> "AI works best with context. So it needs to know your design system, your
> repos, how things work — before it can actually act for you."

There's a "temporary feeling weird, feeling slow" period. Growing pains.
Requires patience to see through — many give up too early.

## Banned Buzzword

> **"Agentic"** — means so many different things to different people. It's
> starting to sound like corporate fluff.

## Relevance to OCR

### Direct Architecture Validation

| Box Principle | OCR Equivalent |
|---------------|----------------|
| Context layer > model | GBrain (context substrate) > LLM (intelligence engine) |
| Build agent into product stack | OCR is n8n + FastAPI integrated, not a separate experiment |
| Model neutrality | Ollama + multi-provider routing |
| Products serve humans + agents | Executive surfaces for humans + API/SDK/RPC for agents |
| Permissions-tied access | Access control tied to ontology/tenant |
| Content explosion | Ingestion pipeline must handle AI outputs as content too |

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Context layer first** | "The era of context" — Box's core thesis matches GBrain |
| **Governance with nuance** | Permission tiers, tool-level control — not just hard security |
| **Headless/API alongside UX** | MCP, CLI, API from day one — matches OCR's RPC + SDK |
| **Human-in-loop** | "Human should always be in charge" — matches governance layer |
| **Multi-provider** | Model neutrality as strategic — matches OCR's design |
| **Observability** | Transparency, metrics, feedback — matches audit ledger + replay |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **90% unstructured stat** | Quantifies the problem OCR solves |
| **Content explosion** | OCR's ingestion layer must treat AI outputs as first-class content |
| **J-curve effect** | OCR deployment will feel slower before faster — manage expectations |
| **Agent as new customer** | OCR needs agent-friendly interfaces (MCP protocol) from day one, not as add-on |
| **Manage agents, not just work** | OCR's governance layer includes agent management skills |
| **"Agentic" is meaningless** | Use precise terms: tool-calling, task-sequencing, state-machine |
| **File tree as hidden metadata** | OCR should extract structural context (folder hierarchy, versioning, recency) |
| **AI with purpose** | OCR should solve specific organizational cognition problems, not be a general AI platform |
