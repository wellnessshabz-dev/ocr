---
title: "AI Harnesses: The Stuff Around the Model — Tejas (IBM)"
source_type: "youtube"
channel: "AI Engineer"
speaker: "Tejas"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "AI Engineer conference. Tejas is an AI developer advocate at IBM, works on open-source OpenRAG project. This talk builds a harness from first principles in 18 minutes."
tags: ["harness-engineering", "deterministic-guardrails", "verify-step", "context-compression", "agent-loop", "gate-enforcement"]
---

# AI Harnesses: The Stuff Around the Model — Tejas, IBM

Source: AI Engineer conference. Tejas, IBM AI developer advocate.

## Core Thesis

**The harness is everything around the model that gives it grounding in reality.**
It's the deterministic layer that anchors the non-deterministic agent to a stable
environment. With a great harness, even a bad model (GPT-3.5-turbo) produces
reliable results. Without a harness, even the best model fails silently.

## What is a Harness?

Analogy: a mountain climber's harness anchors to the mountain (stable) so they
can't drift too far. A dog harness keeps the dog from running away. An AI
harness keeps the model from going off the rails.

**It is NOT the agent loop.** The harness is the stuff *around* the agent loop —
guardrails, verify steps, context management, deterministic overrides.

## Harness Components

| Component | Role | Example from Demo |
|-----------|------|-------------------|
| **Tool registry** | What the agent can do | Browser tools (click, navigate, screenshot) |
| **Model** | The LLM | GPT-3.5-turbo (kept constant, never changed) |
| **Context compression** | Prevent context window overflow | Trim to system + user prompt + last 2 messages |
| **Guardrails** | Hard limits on agent behavior | Max iterations (6), max messages |
| **Agent loop** | Run the agent | While-true loop collecting traces |
| **Verify step** | Check if work actually completed | Deterministic check of tool history |
| **Deterministic handlers** | Override agent failures | Login handler: detect login page → inject credentials |

## The Demo: No Prompt Changes

Tejas built a computer-use agent to upvote the first Hacker News post, using
GPT-3.5-turbo (intentionally bad). **The prompt was never changed.**

**Run 1 — No harness**: Agent clicked upvote, hit login screen, claimed success
but failed. It **lied** — the trace showed the click happened, but the login
intercepted it. The agent reported success because it couldn't tell the
difference.

**Fix: Verify step (deterministic)** — A function that reflects on the tool
history trace and checks for specific failure patterns:
- Did the click actually succeed?
- Did a login redirect happen?
- Did the login handler need to run?

This removed the lie. Now the agent fails correctly (TDD mode: admit failure
honestly before fixing it).

**Fix: Login handler (deterministic override)** — A function that runs every
agent loop, checks the browser URL, and if on a login page, injects credentials
programmatically and submits the form. This happens outside the agent's control
— the harness does it deterministically.

**Result**: Agent successfully upvotes Hacker News using a 2023 model with zero
prompt changes.

## Key Principles

1. **Never change the prompt — change the harness.** If the agent fails, the
   failure is in the harness, not the prompt. Add deterministic guardrails.

2. **The verify step removes lying.** Without verification, agents report
   success for any outcome that matches the output format. Deterministic trace
   inspection catches the mismatch between "I clicked" and "it worked."

3. **Deterministic overrides are safer than prompt instructions.** Instead of
   telling the agent "login with these credentials," let the harness detect the
   login state and inject credentials. This is more secure (secrets in harness
   code, not in prompts) and more reliable (deterministic form filling).

4. **A good harness makes bad models usable.** GPT-3.5-turbo + good harness >
   Opus 4.7 + no harness for this task. The harness is the leverage.

5. **The harness is a loop around the agent loop.** The outer loop (max 3
   attempts) wraps the inner loop (agent tool calls). If the verify step fails,
   the outer loop retries. This is nesting — not parallelism.

## Harness Maturity (Parallels Phil Hetzel's Eval Maturity)

| Level | What You Have | What Happens |
|-------|---------------|--------------|
| 0 | Raw agent | Agent lies, fails silently, burns tokens |
| 1 | Guardrails | Max steps, context compression — agent stops before disaster |
| 2 | Verify step | Deterministic check after each attempt — agent admits failure |
| 3 | Deterministic handlers | Harness fixes common failure modes (login, auth, redirects) |
| 4 | Retry loop | Outer loop retries with fresh context after verify failure |
| 5 | Self-building | Agent creates own harness before task (Tejas's 2027 prediction) |

## Relevance to OCR

### OCR is a Harness

The entire OCR system is an AI harness for organizational cognition. Everything
Tejas describes maps directly:

| Harness Component | OCR Equivalent |
|-------------------|----------------|
| Guardrails (max steps) | cognition/governance/ — policy enforcement |
| Verify step | governance validates evidence, checks ontology contradictions |
| Deterministic handlers | ledger/ writes, gbrain/ updates — deterministic operations |
| Context compression | Each pipeline gate is a compaction point (input → signal → context → positions → synthesis → governance) |
| Outer retry loop | If governance rejects a shipment, it requeues (limited retries) |
| Tool registry | ontology/graph/ — available actions and their constraints |
| Model | The LLM behind council and skills |

### "Don't Change the Prompt — Change the Harness"

This is the same principle as Nick Nisi's "fix the harness, not the code."
Tejas proves it with working code on stage. OCR's entire architecture is a
harness — the gates are the harness components that make the model reliable.

### The Verify Step is the Governance Gate

Tejas's verify step (deterministic reflection on tool history to detect lying)
is exactly what `cognition/governance/` should do — check that the shipment
actually did what it claims, using traces from the pipeline.

### Confirms Existing Decisions

- **Gates > agents** (Nick): The harness IS the gates. Tejas proves this by
  changing only the harness and getting different results.
- **Serial execution** (Luke): The outer loop (retry) is serial. Each attempt
  runs fresh. No parallel agents.
- **Deterministic > non-deterministic** (Daniel): The login handler and verify
  step are deterministic code, not LLM calls. Push validation to deterministic
  systems first.
- **Don't outsource the thinking** (Dex): The harness handles thinking
  (verify step, login detection). The model just does the work.
- **Eval flywheel** (Phil): The verify step is the eval. Production traces
  (tool history) feed the verify step. Failures trigger retry.

### What Tejas Adds That No One Else Does

| Insight | OCR Application |
|---------|-----------------|
| **Harness = everything around the model** | Framing for OCR's entire architecture |
| **Verify step removes agent lying** | Governance must verify trace history, not just output |
| **Deterministic overrides > prompt instructions** | Login handlers, policy enforcement — do it in code, not prompts |
| **Outer loop around agent loop** | Pipeline retry logic: governance rejection → requeue with fresh context |
| **Harness makes bad models good** | OCR should work with any model; the harness provides the reliability |
| **2027 = dynamic self-building harnesses** | Long-term vision: agent creates its own harness before task execution |
