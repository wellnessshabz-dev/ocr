---
title: "Context is the New Code — Patrick Debois, Tessel"
source_type: "youtube"
channel: "AI Engineer"
speaker: "Patrick Debois"
date: "2026-06"
url: ""
status: "reasoned"
processed_by: "human + claude"
source_notes: "Transcript from talk at AI Engineer conference. Patrick Debois is the founder of DevOpsDays, inventor of the term 'DevOps,' and creator of Tessel (context management platform for AI coding agents)."
tags: ["context-lifecycle", "cdlc", "evals", "skills-as-packages", "observability", "context-filter", "sbom", "tessel"]
---

# Context is the New Code — Patrick Debois, Tessel

Source: AI Engineer conference, June 2026. Patrick Debois, Tessel founder.

## Core Thesis

Code used to be what we wrote. Now **context is the new code** — the prompts, instructions, skills, documentation references, and agent configuration we assemble are the primary output of an AI-native developer. Like code before it, context needs a **development lifecycle**: Generate → Evaluate → Distribute → Observe → Adapt.

Patrick proposes the **Context Development Life Cycle (CDLC)**:

```
Generate → Evaluate → Distribute → Observe → Adapt → (back to Generate)
```

Each stage mirrors a phase in the traditional SDLC but adapted for the properties of context (non-deterministic, LLM-dependent, composable).

## CDLC Breakdown

### 1. Generate

Context is generated from multiple sources:
- **Manual prompting** — the baseline, typing into chat
- **Instructions/skills** — reusable prompt packages (agent.md, CLAUDE.md, skills)
- **Documentation fetching** — pull latest docs from libraries to prevent hallucination
- **MCP integrations** — pull context from Slack, GitHub, GitLab, Jira
- **Spec-driven generation** — write a spec, agent decomposes into step-by-step prompts

Key insight: the same content is now both **input** (what we write) and **output** (what agents produce). The distinction between code and context is blurring.

### 2. Evaluate (Most Novel Contribution)

Testing context is fundamentally different from testing code because **context is non-deterministic**. The same input produces different output across runs and models. Patrick proposes a **layered testing model**:

| Level | Analogy | Method | Determinism |
|-------|---------|--------|-------------|
| **Lint** | IDE squiggly lines | Validate format, schema, length constraints | Deterministic |
| **Comprehension** | Grammarly for context | Ask LLM: "Can an agent execute this? Is anything ambiguous?" | Probabilistic |
| **Unit tests** | Rule-based checks | "Does generated code prefix all endpoints with `/awesome`?" — LLM or regex | Hybrid (run multiple times) |
| **E2E tests** | Integration tests | LLM-as-judge with tools — sandbox, execute curl, verify behavior | Probabilistic |

**Critical pattern**: evals must be run multiple times and tracked with **error budgets**. Run 5 times, pass/fail rate = x/5. Some tests need 100% pass rate (security), others can tolerate <20% failure (style).

A/B testing context:
```
Run A: WITHOUT skill loaded → 97% pass rate
Run B: WITH skill loaded    → 77% pass rate
→ Degradation detected. Skill is hurting.
```

This confirms Nick Nisi's finding from a different angle — measurement is the only way to know.

### 3. Distribute

Context packages follow the same trajectory as code libraries:
- **Check into repo** — share with team (zero friction)
- **Package as skill** — reusable context bundles with dependencies (skills are the new npm packages)
- **Registry** — discover and install skills (Tessel registry, marketplace)
- **Dependency hell** — context packages clash (React skill vs Frontend skill)
- **Security scanning** — Snyk for context (credential leaks, third-party exposure, prompt injection)
- **AI SBOM** — who built it? What model? What dependencies? Supply chain for context

Patrick is blunt: "99.9% of skills in public registries is crap." Quality standards need evals.

### 4. Observe

Feedback channels for context quality:
- **Agent logs** — what did the agent try to do? Where did it get stuck? Missing context surfaces here
- **PR reviews** — incomplete PR = feedback on context, not just the code
- **Production instrumentation** — generated code that fails in production = eval case
- **Sandboxing** — run agents in sandbox, monitor for prompt injection, breakout attempts

Organizational observation: if every developer on a team hits the same missing-context problem, fix the context once, distribute to everyone.

### 5. Adapt

Close the loop: use observation data to improve context:
- Production failures → new eval cases
- Missing context signals → new skills
- Agent misunderstanding → rewrite context for clarity
- Team-level adaptation → context becomes organizational asset

## The Two Loops

Patrick distinguishes two feedback loops:

```
SOLO LOOP                     ORGANIZATIONAL LOOP
─────────                     ────────────────────
Individual developer          Team / org scale
Author context                Author context
Test it yourself              Distribute as packages
Fix what breaks               Monitor usage across teams
Repeat                        Collect feedback from all
                              Improve once, benefit all
```

