---
title: "Schemas — Shipment Schemas"
description: "Schema definitions for shipment data structures (context, metadata, entities, decisions)."
status: "active"
district: "shipments/schemas"
type: "neighborhood"
parent: "shipments"
neighbors: ["shipments/compiler", "shipments/storage", "shipments/validator"]
traffic:
  reads: ["Reference for all shipment operations"]
  writes: ["None (schemas are read-only definitions)"]
blast_radius:
  services: ["All shipment processing depends on schema correctness"]
  data: ["Schema definitions"]
  depends_on_accuracy: "critical"
---

# 📋 Schemas — Shipment Schemas

Defines the data schemas for shipments — what fields a shipment must have, what types each field is, and how shipments relate to each other. These schemas are the contract that every other part of the system relies on.

## What It Reads and Writes

**Reads from:** Reference for all shipment operations
**Writes to:** None (schemas are read-only definitions)

## How Important Is This?

**If this breaks:** All shipment processing depends on schema correctness will be affected.
**Data at risk:** Schema definitions.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `shipments/compiler/`
- `shipments/storage/`
- `shipments/validator/`

---
*Schemas — Shipment Schemas — part of the OCR system. See `_index.md` in this directory for orientation.*
