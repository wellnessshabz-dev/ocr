---
title: "Self-Improving Trading Agent with Hermes — Goal-Driven AI Loop (Lewis Jackson)"
source_type: "youtube"
channel: "Lewis Jackson"
speaker: "Lewis Jackson"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Lewis Jackson's YouTube channel. Builds a self-improving trading agent using Hermes agent and Railway. Covers goal definition, self-learning loop, scientific method for improvement, and human approval gates."
tags: ["hermes", "trading-agent", "self-improving", "goal-driven", "scientific-method", "human-approval", "railway", "multi-agent"]
---

# Self-Improving Trading Agent with Hermes — Goal-Driven AI Loop

Source: Lewis Jackson's YouTube channel. Practical build of a self-improving
trading agent using Hermes + Railway for 24/7 hosting.

## Four Criteria for a Trading Agent

| Criterion | Requirement |
|-----------|-------------|
| **Accurate** | Data quality, API reliability, objective interpretation of news |
| **Reliable** | Running 24/7 — hosted on Railway so it survives computer shutdown |
| **Well-defined goal** | Explicit success (sharp score, target return) AND failure (max drawdown) |
| **Self-improving** | Learn from outcomes, form hypotheses, iterate |

## Self-Improvement Loop (Scientific Method)

```
Strategy → Outcome → Analyze (toward/away from goal) → Hypothesis → Updated Strategy
```

**Rules**:
- Change **only one variable** at a time (scientific method)
- If result improves → new baseline
- Iterate on new baseline
- Track what changed and why

> "If you change a load of variables and got more profitable, you wouldn't know
> which variable was responsible. Change one variable at a time."

## Architecture

- **Hermes agent**: self-learning brain, reviews trades weekly
- **Railway**: 24/7 hosting, automatic deployments
- **Cornelius** (separate agent): tunes learned parameters JSON weekly
- **Staggered review**: Cornelius adjusts parameters, Hermes reviews trades 3 days later
- **Human approval gate**: first cycle is read-only → human sets mode to live

## Goal Definition

| Metric | Example |
|--------|---------|
| Target return (30 days) | 47% |
| Minimum sharp score | 1.0 |
| Max drawdown | Configurable |
| Failure condition | Below threshold for N days |
| Maximum positions | 12 |
| Slippage tolerance | Configurable |
| Gas reserve | Configurable |

## Relevance to OCR

### Self-Improving Goal Loop

| Trading Agent | OCR Equivalent |
|---------------|----------------|
| Strategy → outcome → analyze → hypothesis → update | Shipment → governance → trajectory analysis → skill improvement |
| Change one variable at a time | OCR policy experiments should isolate one governance variable |
| Success + failure definition | Governance: Validated / HumanReview / Rejected thresholds |
| Staggered multi-agent review | Council with different perspectives on different schedules |
| Human approval gate before live | Governance: HumanReview before production deployment |
| 24/7 hosted (Railway) | OCR's VPS with n8n + FastAPI |

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Human approval gate for high-stakes** | First cycle read-only → human approval → live |
| **Goal-defined deliberation** | Shipment must have explicit success AND failure criteria |
| **Multi-agent staggered review** | Different agents review at different cadences |
| **One-variable experiments** | OCR governance changes should be isolated and measured |
| **24/7 hosting requirement** | Agent must survive computer shutdown |
| **Audit trail of changes** | Every variable change tracked |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **Scientific method for agent improvement** | Every policy change runs as an A/B test — one variable at a time |
| **Goal requires failure definition, not just success** | OCR shipments need explicit failure thresholds, not just "pass/fail" |
| **Staggered multi-agent review** | Different perspectives on different cadences (weekly vs daily) |
| **Self-learning loop requires bounded scope** | The loop only works if the goal is narrow and quantifiable |
| **One-shot prompt as deployment artifact** | The entire system bootstrapped from a single prompt — OCR should support manifest-based deployment |
