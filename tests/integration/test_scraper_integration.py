"""Integration tests for ScraperRouter with mock adapters."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from ingestion.web.adapter import WebContent, WebSearchResult
from ingestion.web.scraper import ScraperRouter


@pytest.fixture
def mock_firecrawl():
    adapter = MagicMock()
    adapter.scrape = AsyncMock(return_value=WebContent(
        url="https://example.com",
        markdown="# Firecrawl content\n\n" + "x" * 200,
    ))
    adapter.crawl = AsyncMock(return_value=[
        WebContent(url="https://example.com/p1", markdown="# Page 1"),
    ])
    adapter.map_site = AsyncMock(return_value=["https://example.com/p1"])
    adapter.search = AsyncMock(return_value=WebSearchResult(
        query="test", results=[{"url": "https://a.com", "title": "A", "markdown": "# A"}], total_results=1
    ))
    adapter.extract = AsyncMock(return_value={"name": "test"})
    return adapter


@pytest.fixture
def mock_playwright():
    adapter = MagicMock()
    adapter.scrape = AsyncMock(return_value=WebContent(
        url="https://example.com", markdown="# Playwright content"
    ))
    adapter.interact = AsyncMock(return_value=WebContent(
        url="https://example.com", markdown="# After interaction"
    ))
    return adapter


@pytest.fixture
def router(mock_firecrawl, mock_playwright):
    return ScraperRouter(firecrawl=mock_firecrawl, playwright=mock_playwright)


class TestRouterWithMockAdapters:

    async def test_scrape_uses_firecrawl_by_default(self, router, mock_firecrawl):
        content = await router.scrape("https://unknown-site.com")
        mock_firecrawl.scrape.assert_called_once()
        assert "# Firecrawl content" in content.markdown

    async def test_scrape_with_prefer_playwright(self, router, mock_firecrawl, mock_playwright):
        content = await router.scrape("https://unknown-site.com", prefer="playwright")
        mock_playwright.scrape.assert_called_once()
        mock_firecrawl.scrape.assert_not_called()
        assert "# Playwright content" in content.markdown

    async def test_scrape_with_prefer_firecrawl(self, router, mock_firecrawl, mock_playwright):
        content = await router.scrape("https://unknown-site.com", prefer="firecrawl")
        mock_firecrawl.scrape.assert_called_once()
        mock_playwright.scrape.assert_not_called()

    async def test_scrape_routes_stackoverflow_to_playwright(self, router, mock_firecrawl, mock_playwright):
        await router.scrape("https://stackoverflow.com/q/123")
        mock_playwright.scrape.assert_called_once()
        mock_firecrawl.scrape.assert_not_called()

    async def test_scrape_routes_docs_to_firecrawl(self, router, mock_firecrawl, mock_playwright):
        await router.scrape("https://docs.example.com/page")
        mock_firecrawl.scrape.assert_called_once()

    async def test_crawl_uses_firecrawl(self, router, mock_firecrawl):
        await router.crawl("https://example.com", max_pages=5)
        mock_firecrawl.crawl.assert_called_once_with("https://example.com", 5)

    async def test_map_site_uses_firecrawl(self, router, mock_firecrawl):
        await router.map_site("https://example.com")
        mock_firecrawl.map_site.assert_called_once_with("https://example.com")

    async def test_search_uses_firecrawl(self, router, mock_firecrawl):
        await router.search("test query")
        mock_firecrawl.search.assert_called_once_with("test query", 10)

    async def test_extract_uses_firecrawl(self, router, mock_firecrawl):
        await router.extract("https://example.com", {"type": "object"})
        mock_firecrawl.extract.assert_called_once_with("https://example.com", {"type": "object"})

    async def test_interact_always_uses_playwright(self, router, mock_playwright):
        await router.interact("https://example.com", [{"type": "click", "selector": "#btn"}])
        mock_playwright.interact.assert_called_once()


class TestFallback:

    async def test_fallback_on_empty_content(self):
        fc = MagicMock()
        fc.scrape = AsyncMock(return_value=WebContent(url="https://example.com", markdown=""))

        pw = MagicMock()
        pw.scrape = AsyncMock(return_value=WebContent(
            url="https://example.com", markdown="# Good content from Playwright"
        ))

        router = ScraperRouter(firecrawl=fc, playwright=pw)
        result = await router.scrape("https://example.com")
        assert "# Good content from Playwright" in result.markdown

    async def test_fallback_on_blocked_content(self):
        fc = MagicMock()
        fc.scrape = AsyncMock(return_value=WebContent(
            url="https://example.com", markdown="Please enable JavaScript to continue"
        ))

        pw = MagicMock()
        pw.scrape = AsyncMock(return_value=WebContent(
            url="https://example.com", markdown="# Real content after fallback"
        ))

        router = ScraperRouter(firecrawl=fc, playwright=pw)
        result = await router.scrape("https://example.com")
        assert "# Real content after fallback" in result.markdown

    async def test_no_fallback_when_quality_is_good(self):
        fc = MagicMock()
        fc.scrape = AsyncMock(return_value=WebContent(
            url="https://example.com",
            markdown="Good content. " * 20,
        ))

        pw = MagicMock()

        router = ScraperRouter(firecrawl=fc, playwright=pw)
        await router.scrape("https://example.com")
        pw.scrape.assert_not_called()

    async def test_fallback_disabled_via_config(self):
        fc = MagicMock()
        fc.scrape = AsyncMock(return_value=WebContent(url="https://example.com", markdown=""))

        pw = MagicMock()

        router = ScraperRouter(firecrawl=fc, playwright=pw, config={"fallback": False})
        result = await router.scrape("https://example.com")
        assert result.markdown == ""
        pw.scrape.assert_not_called()
