# Scraper Router — Intelligent Tool Selection

## The Problem

OCR has three web scraping backends:

- **Scrapling async_http** — local HTTP client with TLS fingerprint spoofing, fast (~0.1-0.6s), no API key needed
- **Playwright** — local browser, slower (~1-5s), handles JavaScript rendering and interactions
- **Firecrawl** — cloud API, requires subscription, best for search/crawl/extract operations

Picking the wrong tool wastes time. Playwright on a static docs page takes 10x longer than needed. Scrapling on a SPA returns empty content. Firecrawl without an API key is useless.

The Scraper Router solves this: give it a URL, it picks the right tool automatically, checks the result, and falls back if needed.

---

## The Three Backends

| Backend | Type | Latency | Cost | Best For |
|---------|------|---------|------|----------|
| **Scrapling** (`async_http`) | Local HTTP + TLS fingerprint | ~0.1-0.6s | Free | Static docs, SSR sites, blogs, articles |
| **Playwright** | Local headless browser | ~1-5s | Free | SPAs, forums, social media, login walls |
| **Firecrawl** | Cloud API | ~1-3s | Subscription | Site crawling, search, structured extraction |

### Scrapling (Primary Fast Path)

Uses `AsyncFetcher` from the Scrapling library — plain HTTP with browser-grade TLS fingerprint impersonation and stealthy headers. No JavaScript execution, no browser overhead. Gets content from:

- Documentation sites (Readthedocs, FastAPI, Docusaurus)
- Server-side rendered apps (Next.js, Nuxt)
- Static blogs (Medium, Dev.to, Hashnode)
- Wikis, API references, tutorials

### Playwright (Slow Path / Fallback)

Full Chromium browser via Playwright. Renders JavaScript, handles interactions, bypasses simple anti-bot measures. Used for:

- Single-page applications (React, Vue, Angular client-rendered)
- Q&A forums with pagination (Stack Overflow)
- Social media (Twitter/X, Reddit, LinkedIn)
- Sites behind login walls

### Firecrawl (Cloud Path)

Cloud scraping API. Used for operations Scrapling and Playwright don't support:

- Multi-page site crawling (`crawl()`)
- Site mapping (`map_site()`)
- Web search (`search()`)
- Structured data extraction (`extract()`)

If no Firecrawl API key is configured, crawls fall back gracefully (empty results instead of errors).

---

## How It Decides

### Step 1: URL Pattern Matching (instant, free)

Certain URLs are obvious about which tool they need:

| URL Pattern | Tool | Why |
|-------------|------|-----|
| `docs.example.com/*` | Scrapling | Documentation sites are well-structured HTML |
| `readthedocs.io/*` | Scrapling | Static HTML, clean markup |
| `developer.*/*` | Scrapling | Developer docs, SSR or static |
| `learn.*/*` | Scrapling | Learning platforms, mostly static |
| `wikipedia.org/*` | Scrapling | Clean article content |
| `wiki.*/*` | Scrapling | Wiki pages, static HTML |
| `github.com/*/blob/*` | Scrapling | Raw file content (SSR) |
| `github.com/*/wiki/*` | Scrapling | Wiki pages (SSR) |
| `github.com/*/docs/*` | Scrapling | GitHub-hosted docs (SSR) |
| `medium.com/*` | Scrapling | Blog platform (SSR) |
| `dev.to/*` | Scrapling | Blog platform (SSR) |
| `hashnode.com/*` | Scrapling | Blog platform (SSR) |
| `substack.com/*` | Scrapling | Newsletter platform (SSR) |
| `stackoverflow.com/*` | Playwright | JS-heavy, pagination, dynamic content |
| `stackexchange.com/*` | Playwright | JS-heavy, dynamic content |
| `pypi.org/*` | Playwright | Dynamic content loading |
| `npmjs.com/*` | Playwright | SPA, needs JavaScript |
| `twitter.com/*` | Playwright | Login walls, JS-heavy |
| `x.com/*` | Playwright | Login walls, JS-heavy |
| `reddit.com/*` | Playwright | Infinite scroll, JS-heavy |
| `youtube.com/*` | Playwright | Video content, JS-heavy |
| `linkedin.com/*` | Playwright | Login walls, JS-heavy |
| `*/docs/*` | Scrapling | Standard docs path pattern |
| `*/api` | Scrapling | API reference pages |
| `*/reference` | Scrapling | Reference documentation |
| `*/tutorial` | Scrapling | Tutorial pages |
| `*/guide` | Scrapling | Guide pages |
| `*/blog/*` | Scrapling | Blog posts |
| `*/wiki/*` | Scrapling | Wiki pages |
| `*/learn/*` | Scrapling | Learning content |

