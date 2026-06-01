---
title: "Compiler — Shipment Compiler"
description: "Builds shipment context, extracts ontology entities, bounds context, and validates shipments."
status: "active"
district: "shipments/compiler"
type: "neighborhood"
parent: "shipments"
neighbors: ["shipments/validator", "shipments/storage", "ingestion", "ontology"]
traffic:
  reads: ["ingestion/ (raw events)", "ontology/ (concept resolution)"]
  writes: ["shipments/validator (compiled shipments)", "cognition/councils (ready shipments)"]
blast_radius:
  services: ["Shipment compilation"]
  data: ["Compilation state"]
  depends_on_accuracy: "critical"
---

# ⚙️ Compiler — Shipment Compiler

This is where raw signals (like a GitHub commit or a web scrape) get compiled into structured work packages called "shipments." Each shipment is a self-contained unit of work with context, entities, and a clear purpose. When this directory gets code, it will take incoming events and wrap them in the proper shipment format.

## What It Reads and Writes

**Reads from:** ingestion/ (raw events), ontology/ (concept resolution)
**Writes to:** shipments/validator (compiled shipments), cognition/councils (ready shipments)

## How Important Is This?

**If this breaks:** Shipment compilation will be affected.
**Data at risk:** Compilation state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `shipments/validator/`
- `shipments/storage/`
- `ingestion/`
- `ontology/`

---
*Compiler — Shipment Compiler — part of the OCR system. See `_index.md` in this directory for orientation.*
