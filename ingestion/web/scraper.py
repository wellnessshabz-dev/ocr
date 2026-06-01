"""Intelligent router between Scrapling (local HTTP), Playwright (local browser),
and Firecrawl (cloud API).

Picks the right tool for each URL automatically. Falls back from the fast path
to Playwright when content quality is low.

Usage:
    scraper = ScraperRouter()
    content = await scraper.scrape("https://fastapi.tiangolo.com/tutorial/")
    content = await scraper.scrape("https://stackoverflow.com/q/123", prefer="playwright")
"""

import re
from typing import Optional
from urllib.parse import urlparse

from ingestion.web.adapter import WebAdapter, WebContent, WebSearchResult
from ingestion.web.firecrawl import FirecrawlAdapter
from ingestion.web.playwright import PlaywrightAdapter
from ingestion.web.scrapling import ScraplingAdapter


# ── URL pattern rules ──────────────────────────────────────────────────
# First match wins. Order: specific domains before generic patterns.
TOOL_NAMES = ("scrapling", "playwright", "firecrawl")

PATTERN_RULES: list[tuple[str, str]] = [
    # ── Documentation platforms (fast path: Scrapling async_http) ──
    (r"docs\.\w+\.",           "scrapling"),
    (r"readthedocs\.io",       "scrapling"),
    (r"developer\.\w+\.",      "scrapling"),
    (r"learn\.\w+\.",          "scrapling"),
    (r"wikipedia\.org",        "scrapling"),
    (r"wiki\.\w+",             "scrapling"),

    # ── Code platforms ──
    (r"github\.com/.*/blob/",  "scrapling"),
    (r"github\.com/.*/wiki",   "scrapling"),
    (r"github\.com/.*/docs",   "scrapling"),
    (r"pypi\.org",             "playwright"),
    (r"npmjs\.com",            "playwright"),

    # ── Q&A / forums ──
    (r"stackoverflow\.com",    "playwright"),
    (r"stackexchange\.com",    "playwright"),
    (r"reddit\.com",           "playwright"),

    # ── Social / video ──
    (r"twitter\.com",          "playwright"),
    (r"x\.com",                "playwright"),
    (r"youtube\.com",          "playwright"),
    (r"linkedin\.com",         "playwright"),

    # ── Blogs / articles ──
    (r"medium\.com",           "scrapling"),
    (r"dev\.to",               "scrapling"),
    (r"hashnode\.com",         "scrapling"),
    (r"substack\.com",         "scrapling"),

    # ── URL path patterns ──
    (r"/docs/",                "scrapling"),
    (r"/api",                  "scrapling"),
    (r"/reference",            "scrapling"),
    (r"/tutorial",             "scrapling"),
    (r"/guide",                "scrapling"),
    (r"/blog/",                "scrapling"),
    (r"/wiki/",                "scrapling"),
    (r"/learn/",               "scrapling"),
]

# ── Quality check thresholds ─────────────────────────────────────────
DEFAULT_CONFIG = {
    "default_tool": "scrapling",
    "fallback": True,
    "quality": {
        "min_chars": 100,
        "min_ratio": 0.2,
    },
    "timeout": {
        "scrapling": 15,
        "playwright": 30,
    },
    "max_crawl_pages": 100,
}

# ── Signals that content was blocked or requires JS ──────────────────
BLOCKED_PATTERNS: list[re.Pattern] = [
    re.compile(r"enable javascript", re.IGNORECASE),
    re.compile(r"javascript is required", re.IGNORECASE),
    re.compile(r"please enable javascript", re.IGNORECASE),
    re.compile(r"sign in to continue", re.IGNORECASE),
    re.compile(r"sign in \|", re.IGNORECASE),
    re.compile(r"log in to continue", re.IGNORECASE),
    re.compile(r"captcha", re.IGNORECASE),
    re.compile(r"verify you are human", re.IGNORECASE),
    re.compile(r"access denied", re.IGNORECASE),
    re.compile(r"403 forbidden", re.IGNORECASE),
    re.compile(r"we couldn't load", re.IGNORECASE),
]

# ── Boilerplate to strip before ratio check ──────────────────────────
BOILERPLATE: list[str] = [
    "cookie", "privacy policy", "terms of service", "accept cookies",
    "skip to content", "menu", "navigation", "footer", "sidebar",
    "advertisement", "subscribe to our newsletter", "sign up for free",
]


class ScraperRouter(WebAdapter):

    def __init__(
        self,
        scrapling: Optional[WebAdapter] = None,
        playwright: Optional[WebAdapter] = None,
        firecrawl: Optional[WebAdapter] = None,
        config: Optional[dict] = None,
    ):
        self.scrapling = scrapling or ScraplingAdapter(mode="async_http")
        self.playwright = playwright or PlaywrightAdapter()
        self.firecrawl = firecrawl or FirecrawlAdapter()
        self.config = {**DEFAULT_CONFIG, **(config or {})}

    # ── Public API ──────────────────────────────────────────────────────

    async def scrape(self, url: str, format: str = "markdown", prefer: str = "") -> WebContent:
        tool = prefer.lower() if prefer else self._route(url)

        if tool == "playwright":
            return await self.playwright.scrape(url, format)

        if tool == "firecrawl":
            content = await self.firecrawl.scrape(url, format)
            if self.config["fallback"] and not self._quality_check(content):
                content = await self.playwright.scrape(url, format)
            return content

        # Default path: try Scrapling, fall back to Playwright if needed
        content = await self.scrapling.scrape(url, format)

        if self.config["fallback"] and not self._quality_check(content):
            content = await self.playwright.scrape(url, format)

        return content

    async def crawl(self, url: str, max_pages: int = 50) -> list[WebContent]:
        actual_max = min(max_pages, self.config["max_crawl_pages"])
        return await self.firecrawl.crawl(url, actual_max)

    async def map_site(self, url: str) -> list[str]:
        return await self.firecrawl.map_site(url)

    async def search(self, query: str, max_results: int = 10) -> WebSearchResult:
        return await self.firecrawl.search(query, max_results)

    async def extract(self, url: str, schema: dict) -> dict:
        return await self.firecrawl.extract(url, schema)

    async def interact(self, url: str, actions: list[dict]) -> WebContent:
        return await self.playwright.interact(url, actions)

    # ── Routing logic ────────────────────────────────────────────────────

    def _route(self, url: str) -> str:
        for pattern, tool in PATTERN_RULES:
            if re.search(pattern, url, re.IGNORECASE):
                return tool
        return self.config["default_tool"]

    def _quality_check(self, content: WebContent) -> bool:
        text = content.markdown.strip()

        # Too short = useless
        if len(text) < self.config["quality"]["min_chars"]:
            return False

        # Detected a blocked/JS-required page
        for pattern in BLOCKED_PATTERNS:
            if pattern.search(text):
                return False

        # Boilerplate ratio: strip common junk and see what's left
        clean = text.lower()
        for phrase in BOILERPLATE:
            clean = clean.replace(phrase, "")

        ratio = len(clean) / max(len(text), 1)
        if ratio < self.config["quality"]["min_ratio"]:
            return False

        return True

    def _route_for_crawl(self, url: str) -> str:
        domain = urlparse(url).netloc.lower()
        for pattern, tool in PATTERN_RULES:
            if re.search(pattern, domain, re.IGNORECASE):
                return tool
        return "scrapling"
