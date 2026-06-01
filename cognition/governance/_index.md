---
title: "Governance — Policy & Validation"
description: "Validation rules, policy engine, access control, and escalation for council outcomes. The Silver→Gold gate in Medallion architecture."
status: "active"
district: "cognition/governance"
type: "neighborhood"
parent: "cognition"
neighbors: ["cognition/chairman", "ledger", "observability/audits"]
traffic:
  reads: ["cognition/chairman (synthesis drafts)"]
  writes: ["ledger/ (committed decisions)", "cognition/ (rejection feedback)"]
blast_radius:
  services: ["Decision validation, policy enforcement"]
  data: ["Policy state, validation results"]
  depends_on_accuracy: "critical (bad policy = bad decisions go through)"
---

# ⚖️ Governance — Policy & Validation

Documentation for the governance system — policies, rules, escalation procedures, and human-in-loop protocols. Describes how decisions are validated and audited.

## What It Reads and Writes

**Reads from:** cognition/chairman (synthesis drafts)
**Writes to:** ledger/ (committed decisions), cognition/ (rejection feedback)

## How Important Is This?

**If this breaks:** Decision validation, policy enforcement will be affected.
**Data at risk:** Policy state, validation results.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Medallion Role — Silver→Gold Gate

This is the **most important gate in the system.** Per the Nick Nisi thesis
(`raw/bronze-docs/architecture_synthesis.md`), gates matter more than agents. Governance is
the gate between the Silver layer (development, enrichment, decisions) and the
Gold layer (consumption, audit, executive surfaces).

Every decision must pass through this gate before it reaches `ledger/` or
`surfaces/`. The gate enforces:
- Evidence is real (SHA, video, logs)
- No contradiction with past decisions
- Required perspectives are represented
- Confidence threshold is met
- Human-in-loop when required

If the gate rejects, the decision goes back to Silver (`cognition/chairman/`) for
rework. This is Nick Nisi's state machine — enforced by code, not by asking nicely.

## Related Directories

- `cognition/chairman/`
- `ledger/`
- `observability/audits/`

---
*Governance — Policy & Validation — part of the OCR system. See `_index.md` in this directory for orientation.*
