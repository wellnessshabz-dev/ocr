---
title: "Ontology — Ontology Surface"
description: "Ontology browser and graph visualization surface."
status: "active"
district: "surfaces/ontology"
type: "neighborhood"
parent: "surfaces"
neighbors: ["surfaces/executive", "ontology", "gbrain/semantic"]
traffic:
  reads: ["ontology/ (graph data)", "gbrain/semantic (node state)"]
  writes: ["HTTP responses (graph views)"]
blast_radius:
  services: ["Ontology visualization"]
  data: ["View state"]
  depends_on_accuracy: "medium"
---

# 🗺️ Ontology — Ontology Surface

An interactive graph browser for exploring the ontology. Shows concepts as nodes and their relationships as edges. Lets humans navigate the knowledge graph visually.

## What It Reads and Writes

**Reads from:** ontology/ (graph data), gbrain/semantic (node state)
**Writes to:** HTTP responses (graph views)

## How Important Is This?

**If this breaks:** Ontology visualization will be affected.
**Data at risk:** View state.
**Accuracy:** Moderate — nice to have right, but not catastrophic if wrong.

## Related Directories

- `surfaces/executive/`
- `ontology/`
- `gbrain/semantic/`

---
*Ontology — Ontology Surface — part of the OCR system. See `_index.md` in this directory for orientation.*
