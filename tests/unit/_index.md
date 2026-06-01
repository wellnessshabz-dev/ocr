---
title: "Unit Tests — Module-Level Tests"
description: "Unit tests that validate individual source modules in isolation."
status: "active"
district: "tests/unit"
type: "neighborhood"
parent: "tests"
neighbors: ["tests/integration"]
traffic:
  reads: ["All source modules (via imports)"]
  writes: ["Test coverage data"]
blast_radius:
  services: ["CI quality gates"]
  data: ["Test state only"]
  depends_on_accuracy: "high"
---

# 🔬 Unit Tests — Module-Level Tests

This directory contains 3 files.

**Code:**
- `test_firecrawl_adapter.py`
- `test_playwright_adapter.py`
- `test_scraper_router_routing.py`

## What It Reads and Writes

**Reads from:** All source modules (via imports)
**Writes to:** Test coverage data

## How Important Is This?

**If this breaks:** CI quality gates will be affected.
**Data at risk:** Test state only.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `tests/unit/test_firecrawl_adapter.py`
- `tests/unit/test_playwright_adapter.py`
- `tests/unit/test_scraper_router_routing.py`

## Related Directories

- `tests/integration/`

---
*Unit Tests — Module-Level Tests — part of the OCR system. See `_index.md` in this directory for orientation.*
