# ADR-0007: Adversarial Validation — Separate Deliberation from Governance

## Status

Proposed

## Context

OCR's council architecture (ADR-0002, ADR-0005, ADR-0006) defines governance as a gate that validates council syntheses before commitment. It does not specify **who or what performs the validation** — leaving open the default that the same model, same perspective, or even the same session that produced the synthesis also validates it.

Three independent production-tested systems have found that self-validation (same model writes and judges) is unreliable:

1. **Factory Missions (Luke Alvoeiro)**: Their orchestrator-worker-validator architecture failed when the validator used the same model and context as the worker. The validator consistently missed the same blind spots. Fix: the validator must have a **fresh context window** and, ideally, a **different model family**. They report validation never succeeds on the first go — and only catches real issues when the validator hasn't seen the worker's output before.

2. **IBM Harness Engineering (Tejas)**: His verify step is explicitly designed as a **deterministic override** — not an LLM-as-judge. The verify step checks factual claims by running them against deterministic systems (database queries, API calls, file system checks). He calls this "removing the lying" — an LLM cannot verify its own output with the same context it used to produce it, because it will rationalize rather than detect.

3. **Self-Validation Critique (Simon Scrapes)**: In his analysis of Hermes' self-learning loop, the same model writes a skill AND judges its quality. The model cannot see its own blind spots — it judges the skill as good because it doesn't know what it doesn't know. He demonstrates this produces skills that pass self-review but fail in production.

4. **Anthropic Internal (Nate Herk, via email incident)**: An agent sent 150K emails unprompted because the governance check was performed by the same model in the same session. The model validated its own plan as "acceptable" — it had no external reference point to detect the overreach. Karpathy's framing: "instructions are not capabilities" — you can't validate what you can't see.

### The Core Problem

When deliberation and governance share the same:
- **Model**: Same blind spots, same failure modes
- **Context window**: Same framing, same assumptions, same rationalization
- **Session history**: Same narrative constructed during deliberation
- **Perspective**: Same understanding of what "good" means

...the governance gate becomes a rubber stamp. It finds trivial issues (typos, formatting) but misses structural problems (contradictions, overreach, missing evidence).

### What Production Systems Do Instead

| System | Deliberation Model | Governance Model | Governance Type |
|--------|-------------------|------------------|-----------------|
| Josh's Conductor (shpigford) | Opus 4.7 | GPT 3.5 | Adversarial model review |
| Mickey's Cursor (resmic) | GPT 5.5 / Opus 4.7 | Greptile + GPT 5.5 | External code review + auto-fix loop |
| Factory Missions | Orchestrator (Opus) | Validator (Haiku) | Separate model, fresh context, validation contract |
| Matt Pocock | Claude Code | Grill Me skill | Different session, different prompt, fresh context |
| Nick Nisi (Case) | Agent | Gate | Deterministic state machine (no LLM in gate) |

The common pattern: **the governance actor has never seen the proposal before.** It approaches with fresh eyes, a different model (or at minimum a fresh context), and often a different model family to avoid correlated blind spots.

## Decision

OCR enforces **adversarial validation** as an architectural principle:

### Rule 1: Governance Does Not Share Deliberation Context

The governance gate that validates a council synthesis runs in an **independent context window** that has never seen the deliberation session. It receives only:
- The synthesis output (position summaries + chairman draft)
- The validation contract (pre-defined "done" criteria)
- The evidence references (not the evidence itself — it must fetch fresh)

It does NOT receive:
- The deliberation conversation history
- The raw perspective agent outputs
- The chairman's internal reasoning chain

### Rule 2: Governance Uses a Different Model Family

The governance model must be from a **different model family** than the deliberation model:
- If deliberation uses Opus → governance uses GPT (or Haiku, or DeepSeek)
- If deliberation uses GPT 5.5 → governance uses Opus (or Claude Haiku)
- The goal is uncorrelated blind spots: different training data, different alignment, different failure modes

If using the same model family is unavoidable (e.g., single-provider constraint), governance must use a **significantly smaller/cheaper variant** (e.g., Haiku for governance, Opus for deliberation) to force different behavior through scale differences.

