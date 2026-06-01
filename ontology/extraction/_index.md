---
title: "Extraction — Entity Extraction"
description: "Extracts ontology entities from raw signals: candidate node generation and concept resolution."
status: "active"
district: "ontology/extraction"
type: "neighborhood"
parent: "ontology"
neighbors: ["ingestion", "ontology/contradictions", "ontology/graph"]
traffic:
  reads: ["ingestion/ (raw signals)", "ontology/graph (existing nodes)"]
  writes: ["ontology/graph (candidate nodes)"]
blast_radius:
  services: ["Entity extraction quality"]
  data: ["Candidate node state"]
  depends_on_accuracy: "critical (missed entities = incomplete ontology)"
---

# 🔍 Extraction — Entity Extraction

Extracts ontology entities from raw signals. When a signal arrives (like a commit or web page), this component scans it for named entities, concepts, and relationships, then creates candidate nodes for the knowledge graph.

## What It Reads and Writes

**Reads from:** ingestion/ (raw signals), ontology/graph (existing nodes)
**Writes to:** ontology/graph (candidate nodes)

## How Important Is This?

**If this breaks:** Entity extraction quality will be affected.
**Data at risk:** Candidate node state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `ingestion/`
- `ontology/contradictions/`
- `ontology/graph/`

---
*Extraction — Entity Extraction — part of the OCR system. See `_index.md` in this directory for orientation.*
