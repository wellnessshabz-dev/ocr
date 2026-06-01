---
title: "Map Room — Ontology Engine"
description: "The shared cognitive substrate: concept graph, extraction, contradiction detection, lifecycle management."
status: "active"
district: "ontology"
type: "district"
child_districts: ["contradictions", "extraction", "graph", "lifecycle"]
neighbors: ["gbrain/semantic", "cognition", "ingestion", "shipments"]
traffic:
  reads: ["ingestion/ (candidate nodes)", "gbrain/semantic (existing graph)"]
  writes: ["gbrain/semantic (node promotions)", "cognition/ (concept queries)"]
blast_radius:
  services: ["Ontology queries, concept resolution, relationship mapping"]
  data: ["All ontology nodes and edges"]
  depends_on_accuracy: "critical (ontology is the shared backbone)"
connections:
  - direction: "upstream"
    to: "ingestion/"
    via: "Entity extraction pipeline"
    purpose: "New concepts discovered during ingestion"
  - direction: "downstream"
    to: "cognition/skills"
    via: "Concept resolution API"
    purpose: "Skills resolve entities against the ontology"
  - direction: "peer"
    to: "gbrain/semantic"
    via: "Bidirectional sync"
    purpose: "Ontology = index, GBrain = state engine"
naming:
  pattern: "snake_case"
  rules:
    - "One module per ontology function"
partitioning:
  rule: "By ontology function: contradictions, extraction, graph, lifecycle"
maintainers: ["shadabkhan"]
---

# 🗺️ Map Room — Ontology Engine

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **⚡ `contradictions/`** — Contradictions — Contradiction Detection
- **🔍 `extraction/`** — Extraction — Entity Extraction
- **🕸️ `graph/`** — Graph — Ontology Graph Operations
- **🔄 `lifecycle/`** — Lifecycle — Ontology Node Lifecycle

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ⬅️ **Receives from** ingestion/ (via Entity extraction pipeline) — New concepts discovered during ingestion
- ➡️ **Sends to** cognition/skills (via Concept resolution API) — Skills resolve entities against the ontology
- ➡️ **Sends to** gbrain/semantic (via Bidirectional sync) — Ontology = index, GBrain = state engine

## What It Reads and Writes

**Reads from:** ingestion/ (candidate nodes), gbrain/semantic (existing graph)
**Writes to:** gbrain/semantic (node promotions), cognition/ (concept queries)

## How Important Is This?

**If this breaks:** Ontology queries, concept resolution, relationship mapping will be affected.
**Data at risk:** All ontology nodes and edges.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Quick Reference

- `ontology/contradictions/`
- `ontology/extraction/`
- `ontology/graph/`
- `ontology/lifecycle/`

## Related Directories

- `gbrain/semantic/`
- `cognition/`
- `ingestion/`
- `shipments/`

---
*Map Room — Ontology Engine — part of the OCR system. See `_index.md` in this directory for orientation.*
