#!/usr/bin/env python3
"""
GitHub Issues and Contributors Report

This script fetches all issues and contributors from the GitHub repository
and prints a formatted report.
"""

import requests
import sys
from typing import List, Dict, Optional


REPO_OWNER = "dinhlongviolin1"
REPO_NAME = "test-planning"
BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"


def make_request(url: str, params: Optional[Dict] = None) -> Optional[requests.Response]:
    """
    Make a GET request to the GitHub API with rate limiting handling.

    Args:
        url: The API endpoint URL.
        params: Optional query parameters.

    Returns:
        Response object or None if the request fails.
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            print(f"Rate limit exceeded. Please try again later.", file=sys.stderr)
        elif response.status_code == 404:
            print(f"Resource not found: {url}", file=sys.stderr)
        else:
            print(f"HTTP error: {e}", file=sys.stderr)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        return None


def fetch_all_issues(state: str = "all") -> List[Dict]:
    """
    Fetch all issues (open, closed, or all) from the repository.

    Args:
        state: Issue state - "open", "closed", or "all".

    Returns:
        List of issue dictionaries.
    """
    issues = []
    page = 1
    per_page = 100

    while True:
        url = f"{BASE_URL}/issues"
        params = {"state": state, "per_page": per_page, "page": page}

        response = make_request(url, params)
        if response is None:
            break

        data = response.json()
        if not data:
            break

        issues.extend(data)
        page += 1

        # Safety check for infinite loops
        if page > 100:
            print("Warning: Reached maximum page limit", file=sys.stderr)
            break

    return issues


def fetch_contributors() -> List[Dict]:
    """
    Fetch all contributors from the repository.

    Returns:
        List of contributor dictionaries with username and contribution count.
    """
    contributors = []
    page = 1
    per_page = 100

    while True:
        url = f"{BASE_URL}/contributors"
        params = {"per_page": per_page, "page": page}

        response = make_request(url, params)
        if response is None:
            break

        data = response.json()
        if not data:
            break

        contributors.extend(data)
        page += 1

        # Safety check for infinite loops
        if page > 100:
            print("Warning: Reached maximum page limit", file=sys.stderr)
            break

    return contributors


def get_assignee(issue: Dict) -> str:
    """Extract assignee login from an issue."""
    if issue.get("assignee"):
        return issue["assignee"].get("login", "Unassigned")
    return "Unassigned"


def print_issues_report(issues: List[Dict]) -> None:
    """Print a formatted report of all issues."""
    print("\n" + "=" * 80)
    print("GITHUB ISSUES REPORT")
    print(f"Repository: {REPO_OWNER}/{REPO_NAME}")
    print("=" * 80)
    print(f"\n{'#':<6} {'Title':<40} {'State':<10} {'Assignee'}")
    print("-" * 80)

    for issue in sorted(issues, key=lambda x: x.get("number", 0)):
        number = issue.get("number", 0)
        title = issue.get("title", "No title")[:38]
        state = issue.get("state", "unknown")
        assignee = get_assignee(issue)

        print(f"{number:<6} {title:<40} {state:<10} {assignee}")

    print("-" * 80)
    print(f"Total Issues: {len(issues)}")
    print("=" * 80 + "\n")


def print_contributors_report(contributors: List[Dict]) -> None:
    """Print a formatted report of all contributors."""
    print("\n" + "=" * 60)
    print("CONTRIBUTORS REPORT")
    print(f"Repository: {REPO_OWNER}/{REPO_NAME}")
    print("=" * 60)
    print(f"\n{'Username':<30} {'Contributions'}")
    print("-" * 60)

    for contributor in sorted(contributors, key=lambda x: x.get("contributions", 0), reverse=True):
        login = contributor.get("login", "Unknown")
        contributions = contributor.get("contributions", 0)
        print(f"{login:<30} {contributions}")

    print("-" * 60)
    print(f"Total Contributors: {len(contributors)}")
    print("=" * 60 + "\n")


def main() -> int:
    """Main function to fetch and print the report."""
    print("Fetching issues and contributors from GitHub...")

    # Fetch all issues (both open and closed)
    print("Fetching issues...")
    issues = fetch_all_issues(state="all")

    if not issues:
        print("No issues found or failed to fetch issues.", file=sys.stderr)
        return 1

    print(f"Found {len(issues)} issues.")

    # Fetch contributors
    print("Fetching contributors...")
    contributors = fetch_contributors()

    if not contributors:
        print("No contributors found or failed to fetch contributors.", file=sys.stderr)
        contributors = []

    print(f"Found {len(contributors)} contributors.")

    # Print reports
    print_issues_report(issues)
    print_contributors_report(contributors)

    return 0


if __name__ == "__main__":
    sys.exit(main())