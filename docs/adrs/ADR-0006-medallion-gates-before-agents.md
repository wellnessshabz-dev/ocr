# ADR-0006: Medallion Gates Before Agents

## Status

Accepted

## Context

OCR's directory structure is meticulously pre-created with `_index.md` signposts
for every component, but an audit (June 2026) found that 54 of 95 directories
are empty scaffolds — including the ENTIRE core cognitive runtime (shipments,
cognition, ontology, gbrain, orchestration). Only the web ingestion pipeline
is genuinely built.

The architecture document describes a rich cognitive system but does not specify
an implementation order. The ADRs define individual components (shipments,
ontology lifecycle, governance, replay) but not how they compose into a layered
data flow with enforced transitions.

Two external inputs shaped this decision:

1. **Nick Nisi's "Building AI Systems That Ship" talk (June 2026):** His harness
   (Case) uses a state machine to enforce gates between agents — implement →
   verify → review → close. The agents themselves are replaceable; the gates
   are not. His key data point: comprehensive skills degraded performance
   (77% → 97% by removing them). He only knew because he measured.

2. **Karpathy's LLM Wiki pattern (April 2026):** Three-layer knowledge base
   (raw sources → wiki → schema) with ingest/query/lint operations. Multiple
   implementations exist (nvk/llm-wiki 467★, Pratiyush/llm-wiki 252★).
   Graphify (56K★) demonstrates AST-based extraction → knowledge graph for any
   codebase — a reference implementation for what OCR's ontology/ should become.

## Decision

OCR adopts a **Medallion Architecture (Bronze → Silver → Gold) with enforced
gates between layers.** The gates are built before the agents they govern.

### Layer Definitions

```
Bronze (raw, immutable)          Silver (enriched, validated)      Gold (consumption)
─────────────────────────────    ──────────────────────────────    ──────────────────────
Append-only, never edited.       Cleaned, processed, decided.      Verified, human-facing.

raw/bronze-docs/                        shipments/compiler/               surfaces/executive/
raw/images/                      shipments/validator/              surfaces/ontology/
raw/skills/                      shipments/storage/                surfaces/replay/
ingestion/github/                shipments/schemas/                surfaces/shipments/
ingestion/web/                   shipments/replay/                 replay/
ingestion/obsidian/              cognition/councils/               observability/logs/
ingestion/filesystem/            cognition/chairman/               observability/metrics/
ingestion/manual/                cognition/governance/             observability/traces/
tests/                           ontology/extraction/              observability/audits/
                                 ontology/contradictions/
                                 ontology/graph/
                                 ontology/lifecycle/
                                 gbrain/activation/
                                 gbrain/episodic/
                                 gbrain/semantic/
                                 gbrain/temporal/
                                 gbrain/replay/
                                 orchestration/dags/
                                 orchestration/triggers/
                                 orchestration/n8n/
                                 ledger/ (write)
                                 docs/
                                 agents/
                                 infra/
                                 scripts/
                                 src/api/
                                 src/routers/
```

### Gate Definitions

Two gates enforce all layer transitions. Both are implemented as code (state
machines, not prompts) per Nick Nisi's principle: "enforce, don't instruct."

**Gate 1 — Bronze → Silver (Normalize + Validate)**

Located in: `shipments/compiler/` + `shipments/validator/`

Responsibilities:
- Strip PII and secrets from raw signals
- Validate schema compliance
- Resolve entity references against ontology
- Reject malformed signals with structured error messages
- Emit normalized shipment to Silver

Behavior on failure: Reject. Do not pass to Silver. Error logged to ledger/.

**Gate 2 — Silver → Gold (Govern + Prove)**

Located in: `cognition/governance/`

Responsibilities:
- Verify evidence is real (SHA-256 of test output, Playwright video of UI fix)
- Check for contradictions with past decisions (ontology/contradictions/)
- Confirm all required perspectives are represented
- Validate confidence threshold is met
- Escalate to human review when risk threshold is exceeded
- Commit to ledger/ only on pass

Behavior on failure: Reject back to cognition/chairman/ for rework. Do not reach
surfaces/. Three consecutive failures on the same shipment trigger human escalation.

### Build Order

Per "gates before agents," implementation proceeds in this order:

1. **Gate infrastructure first** — The eval pipeline, golden dataset, and gate
   code are built before any Silver agent code. Each gate is tested with
   synthetic shipments before real ones pass through.

2. **Bronze first** — The ingestion pipeline is the only genuinely built layer.
   It stays. New ingestion channels (GitHub, Obsidian, filesystem) are added
   to Bronze before Silver expands.

3. **Silver gates before Silver agents** — The Bronze→Silver gate
   (shipments/compiler + validator) is built and tested before cognition/
   receives a single shipment.

