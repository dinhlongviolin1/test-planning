"""GitHub Report Script.

Fetches and reports on issues and contributors from a GitHub repository.
Uses the GitHub REST API v3 to retrieve data and handles pagination and rate limiting.
"""

from dataclasses import dataclass
from typing import Optional

import requests


REPO_OWNER = "dinhlongviolin1"
REPO_NAME = "test-planning"
BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"


@dataclass
class Issue:
    """Represents a GitHub issue."""

    number: int
    title: str
    state: str
    assignee: Optional[str]


@dataclass
class Contributor:
    """Represents a GitHub contributor."""

    username: str
    contributions: int


def fetch_all_issues() -> list[Issue]:
    """Fetch all issues (open and closed) from the repository.

    Handles pagination to retrieve all issues.

    Returns:
        A list of Issue objects.
    """
    issues: list[Issue] = []
    page = 1
    per_page = 100

    while True:
        params = {"state": "all", "per_page": per_page, "page": page}
        response = requests.get(f"{BASE_URL}/issues", params=params)

        if response.status_code == 403:
            remaining = response.headers.get("X-RateLimit-Remaining", "unknown")
            reset_time = response.headers.get("X-RateLimit-Reset", "unknown")
            print(f"Rate limited. Remaining: {remaining}, Reset: {reset_time}")
            break

        if response.status_code != 200:
            print(f"Error fetching issues: {response.status_code}")
            break

        data = response.json()
        if not data:
            break

        for item in data:
            issue = Issue(
                number=item.get("number", 0),
                title=item.get("title", ""),
                state=item.get("state", ""),
                assignee=item.get("assignee", {}).get("login") if item.get("assignee") else None,
            )
            issues.append(issue)

        page += 1

    return issues


def fetch_all_contributors() -> list[Contributor]:
    """Fetch all contributors from the repository.

    Handles pagination to retrieve all contributors.

    Returns:
        A list of Contributor objects.
    """
    contributors: list[Contributor] = []
    page = 1
    per_page = 100

    while True:
        params = {"per_page": per_page, "page": page}
        response = requests.get(f"{BASE_URL}/contributors", params=params)

        if response.status_code == 403:
            remaining = response.headers.get("X-RateLimit-Remaining", "unknown")
            reset_time = response.headers.get("X-RateLimit-Reset", "unknown")
            print(f"Rate limited. Remaining: {remaining}, Reset: {reset_time}")
            break

        if response.status_code != 200:
            print(f"Error fetching contributors: {response.status_code}")
            break

        data = response.json()
        if not data:
            break

        for item in data:
            contributor = Contributor(
                username=item.get("login", ""),
                contributions=item.get("contributions", 0),
            )
            contributors.append(contributor)

        page += 1

    return contributors


def print_issues_report(issues: list[Issue]) -> None:
    """Print a formatted report of all issues.

    Args:
        issues: A list of Issue objects to report.
    """
    print("\n" + "=" * 80)
    print("ISSUES REPORT")
    print("=" * 80)
    print(f"{'#':<6} {'Title':<50} {'State':<10} {'Assignee'}")
    print("-" * 80)

    for issue in issues:
        title = issue.title[:48] + ".." if len(issue.title) > 50 else issue.title
        assignee = issue.assignee if issue.assignee else "(unassigned)"
        print(f"{issue.number:<6} {title:<50} {issue.state:<10} {assignee}")

    print("-" * 80)
    print(f"Total Issues: {len(issues)}")
    print()


def print_contributors_report(contributors: list[Contributor]) -> None:
    """Print a formatted report of all contributors.

    Args:
        contributors: A list of Contributor objects to report.
    """
    print("\n" + "=" * 80)
    print("CONTRIBUTORS REPORT")
    print("=" * 80)
    print(f"{'Username':<30} {'Contributions'}")
    print("-" * 80)

    for contributor in sorted(contributors, key=lambda c: c.contributions, reverse=True):
        print(f"{contributor.username:<30} {contributor.contributions}")

    print("-" * 80)
    print(f"Total Contributors: {len(contributors)}")
    print()


def main() -> None:
    """Main function to fetch and report GitHub issues and contributors."""
    print(f"Fetching data from {REPO_OWNER}/{REPO_NAME}...")

    issues = fetch_all_issues()
    contributors = fetch_all_contributors()

    print_issues_report(issues)
    print_contributors_report(contributors)


if __name__ == "__main__":
    main()