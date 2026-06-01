---
title: "DAGs — n8n DAG Definitions"
description: "n8n DAG workflow definitions for ingestion, shipment, council, memory, and governance pipelines."
status: "active"
district: "orchestration/dags"
type: "neighborhood"
parent: "orchestration"
neighbors: ["orchestration/n8n", "orchestration/triggers"]
traffic:
  reads: ["ingestion/ (event routing)", "shipments/ (state)"]
  writes: ["All subsystems (via DAG execution)"]
blast_radius:
  services: ["All automated pipeline routing"]
  data: ["DAG execution state"]
  depends_on_accuracy: "critical"
---

# 📊 DAGs — n8n DAG Definitions

Defines the n8n DAGs (workflows) that orchestrate OCR processes. Each DAG is a directed acyclic graph of steps — for example, the Ingestion DAG, Shipment DAG, Council DAG. Described in YAML or JSON.

## What It Reads and Writes

**Reads from:** ingestion/ (event routing), shipments/ (state)
**Writes to:** All subsystems (via DAG execution)

## How Important Is This?

**If this breaks:** All automated pipeline routing will be affected.
**Data at risk:** DAG execution state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `orchestration/n8n/`
- `orchestration/triggers/`

---
*DAGs — n8n DAG Definitions — part of the OCR system. See `_index.md` in this directory for orientation.*