### Rule 3: Deterministic Checks Before LLM Validation

Per Tejas and Daniel Zook's patterns, governance performs deterministic checks FIRST:

1. **Schema validation** — Does the synthesis conform to the expected format?
2. **Evidence verification** — Are the cited evidence references real? (SHA-256 of cited artifacts, or playback of recorded evidence)
3. **Contradiction check** — Does the synthesis contradict any past decision in the ontology? (Query against `ontology/contradictions/`)
4. **Scope check** — Does the synthesis operate within the shipment's declared scope?

Only after all deterministic checks pass does the LLM-based adversarial review run.

### Rule 4: Governance Runs Multiple Passes

Following Greptile + Grep Loop pattern (Mickey) and Josh's "But for Real" skill:

- **Pass 1 — Deterministic checks** (Rule 3, no LLM)
- **Pass 2 — Adversarial review** (fresh context, different model, validation contract)
- **Pass 3 — "But for Real"** — A meta-pass that assumes Pass 2 missed something. Prompt: "You almost certainly missed something. Challenge the synthesis again, specifically where it seems most confident."

Each pass is a separate clean context window with no shared history. The gate does not pass until all three passes succeed.

### Rule 5: Governance Defaults to Human Escalation on Low Confidence

If the governance model's confidence in its own assessment falls below a threshold, or if deterministic checks find anomalies that cannot be automatically resolved:

- The shipment is escalated to human review
- All three passes' outputs are bundled for the human reviewer
- The human sees: validation contract → deterministic check results → adversarial findings → "But for Real" findings
- The human can approve, reject, or request rework

### Implementation

Adversarial validation lives in `cognition/governance/` and is a prerequisite gate in the Medallion architecture (ADR-0006):

```
shipment → cognition/councils/ → governance/validation → governance/adversarial/governance/but-for-real → surfaces/
```

Each governance pass writes its output to the audit ledger (`ledger/`) with:
- `pass_number`: 1, 2, or 3
- `model_used`: the model family for this pass
- `context_fingerprint`: hash of the context window (to prove independence)
- `passed`: boolean
- `findings`: structured list of issues found
- `confidence`: governance model's self-assessed confidence

## Consequences

### Positive

- **Catches blind spots.** Fresh eyes find issues that the deliberation model rationalized away.
- **Uncorrelated failure modes.** Different model families fail differently — what Opus misses, GPT catches, and vice versa.
- **Production-validated pattern.** Josh, Mickey, Luke, Matt, and Tejas all independently use variants of this and report it catches bugs every time.
- **Auditable separation.** The ledger proves that governance had independent context — critical for organizational trust.

### Negative

- **2-3x governance token cost.** Each pass has a fresh context window and may use premium models. Mitigation: Haiku or GPT 3.5 for governance passes (cheaper models work fine for adversarial review).
- **Added latency per shipment.** Three passes with deterministic checks add minutes per governance gate. Mitigation: governance runs in parallel with other shipments' deliberation.
- **"But for Real" meta-pass can loop.** If the meta-pass keeps finding issues, it can run indefinitely. Mitigation: max 3 iterations, then mandatory human escalation.

### Risks

- **Adversarial hallucination.** The governance model might hallucinate issues that don't exist. Mitigation: deterministic checks first (Rule 3) ground the review in reality. Adversarial findings without deterministic evidence are escalated to human.
- **Model family lock-in might not exist.** If all frontier models have correlated blind spots (e.g., all miss the same class of security vulnerability), adversarial validation across model families provides false confidence. Mitigation: invest in deterministic checks (Rule 3) as the primary safety mechanism — LLM review is secondary.
- **Governance becomes the bottleneck.** Three passes per shipment could become the slowest part of the pipeline. Mitigation: right-size governance frequency by risk tier — high-risk shipments get full 3-pass adversarial review, low-risk get 1-pass deterministic only.

## Supersedes

None. This ADR specifies the validation mechanism within the governance gate defined in ADR-0005 and ADR-0006.
