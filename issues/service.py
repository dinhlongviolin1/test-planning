"""GitHub API service for fetching issues."""

import os
import time
from typing import Optional

import requests

from issues.models import Issue


class GitHubAPIError(Exception):
    """Base exception for GitHub API errors."""

    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.status_code = status_code


class RateLimitError(GitHubAPIError):
    """Exception raised when API rate limit is exceeded."""

    def __init__(self, reset_time: Optional[int] = None):
        message = "GitHub API rate limit exceeded"
        if reset_time:
            message += f". Retry after {reset_time} seconds"
        super().__init__(message)
        self.reset_time = reset_time


class GitHubService:
    """Service for interacting with the GitHub API."""

    BASE_URL = "https://api.github.com"

    def __init__(self, token: Optional[str] = None):
        """Initialize the GitHub service.

        Args:
            token: GitHub personal access token. Falls back to GITHUB_TOKEN env var.
        """
        self.token = token or os.environ.get("GITHUB_TOKEN")
        self.session = requests.Session()
        if self.token:
            self.session.headers["Authorization"] = f"token {self.token}"
        self.session.headers["Accept"] = "application/vnd.github.v3+json"
        self.session.headers["User-Agent"] = "GitHub-Issues-Service"

    def _make_request(
        self, url: str, params: Optional[dict] = None
    ) -> requests.Response:
        """Make an HTTP request to the GitHub API.

        Args:
            url: The API endpoint URL.
            params: Query parameters.

        Returns:
            The HTTP response.

        Raises:
            RateLimitError: When rate limit is exceeded.
            GitHubAPIError: When the API returns an error.
        """
        response = self.session.get(url, params=params)

        if response.status_code == 403:
            # Check if it's a rate limit error
            reset_time = response.headers.get("X-RateLimit-Reset")
            if reset_time:
                reset_time = int(reset_time)
                wait_time = max(0, reset_time - int(time.time()))
                raise RateLimitError(wait_time)
            raise GitHubAPIError("Forbidden", 403)

        if response.status_code == 401:
            raise GitHubAPIError("Unauthorized - check your GitHub token", 401)

        if response.status_code == 404:
            raise GitHubAPIError("Resource not found", 404)

        if not response.ok:
            raise GitHubAPIError(
                f"GitHub API error: {response.status_code}",
                response.status_code,
            )

        return response

    def _get_paginated(
        self, url: str, params: Optional[dict] = None
    ) -> list[dict]:
        """Fetch all pages from a paginated API endpoint.

        Args:
            url: The API endpoint URL.
            params: Query parameters.

        Returns:
            List of all items from all pages.
        """
        results = []
        page_params = dict(params) if params else {}
        page_params["per_page"] = 100

        while True:
            response = self._make_request(url, params=page_params)
            data = response.json()

            if isinstance(data, list):
                results.extend(data)
            else:
                results.append(data)

            # Check for next page
            if "next" in response.links:
                url = response.links["next"]["url"]
                page_params = None  # URL already has params
            else:
                break

        return results

    def get_issues(
        self, owner: str, repo: str, state: str = "all"
    ) -> list[Issue]:
        """Fetch all issues from a repository.

        Args:
            owner: Repository owner.
            repo: Repository name.
            state: Issue state filter ("open", "closed", or "all").

        Returns:
            List of Issue objects.

        Raises:
            ValueError: When state is invalid.
            GitHubAPIError: When the API returns an error.
            RateLimitError: When rate limit is exceeded.
        """
        if state not in ("open", "closed", "all"):
            raise ValueError("state must be 'open', 'closed', or 'all'")

        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues"
        params = {"state": state, "sort": "created", "direction": "desc"}

        raw_issues = self._get_paginated(url, params)
        return [Issue.from_github_api(data) for data in raw_issues]

    def get_issue(self, owner: str, repo: str, issue_number: int) -> Issue:
        """Fetch a single issue from a repository.

        Args:
            owner: Repository owner.
            repo: Repository name.
            issue_number: The issue number.

        Returns:
            An Issue object.

        Raises:
            GitHubAPIError: When the API returns an error.
            RateLimitError: When rate limit is exceeded.
        """
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"
        response = self._make_request(url)
        data = response.json()
        return Issue.from_github_api(data)