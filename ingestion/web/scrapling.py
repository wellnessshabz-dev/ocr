"""Scrapling adapter — unified web scraping via the Scrapling library.

Three fetcher modes:
- async_http: AsyncFetcher (plain HTTP + TLS fingerprint) — static pages, docs
- stealthy:   StealthyFetcher (patched browser) — Cloudflare, anti-bot bypass
- playwright: PlayWrightFetcher (full Playwright) — SPAs, complex auth

Usage:
    adapter = ScraplingAdapter(mode="async_http")
    content = await adapter.scrape("https://fastapi.tiangolo.com/")
"""

import logging
from typing import Optional

import html2text

from ingestion.web.adapter import WebAdapter, WebContent, WebSearchResult

logger = logging.getLogger(__name__)

_converter = html2text.HTML2Text()
_converter.body_width = 0
_converter.ignore_links = False
_converter.ignore_images = False
_converter.ignore_emphasis = False


SUPPORTED_MODES = ("async_http", "stealthy", "playwright")


class ScraplingAdapter(WebAdapter):

    def __init__(self, mode: str = "async_http"):
        if mode not in SUPPORTED_MODES:
            raise ValueError(f"ScraplingAdapter mode must be one of {SUPPORTED_MODES}, got {mode!r}")
        self.mode = mode

    async def scrape(self, url: str, format: str = "markdown") -> WebContent:
        try:
            resp = await self._fetch(url)
        except Exception as e:
            logger.error("Scrapling (%s) scrape error for %s: %s", self.mode, url, e)
            return WebContent(url=url, markdown="")

        if resp.status and resp.status >= 400:
            logger.warning("Scrapling (%s) got HTTP %s for %s", self.mode, resp.status, url)

        markdown = self._to_markdown(resp)
        title = self._extract_title(resp)

        return WebContent(
            url=url,
            markdown=markdown,
            title=title,
            metadata={
                "status": resp.status,
                "mode": self.mode,
            },
        )

    async def crawl(self, url: str, max_pages: int = 50) -> list[WebContent]:
        logger.warning("Scrapling crawl not implemented — use scrape()")
        return []

    async def map_site(self, url: str) -> list[str]:
        logger.warning("Scrapling map_site not implemented — use scrape()")
        return []

    async def search(self, query: str, max_results: int = 10) -> WebSearchResult:
        logger.warning("Scrapling search not implemented — use FirecrawlAdapter")
        return WebSearchResult(query=query)

    async def extract(self, url: str, schema: dict) -> dict:
        content = await self.scrape(url)
        return {"markdown": content.markdown, "title": content.title, **content.metadata}

    async def interact(self, url: str, actions: list[dict]) -> WebContent:
        logger.warning("Scrapling interact not implemented — use PlaywrightAdapter")
        return WebContent(url=url, markdown="")

    # ── Internal helpers ────────────────────────────────────────────────

    async def _fetch(self, url: str):
        if self.mode == "async_http":
            from scrapling.fetchers import AsyncFetcher
            return await AsyncFetcher.get(url, follow_redirects=True, timeout=15)
        elif self.mode == "stealthy":
            from scrapling.fetchers import StealthyFetcher
            return await StealthyFetcher.async_fetch(url, headless=True, timeout=30000, network_idle=True)
        elif self.mode == "playwright":
            from scrapling.fetchers import PlayWrightFetcher
            return await PlayWrightFetcher.async_fetch(url, headless=True, timeout=30000, network_idle=True)

    def _to_markdown(self, resp) -> str:
        html = getattr(resp, "html_content", None) or ""
        if not html:
            return resp.get_all_text() if hasattr(resp, "get_all_text") else str(resp.text or "")
        return _converter.handle(html).strip()

    def _extract_title(self, resp) -> str:
        try:
            title_el = resp.css("title::text")
            if title_el:
                return title_el.get(default="")
        except Exception:
            pass
        return ""
