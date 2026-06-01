import asyncio
import logging
from datetime import datetime, timedelta
from typing import Optional

from ingestion.github.client import GitHubMCPClient, resolve_token
from ingestion.github.types import GitHubCommit, GitHubEvent

logger = logging.getLogger(__name__)

DEFAULT_POLL_INTERVAL = 300
MAX_POLL_HISTORY = 50


class GitHubAdapter:
    def __init__(self, repo: str):
        if "/" not in repo:
            raise ValueError(f"repo must be 'owner/name', got {repo!r}")
        self.owner, self.repo_name = repo.split("/", 1)
        self._known_shas: set[str] = set()

    @property
    def repo(self) -> str:
        return f"{self.owner}/{self.repo_name}"

    async def check_connection(self) -> bool:
        token = resolve_token()
        if not token:
            return False
        try:
            async with GitHubMCPClient() as client:
                tools = await client.list_tools()
                return len(tools) > 0
        except Exception as e:
            logger.warning("GitHub MCP connection check failed: %s", e)
            return False

    async def get_me(self) -> dict:
        async with GitHubMCPClient() as client:
            return await client.call_tool("get_me", {})

    async def get_latest_commits(self, limit: int = 10) -> list[GitHubEvent]:
        async with GitHubMCPClient() as client:
            raw = await client.call_tool("list_commits", {
                "owner": self.owner,
                "repo": self.repo_name,
                "limit": limit,
            })
            if not isinstance(raw, list):
                logger.warning("list_commits returned non-list: %s", type(raw))
                return []
            events = []
            for item in raw:
                sha = item.get("sha", "")
                detail = await client.call_tool("get_commit", {
                    "owner": self.owner,
                    "repo": self.repo_name,
                    "sha": sha,
                    "include_diff": True,
                })
                commit = GitHubCommit.from_mcp(detail)
                events.append(GitHubEvent(
                    event_type="commit",
                    repo=self.repo,
                    payload=commit,
                    raw=detail,
                ))
            return events

    async def get_commit(self, sha: str) -> Optional[GitHubEvent]:
        try:
            async with GitHubMCPClient() as client:
                detail = await client.call_tool("get_commit", {
                    "owner": self.owner,
                    "repo": self.repo_name,
                    "sha": sha,
                    "include_diff": True,
                })
            commit = GitHubCommit.from_mcp(detail)
            return GitHubEvent(
                event_type="commit",
                repo=self.repo,
                payload=commit,
                raw=detail,
            )
        except Exception as e:
            logger.error("Failed to get commit %s: %s", sha, e)
            return None

    async def poll(
        self,
        interval: int = DEFAULT_POLL_INTERVAL,
        on_event=None,
        max_history: int = MAX_POLL_HISTORY,
    ):
        last_check = datetime.utcnow()
        logger.info("Starting poll on %s every %ds", self.repo, interval)

        while True:
            try:
                events = await self.get_latest_commits(limit=10)
                new_events = [e for e in events if e.payload.sha not in self._known_shas]
                self._known_shas.update(e.payload.sha for e in new_events)
                if len(self._known_shas) > max_history:
                    self._known_shas = set(list(self._known_shas)[-max_history:])

                for event in reversed(new_events):
                    shipment = event.to_shipment()
                    logger.info(
                        "New commit: %s %s",
                        event.payload.sha[:8],
                        event.payload.message.split("\n")[0],
                    )
                    if on_event:
                        await on_event(shipment)

            except Exception as e:
                logger.error("Poll error: %s", e)

            elapsed = (datetime.utcnow() - last_check).total_seconds()
            sleep_for = max(0, interval - elapsed)
            await asyncio.sleep(sleep_for)
            last_check = datetime.utcnow()
