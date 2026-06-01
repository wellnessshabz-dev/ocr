---
title: "Parliament — Cognition Runtime"
description: "The core deliberation engine: skills, councils, chairman, governance. This is where organizational reasoning happens."
status: "active"
district: "cognition"
type: "district"
child_districts: ["chairman", "councils", "governance", "skills"]
neighbors: ["agents", "shipments", "gbrain", "ontology"]
traffic:
  reads: ["shipments/compiler (incoming shipments)", "ontology/ (concepts)"]
  writes: ["gbrain/ (memory updates)", "ledger/ (audit trail)"]
blast_radius:
  services: ["Council deliberation", "Skill execution", "Chairman synthesis"]
  data: ["All decision-making state"]
  depends_on_accuracy: "critical"
connections:
  - direction: "upstream"
    to: "shipments/compiler"
    via: "ActivationScore computation"
    purpose: "Shipments trigger council deliberation"
  - direction: "downstream"
    to: "gbrain/"
    via: "Memory consolidation pipeline"
    purpose: "Decisions committed to memory substrate"
  - direction: "downstream"
    to: "ledger/"
    via: "Governance commit hook"
    purpose: "Every decision is audit-logged"
naming:
  pattern: "snake_case"
  rules:
    - "Skills are one file per protocol definition"
    - "Council orchestrator is a single module"
partitioning:
  rule: "By cognitive function: chairman, councils, governance, skills"
maintainers: ["shadabkhan"]
---

# 🧠 Parliament — Cognition Runtime

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **👤 `chairman/`** — Chairman — Synthesis Engine
- **🏛️ `councils/`** — Councils — Deliberation Orchestrator
- **⚖️ `governance/`** — Governance — Policy & Validation
- **🔧 `skills/`** — Skills — Skill Protocol Registry

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ⬅️ **Receives from** shipments/compiler (via ActivationScore computation) — Shipments trigger council deliberation
- ➡️ **Sends to** gbrain/ (via Memory consolidation pipeline) — Decisions committed to memory substrate
- ➡️ **Sends to** ledger/ (via Governance commit hook) — Every decision is audit-logged

## What It Reads and Writes

**Reads from:** shipments/compiler (incoming shipments), ontology/ (concepts)
**Writes to:** gbrain/ (memory updates), ledger/ (audit trail)

## How Important Is This?

**If this breaks:** Council deliberation, Skill execution, Chairman synthesis will be affected.
**Data at risk:** All decision-making state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Quick Reference

- `cognition/chairman/`
- `cognition/councils/`
- `cognition/governance/`
- `cognition/skills/`

## Related Directories

- `agents/`
- `shipments/`
- `gbrain/`
- `ontology/`

---
*Parliament — Cognition Runtime — part of the OCR system. See `_index.md` in this directory for orientation.*
