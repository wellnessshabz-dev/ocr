---
title: "Memory Palace — GBrain Memory Substrate"
description: "The cognitive state engine with layered memory: working, episodic, semantic, procedural, temporal."
status: "active"
district: "gbrain"
type: "district"
child_districts: ["activation", "episodic", "replay", "semantic", "temporal"]
neighbors: ["cognition", "ontology", "shipments", "surfaces"]
traffic:
  reads: ["cognition/councils (context queries)", "ontology/ (concept resolution)"]
  writes: ["cognition/ (memory activation results)", "surfaces/ (state updates)"]
blast_radius:
  services: ["All memory operations", "Trajectory modeling", "Ontology queries"]
  data: ["Semantic memory graph", "Episodic shipment history", "Temporal trajectories"]
  depends_on_accuracy: "critical (memory corruption = wrong decisions)"
connections:
  - direction: "upstream"
    to: "shipments/storage"
    via: "Memory consolidation pipeline"
    purpose: "Completed shipments are consolidated into episodic memory"
  - direction: "downstream"
    to: "cognition/skills"
    via: "Memory activation protocol"
    purpose: "Skills query memory for relevant context before deliberation"
  - direction: "peer"
    to: "ontology/"
    via: "Semantic memory <-> ontology graph sync"
    purpose: "GBrain stores, ontology indexes"
naming:
  pattern: "snake_case"
  rules:
    - "Memory layer modules match the GBrain layer name"
partitioning:
  rule: "By memory layer type (activation, episodic, replay, semantic, temporal)"
maintainers: ["shadabkhan"]
---

# 💾 Memory Palace — GBrain Memory Substrate

## What's Inside

This area has several parts. Each one is a subdirectory with its own purpose:

- **⚡ `activation/`** — Activation — Memory Activation Protocol
- **📜 `episodic/`** — Episodic — Episodic Memory
- **⏮️ `replay/`** — Replay — Memory Replay
- **🔗 `semantic/`** — Semantic — Semantic Memory
- **⏳ `temporal/`** — Temporal — Temporal Memory

Explore each subdirectory to learn more about that part of the system.

## How Data Flows Through Here

- ⬅️ **Receives from** shipments/storage (via Memory consolidation pipeline) — Completed shipments are consolidated into episodic memory
- ➡️ **Sends to** cognition/skills (via Memory activation protocol) — Skills query memory for relevant context before deliberation
- ➡️ **Sends to** ontology/ (via Semantic memory <-> ontology graph sync) — GBrain stores, ontology indexes

## What It Reads and Writes

**Reads from:** cognition/councils (context queries), ontology/ (concept resolution)
**Writes to:** cognition/ (memory activation results), surfaces/ (state updates)

## How Important Is This?

**If this breaks:** All memory operations, Trajectory modeling, Ontology queries will be affected.
**Data at risk:** Semantic memory graph, Episodic shipment history, Temporal trajectories.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Quick Reference

- `gbrain/activation/`
- `gbrain/episodic/`
- `gbrain/replay/`
- `gbrain/semantic/`
- `gbrain/temporal/`

## Related Directories

- `cognition/`
- `ontology/`
- `shipments/`
- `surfaces/`

---
*Memory Palace — GBrain Memory Substrate — part of the OCR system. See `_index.md` in this directory for orientation.*
