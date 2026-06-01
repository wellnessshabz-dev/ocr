---
title: "Graph — Ontology Graph Operations"
description: "Neo4j graph CRUD, traversal, indexing, and query operations for the ontology."
status: "active"
district: "ontology/graph"
type: "neighborhood"
parent: "ontology"
neighbors: ["ontology/extraction", "ontology/contradictions", "ontology/lifecycle", "gbrain/semantic"]
traffic:
  reads: ["Neo4j database (graph state)"]
  writes: ["Neo4j database (node/edge mutations)"]
blast_radius:
  services: ["All ontology graph queries"]
  data: ["Graph database state"]
  depends_on_accuracy: "critical (graph corruption = ontology failure)"
---

# 🕸️ Graph — Ontology Graph Operations

Manages the ontology graph structure. Creates, reads, updates, and deletes nodes and edges. Handles graph traversal queries (like "find all decisions that depend on this component"). Underlying data store for semantic memory.

### Design Principle: DAG for Parallel Execution

The graph must model blocking relationships (`blocks`, `enables`, `contradicts`,
`supersedes`) as a DAG. This enables parallel execution: shipments with no
blocking dependencies can proceed simultaneously. The trajectory modeler depends
on this structure to determine concurrency.

## What It Reads and Writes

**Reads from:** Neo4j database (graph state)
**Writes to:** Neo4j database (node/edge mutations)

## How Important Is This?

**If this breaks:** All ontology graph queries will be affected.
**Data at risk:** Graph database state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `ontology/extraction/`
- `ontology/contradictions/`
- `ontology/lifecycle/`
- `gbrain/semantic/`

---
*Graph — Ontology Graph Operations — part of the OCR system. See `_index.md` in this directory for orientation.*
