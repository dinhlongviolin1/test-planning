"""
Get all issues from a GitHub repository.

This script fetches all issues (open and closed) from a GitHub repository
using the GitHub REST API.
"""

import os
import sys
import requests
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class GitHubEpic:
    """Represents a GitHub Epic."""
    number: int
    title: str
    state: str
    body: str
    html_url: str
    user_login: str
    created_at: str
    updated_at: str
    closed_at: Optional[str]
    labels: List[str]
    start_date: Optional[str]
    due_date: Optional[str]
    id: int

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "number": self.number,
            "title": self.title,
            "state": self.state,
            "body": self.body,
            "html_url": self.html_url,
            "user_login": self.user_login,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "closed_at": self.closed_at,
            "labels": self.labels,
            "start_date": self.start_date,
            "due_date": self.due_date,
            "id": self.id
        }


@dataclass
class GitHubIssue:
    """Represents a GitHub issue."""
    number: int
    title: str
    state: str
    body: str
    html_url: str
    user_login: str
    user_type: str
    created_at: str
    updated_at: str
    closed_at: Optional[str]
    labels: List[str]
    assignees: List[str]
    comments: int
    id: int

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "number": self.number,
            "title": self.title,
            "state": self.state,
            "body": self.body,
            "html_url": self.html_url,
            "user_login": self.user_login,
            "user_type": self.user_type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "closed_at": self.closed_at,
            "labels": self.labels,
            "assignees": self.assignees,
            "comments": self.comments,
            "id": self.id
        }


def get_github_api_url() -> str:
    """Get the GitHub API base URL."""
    return "https://api.github.com"


def get_repo_owner_repo() -> tuple:
    """
    Get the repository owner and name from environment or arguments.

    Expected format: owner/repo (e.g., "dinhlongviolin1/test-planning")
    """
    repo = os.environ.get("GITHUB_REPOSITORY", "dinhlongviolin1/test-planning")
    if "/" not in repo:
        raise ValueError(f"Invalid repository format: {repo}. Expected 'owner/repo'")
    owner, repo_name = repo.split("/", 1)
    return owner, repo_name


def get_auth_token() -> Optional[str]:
    """Get GitHub auth token from environment."""
    return os.environ.get("GITHUB_TOKEN")


def make_request(url: str, params: Optional[dict] = None) -> Optional[requests.Response]:
    """
    Make an authenticated request to GitHub API.

    Args:
        url: The API endpoint URL
        params: Optional query parameters

    Returns:
        Response object or None if request failed
    """
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "GitHub-Issue-Fetcher/1.0"
    }

    token = get_auth_token()
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        return None


def get_all_issues(owner: str, repo_name: str, state: str = "all") -> List[GitHubIssue]:
    """
    Get all issues for a repository.

    Args:
        owner: Repository owner
        repo_name: Repository name
        state: Issue state: "open", "closed", or "all"

    Returns:
        List of GitHubIssue objects
    """
    issues = []
    page = 1
    per_page = 100

    while True:
        url = f"{get_github_api_url()}/repos/{owner}/{repo_name}/issues"
        params = {
            "per_page": per_page,
            "page": page,
            "state": state,
            "sort": "created",
            "direction": "asc"
        }

        response = make_request(url, params)
        if response is None:
            break

        data = response.json()
        if not data:
            break

        for item in data:
            # Skip pull requests (GitHub API returns PRs in issues endpoint)
            if item.get("pull_request") is not None:
                continue

            issue = GitHubIssue(
                number=item.get("number", 0),
                title=item.get("title", ""),
                state=item.get("state", "open"),
                body=item.get("body", "") or "",
                html_url=item.get("html_url", ""),
                user_login=item.get("user", {}).get("login", "") if item.get("user") else "",
                user_type=item.get("user", {}).get("type", "User") if item.get("user") else "User",
                created_at=item.get("created_at", ""),
                updated_at=item.get("updated_at", ""),
                closed_at=item.get("closed_at"),
                labels=[label.get("name", "") for label in item.get("labels", [])],
                assignees=[a.get("login", "") for a in item.get("assignees", [])],
                comments=item.get("comments", 0),
                id=item.get("id", 0)
            )
            issues.append(issue)

        if len(data) < per_page:
            break
        page += 1

    return issues


def get_all_epics(owner: str, repo_name: str, state: str = "all") -> List[GitHubEpic]:
    """
    Get all epics for a repository.

    Args:
        owner: Repository owner
        repo_name: Repository name
        state: Epic state: "open", "closed", or "all"

    Returns:
        List of GitHubEpic objects
    """
    epics = []
    page = 1
    per_page = 100

    while True:
        url = f"{get_github_api_url()}/repos/{owner}/{repo_name}/issues"
        params = {
            "per_page": per_page,
            "page": page,
            "state": state,
            "sort": "created",
            "direction": "asc",
            "creator": "all"
        }

        response = make_request(url, params)
        if response is None:
            break

        data = response.json()
        if not data:
            break

        for item in data:
            # Only process items that have the epic label (GitHub uses labels to identify epics)
            labels = [label.get("name", "") for label in item.get("labels", [])]
            is_epic = any("Epic:" in label for label in labels)

            if not is_epic:
                continue

            epic = GitHubEpic(
                number=item.get("number", 0),
                title=item.get("title", ""),
                state=item.get("state", "open"),
                body=item.get("body", "") or "",
                html_url=item.get("html_url", ""),
                user_login=item.get("user", {}).get("login", "") if item.get("user") else "",
                created_at=item.get("created_at", ""),
                updated_at=item.get("updated_at", ""),
                closed_at=item.get("closed_at"),
                labels=labels,
                start_date=item.get("start_date"),
                due_date=item.get("due_date"),
                id=item.get("id", 0)
            )
            epics.append(epic)

        if len(data) < per_page:
            break
        page += 1

    return epics


