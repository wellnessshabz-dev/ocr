import json
import logging
import os
import subprocess
from contextlib import AsyncExitStack
from typing import Optional

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

logger = logging.getLogger(__name__)

GITHUB_MCP_SERVER = os.path.expanduser(
    os.environ.get("GITHUB_MCP_SERVER_PATH") or "~/go/bin/github-mcp-server"
)
DEFAULT_TOOLSETS = "repos,context"
TOOLSETS_READONLY = "repos,pull_requests,context,search"


def resolve_token() -> Optional[str]:
    token = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True, text=True, timeout=5,
        )
        if result.returncode == 0:
            token = result.stdout.strip()
            if token:
                return token
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        pass
    logger.warning(
        "No GitHub token found. Set GITHUB_PERSONAL_ACCESS_TOKEN env var "
        "or authenticate with `gh auth login`."
    )
    return None


class GitHubMCPClient:
    """Persistent MCP client that keeps the session open across multiple calls.

    Usage:
        async with GitHubMCPClient() as client:
            commits = await client.call_tool("list_commits", {...})
            details = await client.call_tool("get_commit", {...})
    """

    def __init__(self, toolsets: str = DEFAULT_TOOLSETS):
        self.toolsets = toolsets
        self._session: Optional[ClientSession] = None

    async def __aenter__(self) -> "GitHubMCPClient":
        token = resolve_token()
        if not token:
            raise RuntimeError(
                "Cannot connect to GitHub MCP server: no token available. "
                "Set GITHUB_PERSONAL_ACCESS_TOKEN or run `gh auth login`."
            )
        server_params = StdioServerParameters(
            command=GITHUB_MCP_SERVER,
            args=["stdio", f"--toolsets={self.toolsets}"],
            env={"GITHUB_PERSONAL_ACCESS_TOKEN": token},
        )
        self._stack = AsyncExitStack()
        read, write = await self._stack.enter_async_context(stdio_client(server_params))
        self._session = await self._stack.enter_async_context(ClientSession(read, write))
        await self._session.initialize()
        return self

    async def __aexit__(self, *args) -> None:
        if hasattr(self, "_stack"):
            await self._stack.__aexit__(*args)

    async def call_tool(self, name: str, arguments: dict) -> dict:
        if not self._session:
            raise RuntimeError("Client not connected — use 'async with GitHubMCPClient()'")
        result = await self._session.call_tool(name, arguments)
        text = result.content[0].text if result.content else "{}"
        return json.loads(text)

    async def list_tools(self) -> list[dict]:
        if not self._session:
            raise RuntimeError("Client not connected — use 'async with GitHubMCPClient()'")
        result = await self._session.list_tools()
        return [{"name": t.name, "description": t.description, "inputSchema": t.inputSchema} for t in result.tools]



