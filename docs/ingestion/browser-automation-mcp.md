# Browser Control — How OCR Scrapes Documentation and the Web

## The Problem

OCR needs to read documentation, scrape web pages, and extract content from the
internet. Some documentation is static HTML, some is JavaScript-rendered SPAs,
some requires clicking through menus, and some is behind login walls. One tool
cannot handle all of these.

## The Landscape

The browser automation MCP space in 2026 has a clear winner and several
specialists:

| Server | Approach | Cost | Best For |
|--------|----------|------|----------|
| **Playwright MCP** | Accessibility tree snapshots | Free | 90% of browser automation |
| Firecrawl MCP | Clean markdown extraction | Paid (free tier) | Bulk doc scraping |
| Browserbase MCP | Cloud browser + natural language | $20-99/mo | Production scraping |
| Puppeteer MCP | CSS selectors + screenshots | Free (deprecated) | Nothing — migrate away |
| Ghost Browser MCP | CDP-level stealth | Free | Anti-bot bypass |
| Browser MCP (Agent360) | Your real Chrome with logins | Free (MIT) | Logged-in sessions |
| MCP Browser (wgarrido) | Real Chrome via CDP | Free | Simple browsing |
| Fetch MCP | HTTP request only | Free | Static pages |

---

## The Winner: Playwright MCP (Microsoft)

**Official**: `@playwright/mcp` from Microsoft
**Stars**: 29,150+ | **Global rank**: #10 across all MCP servers
**Tools**: 40+ | **Browsers**: Chromium, Firefox, WebKit, Edge
**License**: Apache 2.0 (free forever)

### Why It Won

Playwright MCP does not use screenshots. It reads the browser's accessibility
tree — a structured, text-based representation of every interactive element on
the page. Every button, link, and form field gets a reference number. The AI
reads that tree, finds the element it wants, and sends an action.

```
Accessibility snapshot (playwright):
─────────────────────────────────────
  [ref=e45] heading "Installation"
  [ref=e46] link "Quick Start" 
  [ref=e47] link "API Reference"
  [ref=e48] search input "Search docs..."
  [ref=e49] button "Submit"
─────────────────────────────────────

The AI says: browser_click(ref="e46") — no guessing, no CSS selectors.
```

**This is ~200-400 tokens per snapshot**, versus thousands of tokens for raw
HTML or a screenshot that needs a vision model.

### When Playwright MCP Is Not Enough

| Limitation | What fails | Alternative |
|-----------|-----------|-------------|
| Anti-bot detection | Cloudflare, DataDome block Playwright | Ghost Browser or Browserbase |
| Clean markdown output | Playwright returns HTML, not markdown | Firecrawl (markdown native) |
| Bulk crawling | Single-page focused | Firecrawl crawl tool |
| Already-logged-in sessions | Playwright starts fresh | Browser MCP (Agent360) — uses your Chrome |
| CAPTCHA challenges | Playwright cannot solve them | Browser MCP with human-in-loop |

---

## For OCR Specifically: Firecrawl + Playwright Together

OCR's web needs split into two categories:

### Category A: Pulling Documentation (the primary use case)

**Use Firecrawl MCP.** It converts any URL to clean markdown in one call.
Handles JS rendering, pagination, anti-bot pages. Perfect for:
- `scrape` — single URL → clean markdown
- `crawl` — entire documentation site → all pages
- `map` — discover all URLs on a site → sitemap
- `search` — web search → full page content
- `extract` — structured data with JSON schema

### Category B: Interactive Web Tasks (secondary)

**Use Playwright MCP** when you need to:
- Click through documentation menus
- Fill in search forms  
- Log into a site, then scrape
- Wait for dynamic content to load
- Take screenshots for visual context

### How They Work Together

```
OCR Web Request
       │
       ├── "Scrape this URL for docs"
       │   └── Firecrawl.scrape(url) → clean markdown → Ontology Extractor
       │
       ├── "Crawl this documentation site"
       │   └── Firecrawl.crawl(url) → all pages → Shipment Compiler
       │
       ├── "Find this topic on the web"
       │   └── Firecrawl.search(query) → results → Strategic Questions
       │
       ├── "Click through this setup guide"
       │   └── Playwright.navigate(url) → snapshot → click → read
       │
       └── "Extract pricing table from this SaaS page"
           └── Firecrawl.scrape(url, format="json") → structured data
```

---

## What One Call Gives OCR

### Firecrawl `scrape` response:

```
URL: https://docs.someframework.com/api
Response:
├── markdown: "# API Reference\n\n## Authentication\n\n..."  ← Clean docs
├── metadata:
│   ├── title: "API Reference"
│   ├── description: "Complete API documentation"
│   ├── language: "en"
│   ├── sourceURL: "https://docs.someframework.com/api"
│   └── statusCode: 200
└── (optional JSON schema extraction)
```