def get_issue_counts(owner: str, repo_name: str) -> dict:
    """
    Get the count of open and closed issues.

    Args:
        owner: Repository owner
        repo_name: Repository name

    Returns:
        Dictionary with open_count and closed_count
    """
    url = f"{get_github_api_url()}/repos/{owner}/{repo_name}"

    response = make_request(url)
    if response is None:
        return {"open_issues": 0, "closed_issues": 0}

    data = response.json()
    return {
        "open_issues": data.get("open_issues_count", 0)
    }


def print_issues(issues: List[GitHubIssue], title: str):
    """Print issues in a formatted table."""
    print(f"\n{'=' * 80}")
    print(f"{title}")
    print(f"{'=' * 80}")
    print(f"{'#':<6} {'State':<10} {'Title':<40} {'Labels':<15}")
    print(f"{'-' * 80}")

    for issue in issues:
        truncated_title = issue.title[:37] + "..." if len(issue.title) > 40 else issue.title
        labels_str = ",".join(issue.labels[:3])
        if len(",".join(issue.labels)) > 15:
            labels_str = labels_str[:12] + "..."
        state_indicator = "[OPEN]" if issue.state == "open" else "[CLOSED]"
        print(f"#{issue.number:<5} {state_indicator:<10} {truncated_title:<40} {labels_str:<15}")

    print(f"{'=' * 80}")
    print(f"Total: {len(issues)}\n")


def print_epics(epics: List[GitHubEpic], title: str):
    """Print epics in a formatted table."""
    print(f"\n{'=' * 80}")
    print(f"{title}")
    print(f"{'=' * 80}")
    print(f"{'#':<6} {'State':<10} {'Title':<40} {'Due Date':<15}")
    print(f"{'-' * 80}")

    for epic in epics:
        truncated_title = epic.title[:37] + "..." if len(epic.title) > 40 else epic.title
        due_date = epic.due_date if epic.due_date else "N/A"
        state_indicator = "[OPEN]" if epic.state == "open" else "[CLOSED]"
        print(f"#{epic.number:<5} {state_indicator:<10} {truncated_title:<40} {due_date:<15}")

    print(f"{'=' * 80}")
    print(f"Total: {len(epics)}\n")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Get all issues or epics from a GitHub repository",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--repo", "-r",
        default=os.environ.get("GITHUB_REPOSITORY", "dinhlongviolin1/test-planning"),
        help="Repository in 'owner/repo' format (default: dinhlongviolin1/test-planning)"
    )
    parser.add_argument(
        "--state", "-s",
        choices=["open", "closed", "all"],
        default="all",
        help="Issue/Epic state filter (default: all)"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON"
    )
    parser.add_argument(
        "--token", "-t",
        default=os.environ.get("GITHUB_TOKEN", ""),
        help="GitHub API token (or set GITHUB_TOKEN env var)"
    )
    parser.add_argument(
        "--epics", "-e",
        action="store_true",
        help="Fetch epics instead of issues"
    )

    args = parser.parse_args()

    # Parse repo
    if "/" not in args.repo:
        parser.error(f"Invalid repository format: {args.repo}. Expected 'owner/repo'")
    owner, repo_name = args.repo.split("/", 1)

    # Set token if provided
    if args.token:
        os.environ["GITHUB_TOKEN"] = args.token

    if args.epics:
        epics = get_all_epics(owner, repo_name, args.state)
        if args.json:
            import json
            result = {
                "repository": f"{owner}/{repo_name}",
                "state_filter": args.state,
                "total_count": len(epics),
                "epics": [epic.to_dict() for epic in epics]
            }
            print(json.dumps(result, indent=2))
        else:
            state_title = {
                "open": "Open Epics",
                "closed": "Closed Epics",
                "all": "All Epics (Open and Closed)"
            }
            print_epics(epics, f"{owner}/{repo_name} - {state_title[args.state]}")
    else:
        issues = get_all_issues(owner, repo_name, args.state)
        if args.json:
            import json
            result = {
                "repository": f"{owner}/{repo_name}",
                "state_filter": args.state,
                "total_count": len(issues),
                "issues": [issue.to_dict() for issue in issues]
            }
            print(json.dumps(result, indent=2))
        else:
            state_title = {
                "open": "Open Issues",
                "closed": "Closed Issues",
                "all": "All Issues (Open and Closed)"
            }
            print_issues(issues, f"{owner}/{repo_name} - {state_title[args.state]}")


if __name__ == "__main__":
    main()