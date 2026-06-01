from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class GitHubAuthor:
    login: str
    name: str
    email: str
    profile_url: str = ""

    @classmethod
    def from_mcp(cls, data: dict) -> "GitHubAuthor":
        commit_author = data.get("commit", {}).get("author", {})
        return cls(
            login=data.get("login", ""),
            name=commit_author.get("name", ""),
            email=commit_author.get("email", ""),
            profile_url=data.get("profile_url", ""),
        )


@dataclass
class GitHubCommit:
    sha: str
    message: str
    author: GitHubAuthor
    date: datetime
    html_url: str
    stats: dict = field(default_factory=dict)
    files: list[dict] = field(default_factory=list)
    parent_shas: list[str] = field(default_factory=list)

    @classmethod
    def from_mcp(cls, data: dict) -> "GitHubCommit":
        commit_data = data.get("commit", {})
        author_data = data.get("author", {})
        raw_date = commit_data.get("author", {}).get("date", "")
        parsed_date = datetime.fromisoformat(raw_date.replace("Z", "+00:00")) if raw_date else datetime.utcnow()

        parents = []
        for p in data.get("parents", []):
            if isinstance(p, dict):
                parents.append(p.get("sha", ""))
            elif isinstance(p, str):
                parents.append(p)

        return cls(
            sha=data.get("sha", ""),
            message=commit_data.get("message", ""),
            author=GitHubAuthor(
                login=author_data.get("login", ""),
                name=commit_data.get("author", {}).get("name", ""),
                email=commit_data.get("author", {}).get("email", ""),
                profile_url=author_data.get("profile_url", ""),
            ),
            date=parsed_date,
            html_url=data.get("html_url", ""),
            stats=data.get("stats", {}),
            files=data.get("files", []),
            parent_shas=parents,
        )


@dataclass
class GitHubEvent:
    event_type: str
    repo: str
    payload: GitHubCommit
    raw: dict = field(default_factory=dict)

    def to_shipment(self) -> dict:
        return {
            "id": f"github_commit_{self.payload.sha[:12]}",
            "type": self.event_type,
            "source": "github",
            "repo": self.repo,
            "timestamp": self.payload.date.isoformat(),
            "entities": {
                "components": [f.get("filename", "") for f in self.payload.files],
                "people": [self.payload.author.login],
            },
            "trajectory": {
                "sha": self.payload.sha,
                "message": self.payload.message,
                "stats": self.payload.stats,
                "parent_shas": self.payload.parent_shas,
            },
            "raw": self.raw,
        }
