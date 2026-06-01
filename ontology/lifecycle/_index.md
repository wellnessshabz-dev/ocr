---
title: "Lifecycle — Ontology Node Lifecycle"
description: "Manages the lifecycle of ontology nodes: candidate → confirmed → dormant → archived."
status: "active"
district: "ontology/lifecycle"
type: "neighborhood"
parent: "ontology"
neighbors: ["ontology/extraction", "ontology/graph", "ontology/contradictions"]
traffic:
  reads: ["ontology/graph (node state)"]
  writes: ["ontology/graph (state transitions)"]
blast_radius:
  services: ["Ontology node lifecycle"]
  data: ["Node lifecycle state"]
  depends_on_accuracy: "critical"
---

# 🔄 Lifecycle — Ontology Node Lifecycle

Manages the lifecycle of ontology nodes: candidate → promoted → confirmed → dormant → archived. Each concept goes through stages, and this component handles the transitions, timing, and cleanup.

## What It Reads and Writes

**Reads from:** ontology/graph (node state)
**Writes to:** ontology/graph (state transitions)

## How Important Is This?

**If this breaks:** Ontology node lifecycle will be affected.
**Data at risk:** Node lifecycle state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `ontology/extraction/`
- `ontology/graph/`
- `ontology/contradictions/`

---
*Lifecycle — Ontology Node Lifecycle — part of the OCR system. See `_index.md` in this directory for orientation.*
