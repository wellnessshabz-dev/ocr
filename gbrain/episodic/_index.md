---
title: "Episodic — Episodic Memory"
description: "Memory of past shipments, deliberations, and decisions — the 'what happened' layer."
status: "active"
district: "gbrain/episodic"
type: "neighborhood"
parent: "gbrain"
neighbors: ["gbrain/activation", "gbrain/semantic", "gbrain/replay"]
traffic:
  reads: ["gbrain/activation (new memories)", "shipments/storage (completed)"]
  writes: ["gbrain/replay (consolidation checkpoints)"]
blast_radius:
  services: ["Past decision recall"]
  data: ["Episodic memory state"]
  depends_on_accuracy: "critical"
---

# 📜 Episodic — Episodic Memory

Stores the history of past shipments and decisions — the "what happened" memory. Unlike semantic memory (which stores "what things mean"), this layer keeps a chronological record of events the system has processed. Supports replay and audit queries.

## What It Reads and Writes

**Reads from:** gbrain/activation (new memories), shipments/storage (completed)
**Writes to:** gbrain/replay (consolidation checkpoints)

## How Important Is This?

**If this breaks:** Past decision recall will be affected.
**Data at risk:** Episodic memory state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `gbrain/activation/`
- `gbrain/semantic/`
- `gbrain/replay/`

---
*Episodic — Episodic Memory — part of the OCR system. See `_index.md` in this directory for orientation.*
