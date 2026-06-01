---
title: "Scrapling — Ingestion Architecture Evaluation"
description: "Live evaluation results after building a ScraplingAdapter and testing against real sites."
status: "active"
district: "ingestion/web"
type: "analysis"
author: "Karim Shoair (D4Vinci)"
source_url: "https://scrapling.readthedocs.io/"
stars: "54K+ on GitHub"
version: "v0.2.99 (installed)"
evaluated: "2026-06-01"
---

# Scrapling — Evaluation Results

## What Was Built

A full `ScraplingAdapter` implementing the `WebAdapter` ABC (`ingestion/web/scrapling.py`). Three fetcher modes:

| Mode | Class | Use Case | Status |
|------|-------|----------|--------|
| `async_http` | `AsyncFetcher` | Static docs, SSR sites | ✅ Works |
| `stealthy` | `StealthyFetcher` | Cloudflare, anti-bot bypass | ❌ Broken (Py3.9) |
| `playwright` | `PlayWrightFetcher` | SPAs, complex auth | ✅ Works |

## Test Results

### async_http (static/SSR sites)

| Target | Status | Content | Time | Notes |
|--------|--------|---------|------|-------|
| FastAPI docs | 200 | 38KB | **0.12s** | SSR, full content |
| Readthedocs | 200 | 18KB | **0.47s** | SSR, full content |
| Python.org | 200 | 15KB | **0.10s** | Static, full content |
| React.dev (Next.js) | 200 | 17KB | **0.22s** | SSR, matches Playwright |
| Vue Mastery (Nuxt) | 200 | 26KB | **0.60s** | SSR, 90% of Playwright content |

**Verdict:** AsyncFetcher replaces Firecrawl for all static/SSR sites. No API key, faster, local.

### playwright (browser-based)

| Target | Status | Content | Time | Notes |
|--------|--------|---------|------|-------|
| React.dev | 200 | 17KB | 2.26s | Same content as async_http, 10x slower |
| Vue Mastery | 200 | 29KB | 3.88s | 2.6KB more than async_http, 6x slower |

**Verdict:** Works but is equivalent to our existing PlaywrightAdapter. Only needed for sites that require true client-side rendering.

### stealthy (anti-bot bypass)

| Target | Result |
|--------|--------|
| Python.org | ❌ Camoufox crash — "Connection closed while reading from the driver" |
| nowsecure.nl | ❌ Same crash |
| httpstat.us | ❌ "NS_ERROR_NET_RESET" — timeout after 17s |

**Verdict:** Broken on Python 3.9 (Scrapling requires 3.10+). StealthyFetcher relies on Camoufox which has compatibility issues with our Python/Playwright versions. Needs Python upgrade to use.

## Key Findings

1. **async_http is production-ready** — replaces Firecrawl for the common case. No API key. Faster (0.1-0.6s vs ~2s for Firecrawl).
2. **PlayWrightFetcher adds nothing** — our existing PlaywrightAdapter does the same thing.
3. **StealthyFetcher is blocked** — requires Python 3.10+. Worth revisiting after upgrade.
4. **Scrapling's Spider/MCP features unused** — the spider framework and MCP server are extra value we haven't tapped. Spider could be useful for large doc crawls.

## Updated Recommendation

1. **Now:** Add `ScraplingAdapter(mode="async_http")` to the ScraperRouter as the default "fast path" — replacing Firecrawl as the primary backend. Keep Playwright as fallback.
2. **When we upgrade to Python 3.10+:** Evaluate StealthyFetcher for Cloudflare bypass. If it works, it can replace 50%+ of Playwright usage.
3. **Later:** Evaluate Scrapling Spider for large-scale doc crawls (pause/resume, streaming). Evaluate MCP server for AI-assisted extraction (reduces token usage).

## Code

```python
# ingestion/web/scrapling.py — implemented and tested
class ScraplingAdapter(WebAdapter):
    SUPPORTED_MODES = ("async_http", "stealthy", "playwright")

    async def scrape(self, url, format="markdown") -> WebContent:
        resp = await self._fetch(url)
        markdown = self._to_markdown(resp)
        title = self._extract_title(resp)
        ...
```

## Dependencies

- `scrapling==0.2.99` (PyPI)
- `scrapling[fetchers]` for browser modes (~200MB for Camoufox)
- Python 3.10+ required for stealthy mode (we're on 3.9)
