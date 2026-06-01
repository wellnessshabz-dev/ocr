"""Tool-agnostic interface for web scraping and browser automation.

Every web backend (Firecrawl, Playwright, etc.) implements this interface.
The runtime never calls a scraping API directly.
"""

from dataclasses import dataclass, field
from typing import Optional
from abc import ABC, abstractmethod
from uuid import UUID, uuid4
from datetime import datetime


@dataclass
class WebContent:
    url: str
    markdown: str
    title: str = ""
    description: str = ""
    metadata: dict = field(default_factory=dict)
    fetched_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class WebSession:
    session_id: UUID = field(default_factory=uuid4)
    tool: str = ""
    url: str = ""
    status: str = "pending"
    pages: list[WebContent] = field(default_factory=list)
    error: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class WebSearchResult:
    query: str
    results: list[dict] = field(default_factory=list)
    total_results: int = 0


class WebAdapter(ABC):

    @abstractmethod
    async def scrape(self, url: str, format: str = "markdown") -> WebContent:
        ...

    @abstractmethod
    async def crawl(self, url: str, max_pages: int = 50) -> list[WebContent]:
        ...

    @abstractmethod
    async def map_site(self, url: str) -> list[str]:
        ...

    @abstractmethod
    async def search(self, query: str, max_results: int = 10) -> WebSearchResult:
        ...

    @abstractmethod
    async def extract(self, url: str, schema: dict) -> dict:
        ...

    @abstractmethod
    async def interact(self, url: str, actions: list[dict]) -> WebContent:
        ...
