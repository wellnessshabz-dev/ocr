---
title: "ADRs — Architecture Decision Records"
description: "Date-prefixed records of architectural decisions made during the OCR project."
status: "active"
district: "docs/adrs"
type: "neighborhood"
parent: "docs"
neighbors: ["docs/architecture", "agents.md"]
traffic:
  reads: ["Agents seeking historical decision context"]
  writes: ["Humans logging new decisions"]
blast_radius:
  services: ["None directly"]
  data: ["Historical decisions"]
  depends_on_accuracy: "high (misleading ADRs cause wrong future decisions)"
---

# 📝 ADRs — Architecture Decision Records

This directory contains 6 files.

**Documentation:**
- `ADR-0001-agent-agnostic-runtime.md`
- `ADR-0002-shipment-first-cognition.md`
- `ADR-0003-ontology-lifecycle-governance.md`
- `ADR-0004-replayability-requirements.md`
- `ADR-0005-governance-before-autonomy.md`
- `ADR-0006-medallion-gates-before-agents.md`

## What It Reads and Writes

**Reads from:** Agents seeking historical decision context
**Writes to:** Humans logging new decisions

## How Important Is This?

**If this breaks:** None directly will be affected.
**Data at risk:** Historical decisions.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `docs/adrs/ADR-0001-agent-agnostic-runtime.md`
- `docs/adrs/ADR-0002-shipment-first-cognition.md`
- `docs/adrs/ADR-0003-ontology-lifecycle-governance.md`
- `docs/adrs/ADR-0004-replayability-requirements.md`
- `docs/adrs/ADR-0005-governance-before-autonomy.md`
- `docs/adrs/ADR-0006-medallion-gates-before-agents.md`

## Related Directories

- `docs/architecture/`
- `agents.md/`

---
*ADRs — Architecture Decision Records — part of the OCR system. See `_index.md` in this directory for orientation.*
