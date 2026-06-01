---
title: "Audits — Audit Observability"
description: "Audit-specific observability: compliance views, lineage queries, and audit trail exploration."
status: "active"
district: "observability/audits"
type: "neighborhood"
parent: "observability"
neighbors: ["ledger", "observability/logs", "observability/metrics"]
traffic:
  reads: ["ledger/ (audit records)"]
  writes: ["surfaces/executive (compliance views)"]
blast_radius:
  services: ["Compliance monitoring"]
  data: ["Audit observability state"]
  depends_on_accuracy: "critical"
---

# 📋 Audits — Audit Observability

Audit-specific observability. Separate from regular logging, this tracks governance decisions, policy violations, and human review actions. Feeds the audit ledger.

## What It Reads and Writes

**Reads from:** ledger/ (audit records)
**Writes to:** surfaces/executive (compliance views)

## How Important Is This?

**If this breaks:** Compliance monitoring will be affected.
**Data at risk:** Audit observability state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `ledger/`
- `observability/logs/`
- `observability/metrics/`

---
*Audits — Audit Observability — part of the OCR system. See `_index.md` in this directory for orientation.*
