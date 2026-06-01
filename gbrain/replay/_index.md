---
title: "Replay — Memory Replay"
description: "Replay manager for memory: snapshots, checkpoint-based restore, step-through debugging."
status: "active"
district: "gbrain/replay"
type: "neighborhood"
parent: "gbrain"
neighbors: ["gbrain/episodic", "replay", "surfaces/replay"]
traffic:
  reads: ["gbrain/episodic (memory state)"]
  writes: ["replay/ (replay data)"]
blast_radius:
  services: ["Replay and debugging"]
  data: ["Memory snapshots"]
  depends_on_accuracy: "high"
---

# ⏮️ Replay — Memory Replay

The replay system. Handles replaying past shipments, memory states, and decisions. Essential for debugging, auditing, and testing how changes affect past decisions.

## What It Reads and Writes

**Reads from:** gbrain/episodic (memory state)
**Writes to:** replay/ (replay data)

## How Important Is This?

**If this breaks:** Replay and debugging will be affected.
**Data at risk:** Memory snapshots.
**Accuracy:** Important — mistakes here cause downstream issues.

## Related Directories

- `gbrain/episodic/`
- `replay/`
- `surfaces/replay/`

---
*Replay — Memory Replay — part of the OCR system. See `_index.md` in this directory for orientation.*
