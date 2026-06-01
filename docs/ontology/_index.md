---
title: "Ontology — Ontology Documentation"
description: "Ontology schema definitions, evolution rules, and concept lifecycle documentation."
status: "active"
district: "docs/ontology"
type: "neighborhood"
parent: "docs"
neighbors: ["ontology", "docs/architecture"]
traffic:
  reads: ["ontology/ (implementation reference)"]
  writes: ["Humans"]
blast_radius:
  services: ["Ontology implementation"]
  data: ["Ontology design knowledge"]
  depends_on_accuracy: "high"
---

# 🗺️ Ontology — Ontology Documentation

An interactive graph browser for exploring the ontology. Shows concepts as nodes and their relationships as edges. Lets humans navigate the knowledge graph visually.

## What It Reads and Writes

**Reads from:** ontology/ (implementation reference)
**Writes to:** Humans

## How Important Is This?

**If this breaks:** Ontology implementation will be affected.
**Data at risk:** Ontology design knowledge.
**Accuracy:** Important — mistakes here cause downstream issues.

## Related Directories

- `ontology/`
- `docs/architecture/`

---
*Ontology — Ontology Documentation — part of the OCR system. See `_index.md` in this directory for orientation.*