Patterns are checked top-to-bottom. First match wins. Specific domains before generic path patterns.

### Step 2: Default to Scrapling (fast path)

If no pattern matches, the router defaults to Scrapling `async_http` mode. Most URLs on the web are documentation, articles, or SSR sites — Scrapling handles them in 0.1-0.6s with no API key.

### Step 3: Quality Check

After Scrapling (or Firecrawl) returns, the router checks if the content is actually useful:

| Check | What it detects | Threshold |
|-------|----------------|-----------|
| Empty content | Blank page, blocked request | markdown length < 100 chars |
| Boilerplate-only | Nav bar + footer, no article | meaningful text ratio < 20% |
| JS required | "Enable JavaScript" message | regex match for common patterns |
| Login wall | "Sign in to continue" | regex match for auth patterns |
| Blocked | CAPTCHA, rate limited | regex match for blocked patterns |

If any check fails, the router escalates to Step 4.

### Step 4: Fallback to Playwright (slow path)

Playwright launches a real browser and loads the page properly. It handles:
- JavaScript rendering that Scrapling couldn't execute
- Pages behind simple login forms
- Content that loads after scrolling
- Anti-bot detection that blocked the HTTP path

Playwright is slower (1-5s per page vs Scrapling's 0.1-0.6s) but more capable.

---

## Routing Flow

```
User/OCR: "Scrape this URL"
         │
         ▼
   ┌─────────────────────┐
   │ URL Pattern Matching│ ──→ Match found → route to Scrapling or Playwright
   └─────────┬───────────┘
             │ No match
             ▼
   ┌─────────────────────┐
   │ Try Scrapling       │ ──→ Default fast path
   │ (async_http)        │
   └─────────┬───────────┘
             │
             ▼
   ┌─────────────────────┐
   │ Quality Check        │ ──→ Content good → return result
   └─────────┬───────────┘
             │ Bad content
             ▼
   ┌─────────────────────┐
   │ Fallback to          │
   │ Playwright (browser) │ ──→ Get content → return result
   └─────────────────────┘
```

When explicitly requested via `prefer="firecrawl"`:

```
   ┌─────────────────────┐
   │ Try Firecrawl        │ ──→ If API key configured, try cloud path
   └─────────┬───────────┘
             │
             ▼
   ┌─────────────────────┐
   │ Quality Check        │ ──→ Content good → return result
   └─────────┬───────────┘
             │ Bad content
             ▼
   ┌─────────────────────┐
   │ Fallback to          │
   │ Playwright           │ ──→ Get content → return result
   └─────────────────────┘
```

---

## Crawl, Search, and Extract Routing

These operations always go through Firecrawl because Scrapling and Playwright adapters don't implement them:

| Operation | Backend | Why |
|-----------|---------|-----|
| `crawl()` | Firecrawl | Multi-page crawling requires orchestration |
| `map_site()` | Firecrawl | Site discovery requires breadth-first crawl |
| `search()` | Firecrawl | Web search is a cloud-native operation |
| `extract()` | Firecrawl | Structured extraction uses LLM integration |
| `interact()` | Playwright | Browser actions (click, fill, scroll) need a real browser |

---

## Configuration

The router accepts a config dict on construction:

| Setting | Default | Description |
|---------|---------|-------------|
| `prefer` | `auto` | Force `scrapling`, `playwright`, or `firecrawl`, bypass routing |
| `fallback` | `true` | Enable Playwright fallback when fast path returns bad content |
| `quality.min_chars` | `100` | Minimum markdown length to pass quality check |
| `quality.min_ratio` | `0.2` | Minimum meaningful text ratio after boilerplate stripping |
| `timeout.scrapling` | `15` | Scrapling HTTP timeout in seconds |
| `timeout.playwright` | `30` | Playwright browser timeout in seconds |
| `max_crawl_pages` | `100` | Maximum pages for a crawl operation |

```python
router = ScraperRouter(config={
    "fallback": True,
    "quality": {"min_chars": 200, "min_ratio": 0.3},
    "timeout": {"scrapling": 30, "playwright": 60},
})
```

---

## Example Decisions

| URL | Decision | Why |
|-----|----------|-----|
| `https://fastapi.tiangolo.com/tutorial/` | Scrapling | `tutorial` path match, docs site |
| `https://docs.npmjs.com/cli/` | Scrapling | `docs` subdomain match |
| `https://stackoverflow.com/questions/123` | Playwright | Pattern match for stackoverflow |
| `https://www.npmjs.com/package/express` | Playwright | Pattern match for npmjs (SPA) |
| `https://blog.opensource.org/post` | Scrapling → Playwright fallback | No pattern → Scrapling → if SPA, fallback |
| `https://github.com/user/repo/blob/main/file.py` | Scrapling | Pattern match for GitHub blob (SSR) |
| `https://some-random-startup.com/docs` | Scrapling | `*/docs*` path pattern match |
| `https://app.saas.com/dashboard` | Scrapling → Playwright fallback | Scrapling hits login wall → Playwright handles auth |

---

## Usage

```python
from ingestion.web.scraper import ScraperRouter

router = ScraperRouter()

# Auto-route (recommended)
content = await router.scrape("https://fastapi.tiangolo.com/")

# Force a specific backend
content = await router.scrape("https://example.com", prefer="playwright")
content = await router.scrape("https://example.com", prefer="firecrawl")

# Crawl (always uses Firecrawl)
pages = await router.crawl("https://docs.example.com/", max_pages=50)

# Search (always uses Firecrawl)
results = await router.search("FastAPI tutorial")

# Browser interaction (always uses Playwright)
content = await router.interact("https://example.com/login", [
    {"type": "fill", "selector": "#username", "value": "user"},
    {"type": "click", "selector": "#submit"},
])
```

---

## Adding New Rules

Rules live in `PATTERN_RULES` at the top of `ingestion/web/scraper.py`:

```python
PATTERN_RULES: list[tuple[str, str]] = [
    # ... existing rules ...
    (r"news\.ycombinator\.com", "playwright"),  # HN is dynamic
    (r"vercel\.com/docs",       "scrapling"),    # Vercel docs are SSR
]
```

Rules are checked top-to-bottom. First match wins. Add specific domains before generic path patterns.

The tool name must be one of `"scrapling"`, `"playwright"`, or `"firecrawl"`.

---

## Summary

The Scraper Router removes the mental overhead of choosing a scraping tool. Give it a URL, it:

1. Checks URL patterns for known tool requirements (instant)
2. Tries Scrapling async_http (fast, local, ~0.1-0.6s)
3. Validates content quality (instant)
4. Falls back to Playwright if content is garbage (~1-5s)

Three backends, one interface. OCR never has to think about which engine to use.

For supported files, see:
- `ingestion/web/scraper.py` — Router implementation and pattern rules
- `ingestion/web/scrapling.py` — ScraplingAdapter (async_http, stealthy, playwright modes)
- `ingestion/web/playwright.py` — PlaywrightAdapter (browser automation)
- `ingestion/web/firecrawl.py` — FirecrawlAdapter (cloud scraping)
- `ingestion/web/adapter.py` — WebAdapter ABC and data types
- `ingestion/web/_scrapling.md` — Scrapling evaluation results
