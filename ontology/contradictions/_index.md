---
title: "Contradictions — Contradiction Detection"
description: "Detects and resolves contradictions between ontology nodes and decisions."
status: "active"
district: "ontology/contradictions"
type: "neighborhood"
parent: "ontology"
neighbors: ["ontology/extraction", "ontology/graph", "ontology/lifecycle"]
traffic:
  reads: ["ontology/graph (nodes and edges)"]
  writes: ["ontology/graph (contradiction edges)", "cognition/ (alerts)"]
blast_radius:
  services: ["Ontology consistency"]
  data: ["Contradiction state"]
  depends_on_accuracy: "critical (missed contradictions = inconsistent ontology)"
---

# ⚡ Contradictions — Contradiction Detection

Detects contradictions in the ontology — two nodes that say opposite things, a decision that contradicts a past decision, or a relationship that conflicts with established knowledge. Surfaces these for human or council resolution.

## What It Reads and Writes

**Reads from:** ontology/graph (nodes and edges)
**Writes to:** ontology/graph (contradiction edges), cognition/ (alerts)

## How Important Is This?

**If this breaks:** Ontology consistency will be affected.
**Data at risk:** Contradiction state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `ontology/extraction/`
- `ontology/graph/`
- `ontology/lifecycle/`

---
*Contradictions — Contradiction Detection — part of the OCR system. See `_index.md` in this directory for orientation.*
