"""Tests for FastAPI ingestion endpoints via TestClient."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def mock_scraper():
    """Mock the global scraper instance in the router to avoid real calls."""
    with patch("src.routers.ingestion.scraper") as mock:
        mock.scrape = AsyncMock(return_value=MagicMock(
            url="https://example.com",
            markdown="# Test content",
            title="Test Page",
            description="A test",
            metadata={"source": "test"},
        ))
        mock.crawl = AsyncMock(return_value=[
            MagicMock(url="https://example.com/p1", markdown="# Page 1", title="Page 1"),
        ])
        mock.map_site = AsyncMock(return_value=[
            "https://example.com",
            "https://example.com/about",
        ])
        mock.search = AsyncMock(return_value=MagicMock(
            query="test",
            results=[{"url": "https://a.com", "title": "A", "markdown": "# A"}],
            total_results=1,
        ))
        mock.extract = AsyncMock(return_value={"name": "test", "price": 100})
        mock.interact = AsyncMock(return_value=MagicMock(
            url="https://example.com",
            markdown="# After interaction",
            title="Interacted",
            metadata={"actions": 3},
        ))
        yield mock


class TestScrapeEndpoint:

    def test_scrape_returns_200(self, client):
        resp = client.post("/ingest/web/scrape", json={"url": "https://example.com"})
        assert resp.status_code == 200

    def test_scrape_returns_markdown(self, client):
        resp = client.post("/ingest/web/scrape", json={"url": "https://example.com"})
        assert resp.json()["markdown"] == "# Test content"

    def test_scrape_returns_title(self, client):
        resp = client.post("/ingest/web/scrape", json={"url": "https://example.com"})
        assert resp.json()["title"] == "Test Page"

    def test_scrape_with_prefer(self, client):
        resp = client.post("/ingest/web/scrape", json={
            "url": "https://example.com",
            "prefer": "playwright",
        })
        assert resp.status_code == 200

    def test_scrape_validates_url_required(self, client):
        resp = client.post("/ingest/web/scrape", json={})
        assert resp.status_code == 422


class TestCrawlEndpoint:

    def test_crawl_returns_200(self, client):
        resp = client.post("/ingest/web/crawl", json={
            "url": "https://example.com",
            "max_pages": 3,
        })
        assert resp.status_code == 200

    def test_crawl_returns_pages(self, client):
        resp = client.post("/ingest/web/crawl", json={"url": "https://example.com"})
        data = resp.json()
        assert len(data["pages"]) == 1
        assert data["pages"][0]["title"] == "Page 1"


class TestMapEndpoint:

    def test_map_returns_200(self, client):
        resp = client.post("/ingest/web/map", json={"url": "https://example.com"})
        assert resp.status_code == 200

    def test_map_returns_urls(self, client):
        resp = client.post("/ingest/web/map", json={"url": "https://example.com"})
        data = resp.json()
        assert data["count"] == 2
        assert "https://example.com" in data["urls"]


class TestSearchEndpoint:

    def test_search_returns_200(self, client):
        resp = client.post("/ingest/web/search", json={"query": "test", "max_results": 5})
        assert resp.status_code == 200

    def test_search_returns_results(self, client):
        resp = client.post("/ingest/web/search", json={"query": "test"})
        data = resp.json()
        assert data["total"] == 1
        assert data["results"][0]["url"] == "https://a.com"


class TestExtractEndpoint:

    def test_extract_returns_200(self, client):
        resp = client.post("/ingest/web/extract", json={
            "url": "https://example.com",
            "schema": {"type": "object", "properties": {"name": {"type": "string"}}},
        })
        assert resp.status_code == 200

    def test_extract_returns_data(self, client):
        resp = client.post("/ingest/web/extract", json={
            "url": "https://example.com",
            "schema": {"type": "object"},
        })
        assert resp.json()["name"] == "test"


class TestInteractEndpoint:

    def test_interact_returns_200(self, client):
        resp = client.post("/ingest/web/interact", json={
            "url": "https://example.com",
            "actions": [{"type": "click", "selector": "#btn"}],
        })
        assert resp.status_code == 200

    def test_interact_returns_content(self, client):
        resp = client.post("/ingest/web/interact", json={
            "url": "https://example.com",
            "actions": [{"type": "wait", "ms": 500}],
        })
        assert resp.json()["markdown"] == "# After interaction"
