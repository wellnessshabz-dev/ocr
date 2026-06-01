---
title: "Replay — Shipment Replay"
description: "Replays past shipments for debugging, testing, and audit review."
status: "active"
district: "shipments/replay"
type: "neighborhood"
parent: "shipments"
neighbors: ["shipments/storage", "replay"]
traffic:
  reads: ["shipments/storage (archived shipments)"]
  writes: ["replay/ (replay data)"]
blast_radius:
  services: ["Shipment debugging"]
  data: ["Replay state"]
  depends_on_accuracy: "medium"
---

# ⏮️ Replay — Shipment Replay

The replay system. Handles replaying past shipments, memory states, and decisions. Essential for debugging, auditing, and testing how changes affect past decisions.

## What It Reads and Writes

**Reads from:** shipments/storage (archived shipments)
**Writes to:** replay/ (replay data)

## How Important Is This?

**If this breaks:** Shipment debugging will be affected.
**Data at risk:** Replay state.
**Accuracy:** Moderate — nice to have right, but not catastrophic if wrong.

## Related Directories

- `shipments/storage/`
- `replay/`

---
*Replay — Shipment Replay — part of the OCR system. See `_index.md` in this directory for orientation.*
