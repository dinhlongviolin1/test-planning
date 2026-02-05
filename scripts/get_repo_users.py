"""
Get all users (collaborators) from a GitHub repository.

This script fetches all users who have access to the repository
(collaborators, organization members, etc.) using the GitHub REST API.
"""

import os
import sys
import requests
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class GitHubUser:
    """Represents a GitHub user."""
    login: str
    id: int
    avatar_url: str
    html_url: str
    type: str
    site_admin: bool

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "login": self.login,
            "id": self.id,
            "avatar_url": self.avatar_url,
            "html_url": self.html_url,
            "type": self.type,
            "site_admin": self.site_admin
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
        "User-Agent": "GitHub-User-Fetcher/1.0"
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


def get_all_collaborators(owner: str, repo_name: str) -> List[GitHubUser]:
    """
    Get all collaborators for a repository.

    Args:
        owner: Repository owner
        repo_name: Repository name

    Returns:
        List of GitHubUser objects
    """
    users = []
    page = 1
    per_page = 100

    while True:
        url = f"{get_github_api_url()}/repos/{owner}/{repo_name}/collaborators"
        params = {"per_page": per_page, "page": page}

        response = make_request(url, params)
        if response is None:
            break

        data = response.json()
        if not data:
            break

        for item in data:
            # Check if user has full access (not just a pending invite)
            if isinstance(item, dict) and item.get("role") is not None or isinstance(item, dict) and "login" in item:
                user = GitHubUser(
                    login=item.get("login", ""),
                    id=item.get("id", 0),
                    avatar_url=item.get("avatar_url", ""),
                    html_url=item.get("html_url", ""),
                    type=item.get("type", "User"),
                    site_admin=item.get("site_admin", False)
                )
                users.append(user)

        # Check if there are more pages
        if len(data) < per_page:
            break
        page += 1

    return users


def get_all_contributors(owner: str, repo_name: str) -> List[GitHubUser]:
    """
    Get all contributors for a repository.

    Args:
        owner: Repository owner
        repo_name: Repository name

    Returns:
        List of GitHubUser objects (ordered by contributions)
    """
    users = []
    page = 1
    per_page = 100
    anon = os.environ.get("INCLUDE_ANONYMOUS", "").lower() in ("true", "1", "yes")

    while True:
        url = f"{get_github_api_url()}/repos/{owner}/{repo_name}/contributors"
        params = {"per_page": per_page, "page": page, "anon": str(anon).lower()}

        response = make_request(url, params)
        if response is None:
            break

        data = response.json()
        if not data:
            break

        for item in data:
            if isinstance(item, dict) and "login" in item:
                user = GitHubUser(
                    login=item.get("login", ""),
                    id=item.get("id", 0),
                    avatar_url=item.get("avatar_url", ""),
                    html_url=item.get("html_url", ""),
                    type=item.get("type", "User"),
                    site_admin=item.get("site_admin", False)
                )
                users.append(user)

        if len(data) < per_page:
            break
        page += 1

    return users


def get_all_members(owner: str, repo_name: str) -> List[GitHubUser]:
    """
    Get all organization members if the repo is owned by an org.

    Args:
        owner: Repository owner (could be organization)
        repo_name: Repository name

    Returns:
        List of GitHubUser objects
    """
    users = []
    page = 1
    per_page = 100

    while True:
        url = f"{get_github_api_url()}/orgs/{owner}/members"
        params = {"per_page": per_page, "page": page}

        response = make_request(url, params)
        if response is None:
            break

        data = response.json()
        if not data:
            break

        for item in data:
            if isinstance(item, dict) and "login" in item:
                user = GitHubUser(
                    login=item.get("login", ""),
                    id=item.get("id", 0),
                    avatar_url=item.get("avatar_url", ""),
                    html_url=item.get("html_url", ""),
                    type=item.get("type", "User"),
                    site_admin=item.get("site_admin", False)
                )
                users.append(user)

        if len(data) < per_page:
            break
        page += 1

    return users


def get_all_users(owner: str, repo_name: str) -> dict:
    """
    Get all users from a repository (collaborators, contributors, and members).

    Args:
        owner: Repository owner
        repo_name: Repository name

    Returns:
        Dictionary with keys: 'collaborators', 'contributors', 'members'
    """
    return {
        "collaborators": get_all_collaborators(owner, repo_name),
        "contributors": get_all_contributors(owner, repo_name),
        "members": get_all_members(owner, repo_name)
    }


def print_users(users: List[GitHubUser], title: str):
    """Print users in a formatted table."""
    print(f"\n{'=' * 70}")
    print(f"{title}")
    print(f"{'=' * 70}")
    print(f"{'Login':<20} {'Type':<10} {'Admin':<6} {'URL'}")
    print(f"{'-' * 70}")

    for user in users:
        print(f"{user.login:<20} {user.type:<10} {'Yes' if user.site_admin else 'No':<6} {user.html_url}")

    print(f"{'=' * 70}")
    print(f"Total: {len(users)}\n")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Get all users from a GitHub repository",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--repo", "-r",
        default=os.environ.get("GITHUB_REPOSITORY", "dinhlongviolin1/test-planning"),
        help="Repository in 'owner/repo' format (default: dinhlongviolin1/test-planning)"
    )
    parser.add_argument(
        "--collaborators", "-c",
        action="store_true",
        help="Get only collaborators"
    )
    parser.add_argument(
        "--contributors", "-C",
        action="store_true",
        help="Get only contributors"
    )
    parser.add_argument(
        "--members", "-m",
        action="store_true",
        help="Get only organization members"
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

    args = parser.parse_args()

    # Parse repo
    if "/" not in args.repo:
        parser.error(f"Invalid repository format: {args.repo}. Expected 'owner/repo'")
    owner, repo_name = args.repo.split("/", 1)

    # Set token if provided
    if args.token:
        os.environ["GITHUB_TOKEN"] = args.token

    all_users = get_all_users(owner, repo_name)

    if args.json:
        import json
        result = {}

        if args.collaborators or not (args.collaborators or args.contributors or args.members):
            result["collaborators"] = [u.to_dict() for u in all_users["collaborators"]]
        if args.contributors or not (args.collaborators or args.contributors or args.members):
            result["contributors"] = [u.to_dict() for u in all_users["contributors"]]
        if args.members or not (args.collaborators or args.contributors or args.members):
            result["members"] = [u.to_dict() for u in all_users["members"]]

        print(json.dumps(result, indent=2))
    else:
        if args.collaborators or not (args.collaborators or args.contributors or args.members):
            print_users(all_users["collaborators"], "Collaborators")
        if args.contributors:
            print_users(all_users["contributors"], "Contributors")
        if args.members:
            print_users(all_users["members"], "Organization Members")


if __name__ == "__main__":
    main()