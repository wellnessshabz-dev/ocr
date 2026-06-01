---
title: "Semantic — Semantic Memory"
description: "The live ontology graph — the 'what things mean' layer of GBrain."
status: "active"
district: "gbrain/semantic"
type: "neighborhood"
parent: "gbrain"
neighbors: ["gbrain/episodic", "ontology", "cognition"]
traffic:
  reads: ["ontology/ (graph updates)", "gbrain/activation (queries)"]
  writes: ["cognition/ (context data)"]
blast_radius:
  services: ["Semantic queries, concept resolution"]
  data: ["Semantic memory graph"]
  depends_on_accuracy: "critical"
---

# 🔗 Semantic — Semantic Memory

The "what things mean" layer. Stores the live ontology graph — all the concepts the system knows about and how they relate to each other (product depends_on component, person owns decision, etc.). This is not a vector database. It is a structured knowledge graph.

## What It Reads and Writes

**Reads from:** ontology/ (graph updates), gbrain/activation (queries)
**Writes to:** cognition/ (context data)

## How Important Is This?

**If this breaks:** Semantic queries, concept resolution will be affected.
**Data at risk:** Semantic memory graph.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `gbrain/episodic/`
- `ontology/`
- `cognition/`

---
*Semantic — Semantic Memory — part of the OCR system. See `_index.md` in this directory for orientation.*
