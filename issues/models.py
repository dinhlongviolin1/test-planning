"""Data models for GitHub issues."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Issue:
    """Represents a GitHub issue.

    Attributes:
        number: The issue number.
        title: The issue title.
        state: The issue state (open or closed).
        created_at: When the issue was created.
        updated_at: When the issue was last updated.
        closed_at: When the issue was closed (None if open).
        body: The issue body/description.
        html_url: The HTML URL of the issue.
        user_login: The login of the user who created the issue.
        labels: List of label names on the issue.
        assignees: List of assignee logins.
        comments_count: Number of comments on the issue.
    """

    number: int
    title: str
    state: str
    created_at: datetime
    updated_at: datetime
    closed_at: Optional[datetime]
    body: Optional[str]
    html_url: str
    user_login: str
    labels: list[str]
    assignees: list[str]
    comments_count: int

    @classmethod
    def from_github_api(cls, data: dict) -> "Issue":
        """Create an Issue from GitHub API response data.

        Args:
            data: The JSON data from the GitHub API.

        Returns:
            A new Issue instance.
        """
        return cls(
            number=data.get("number", 0),
            title=data.get("title", ""),
            state=data.get("state", "open"),
            created_at=datetime.fromisoformat(
                data.get("created_at", "").replace("Z", "+00:00")
            ),
            updated_at=datetime.fromisoformat(
                data.get("updated_at", "").replace("Z", "+00:00")
            ),
            closed_at=(
                datetime.fromisoformat(data["closed_at"].replace("Z", "+00:00"))
                if data.get("closed_at")
                else None
            ),
            body=data.get("body"),
            html_url=data.get("html_url", ""),
            user_login=data.get("user", {}).get("login", ""),
            labels=[label["name"] for label in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            comments_count=data.get("comments", 0),
        )