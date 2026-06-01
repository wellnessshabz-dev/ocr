---
title: "Transit Authority — Orchestration"
description: "n8n orchestration DAGs, triggers, and workflow definitions. The nervous system connecting all districts."
status: "active"
district: "orchestration"
type: "district"
child_districts: ["dags", "n8n", "triggers"]
neighbors: ["ingestion", "shipments", "cognition", "gbrain"]
traffic:
  reads: ["ingestion/ (event streams)", "shipments/ (state)"]
  writes: ["All districts (via DAG triggers)"]
blast_radius:
  services: ["All automated workflows"]
  data: ["Workflow state, execution history"]
  depends_on_accuracy: "high (wrong routing = lost signals)"
connections:
  - direction: "upstream"
    to: "ingestion/"
    via: "Ingestion DAG"
    purpose: "Routes normalized events to the compiler"
  - direction: "downstream"
    to: "shipments/compiler"
    via: "Shipment DAG"
    purpose: "Triggers compilation on new events"
  - direction: "peer"
    to: "cognition/ -> gbrain/"
    via: "Council DAG -> Memory DAG"
    purpose: "Chains deliberation into memory consolidation"
naming:
  pattern: "snake_case"
  rules:
    - "DAGs named after the pipeline they orchestrate"
    - "Triggers named after the event pattern they match"
partitioning:
  rule: "By workflow category: dags (definitions), n8n (n8n exports), triggers (event patterns)"
maintainers: ["shadabkhan"]
---

# 🎼 Transit Authority — Orchestration

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **📊 `dags/`** — DAGs — n8n DAG Definitions
- **📂 `n8n/`** — n8n — n8n Workflow Exports
- **🔔 `triggers/`** — Triggers — Event Triggers

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ⬅️ **Receives from** ingestion/ (via Ingestion DAG) — Routes normalized events to the compiler
- ➡️ **Sends to** shipments/compiler (via Shipment DAG) — Triggers compilation on new events
- ➡️ **Sends to** cognition/ -> gbrain/ (via Council DAG -> Memory DAG) — Chains deliberation into memory consolidation

## What It Reads and Writes

**Reads from:** ingestion/ (event streams), shipments/ (state)
**Writes to:** All districts (via DAG triggers)

## How Important Is This?

**If this breaks:** All automated workflows will be affected.
**Data at risk:** Workflow state, execution history.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `orchestration/dags/`
- `orchestration/n8n/`
- `orchestration/triggers/`

## Related Directories

- `ingestion/`
- `shipments/`
- `cognition/`
- `gbrain/`

---
*Transit Authority — Orchestration — part of the OCR system. See `_index.md` in this directory for orientation.*
