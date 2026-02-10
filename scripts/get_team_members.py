"""
Team Members Utility Script

This script provides functions to read and parse team member information
from the team.md file in the planning repository.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass

# Add src directory to path for imports
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from team_members import (
    TeamMember,
    get_team_members as _get_team_members,
    get_member_by_username,
    get_members_by_role,
)


@dataclass
class TeamMemberScript:
    """Represents a team member with their details."""
    username: str
    name: str
    role: str
    capacity: str

    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary."""
        return {
            "username": self.username,
            "name": self.name,
            "role": self.role,
            "capacity": self.capacity
        }


def get_repo_root() -> Path:
    """Get the root directory of the repository."""
    # Go up from this file's location to find repo root
    current = Path(__file__).resolve()
    # Assuming script is in a scripts/ folder at repo root
    return current.parent.parent


def get_team_file_path() -> Path:
    """Get the path to the team.md file."""
    return get_repo_root() / "team.md"


def parse_markdown_table(table_text: str) -> List[List[str]]:
    """
    Parse a markdown table and return a list of rows.

    Args:
        table_text: The markdown table text

    Returns:
        List of rows, where each row is a list of cell values
    """
    lines = table_text.strip().split('\n')
    rows = []

    for line in lines:
        # Skip separator lines (like |---|)
        if re.match(r'^[\s\|]*[-:]+[\s\|]*$', line):
            continue

        # Extract cells from the line
        cells = []
        for cell in line.strip('|').split('|'):
            cells.append(cell.strip())
        rows.append(cells)

    return rows


def get_team_members(file_path: Optional[str] = None) -> List[TeamMember]:
    """
    Read and parse team members from team.md file.

    Args:
        file_path: Optional path to team.md file. If not provided,
                   uses the default location in the repo.

    Returns:
        List of TeamMember objects
    """
    return _get_team_members(file_path)


def get_team_members_dict(file_path: Optional[str] = None) -> List[Dict[str, str]]:
    """
    Get team members as a list of dictionaries.

    Args:
        file_path: Optional path to team.md file

    Returns:
        List of dictionaries with team member info
    """
    members = get_team_members(file_path)
    return [m.to_dict() if hasattr(m, 'to_dict') else {
        "username": m.username,
        "name": m.name,
        "role": m.role,
        "capacity": m.capacity
    } for m in members]


def print_team_members(members: Optional[List[TeamMember]] = None):
    """
    Print team members in a formatted table.

    Args:
        members: List of TeamMember objects. If None, fetches all members.
    """
    if members is None:
        members = get_team_members()

    print("\n" + "=" * 70)
    print(f"{'Username':<15} {'Name':<20} {'Role':<25} {'Capacity':<10}")
    print("=" * 70)

    for member in members:
        print(f"@{member.username:<13} {member.name:<20} {member.role:<25} {member.capacity:<10}")

    print("=" * 70)
    print(f"Total team members: {len(members)}\n")


# CLI Entry Point
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Get team members from team.md")
    parser.add_argument('--username', '-u', type=str, help="Filter by username")
    parser.add_argument('--role', '-r', type=str, help="Filter by role")
    parser.add_argument('--json', action='store_true', help="Output as JSON")

    args = parser.parse_args()

    members = get_team_members()

    if args.username:
        member = get_member_by_username(args.username)
        if member:
            members = [member]
        else:
            print(f"Member not found: {args.username}")
            members = []

    if args.role:
        members = get_members_by_role(args.role)

    if args.json:
        import json
        print(json.dumps(get_team_members_dict(), indent=2))
    else:
        print_team_members(members)