"""Tests for PlaywrightAdapter — mocks playwright browser."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from ingestion.web.adapter import WebContent
from ingestion.web.playwright import PlaywrightAdapter, _html_to_markdown, _is_same_domain, _resolve_urls


class TestHtmlToMarkdown:

    def test_converts_simple_html(self):
        result = _html_to_markdown("<h1>Title</h1><p>Paragraph.</p>")
        assert "Title" in result
        assert "Paragraph" in result

    def test_handles_empty_string(self):
        assert _html_to_markdown("") == ""

    def test_converts_links(self):
        result = _html_to_markdown('<a href="https://example.com">click</a>')
        assert "click" in result
        assert "example.com" in result


class TestIsSameDomain:

    def test_same_domain_returns_true(self):
        assert _is_same_domain("https://example.com/page", "https://example.com/other") is True

    def test_different_domain_returns_false(self):
        assert _is_same_domain("https://example.com", "https://other.com") is False

    def test_relative_url_returns_true(self):
        assert _is_same_domain("https://example.com", "/page") is True

    def test_subdomain_different_domain(self):
        assert _is_same_domain("https://example.com", "https://sub.example.com") is False


class TestResolveUrls:

    def test_resolves_relative_paths(self):
        result = _resolve_urls("https://example.com/base", ["/page1", "/page2"])
        assert "https://example.com/page1" in result
        assert "https://example.com/page2" in result

    def test_deduplicates(self):
        result = _resolve_urls("https://example.com", ["/page", "/page"])
        assert len(result) == 1

    def test_keeps_absolute_urls(self):
        result = _resolve_urls("https://example.com", ["https://other.com/page"])
        assert "https://other.com/page" in result

    def test_filters_non_http(self):
        result = _resolve_urls("https://example.com", ["mailto:test@example.com"])
        assert result == []


class TestAdapterWithMocks:

    async def test_scrape_returns_webcontent(self, mock_playwright):
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.scrape("https://example.com")
            assert isinstance(result, WebContent)

    async def test_scrape_returns_markdown(self, mock_playwright):
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.scrape("https://example.com")
            assert "Hello from Playwright" in result.markdown

    async def test_scrape_returns_title(self, mock_playwright):
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.scrape("https://example.com")
            assert result.title == "Test Page"

    async def test_scrape_handles_navigation_error(self, mock_playwright_page, mock_playwright_browser, mock_playwright):
        mock_playwright_page.goto.side_effect = Exception("Timeout")
        mock_playwright_browser.new_page.return_value = mock_playwright_page
        mock_playwright.chromium.launch.return_value = mock_playwright_browser
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.scrape("https://example.com")
            assert result.markdown == ""

    async def test_scrape_handles_inner_html_error(self, mock_playwright_page, mock_playwright_browser, mock_playwright):
        mock_playwright_page.inner_html.side_effect = Exception("DOM error")
        mock_playwright_browser.new_page.return_value = mock_playwright_page
        mock_playwright.chromium.launch.return_value = mock_playwright_browser
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.scrape("https://example.com")
            assert result.markdown == ""

    async def test_search_returns_empty(self, mock_playwright):
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter()
            result = await adapter.search("test")
            assert result.total_results == 0

    async def test_extract_returns_markdown(self, mock_playwright):
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.extract("https://example.com", {})
            assert "markdown" in result
            assert "title" in result

    async def test_interact_performs_actions(self, mock_playwright_page, mock_playwright_browser, mock_playwright):
        mock_playwright_browser.new_page.return_value = mock_playwright_page
        mock_playwright.chromium.launch.return_value = mock_playwright_browser
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            actions = [
                {"type": "click", "selector": "#btn"},
                {"type": "fill", "selector": "#input", "value": "hello"},
                {"type": "wait", "ms": 500},
                {"type": "scroll"},
            ]
            result = await adapter.interact("https://example.com", actions)
            assert isinstance(result, WebContent)
            mock_playwright_page.click.assert_called_once_with("#btn")
            mock_playwright_page.fill.assert_called_once_with("#input", "hello")

    async def test_interact_handles_action_failure(self, mock_playwright_page, mock_playwright_browser, mock_playwright):
        mock_playwright_page.click.side_effect = Exception("Click failed")
        mock_playwright_browser.new_page.return_value = mock_playwright_page
        mock_playwright.chromium.launch.return_value = mock_playwright_browser
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.interact("https://example.com", [{"type": "click", "selector": "#btn"}])
            assert result.markdown != ""

    async def test_map_site_returns_urls(self, mock_playwright):
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.map_site("https://example.com")
            assert len(result) > 0
            assert "https://example.com/page1" in result

    async def test_map_site_filters_external_domains(self, mock_playwright_page, mock_playwright_browser, mock_playwright):
        mock_playwright_page.eval_on_selector_all.return_value = [
            "https://example.com/page1",
            "https://other.com/page",
        ]
        mock_playwright_browser.new_page.return_value = mock_playwright_page
        mock_playwright.chromium.launch.return_value = mock_playwright_browser
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.map_site("https://example.com")
            assert "https://other.com/page" not in result

    async def test_crawl_returns_pages(self, mock_playwright):
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.crawl("https://example.com", max_pages=3)
            assert len(result) >= 1
            assert all(isinstance(p, WebContent) for p in result)

    async def test_crawl_handles_discovery_failure(self, mock_playwright_page, mock_playwright_browser, mock_playwright):
        mock_playwright_page.goto.side_effect = Exception("Nav failed")
        mock_playwright_browser.new_page.return_value = mock_playwright_page
        mock_playwright.chromium.launch.return_value = mock_playwright_browser
        with patch("ingestion.web.playwright.async_playwright") as mock_pw:
            mock_pw.return_value.__aenter__.return_value = mock_playwright
            adapter = PlaywrightAdapter(headless=True, timeout=10)
            result = await adapter.crawl("https://example.com")
            assert result == []
