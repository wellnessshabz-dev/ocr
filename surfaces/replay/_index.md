---
title: "Replay — Replay Surface"
description: "Replay timeline browser for navigating past decisions and memory states."
status: "active"
district: "surfaces/replay"
type: "neighborhood"
parent: "surfaces"
neighbors: ["surfaces/executive", "replay", "gbrain/replay"]
traffic:
  reads: ["replay/ (replay state)"]
  writes: ["HTTP responses (timeline views)"]
blast_radius:
  services: ["Replay UX"]
  data: ["Timeline view state"]
  depends_on_accuracy: "medium"
---

# ⏮️ Replay — Replay Surface

The replay system. Handles replaying past shipments, memory states, and decisions. Essential for debugging, auditing, and testing how changes affect past decisions.

## What It Reads and Writes

**Reads from:** replay/ (replay state)
**Writes to:** HTTP responses (timeline views)

## How Important Is This?

**If this breaks:** Replay UX will be affected.
**Data at risk:** Timeline view state.
**Accuracy:** Moderate — nice to have right, but not catastrophic if wrong.

## Related Directories

- `surfaces/executive/`
- `replay/`
- `gbrain/replay/`

---
*Replay — Replay Surface — part of the OCR system. See `_index.md` in this directory for orientation.*
