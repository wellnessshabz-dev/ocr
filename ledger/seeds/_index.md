---
title: "Seeds — Seed Data"
description: "Seed data for development and testing the audit ledger."
status: "active"
district: "ledger/seeds"
type: "neighborhood"
parent: "ledger"
neighbors: ["ledger/schemas"]
traffic:
  reads: ["ledger/schemas (target tables)"]
  writes: ["Development/test databases"]
blast_radius:
  services: ["Development/testing"]
  data: ["Seed data only"]
  depends_on_accuracy: "low (dev-only)"
---

# 🌱 Seeds — Seed Data

Seed data for the ledger — initial records, test data, and reference entries that populate a fresh ledger database. Used during development and deployment to give the system starting data.

## What It Reads and Writes

**Reads from:** ledger/schemas (target tables)
**Writes to:** Development/test databases

## How Important Is This?

**If this breaks:** Development/testing will be affected.
**Data at risk:** Seed data only.
**Accuracy:** Low — not very sensitive.

## Related Directories

- `ledger/schemas/`

---
*Seeds — Seed Data — part of the OCR system. See `_index.md` in this directory for orientation.*
