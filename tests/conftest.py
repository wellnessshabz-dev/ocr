from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from ingestion.web.adapter import WebContent, WebSearchResult


@pytest.fixture
def mock_firecrawl_app():
    """Mock the AsyncV1FirecrawlApp SDK with controlled responses."""
    mock = MagicMock()
    mock.scrape_url = AsyncMock()
    mock.crawl_url = AsyncMock()
    mock.check_crawl_status = AsyncMock()
    mock.map_url = AsyncMock()
    mock.search = AsyncMock()
    return mock


@pytest.fixture
def mock_firecrawl_scrape_response():
    """Simulate a successful Firecrawl scrape_url response."""
    resp = MagicMock()
    resp.success = True
    resp.url = "https://example.com"
    resp.markdown = "# Example\n\nThis is a test page."
    resp.title = "Example Page"
    resp.description = "A test page"
    resp.metadata = {"sourceURL": "https://example.com", "statusCode": 200}
    resp.error = None
    return resp


@pytest.fixture
def mock_firecrawl_crawl_job():
    """Simulate a crawl_url job response."""
    resp = MagicMock()
    resp.success = True
    resp.id = "crawl-job-123"
    resp.error = None
    return resp


@pytest.fixture
def mock_firecrawl_crawl_completed():
    """Simulate a completed crawl status check."""
    resp = MagicMock()
    resp.success = True
    resp.status = "completed"

    page1 = MagicMock()
    page1.url = "https://example.com"
    page1.markdown = "# Page 1"
    page1.title = "Page 1"
    page1.description = ""
    page1.metadata = {}

    page2 = MagicMock()
    page2.url = "https://example.com/page2"
    page2.markdown = "# Page 2"
    page2.title = "Page 2"
    page2.description = ""
    page2.metadata = {}

    resp.data = [page1, page2]
    return resp


@pytest.fixture
def mock_firecrawl_map_response():
    """Simulate a map_url response."""
    resp = MagicMock()
    resp.success = True
    resp.links = [
        "https://example.com",
        "https://example.com/about",
        "https://example.com/contact",
    ]
    resp.error = None
    return resp


@pytest.fixture
def mock_firecrawl_search_response():
    """Simulate a search response."""
    return {
        "success": True,
        "data": [
            {
                "url": "https://example.com",
                "title": "Example",
                "description": "Test page",
                "markdown": "# Example\nContent.",
            },
            {
                "url": "https://example.org",
                "title": "Example Org",
                "description": "Another test",
                "markdown": "# Example Org\nContent.",
            },
        ],
    }


@pytest.fixture
def mock_playwright_page():
    """Mock a Playwright page with controllable content."""
    page = MagicMock()
    page.title = AsyncMock(return_value="Test Page")
    page.goto = AsyncMock()
    page.inner_html = AsyncMock(
        return_value="<h1>Test Page</h1><p>Hello from Playwright.</p>"
    )
    page.click = AsyncMock()
    page.fill = AsyncMock()
    page.select_option = AsyncMock()
    page.wait_for_timeout = AsyncMock()
    page.evaluate = AsyncMock()
    page.eval_on_selector_all = AsyncMock(
        return_value=[
            "https://example.com/page1",
            "https://example.com/page2",
            "https://other.com/",
        ]
    )
    return page


@pytest.fixture
def mock_playwright_browser(mock_playwright_page):
    """Mock a Playwright browser that returns mock pages."""
    browser = MagicMock()
    context = MagicMock()
    context.new_page = AsyncMock(return_value=mock_playwright_page)
    browser.new_page = AsyncMock(return_value=mock_playwright_page)
    browser.close = AsyncMock()
    return browser


@pytest.fixture
def mock_playwright(mock_playwright_browser):
    """Mock async_playwright."""
    pw = MagicMock()
    pw.chromium = MagicMock()
    pw.chromium.launch = AsyncMock(return_value=mock_playwright_browser)
    return pw


@pytest.fixture
def sample_web_content():
    return WebContent(
        url="https://example.com",
        markdown="# Hello\n\nWorld.",
        title="Hello Page",
        description="A hello page",
        metadata={"sourceURL": "https://example.com"},
    )


@pytest.fixture
def sample_search_result():
    return WebSearchResult(
        query="test",
        results=[
            {"url": "https://a.com", "title": "A", "markdown": "# A"},
            {"url": "https://b.com", "title": "B", "markdown": "# B"},
        ],
        total_results=2,
    )
