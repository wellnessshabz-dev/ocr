---
title: "Storage — Shipment Storage"
description: "Persistence and retrieval for shipments at every stage of the pipeline."
status: "active"
district: "shipments/storage"
type: "neighborhood"
parent: "shipments"
neighbors: ["shipments/compiler", "shipments/replay", "gbrain/episodic"]
traffic:
  reads: ["shipments/compiler (new shipments)"]
  writes: ["Database (shipment records)", "gbrain/episodic (memory consolidation)"]
blast_radius:
  services: ["Shipment persistence"]
  data: ["All shipment records"]
  depends_on_accuracy: "critical (lost shipments = lost decisions)"
---

# 🗄️ Storage — Shipment Storage

Holds compiled shipments in persistent storage. Think of it as the cargo hold — every shipment that gets created needs to be stored here before it can be processed. Will contain database access code and a shipment repository.

## What It Reads and Writes

**Reads from:** shipments/compiler (new shipments)
**Writes to:** Database (shipment records), gbrain/episodic (memory consolidation)

## How Important Is This?

**If this breaks:** Shipment persistence will be affected.
**Data at risk:** All shipment records.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `shipments/compiler/`
- `shipments/replay/`
- `gbrain/episodic/`

---
*Storage — Shipment Storage — part of the OCR system. See `_index.md` in this directory for orientation.*