The solo loop is where most people are. The organizational loop is where OCR lives — an org-scale context lifecycle.

## Relevance to OCR

### CDLC Maps to Medallion

| CDLC Stage | Medallion Layer | OCR Component |
|------------|----------------|---------------|
| Generate | Bronze | ingestion/, raw/bronze-docs/ |
| Evaluate | Silver gate | cognition/governance/ + shipments/validator/ |
| Distribute | Silver → Gold | skills/, ontology/graph/ |
| Observe | Gold | observability/, replay/ |
| Adapt | Feedback to Bronze | replay/ → new raw/ |


### New Insights Not Covered by Other Sources

1. **Context Filter (WAF for prompts)** — Patrick notes that agents load agent.md and skill.md without restriction. A prompt injection WAF is needed to filter context loaded from untrusted registries. OCR's governance layer should include a context filter.

2. **Error budget model for evals** — Nick says "run evals once" implicitly. Patrick says run them 5 times, use error budgets. OCR's eval pipeline should implement this.

3. **AI SBOM for skills** — every skill package needs metadata: model version it was built for, dependencies, security scan results, provenance. OCR's `raw/skills/` and any future registry should include SBOM fields.

4. **Production feedback as eval generatator** — instrument generated code to report failures. OCR's observability layer should connect to production failures → new golden eval cases.

5. **Context as library, not config** — context needs versioning, dependency management, security scanning, and quality gates — the same treatment code libraries get in mature orgs.

### Confirms Existing OCR Decisions

- **Evals are a precondition** — the CDLC starts with evaluation. You cannot improve what you don't measure. (Confirms ADR-0006)
- **Skills as gotchas** — Patrick's data that 99.9% of skills are crap and degrade performance confirms Nick's 77% finding
- **Test context like code** — lint → unit → e2e layered testing matches OCR's gate structure
- **Serial processing** — Patrick's funnel structure (one item through all stages) is inherently serial, confirming Luke's correction
- **Organizational loop** — OCR's entire purpose is the organizational loop, not just the solo loop

### Key Divergence (OCR vs Tessel)

| Dimension | Tessel | OCR |
|-----------|--------|-----|
| Scope | Context for coding agents | Organizational cognition (decisions, strategy) |
| Output | Better code generation | Better organizational decisions |
| User | Individual developer | Organization / executives |
| Scale | Team-level | Enterprise-level |
| Context type | Prompts, instructions, skills | Shipments, ontology, trajectories |

Tessel is about making code agents better. OCR is about making organizations smarter. They overlap at the context-management layer but serve different end goals.

## Comparison with Other Sources

| Dimension | Nick Nisi | Matt Pocock | Luke Alvoeiro | Patrick Debois | Dex Horthy | Karpathy | Boris Cherny | Phil Hetzel |
|-----------|-----------|-------------|---------------|----------------|------------|----------|--------------|------------|
| **Core frame** | Gates + measurement | Workflow + design | Production architecture | **Lifecycle management** | **Context window management** | **Paradigm shift (SW 3.0)** | **Product overhang + org process** | **Eval maturity continuum** |
| **Key concept** | State machine | Grill Me, deep modules | Orchestrator/worker/validator | **CDLC** | **RPI** | **Jagged intelligence** | **Loops, routines** | **Eval flywheel** |
| **Testing approach** | SHA/video proof, evals | TDD | Validation contracts | **Layered evals** | **Plan verification** | **Verifiability lever** | **Auto loops** | **Human annotation → LLM-judge → trace eval → automated discovery** |
| **Distribution model** | Skills in repo | Skills, once.sh | Structured handoffs | **Packages + SBOM** | **Compressed artifacts** | **Agent-native infra** | **MCP for everything** | **Production traces as datasets** |
| **Biggest insight** | Gates > intelligence | Code is NOT cheap | Serial beats parallel | **Context needs lifecycle** | **Don't outsource thinking** | **Can't outsource understanding** | **Org process > technology** | **Eval your eval. Start with human justification, not automation.** |
| **Org scope** | Team | Individual + team | Team + product | **Team + org** | **Team + org** | **Industry-wide** | **Company-wide** | **Team → org** |

**What Patrick adds that no one else covers:**
- The *full lifecycle view* — no one else connects Generate→Evaluate→Distribute→Observe→Adapt
- *Context as a library discipline* — registries, dependencies, SBOMs, security scanning
- *Error budgets for non-deterministic testing* — run 5x, track rate, allow thresholds
- *Context filters* — security at the context-loading layer
- *Production instrumentation → eval cases* — the observe→adapt→generate feedback loop
- *Organizational vs solo loop* — the flywheel effect of shared context at scale