OCR feeds this markdown directly into the Ontology Extractor:
- Headings → concept nodes (feature, endpoint, parameter)
- Code blocks → component nodes (syntax, examples)
- Descriptions → context for existing ontology nodes
- Links → cross-reference edges between concepts

### Playwright `browser_snapshot` response:

```
Accessibility tree:
├── [ref=e1]  banner "SomeFramework Docs"
├── [ref=e2]  navigation "Sidebar"  
│   ├── [ref=e3] link "Getting Started"
│   ├── [ref=e4] link "Installation"
│   └── [ref=e5] link "API Reference" ← click this
├── [ref=e6]  main "API Reference content"
│   ├── [ref=e7]  heading "Authentication"
│   └── [ref=e8]  code "api_key = 'sk-...'"
└── [ref=e9]  search "Search documentation..."
```

OCR uses this to navigate multi-page documentation. It reads the snapshot,
decides what to click next, and extracts content from the resulting page.

---

## MCP Tools Reference

### Playwright MCP — 40+ tools

| Group | Tools |
|-------|-------|
| **Navigation** | `browser_navigate`, `browser_navigate_back`, `browser_navigate_forward`, `browser_reload` |
| **Reading** | `browser_snapshot` (accessibility tree), `browser_console_messages` |
| **Interaction** | `browser_click`, `browser_type`, `browser_fill_form`, `browser_select_option`, `browser_check`, `browser_uncheck`, `browser_hover`, `browser_drag`, `browser_press_key` |
| **Screenshots** | `browser_take_screenshot` (PNG/JPEG) |
| **Tabs** | `browser_tabs` (list, create, close, switch) |
| **Storage** | `browser_cookie_*`, `browser_localstorage_*`, `browser_storage_state` |
| **Network** | `browser_network_requests`, `browser_route`, `browser_route_list`, `browser_unroute` |
| **Execution** | `browser_run_code`, `browser_evaluate` (JavaScript) |
| **Utilities** | `browser_file_upload`, `browser_wait_for`, `browser_resize`, `browser_handle_dialog`, `browser_close` |
| **Assertions** | `browser_verify_element_visible`, `browser_verify_text_visible` |
| **Recording** | `browser_start_tracing`, `browser_stop_tracing`, `browser_start_video`, `browser_stop_video` |
| **PDF** | `browser_pdf_save` |
| **Mouse** | `browser_mouse_move_xy`, `browser_mouse_click_xy`, `browser_mouse_drag_xy`, `browser_mouse_wheel` |
| **Locator** | `browser_generate_locator` |

### Firecrawl MCP — 8 tools

| Tool | What it does | Returns |
|------|-------------|---------|
| `firecrawl_scrape` | Single URL → clean content | JSON (preferred) or markdown |
| `firecrawl_crawl` | Multi-page site extraction | markdown/html[] |
| `firecrawl_map` | Discover all URLs on a site | URL[] |
| `firecrawl_search` | Web search with full page content | results[] |
| `firecrawl_extract` | Structured data extraction | JSON schema |
| `firecrawl_agent` | Autonomous multi-source research | JSON |
| `firecrawl_batch_scrape` | Multiple known URLs | JSON/markdown[] |
| `firecrawl_interact` | Click, fill forms on a scraped page | Execution result |

---

## What Not to Use (and Why)

| Skip this | Reason |
|-----------|--------|
| Puppeteer MCP | Deprecated by Anthropic. Playwright is the successor with 5x more tools and 3x more browsers. |
| Browserbase MCP | Costs $20-99/mo. Overkill for documentation scraping. Use Firecrawl + Playwright for free. |
| Ghost Browser MCP | 225 tools is overwhelming. Designed for pentesting, not doc scraping. |
| Fetch MCP | Cannot handle JavaScript-rendered sites. Most documentation is SPA-based. |

---

## Summary

OCR uses **two browser MCP servers together**:

| Tool | When | What it gives OCR |
|------|------|-------------------|
| Firecrawl MCP | Pulling docs, crawling sites, web search | Clean markdown → Ontology Extractor |
| Playwright MCP | Clicking through menus, logging in, interactive pages | Accessibility tree → Shipment Compiler |

Both are configured as MCP servers alongside GitHub MCP. OCR chooses the right
tool based on the task — fetch docs with Firecrawl, interact with Playwright.

---

## Reference

- Playwright MCP: https://github.com/microsoft/playwright-mcp
- Playwright MCP docs: https://playwright.dev/mcp/introduction
- Firecrawl MCP: https://github.com/firecrawl/firecrawl-mcp-server
- Pricing: Playwright (free forever), Firecrawl (free tier available)
- Deprecated Puppeteer: https://github.com/modelcontextprotocol/servers (archived)
