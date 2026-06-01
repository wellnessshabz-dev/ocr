"""Tests for FirecrawlAdapter — mocks the SDK client."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from ingestion.web.adapter import WebContent
from ingestion.web.firecrawl import FirecrawlAdapter


@pytest.fixture
def adapter(mock_firecrawl_app, mock_firecrawl_scrape_response):
    adapter = FirecrawlAdapter(api_key="test-key")
    adapter._app = mock_firecrawl_app
    adapter._app.scrape_url.return_value = mock_firecrawl_scrape_response
    return adapter


class TestScrape:

    async def test_returns_webcontent(self, adapter):
        result = await adapter.scrape("https://example.com")
        assert isinstance(result, WebContent)

    async def test_returns_markdown(self, adapter):
        result = await adapter.scrape("https://example.com")
        assert "# Example" in result.markdown

    async def test_returns_title(self, adapter):
        result = await adapter.scrape("https://example.com")
        assert result.title == "Example Page"

    async def test_returns_metadata(self, adapter):
        result = await adapter.scrape("https://example.com")
        assert result.metadata["sourceURL"] == "https://example.com"

    async def test_calls_scrape_url_with_correct_args(self, adapter):
        await adapter.scrape("https://example.com", format="markdown")
        adapter._app.scrape_url.assert_called_once_with(
            "https://example.com", formats=["markdown"]
        )

    async def test_handles_api_failure(self, adapter, mock_firecrawl_scrape_response):
        mock_firecrawl_scrape_response.success = False
        mock_firecrawl_scrape_response.error = "Rate limited"
        result = await adapter.scrape("https://example.com")
        assert result.markdown == ""

    async def test_handles_exception(self, adapter):
        adapter._app.scrape_url.side_effect = Exception("Connection failed")
        result = await adapter.scrape("https://example.com")
        assert result.markdown == ""

    async def test_handles_empty_markdown(self, adapter, mock_firecrawl_scrape_response):
        mock_firecrawl_scrape_response.markdown = None
        result = await adapter.scrape("https://example.com")
        assert result.markdown == ""


class TestSearch:

    async def test_returns_search_result(self, adapter, mock_firecrawl_search_response):
        adapter._app.search.return_value = mock_firecrawl_search_response
        result = await adapter.search("test query", max_results=2)
        assert result.total_results == 2

    async def test_returns_result_urls(self, adapter, mock_firecrawl_search_response):
        adapter._app.search.return_value = mock_firecrawl_search_response
        result = await adapter.search("test query")
        assert result.results[0]["url"] == "https://example.com"

    async def test_returns_result_titles(self, adapter, mock_firecrawl_search_response):
        adapter._app.search.return_value = mock_firecrawl_search_response
        result = await adapter.search("test query")
        assert result.results[1]["title"] == "Example Org"

    async def test_calls_search_with_correct_args(self, adapter, mock_firecrawl_search_response):
        adapter._app.search.return_value = mock_firecrawl_search_response
        await adapter.search("hello world", max_results=5)
        adapter._app.search.assert_called_once_with("hello world", limit=5)

    async def test_handles_search_exception(self, adapter):
        adapter._app.search.side_effect = Exception("Search failed")
        result = await adapter.search("test")
        assert result.total_results == 0

    async def test_handles_search_failure(self, adapter):
        adapter._app.search.return_value = {"success": False}
        result = await adapter.search("test")
        assert result.total_results == 0


class TestMapSite:

    async def test_returns_urls(self, adapter, mock_firecrawl_map_response):
        adapter._app.map_url.return_value = mock_firecrawl_map_response
        result = await adapter.map_site("https://example.com")
        assert len(result) == 3

    async def test_includes_homepage(self, adapter, mock_firecrawl_map_response):
        adapter._app.map_url.return_value = mock_firecrawl_map_response
        result = await adapter.map_site("https://example.com")
        assert "https://example.com" in result

    async def test_calls_map_url_with_correct_args(self, adapter, mock_firecrawl_map_response):
        adapter._app.map_url.return_value = mock_firecrawl_map_response
        await adapter.map_site("https://example.com")
        adapter._app.map_url.assert_called_once_with("https://example.com")

    async def test_handles_map_failure(self, adapter, mock_firecrawl_map_response):
        mock_firecrawl_map_response.success = False
        adapter._app.map_url.return_value = mock_firecrawl_map_response
        result = await adapter.map_site("https://example.com")
        assert result == []


class TestCrawl:

    async def test_returns_pages(self, adapter, mock_firecrawl_crawl_job, mock_firecrawl_crawl_completed):
        adapter._app.crawl_url.return_value = mock_firecrawl_crawl_job
        adapter._app.check_crawl_status.return_value = mock_firecrawl_crawl_completed
        result = await adapter.crawl("https://example.com", max_pages=5)
        assert len(result) == 2

    async def test_returns_webcontent_list(self, adapter, mock_firecrawl_crawl_job, mock_firecrawl_crawl_completed):
        adapter._app.crawl_url.return_value = mock_firecrawl_crawl_job
        adapter._app.check_crawl_status.return_value = mock_firecrawl_crawl_completed
        result = await adapter.crawl("https://example.com")
        assert all(isinstance(p, WebContent) for p in result)

    async def test_has_page_content(self, adapter, mock_firecrawl_crawl_job, mock_firecrawl_crawl_completed):
        adapter._app.crawl_url.return_value = mock_firecrawl_crawl_job
        adapter._app.check_crawl_status.return_value = mock_firecrawl_crawl_completed
        result = await adapter.crawl("https://example.com")
        assert result[0].markdown == "# Page 1"

    async def test_handles_crawl_failure(self, adapter, mock_firecrawl_crawl_job):
        mock_firecrawl_crawl_job.success = False
        adapter._app.crawl_url.return_value = mock_firecrawl_crawl_job
        result = await adapter.crawl("https://example.com")
        assert result == []


class TestExtract:

    async def test_returns_dict(self, adapter, mock_firecrawl_scrape_response):
        mock_firecrawl_scrape_response.extract = {"name": "Test", "price": 100}
        adapter._app.scrape_url.return_value = mock_firecrawl_scrape_response
        result = await adapter.extract("https://example.com", {"type": "object"})
        assert isinstance(result, dict)

    async def test_returns_extracted_data(self, adapter, mock_firecrawl_scrape_response):
        mock_firecrawl_scrape_response.extract = {"name": "Test", "price": 100}
        adapter._app.scrape_url.return_value = mock_firecrawl_scrape_response
        result = await adapter.extract("https://example.com", {"type": "object"})
        assert result["name"] == "Test"

    async def test_falls_back_to_markdown(self, adapter, mock_firecrawl_scrape_response):
        mock_firecrawl_scrape_response.extract = None
        adapter._app.scrape_url.return_value = mock_firecrawl_scrape_response
        result = await adapter.extract("https://example.com", {"type": "object"})
        assert "markdown" in result


class TestInteract:

    async def test_returns_empty_webcontent(self, adapter):
        result = await adapter.interact("https://example.com", [{"type": "click", "selector": "#btn"}])
        assert isinstance(result, WebContent)
        assert result.markdown == ""


class TestNoApiKey:

    async def test_returns_empty_on_scrape(self, monkeypatch):
        monkeypatch.setenv("FIRECRAWL_API_KEY", "")
        adapter = FirecrawlAdapter(api_key="")
        result = await adapter.scrape("https://example.com")
        assert result.markdown == ""

    async def test_returns_empty_on_search(self, monkeypatch):
        monkeypatch.setenv("FIRECRAWL_API_KEY", "")
        adapter = FirecrawlAdapter(api_key="")
        result = await adapter.search("test")
        assert result.total_results == 0

    async def test_returns_empty_on_crawl(self, monkeypatch):
        monkeypatch.setenv("FIRECRAWL_API_KEY", "")
        adapter = FirecrawlAdapter(api_key="")
        result = await adapter.crawl("https://example.com")
        assert result == []

    async def test_returns_empty_on_map(self, monkeypatch):
        monkeypatch.setenv("FIRECRAWL_API_KEY", "")
        adapter = FirecrawlAdapter(api_key="")
        result = await adapter.map_site("https://example.com")
        assert result == []
