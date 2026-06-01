---
title: "Why Rust is the Ideal Language for Vibe Coding — Daniel Zook (Sentry)"
source_type: "youtube"
channel: "AI Engineer"
speaker: "Daniel Zook"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "AI Engineer conference. Daniel Zook is the Rust SDK maintainer at Sentry."
tags: ["rust", "vibe-coding", "deterministic-guardrails", "compiler-as-gate", "alien-intelligence"]
---

# Why Rust is the Ideal Language for Vibe Coding — Daniel Zook, Sentry

Source: AI Engineer conference. Daniel Zook, Sentry Rust SDK maintainer.

## Core Thesis

The conventional wisdom (TypeScript, Python, JavaScript for AI coding) optimizes for
the wrong thing — how easy it is for the model to write code on the first try.
The real optimization is **deterministic guardrails that catch errors before
they reach production.** Rust's compiler provides those guardrails. An AI agent
in a loop can compile → fix → recompile faster than a human reviewing code.

## The Conventional Wisdom

TypeScript and Python are dominant for agentic coding because:
- They're common and on-distribution for LLM training data
- Dynamic/interpreted = fast scaffold → run → iterate
- Simple syntax = high first-try success rate
- TypeScript's typing adds some guardrails, but `any` undermines them

Daniel's counter: **"Easy for the model to write is a bad thing to optimize for."**
The same flexibility that makes these languages easy also makes it easy for
models to write buggy code that looks correct.

## Why Testing Isn't Enough

1. Tests written after implementation test implementation details, not behavior
2. Tests can only prove incorrectness (not correctness) — impractical to test
   every input combination
3. LLMs generating tests make the same mistakes as LLMs generating code
4. Code review agents have the same failure modes as coding agents

The fundamental problem: non-deterministic systems reviewing non-deterministic
output. **You need deterministic guardrails.**

## Alien Intelligence

Reference: Yuval Noah Harari, _Nexus_. LLMs are not artificial intelligence —
they're **alien intelligence**. Their internal workings (token prediction streams)
are fundamentally different from human cognition. Their failure modes will be
unexpected. Code that "looks good" to a human reviewer may have subtle,
unexpected bugs. Deterministic enforcement catches what human intuition misses.

## Rust's Guardrails

- **Strict type safety** — no `any`, no unchecked casts
- **No universal null** — `Option<T>` with compiler-enforced checking
- **Fearless concurrency** — data races caught at compile time, not in production
- **Memory safety** — ownership + borrowing prevents entire classes of bugs
- **Actionable compiler errors** — descriptive messages tell the agent exactly
  what's wrong and how to fix it

The workflow: agent writes Rust → compiles → gets error → fixes → compiles
again. Every compile error = a production bug avoided. Compile time is faster
than human code review and catches more errors deterministically.

## Relevance to OCR

### The Compiler is the Ultimate Gate

This is Nick Nisi's "gates over agents" applied at the language level. The
Rust compiler is the most reliable gate in the system — it enforces correctness
deterministically, cannot be bypassed, and provides actionable feedback.

### Principle: Deterministic > Non-Deterministic for Validation

Evals, tests, and code review are non-deterministic (LLM-as-judge, flaky tests,
human error). The compiler is deterministic. **OCR should push as much validation
as possible into deterministic gates** — schema validation, type checking,
contract enforcement — before relying on non-deterministic gates (LLM-as-judge,
human review).

### Confirms Existing Decisions

- **Gates > agents** (Nick Nisi): The compiler is proof that deterministic gates
  outperform non-deterministic review
- **Evals as ETL** (Phil Hetzel): Tests are part of the eval pipeline, but
  they're not sufficient. Compile-time enforcement is better
- **Don't outsource the thinking** (Dex Horthy): If the compiler handles it,
  you don't need to think about it. Push to deterministic systems first.
