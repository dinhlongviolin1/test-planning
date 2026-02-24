#!/usr/bin/env python3
"""
List all users, issues, and epics from the planning repository.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class TeamMember:
    """Represents a team member with their details."""
    username: str
    name: str
    role: str
    capacity: str


@dataclass
class Issue:
    """Represents an issue with its details."""
    id: str
    title: str
    status: str
    assignee: Optional[str]
    points: Optional[int]
    created: str
    updated: str


@dataclass
class Epic:
    """Represents an epic with its details."""
    id: str
    title: str
    status: str
    created: str
    updated: str


def get_base_path() -> Path:
    """Get the base path of the repository."""
    return Path(__file__).parent.parent


def get_team_members(file_path: Optional[Path] = None) -> List[TeamMember]:
    """Get all team members from team.md file."""
    if file_path is None:
        file_path = get_base_path() / "team.md"

    if not file_path.exists():
        raise FileNotFoundError(f"Team file not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return parse_team_table(content)


def parse_team_table(markdown_content: str) -> List[TeamMember]:
    """Parse team member information from markdown table format."""
    members = []
    lines = markdown_content.split('\n')
    in_table = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith('|') and stripped.endswith('|'):
            if '---' in stripped and not in_table:
                in_table = True
                continue

            if in_table and '---' not in stripped:
                cells = [cell.strip() for cell in stripped.strip('|').split('|')]

                if len(cells) >= 4:
                    username = cells[0].lstrip('@')
                    name = cells[1]
                    role = cells[2]
                    capacity = cells[3]

                    member = TeamMember(
                        username=username,
                        name=name,
                        role=role,
                        capacity=capacity
                    )
                    members.append(member)
        elif in_table and not stripped.startswith('|'):
            break

    return members


def get_issues(issues_dir: Optional[Path] = None) -> List[Issue]:
    """Get all issues from the issues directory."""
    if issues_dir is None:
        issues_dir = get_base_path() / "issues"

    if not issues_dir.exists():
        raise FileNotFoundError(f"Issues directory not found: {issues_dir}")

    issues = []
    for md_file in sorted(issues_dir.glob("i-*.md")):
        issue = parse_issue(md_file)
        if issue:
            issues.append(issue)

    return issues


def parse_issue(file_path: Path) -> Optional[Issue]:
    """Parse an issue from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    issue_id = None
    title = None
    status = None
    assignee = None
    points = None
    created = None
    updated = None

    in_meta = False
    in_title = False

    for line in lines:
        stripped = line.strip()

        if stripped == "# Meta":
            in_meta = True
            continue
        elif stripped == "## Title":
            in_meta = False
            in_title = True
            continue
        elif stripped.startswith("## "):
            in_title = False

        if in_meta and '|' in stripped:
            cells = [cell.strip() for cell in stripped.strip('|').split('|')]
            if len(cells) >= 2:
                key = cells[0].strip()
                value = cells[1].strip()
                if key == "ID":
                    issue_id = value
                elif key == "Status":
                    status = value
                elif key == "Created":
                    created = value
                elif key == "Updated":
                    updated = value
                elif key == "Points":
                    try:
                        points = int(value)
                    except ValueError:
                        points = None
                elif key == "Assignee":
                    assignee = value.lstrip('@') if value else None
        elif in_title and stripped:
            title = stripped

    if issue_id:
        return Issue(
            id=issue_id,
            title=title or "",
            status=status or "",
            assignee=assignee,
            points=points,
            created=created or "",
            updated=updated or ""
        )
    return None


def get_epics(epics_dir: Optional[Path] = None) -> List[Epic]:
    """Get all epics from the epics directory."""
    if epics_dir is None:
        epics_dir = get_base_path() / "epics"

    if not epics_dir.exists():
        raise FileNotFoundError(f"Epics directory not found: {epics_dir}")

    epics = []
    for md_file in sorted(epics_dir.glob("e-*.md")):
        epic = parse_epic(md_file)
        if epic:
            epics.append(epic)

    return epics


def parse_epic(file_path: Path) -> Optional[Epic]:
    """Parse an epic from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')

    epic_id = None
    title = None
    status = None
    created = None
    updated = None

    in_meta = False
    in_title = False
    in_description = False

    for line in lines:
        stripped = line.strip()

        if stripped == "# Meta":
            in_meta = True
            continue
        elif stripped == "## Title":
            in_meta = False
            in_title = True
            in_description = False
            continue
        elif stripped == "## Description":
            in_meta = False
            in_title = False
            in_description = True
            continue
        elif stripped.startswith("## "):
            in_title = False
            in_description = False

        if in_meta and '|' in stripped:
            cells = [cell.strip() for cell in stripped.strip('|').split('|')]
            if len(cells) >= 2:
                key = cells[0].strip()
                value = cells[1].strip()
                if key == "ID":
                    epic_id = value
                elif key == "Status":
                    status = value
                elif key == "Created":
                    created = value
                elif key == "Updated":
                    updated = value
        elif in_title and stripped:
            title = stripped
        elif in_description and stripped and title is None:
            # Use first line of description as title if no title section exists
            title = stripped

    if epic_id:
        return Epic(
            id=epic_id,
            title=title or "",
            status=status or "",
            created=created or "",
            updated=updated or ""
        )
    return None


def print_all():
    """Print all users, issues, and epics."""
    base_path = get_base_path()

    # Print Users/Team Members
    print("\n" + "=" * 70)
    print("USERS / TEAM MEMBERS")
    print("=" * 70)
    try:
        members = get_team_members(base_path / "team.md")
        print(f"{'Username':<20} {'Name':<20} {'Role':<20} {'Capacity'}")
        print("-" * 70)
        for member in members:
            print(f"@{member.username:<19} {member.name:<20} {member.role:<20} {member.capacity}")
        print("-" * 70)
        print(f"Total Users: {len(members)}")
    except FileNotFoundError:
        print("No team.md file found")

    # Print Issues
    print("\n" + "=" * 70)
    print("ISSUES")
    print("=" * 70)
    try:
        issues = get_issues(base_path / "issues")
        print(f"{'ID':<10} {'Title':<35} {'Status':<12} {'Assignee':<15} {'Points'}")
        print("-" * 70)
        for issue in issues:
            title = issue.title[:32] + "..." if len(issue.title) > 35 else issue.title
            assignee = issue.assignee if issue.assignee else "Unassigned"
            points = issue.points if issue.points else "-"
            print(f"{issue.id:<10} {title:<35} {issue.status:<12} @{assignee:<14} {points}")
        print("-" * 70)
        print(f"Total Issues: {len(issues)}")
    except FileNotFoundError:
        print("No issues directory found")

    # Print Epics
    print("\n" + "=" * 70)
    print("EPICS")
    print("=" * 70)
    try:
        epics = get_epics(base_path / "epics")
        print(f"{'ID':<10} {'Title':<45} {'Status'}")
        print("-" * 70)
        for epic in epics:
            title = epic.title[:42] + "..." if len(epic.title) > 45 else epic.title
            print(f"{epic.id:<10} {title:<45} {epic.status}")
        print("-" * 70)
        print(f"Total Epics: {len(epics)}")
    except FileNotFoundError:
        print("No epics directory found")

    print("\n")


def main():
    """Main entry point."""
    print_all()


if __name__ == "__main__":
    main()