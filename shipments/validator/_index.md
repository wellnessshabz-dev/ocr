---
title: "Validator — Shipment Validator"
description: "Validates shipments for scope compliance, completeness, signatures, and schema conformance."
status: "active"
district: "shipments/validator"
type: "neighborhood"
parent: "shipments"
neighbors: ["shipments/compiler", "shipments/schemas", "cognition/governance"]
traffic:
  reads: ["shipments/compiler (compiled shipments)", "shipments/schemas (validation rules)"]
  writes: ["shipments/compiler (validation feedback)"]
blast_radius:
  services: ["Shipment quality"]
  data: ["Validation state"]
  depends_on_accuracy: "critical"
---

# ✅ Validator — Shipment Validator

Makes sure shipments are well-formed before they move on to the cognition layer. Validation checks include: required fields present, entity references resolve to the ontology, and the shipment type is known. Rejects malformed shipments with clear error messages.

## What It Reads and Writes

**Reads from:** shipments/compiler (compiled shipments), shipments/schemas (validation rules)
**Writes to:** shipments/compiler (validation feedback)

## How Important Is This?

**If this breaks:** Shipment quality will be affected.
**Data at risk:** Validation state.
**Accuracy:** Critical — getting this wrong could break the whole system.

## Related Directories

- `shipments/compiler/`
- `shipments/schemas/`
- `cognition/governance/`

---
*Validator — Shipment Validator — part of the OCR system. See `_index.md` in this directory for orientation.*
