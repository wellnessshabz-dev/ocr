"""Tests for ScraperRouter URL routing and quality check logic."""

import pytest
from ingestion.web.adapter import WebContent
from ingestion.web.scraper import ScraperRouter


@pytest.fixture
def router():
    return ScraperRouter()


class TestRouting:

    def test_docs_subdomain_routes_to_firecrawl(self, router):
        assert router._route("https://docs.python.org/3/") == "firecrawl"

    def test_readthedocs_routes_to_firecrawl(self, router):
        assert router._route("https://fastapi.readthedocs.io/") == "firecrawl"

    def test_developer_subdomain_routes_to_firecrawl(self, router):
        assert router._route("https://developer.mozilla.org/") == "firecrawl"

    def test_wikipedia_routes_to_firecrawl(self, router):
        assert router._route("https://en.wikipedia.org/wiki/Python") == "firecrawl"

    def test_github_blob_routes_to_firecrawl(self, router):
        assert router._route("https://github.com/user/repo/blob/main/file.py") == "firecrawl"

    def test_github_wiki_routes_to_firecrawl(self, router):
        assert router._route("https://github.com/user/repo/wiki") == "firecrawl"

    def test_stackoverflow_routes_to_playwright(self, router):
        assert router._route("https://stackoverflow.com/questions/123") == "playwright"

    def test_reddit_routes_to_playwright(self, router):
        assert router._route("https://www.reddit.com/r/python/") == "playwright"

    def test_twitter_routes_to_playwright(self, router):
        assert router._route("https://twitter.com/user") == "playwright"

    def test_xcom_routes_to_playwright(self, router):
        assert router._route("https://x.com/user") == "playwright"

    def test_youtube_routes_to_playwright(self, router):
        assert router._route("https://youtube.com/watch?v=abc") == "playwright"

    def test_medium_routes_to_firecrawl(self, router):
        assert router._route("https://medium.com/article") == "firecrawl"

    def test_devto_routes_to_firecrawl(self, router):
        assert router._route("https://dev.to/article") == "firecrawl"

    def test_docs_path_routes_to_firecrawl(self, router):
        assert router._route("https://example.com/docs/guide") == "firecrawl"

    def test_api_path_routes_to_firecrawl(self, router):
        assert router._route("https://example.com/api/v1") == "firecrawl"

    def test_unknown_site_defaults_to_firecrawl(self, router):
        assert router._route("https://random-site-123.com/page") == "firecrawl"

    def test_ip_address_defaults_to_firecrawl(self, router):
        assert router._route("https://192.168.1.1/") == "firecrawl"

    def test_pypi_routes_to_playwright(self, router):
        assert router._route("https://pypi.org/project/fastapi/") == "playwright"

    def test_npmjs_routes_to_playwright(self, router):
        assert router._route("https://www.npmjs.com/package/express") == "playwright"

    def test_case_insensitive_routing(self, router):
        assert router._route("https://STACKOVERFLOW.COM/q/1") == "playwright"

    def test_blog_path_routes_to_firecrawl(self, router):
        assert router._route("https://example.com/blog/post") == "firecrawl"

    def test_tutorial_path_routes_to_firecrawl(self, router):
        assert router._route("https://example.com/tutorial/getting-started") == "firecrawl"


class TestQualityCheck:

    def test_good_content_passes(self, router):
        content = WebContent(
            url="https://example.com",
            markdown="# Real Article\n\nThis is a real page with useful content about programming. "
                      "It has multiple paragraphs and enough detail to be valuable. "
                      "We need at least 100 characters for a quality check pass. "
                      "This should definitely pass the quality check now.",
        )
        assert router._quality_check(content) is True

    def test_short_content_fails(self, router):
        content = WebContent(url="https://example.com", markdown="Short")
        assert router._quality_check(content) is False

    def test_blocked_javascript_pattern_fails(self, router):
        content = WebContent(
            url="https://example.com",
            markdown="Please enable JavaScript to continue. This site requires JS.",
        )
        assert router._quality_check(content) is False

    def test_blocked_login_pattern_fails(self, router):
        content = WebContent(
            url="https://example.com",
            markdown="Sign in to continue viewing this content.",
        )
        assert router._quality_check(content) is False

    def test_blocked_captcha_pattern_fails(self, router):
        content = WebContent(url="https://example.com", markdown="captcha verification required")
        assert router._quality_check(content) is False

    def test_blocked_access_denied_fails(self, router):
        content = WebContent(url="https://example.com", markdown="Access Denied. 403 Forbidden.")
        assert router._quality_check(content) is False

    def test_boilerplate_only_fails(self, router):
        content = WebContent(
            url="https://example.com",
            markdown="Cookie settings Privacy policy Terms of service Accept cookies "
                      "Subscribe to our newsletter Sign up for free Navigation Menu Footer",
        )
        assert router._quality_check(content) is False

    def test_empty_content_fails(self, router):
        content = WebContent(url="https://example.com", markdown="")
        assert router._quality_check(content) is False

    def test_exactly_min_chars_passes(self, router):
        text = "x" * 100
        content = WebContent(url="https://example.com", markdown=text)
        assert router._quality_check(content) is True

    def test_just_below_min_chars_fails(self, router):
        text = "x" * 99
        content = WebContent(url="https://example.com", markdown=text)
        assert router._quality_check(content) is False