4. **Gold gates before Gold surfaces** — The Silver→Gold gate
   (cognition/governance) is built before surfaces/executive/ receives
   real decisions.

5. **Evals as build precondition** — Every new component ships with its eval
   cases built first. The golden dataset in replay/ grows with each component.
   A component is not "done" until it passes its eval suite.

### Skills as Gotchas

Per Nick Nisi's data (comprehensive skills: 77% correct; no skills: 97% correct),
the existing 17 skill templates in `raw/skills/` are reframed from comprehensive
reference documents to **gotcha files** — 3-5 common failure modes per topic.

Format:

```markdown
# Skill: Next.js AuthKit

## Gotchas

1. **Proxy redirects** — In Next.js middleware, `redirect()` only works inside
   the proxy. Calling it outside the proxy throws silently.
2. **Route handler exports** — App Router route handlers must export named
   functions (`GET`, `POST`), not default exports.
3. **Edge runtime** — AuthKit middleware requires the Edge runtime. If your
   project uses Node.js runtime in middleware, AuthKit won't initialize.
```

The full `raw/skills/` directory is preserved as Bronze reference, but the
active skills loaded into cognition/ are the gotcha variants.

### Ontology Implementation Pattern

Per the LLM Wiki and Graphify patterns, OCR's ontology layer follows three
passes matching the existing directory structure:

```
Pass 1 — Extraction (ontology/extraction/)
    AST-based for code (tree-sitter, 25 languages)
    LLM-based for docs, signals, images
    Output: candidate nodes + relationships

Pass 2 — Graph (ontology/graph/)
    Merge candidates into existing NetworkX graph
    Leiden community detection for clustering
    Export: interactive HTML + queryable JSON + index.md

Pass 3 — Maintenance (ontology/contradictions/ + lifecycle/)
    Detect contradictions, gaps, stale claims
    Apply lifecycle transitions (candidate → confirmed → dormant)
    Schedule periodic lint council
```

This builds on ADR-0003 (Ontology Lifecycle Governance) and ADR-0004
(Replayability Requirements) by specifying the implementation pattern.

### Eval Pipeline as ETL

Following Nick Nisi's "measure everything" principle, an eval pipeline runs
alongside the build process:

```
EXTRACT                          TRANSFORM                          LOAD
───────                          ─────────                          ────

replay/ golden dataset           cognition/ pipeline                observability/
past shipments + expected         current councils +                 metrics keyed by
decisions                         chairman + governance              trace_id

ledger/ expected                  ontology/ resolution              surfaces/executive
outcomes                          compare extraction                 alert on degradation

eval configuration                gbrain/ memory                    ledger/
(suite definition)                 replay memory activation          commit eval audit trail
```

Each eval run compares a variant against a baseline:
- Run A: current system (baseline)
- Run B: proposed change (variant)
- Result: pass rate, confidence delta, latency regression, cost impact
- Gate: if pass rate drops beyond threshold, the change is rejected

The eval pipeline itself is governed by the Silver→Gold gate — an eval result
is a decision that goes through governance before it can promote a change.

## Consequences

### Positive

- **Build order is defined.** No more ambiguity about what to implement first.
  Gates before agents, Bronze before Silver before Gold.
- **Evals prevent degradation.** Nick Nisi's 77% → 97% regression would be
  caught before deployment.
- **Skills stop being harmful.** Comprehensive docs → gotchas = better performance.
- **Ontology has a reference implementation.** Graphify and LLM Wiki provide
  proven patterns for extraction and graph building.
- **Gates are the non-negotiable core.** If the system has nothing else, it has
  gates that validate, govern, and prove. Everything else is replaceable.

### Negative

- **Slower initial velocity.** Building gates and evals before agents means
  the first shipment through cognition takes longer to achieve.
- **Golden dataset bootstrapping cost.** Evals need known-good cases, which
  don't exist yet for 85% of the system. Initial evals run on synthetic data.
- **Two codebases to maintain.** The gate code (state machines) and the agent
  code (LLM-driven) evolve separately. Changes to agent interfaces may require
  gate updates.

### Risks

- **Premature gate hardening.** Gates built before agents might over-constrain
  the system. Mitigation: gates start permissive and tighten as agent behavior
  stabilizes.
- **Eval dataset drift.** As the system evolves, golden cases become stale.
  Mitigation: periodic eval dataset refresh via replay/.
- **Medallion rigidity.** Strict layering might discourage cross-layer patterns
  that emerge as optimal. Mitigation: documented escape hatch (peer connections
  bypass gates with explicit governance approval).

## Supersedes

None. This ADR complements ADR-0005 (Governance Before Autonomy) by specifying
what governance actually enforces and in what order to build it.
