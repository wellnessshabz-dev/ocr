---
title: "Triggers — Event Triggers"
description: "Event trigger patterns and webhook definitions that start n8n DAG execution."
status: "active"
district: "orchestration/triggers"
type: "neighborhood"
parent: "orchestration"
neighbors: ["orchestration/dags", "ingestion"]
traffic:
  reads: ["ingestion/ (event patterns)"]
  writes: ["orchestration/dags (trigger bindings)"]
blast_radius:
  services: ["Event-driven DAG execution"]
  data: ["Trigger registration state"]
  depends_on_accuracy: "high"
---

# 🔔 Triggers — Event Triggers

Defines what triggers each n8n DAG — time-based schedules, webhooks, file events, or manual launches. Maps external events to the right DAG execution.

## What It Reads and Writes

**Reads from:** ingestion/ (event patterns)
**Writes to:** orchestration/dags (trigger bindings)

## How Important Is This?

**If this breaks:** Event-driven DAG execution will be affected.
**Data at risk:** Trigger registration state.
**Accuracy:** Important — mistakes here cause downstream issues.

## Related Directories

- `orchestration/dags/`
- `ingestion/`

---
*Triggers — Event Triggers — part of the OCR system. See `_index.md` in this directory for orientation.*
