"""Playwright adapter — full browser automation with HTML-to-markdown output.

Best for: interactive pages, login flows, multi-step documentation navigation.
Runs a local Chromium browser via Playwright library.
"""

import logging
from urllib.parse import urljoin, urlparse

import html2text
from playwright.async_api import async_playwright

from ingestion.web.adapter import WebAdapter, WebContent, WebSearchResult

logger = logging.getLogger(__name__)

_converter = html2text.HTML2Text()
_converter.body_width = 0
_converter.ignore_links = False
_converter.ignore_images = False
_converter.ignore_emphasis = False


def _html_to_markdown(html: str) -> str:
    return _converter.handle(html).strip()


def _is_same_domain(base: str, href: str) -> bool:
    base_domain = urlparse(base).netloc
    target_domain = urlparse(href).netloc
    if not target_domain:
        return True
    return base_domain == target_domain


def _resolve_urls(base: str, hrefs: list[str]) -> list[str]:
    resolved = set()
    for href in hrefs:
        full = urljoin(base, href)
        parsed = urlparse(full)
        if parsed.scheme in ("http", "https") and full not in resolved:
            resolved.add(full)
    return list(resolved)


class PlaywrightAdapter(WebAdapter):

    def __init__(self, headless: bool = True, timeout: int = 30):
        self.headless = headless
        self.timeout = timeout * 1000

    async def _scrape_page(self, url: str) -> WebContent:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=self.headless)
            try:
                page = await browser.new_page()
                await page.goto(url, timeout=self.timeout, wait_until="domcontentloaded")
                title = await page.title()
                html = await page.inner_html("body")
                markdown = _html_to_markdown(html)
                return WebContent(
                    url=url,
                    markdown=markdown,
                    title=title,
                )
            except Exception as e:
                logger.warning("Playwright scrape failed for %s: %s", url, e)
                return WebContent(url=url, markdown="")
            finally:
                await browser.close()

    async def scrape(self, url: str, format: str = "markdown") -> WebContent:
        return await self._scrape_page(url)

    async def crawl(self, url: str, max_pages: int = 50) -> list[WebContent]:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=self.headless)
            try:
                page = await browser.new_page()
                await page.goto(url, timeout=self.timeout, wait_until="domcontentloaded")
                links = await page.eval_on_selector_all(
                    "a[href]", "els => els.map(e => e.href)"
                )
                same_domain = [l for l in links if _is_same_domain(url, l)]
                targets = _resolve_urls(url, same_domain)[:max_pages]
            except Exception as e:
                logger.warning("Playwright crawl failed at %s: %s", url, e)
                return []
            finally:
                await browser.close()

        results = [await self._scrape_page(url)]
        for target in targets:
            if len(results) >= max_pages:
                break
            content = await self._scrape_page(target)
            if content.markdown:
                results.append(content)
        return results

    async def map_site(self, url: str) -> list[str]:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=self.headless)
            try:
                page = await browser.new_page()
                await page.goto(url, timeout=self.timeout, wait_until="domcontentloaded")
                links = await page.eval_on_selector_all(
                    "a[href]", "els => els.map(e => e.href)"
                )
                same_domain = [l for l in links if _is_same_domain(url, l)]
                return _resolve_urls(url, same_domain)
            except Exception as e:
                logger.warning("Playwright map_site failed at %s: %s", url, e)
                return []
            finally:
                await browser.close()

    async def search(self, query: str, max_results: int = 10) -> WebSearchResult:
        logger.warning("Playwright search not implemented — use FirecrawlAdapter")
        return WebSearchResult(query=query)

    async def extract(self, url: str, schema: dict) -> dict:
        content = await self._scrape_page(url)
        result = {"markdown": content.markdown, "title": content.title}
        return result

    async def interact(self, url: str, actions: list[dict]) -> WebContent:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=self.headless)
            try:
                page = await browser.new_page()
                await page.goto(url, timeout=self.timeout, wait_until="domcontentloaded")

                for action in actions:
                    action_type = action.get("type", "")
                    try:
                        if action_type == "click":
                            await page.click(action["selector"])
                            await page.wait_for_timeout(500)
                        elif action_type == "fill":
                            await page.fill(action["selector"], action["value"])
                        elif action_type == "select":
                            await page.select_option(action["selector"], action["value"])
                        elif action_type == "wait":
                            await page.wait_for_timeout(action.get("ms", 1000))
                        elif action_type == "scroll":
                            await page.evaluate("window.scrollBy(0, window.innerHeight)")
                            await page.wait_for_timeout(300)
                    except Exception as e:
                        logger.warning("Playwright action %s failed: %s", action_type, e)

                title = await page.title()
                html = await page.inner_html("body")
                markdown = _html_to_markdown(html)
                return WebContent(
                    url=url,
                    markdown=markdown,
                    title=title,
                )
            except Exception as e:
                logger.warning("Playwright interact failed at %s: %s", url, e)
                return WebContent(url=url, markdown="")
            finally:
                await browser.close()
