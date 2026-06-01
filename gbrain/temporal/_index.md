---
title: "Temporal — Temporal Memory"
description: "Time-aware memory: trajectories, timelines, recency weighting, and decay functions."
status: "active"
district: "gbrain/temporal"
type: "neighborhood"
parent: "gbrain"
neighbors: ["gbrain/activation", "gbrain/episodic", "cognition"]
traffic:
  reads: ["gbrain/episodic (events with timestamps)"]
  writes: ["gbrain/activation (trajectory data)"]
blast_radius:
  services: ["Time-aware queries, trajectory modeling"]
  data: ["Temporal state, trajectories"]
  depends_on_accuracy: "high"
---

# ⏳ Temporal — Temporal Memory

Handles time-aware memory: what the system knew at different points in time, how concepts evolved, and which decisions were active when. Enables "time travel" queries like "what did we know about X in January?"

## What It Reads and Writes

**Reads from:** gbrain/episodic (events with timestamps)
**Writes to:** gbrain/activation (trajectory data)

## How Important Is This?

**If this breaks:** Time-aware queries, trajectory modeling will be affected.
**Data at risk:** Temporal state, trajectories.
**Accuracy:** Important — mistakes here cause downstream issues.

## Related Directories

- `gbrain/activation/`
- `gbrain/episodic/`
- `cognition/`

---
*Temporal — Temporal Memory — part of the OCR system. See `_index.md` in this directory for orientation.*
