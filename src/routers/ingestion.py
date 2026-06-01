"""FastAPI router for web ingestion endpoints.

Uses the ScraperRouter to intelligently pick between Firecrawl and Playwright.
Pass `prefer="firecrawl"` or `prefer="playwright"` to force a specific tool.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ingestion.web.scraper import ScraperRouter

router = APIRouter(prefix="/ingest/web", tags=["web-ingestion"])

scraper = ScraperRouter()


class ScrapeRequest(BaseModel):
    url: str
    prefer: str = ""             # "firecrawl", "playwright", or "" for auto
    format: str = "markdown"


class CrawlRequest(BaseModel):
    url: str
    max_pages: int = 50


class MapRequest(BaseModel):
    url: str


class SearchRequest(BaseModel):
    query: str
    max_results: int = 10


class ExtractRequest(BaseModel):
    url: str
    schema: dict


class InteractRequest(BaseModel):
    url: str
    actions: list[dict]


@router.post("/scrape")
async def scrape(request: ScrapeRequest):
    kwargs = {"url": request.url, "format": request.format}
    if request.prefer:
        kwargs["prefer"] = request.prefer
    content = await scraper.scrape(**kwargs)
    return {
        "url": content.url,
        "title": content.title,
        "markdown": content.markdown,
        "metadata": content.metadata,
    }


@router.post("/crawl")
async def crawl(request: CrawlRequest):
    pages = await scraper.crawl(request.url, request.max_pages)
    return {
        "pages": [
            {"url": p.url, "title": p.title, "markdown": p.markdown}
            for p in pages
        ]
    }


@router.post("/map")
async def map_site(request: MapRequest):
    urls = await scraper.map_site(request.url)
    return {"urls": urls, "count": len(urls)}


@router.post("/search")
async def search(request: SearchRequest):
    result = await scraper.search(request.query, request.max_results)
    return {"query": result.query, "results": result.results, "total": result.total_results}


@router.post("/extract")
async def extract(request: ExtractRequest):
    data = await scraper.extract(request.url, request.schema)
    return data


@router.post("/interact")
async def interact(request: InteractRequest):
    content = await scraper.interact(request.url, request.actions)
    return {
        "url": content.url,
        "markdown": content.markdown,
        "metadata": content.metadata,
    }
