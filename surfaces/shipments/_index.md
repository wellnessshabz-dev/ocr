---
title: "Shipments — Shipment Surface"
description: "Shipment tracker and status viewer for monitoring pipeline activity."
status: "active"
district: "surfaces/shipments"
type: "neighborhood"
parent: "surfaces"
neighbors: ["surfaces/executive", "shipments"]
traffic:
  reads: ["shipments/ (pipeline state)"]
  writes: ["HTTP responses (status views)"]
blast_radius:
  services: ["Shipment tracking UX"]
  data: ["Tracker view state"]
  depends_on_accuracy: "medium"
---

# 📦 Shipments — Shipment Surface

A web interface showing all shipments in the system — active, completed, failed. Lets users inspect shipment contents, see their processing history, and retry failed ones.

## What It Reads and Writes

**Reads from:** shipments/ (pipeline state)
**Writes to:** HTTP responses (status views)

## How Important Is This?

**If this breaks:** Shipment tracking UX will be affected.
**Data at risk:** Tracker view state.
**Accuracy:** Moderate — nice to have right, but not catastrophic if wrong.

## Related Directories

- `surfaces/executive/`
- `shipments/`

---
*Shipments — Shipment Surface — part of the OCR system. See `_index.md` in this directory for orientation.*
