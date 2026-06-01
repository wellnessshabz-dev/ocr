---
title: "Spec-Driven Validation for AI Agents — Smart vs Safe (Steve / Safe Intelligence / AI Engineer)"
source_type: "youtube"
channel: "AI Engineer"
speaker: "Steve (Safe Intelligence)"
date: "2026"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "AI Engineer conference talk. Steve (CEO, Safe Intelligence) presents spec-driven validation for AI agents — going beyond datasets to explicit specifications with rules, ontologies, domain knowledge, and robustness requirements. Draws parallels to his previous work on OpenAPI spec."
tags: ["spec-driven-validation", "agent-validation", "smart-vs-safe", "rules", "ontologies", "robustness", "agent-card", "a2a-spec", "implementation-independence"]
---

# Spec-Driven Validation for AI Agents — Smart vs Safe

Source: AI Engineer conference. Steve (CEO, Safe Intelligence) on spec-driven
validation — specifying what agents should do beyond just datasets.

## Smart ≠ Safe

Bigger models are smarter but:
- **More jailbreak surface**: a poem-based jailbreak works on a smart model but
  a low-end model doesn't even understand the poem
- **More surface area to test**: broader remit = more to test
- **More expensive**: paying for tokens on simple tasks
- **Slower**: overkill for simple math

Goal: "good enough to perform, not capable of arbitrary harm."

Arbitrary harm has two dimensions:
1. **Input flexibility**: how instructions can be formulated
2. **Tool/task access**: what it can do in infrastructure (wire money vs answer questions)

## Components of an Agent Spec

| Component | Description | Example |
|-----------|-------------|---------|
| **Data sets** | Ground truth: what good looks like | Labeled Q&A pairs |
| **Rules** | Hard constraints | "Never give >10% discount" |
| **Ontologies / dictionaries** | Valid universe | Airline destinations, internal terminology |
| **Domain knowledge** | Substitutability rules | Gross profit ≠ gross sales |
| **Rights and roles** | Behavior varies by context | Logged in vs out, admin vs user |
| **Robustness requirements** | Stress conditions | Typos, rephrasing, fog equivalent for agents |

## Agent Card (A2A Spec)

Describes what the agent does. From the A2A spec. But even with an agent card,
you still need to define the range of valid variation (e.g., "what kind of
people can meetings be booked for").

## Security Testing via Specs

The edges of what the agent is supposed to do are where it's most vulnerable:
- It will be willing to talk about those domains
- It has more power to act in those areas

Pull spec information into security testing.

## Implementation Independence

> "You may be building in LangSmith or Vertex agents now, but later you may
> change infrastructure. Keep those integration tests, unit tests, and
> penetration tests independent."

Tests should live independently of the agent framework so you can swap.

## Close the Loop

Run automatically → get results → iterate to fill robustness gaps. "Jury-rigged
RL around the outside" — not proper RL on the model, but an outer loop that
improves the harness/guardrails.

## Future: OpenAPI-Style Agent Spec

Steve helped write OpenAPI spec. He's thinking about a similar approach for
agent validation: express the spec in a GitHub repo, version-controlled,
tool-agnostic, pull into whatever tool you want.

## Relevance to OCR

### Direct Architecture Parallels

| Safe Intelligence Concept | OCR Equivalent |
|---------------------------|----------------|
| Rules (hard constraints) | Policy engine — governance rules per shipment type |
| Ontologies / dictionaries | Ontology Manager — valid entity universe |
| Rights and roles | Access control — tenant permissions |
| Agent card (A2A spec) | Skill registry metadata — what each perspective agent does |
| Robustness requirements | Eval framework — test under stress conditions |
| Implementation independence | OCR's n8n + FastAPI testable independently of each other |
| Close the loop (jury-rigged RL) | Governance feedback → skill improvement cycle |

### Confirms Existing Decisions

| Decision | Confirmed By |
|----------|-------------|
| **Governance layer** (Validated / HumanReview / Rejected) | Rules + robustness checks match governance gates |
| **Ontology as shared substrate** | Ontologies/dictionaries are a spec component |
| **Policy engine** | Hard rules ("never give >10% discount") = policy engine |
| **Skill registry with metadata** | Agent card = skill metadata |
| **Implementation independence** | Tests should not depend on framework |
| **Audit → feedback loop** | Close the loop = audit → improve |

### What This Adds

| Insight | OCR Application |
|---------|-----------------|
| **Smart ≠ Safe is a design principle** | OCR's perspective agents should be "good enough to perform, not capable of arbitrary harm" — don't use Opus for everything |
| **Spec as version-controlled artifact** | OCR governance rules should live in GitHub, versioned, tool-agnostic — like OpenAPI |
| **Robustness requirements as first-class spec component** | Test OCR agents under stress: typos, rephrasing, edge cases |
| **The edges are where agents are most vulnerable** | Security test the ontology domain the agent operates in, not random inputs |
| **Jailbreaks work better on smart models** | A smaller, well-guarded model can be safer than a frontier model with broad remit |
| **"Jury-rigged RL" around the outside** | OCR doesn't need to fine-tune models — just improve the harness loop based on governance outcomes |
