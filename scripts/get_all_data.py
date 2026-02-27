#!/usr/bin/env python3
"""
Get All Data Utility Script

This script retrieves both users and issues from the planning repository
and displays them in a formatted output or as JSON.
"""

import sys
import json
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from team_members import get_team_members
from issues import get_issues


def get_repo_root() -> Path:
    """Get the root directory of the repository."""
    current = Path(__file__).resolve()
    return current.parent.parent


def print_users():
    """Print all team members in a formatted table."""
    members = get_team_members()

    print("\n" + "=" * 70)
    print("TEAM MEMBERS")
    print("=" * 70)
    print(f"{'Username':<15} {'Name':<20} {'Role':<25} {'Capacity':<10}")
    print("=" * 70)

    for member in members:
        print(
            f"@{member.username:<13} {member.name:<20} {member.role:<25} {member.capacity:<10}"
        )

    print("=" * 70)
    print(f"Total team members: {len(members)}\n")


def print_issues():
    """Print all issues in a formatted table."""
    issues = get_issues()

    print("\n" + "=" * 90)
    print("ISSUES")
    print("=" * 90)
    print(f"{'ID':<10} {'Status':<15} {'Title':<45} {'Assignee':<15}")
    print("=" * 90)

    for issue in issues:
        title = issue.title[:42] + "..." if len(issue.title) > 45 else issue.title
        print(f"{issue.id:<10} {issue.status:<15} {title:<45} @{issue.assignee:<14}")

    print("=" * 90)
    print(f"Total issues: {len(issues)}\n")


def print_json(users: bool = True, issues: bool = True):
    """Print all data as JSON."""
    data = {}

    if users:
        members = get_team_members()
        data["users"] = [m.to_dict() for m in members]

    if issues:
        issue_list = get_issues()
        data["issues"] = [i.to_dict() for i in issue_list]

    print(json.dumps(data, indent=2))


# CLI Entry Point
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Get all users and issues from the planning repository"
    )
    parser.add_argument("--users", "-u", action="store_true", help="Show only users")
    parser.add_argument("--issues", "-i", action="store_true", help="Show only issues")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Default: show both users and issues
    show_users = args.users or (not args.users and not args.issues)
    show_issues = args.issues or (not args.users and not args.issues)

    if args.json:
        print_json(users=show_users, issues=show_issues)
    else:
        if show_users:
            print_users()
        if show_issues:
            print_issues()
