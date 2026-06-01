---
title: "Web — Web Scraping Engine"
description: "Intelligent ScraperRouter that picks between Scrapling async_http (local), Playwright (local browser), and Firecrawl (cloud) based on URL patterns and content quality."
status: "active"
district: "ingestion/web"
type: "neighborhood"
parent: "ingestion"
neighbors: ["ingestion/github", "raw/bronze-docs"]
traffic:
  reads: ["Web pages, APIs"]
  writes: ["shipments/compiler", "raw/bronze-docs (scraped content)"]
blast_radius:
  services: ["Web content ingestion"]
  data: ["Scraped content state"]
  depends_on_accuracy: "high (garbage HTML = bad ontology extraction)"
connections:
  - direction: "upstream"
    to: "External web"
    via: "Firecrawl API + Playwright browser"
    purpose: "Fetches web content for OCR processing"
  - direction: "upstream"
    to: "Scrapling"
    via: "Python SDK integration"
    purpose: "Primary fast path — async_http mode replaces Firecrawl for static/SSR pages"
---

# 🌐 Web — Web Scraping Engine

This directory contains 6 files.

**Documentation:**
- `_scrapling.md`

**Code:**
- `__init__.py`
- `adapter.py`
- `firecrawl.py`
- `playwright.py`
- `scraper.py`

## How Data Flows Through Here

- ⬅️ **Receives from** External web (via Firecrawl API + Playwright browser) — Fetches web content for OCR processing
- ⬅️ **Receives from** Scrapling (future) (via Python SDK integration) — Potential upgrade for anti-bot bypass + unified fetchers

## What It Reads and Writes

**Reads from:** Web pages, APIs
**Writes to:** shipments/compiler, raw/bronze-docs (scraped content)

## How Important Is This?

**If this breaks:** Web content ingestion will be affected.
**Data at risk:** Scraped content state.
**Accuracy:** Important — mistakes here cause downstream issues.

## Quick Reference

- `ingestion/web/__init__.py`
- `ingestion/web/_scrapling.md`
- `ingestion/web/adapter.py`
- `ingestion/web/firecrawl.py`
- `ingestion/web/playwright.py`
- `ingestion/web/scraper.py`

## Related Directories

- `ingestion/github/`
- `raw/bronze-docs/`

## Files

- `__init__.py` — Package init
- `adapter.py` — `WebAdapter` ABC with `WebContent`, `WebSession`, `WebSearchResult` types
- `scraper.py` — `ScraperRouter`: picks Scrapling (fast), Playwright (heavy), or Firecrawl (cloud)
- `scrapling.py` — `ScraplingAdapter`: wraps Scrapling's `AsyncFetcher`, `StealthyFetcher`, `PlayWrightFetcher`
- `firecrawl.py` — `FirecrawlAdapter`: cloud scraping via Firecrawl SDK
- `playwright.py` — `PlaywrightAdapter`: browser automation via Playwright with HTML-to-markdown
- `_scrapling.md` — Scrapling evaluation results

---

*Web — Web Scraping Engine — part of the OCR system. See `_index.md` in this directory for orientation.*
