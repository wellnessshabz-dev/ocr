---
title: "Integration Tests — End-to-End Tests"
description: "Integration tests that validate cross-subsystem flows and end-to-end pipelines."
status: "active"
district: "tests/integration"
type: "neighborhood"
parent: "tests"
neighbors: ["tests/unit"]
traffic:
  reads: ["All subsystems (via imports)"]
  writes: ["Test state, fixtures"]
blast_radius:
  services: ["CI quality gates, release confidence"]
  data: ["Test state, fixture data"]
  depends_on_accuracy: "high"
---

# 🔗 Integration Tests — End-to-End Tests

This directory contains 2 files.

**Code:**
- `test_ingestion_api.py`
- `test_scraper_integration.py`

## What It Reads and Writes

**Reads from:** All subsystems (via imports)
**Writes to:** Test state, fixtures

## How Important Is This?

**If this breaks:** CI quality gates, release confidence will be affected.
**Data at risk:** Test state, fixture data.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `tests/integration/test_ingestion_api.py`
- `tests/integration/test_scraper_integration.py`

## Related Directories

- `tests/unit/`

---
*Integration Tests — End-to-End Tests — part of the OCR system. See `_index.md` in this directory for orientation.*
