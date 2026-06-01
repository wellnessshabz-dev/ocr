"""Firecrawl adapter — cloud-based web scraping via the official SDK.

Best for: pulling documentation, crawling docs sites, web search.
"""

import asyncio
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from firecrawl import AsyncV1FirecrawlApp

from ingestion.web.adapter import WebAdapter, WebContent, WebSearchResult

logger = logging.getLogger(__name__)

_POLL_INTERVAL = 3
_MAX_POLL_ATTEMPTS = 60


class FirecrawlAdapter(WebAdapter):

    def __init__(self, api_key: str = "", env_file: str = ""):
        if env_file:
            load_dotenv(dotenv_path=Path(env_file))
        key = api_key or os.getenv("FIRECRAWL_API_KEY", "")
        self._app: AsyncV1FirecrawlApp | None = None
        if key:
            self._app = AsyncV1FirecrawlApp(api_key=key)
        else:
            logger.warning("FIRECRAWL_API_KEY not set — FirecrawlAdapter will return empty results")

    async def scrape(self, url: str, format: str = "markdown") -> WebContent:
        if not self._app:
            return WebContent(url=url, markdown="")

        try:
            resp = await self._app.scrape_url(url, formats=[format])
            if not resp.success:
                logger.warning("Firecrawl scrape failed for %s: %s", url, resp.error)
                return WebContent(url=url, markdown="")
        except Exception as e:
            logger.error("Firecrawl scrape error for %s: %s", url, e)
            return WebContent(url=url, markdown="")

        return WebContent(
            url=resp.url or url,
            markdown=resp.markdown or "",
            title=resp.title or "",
            description=resp.description or "",
            metadata=resp.metadata or {},
        )

    async def crawl(self, url: str, max_pages: int = 50) -> list[WebContent]:
        if not self._app:
            return []

        try:
            job = await self._app.crawl_url(url, limit=max_pages)
            if not job.success:
                logger.warning("Firecrawl crawl failed for %s: %s", url, job.error)
                return []
        except Exception as e:
            logger.error("Firecrawl crawl error for %s: %s", url, e)
            return []

        for _ in range(_MAX_POLL_ATTEMPTS):
            await asyncio.sleep(_POLL_INTERVAL)
            try:
                status = await self._app.check_crawl_status(job.id)
            except Exception as e:
                logger.error("Firecrawl crawl poll error: %s", e)
                return []

            if status.status == "completed":
                pages = []
                for item in (status.data or []):
                    pages.append(WebContent(
                        url=getattr(item, "url", url),
                        markdown=getattr(item, "markdown", ""),
                        title=getattr(item, "title", ""),
                        description=getattr(item, "description", ""),
                        metadata=getattr(item, "metadata", {}),
                    ))
                return pages
            elif status.status == "failed":
                logger.error("Firecrawl crawl job %s failed", job.id)
                return []

        logger.warning("Firecrawl crawl job %s timed out", job.id)
        return []

    async def map_site(self, url: str) -> list[str]:
        if not self._app:
            return []

        try:
            resp = await self._app.map_url(url)
            if not resp.success:
                logger.warning("Firecrawl map failed for %s: %s", url, resp.error)
                return []
            return resp.links or []
        except Exception as e:
            logger.error("Firecrawl map error for %s: %s", url, e)
            return []

    async def search(self, query: str, max_results: int = 10) -> WebSearchResult:
        if not self._app:
            return WebSearchResult(query=query)

        try:
            resp = await self._app.search(query, limit=max_results)
        except Exception as e:
            logger.error("Firecrawl search error for '%s': %s", query, e)
            return WebSearchResult(query=query)

        if isinstance(resp, dict):
            if not resp.get("success"):
                logger.warning("Firecrawl search failed for '%s'", query)
                return WebSearchResult(query=query)
            items = resp.get("data", [])
        else:
            if not resp.success:
                logger.warning("Firecrawl search failed for '%s': %s", query, getattr(resp, "error", ""))
                return WebSearchResult(query=query)
            items = getattr(resp, "data", []) or []

        results = []
        for item in items:
            if isinstance(item, dict):
                results.append({
                    "url": item.get("url", ""),
                    "title": item.get("title", ""),
                    "description": item.get("description", ""),
                    "markdown": item.get("markdown", ""),
                })
            else:
                results.append({
                    "url": getattr(item, "url", ""),
                    "title": getattr(item, "title", ""),
                    "description": getattr(item, "description", ""),
                    "markdown": getattr(item, "markdown", ""),
                })

        return WebSearchResult(
            query=query,
            results=results,
            total_results=len(results),
        )

    async def extract(self, url: str, schema: dict) -> dict:
        if not self._app:
            return {}

        try:
            resp = await self._app.scrape_url(url, formats=["extract"], extract=schema)
            if not resp.success:
                logger.warning("Firecrawl extract failed for %s: %s", url, resp.error)
                return {}
            if resp.extract:
                return resp.extract if isinstance(resp.extract, dict) else {"data": resp.extract}
            return {"markdown": resp.markdown or ""}
        except Exception as e:
            logger.error("Firecrawl extract error for %s: %s", url, e)
            fallback = await self.scrape(url)
            return {"markdown": fallback.markdown}

    async def interact(self, url: str, actions: list[dict]) -> WebContent:
        logger.warning("Firecrawl does not support interact — use Playwright")
        return WebContent(url=url, markdown="")
