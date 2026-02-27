"""
Issue Retrieval Module

This module provides functionality to retrieve and parse issue
information from the issues/ folder in the planning repository.
"""

from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class Issue:
    """Represents an issue with its details."""

    id: str
    status: str
    created: str
    updated: str
    points: str
    assignee: str
    title: str
    description: str

    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "status": self.status,
            "created": self.created,
            "updated": self.updated,
            "points": self.points,
            "assignee": self.assignee,
            "title": self.title,
            "description": self.description,
        }


def get_repo_root() -> Path:
    """Get the root directory of the repository."""
    current = Path(__file__).resolve()
    return current.parent


def get_issues_dir() -> Path:
    """Get the path to the issues directory."""
    return get_repo_root() / "issues"


def parse_markdown_meta(content: str) -> Dict[str, str]:
    """
    Parse the Meta table from markdown content.

    Args:
        content: The raw markdown content

    Returns:
        Dictionary of meta field values
    """
    meta = {}
    lines = content.split("\n")

    in_meta_table = False

    for line in lines:
        stripped = line.strip()

        # Detect start of meta table
        if stripped == "# Meta":
            in_meta_table = True
            continue

        # Detect end of meta table (next ## section)
        if in_meta_table and stripped.startswith("##"):
            break

        # Parse table rows
        if in_meta_table and stripped.startswith("|") and "---" not in stripped:
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if len(cells) >= 2:
                field = cells[0]
                value = cells[1]
                meta[field] = value

    return meta


def parse_title_section(content: str) -> str:
    """Extract title from ## Title section."""
    lines = content.split("\n")
    in_title = False
    title_lines = []

    for line in lines:
        stripped = line.strip()

        if stripped == "## Title":
            in_title = True
            continue

        if in_title:
            if stripped.startswith("## "):
                break
            if stripped:
                title_lines.append(stripped)

    return " ".join(title_lines).strip()


def parse_description_section(content: str) -> str:
    """Extract description from ## Description section."""
    lines = content.split("\n")
    in_desc = False
    desc_lines = []

    for line in lines:
        stripped = line.strip()

        if stripped == "## Description":
            in_desc = True
            continue

        if in_desc:
            if stripped.startswith("## "):
                break
            if stripped:
                desc_lines.append(stripped)

    return " ".join(desc_lines).strip()


def parse_issue_file(file_path: Path) -> Issue:
    """
    Parse a single issue file.

    Args:
        file_path: Path to the issue .md file

    Returns:
        Issue object
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse meta table
    meta = parse_markdown_meta(content)

    # Parse title and description
    title = parse_title_section(content)
    description = parse_description_section(content)

    # Get assignee without @ prefix
    assignee = meta.get("Assignee", "")
    if assignee.startswith("@"):
        assignee = assignee[1:]

    return Issue(
        id=meta.get("ID", ""),
        status=meta.get("Status", ""),
        created=meta.get("Created", ""),
        updated=meta.get("Updated", ""),
        points=meta.get("Points", ""),
        assignee=assignee,
        title=title,
        description=description,
    )


def get_issues(issues_dir: Optional[str] = None) -> List[Issue]:
    """
    Retrieve all issues from the issues folder.

    Args:
        issues_dir: Optional path to the issues directory. If not provided,
                    will look for issues/ in the current directory.

    Returns:
        List of Issue objects representing all issues.

    Raises:
        FileNotFoundError: If the issues directory is not found.
    """
    issues_path: Path
    if issues_dir is None:
        issues_path = get_issues_dir()
    else:
        issues_path = Path(issues_dir)

    if not issues_path.exists():
        raise FileNotFoundError(f"Issues directory not found: {issues_path}")

    issues = []

    # Find all issue files (i-*.md but not _index.md)
    for file_path in sorted(issues_path.glob("i-*.md")):
        issue = parse_issue_file(file_path)
        issues.append(issue)

    return issues


def get_issues_by_status(status: str, issues_dir: Optional[str] = None) -> List[Issue]:
    """
    Get all issues with a specific status.

    Args:
        status: The status to filter by (todo, in_progress, done)
        issues_dir: Optional path to the issues directory

    Returns:
        List of Issue objects with the specified status
    """
    issues = get_issues(issues_dir)
    return [issue for issue in issues if issue.status.lower() == status.lower()]


def get_issue_by_id(issue_id: str, issues_dir: Optional[str] = None) -> Optional[Issue]:
    """
    Get a specific issue by its ID.

    Args:
        issue_id: The issue ID to search for (e.g., 'i-001')
        issues_dir: Optional path to the issues directory

    Returns:
        Issue object if found, None otherwise
    """
    issues = get_issues(issues_dir)

    for issue in issues:
        if issue.id.lower() == issue_id.lower():
            return issue

    return None


def get_issues_by_assignee(
    assignee: str, issues_dir: Optional[str] = None
) -> List[Issue]:
    """
    Get all issues assigned to a specific user.

    Args:
        assignee: The username to filter by (without @)
        issues_dir: Optional path to the issues directory

    Returns:
        List of Issue objects assigned to the user
    """
    issues = get_issues(issues_dir)
    return [issue for issue in issues if issue.assignee.lower() == assignee.lower()]


def print_issues(issues: Optional[List[Issue]] = None):
    """
    Print issues in a formatted table.

    Args:
        issues: List of Issue objects. If None, fetches all issues.
    """
    if issues is None:
        issues = get_issues()

    print("\n" + "=" * 80)
    print(f"{'ID':<10} {'Status':<15} {'Title':<35} {'Assignee':<15}")
    print("=" * 80)

    for issue in issues:
        title = issue.title[:32] + "..." if len(issue.title) > 35 else issue.title
        print(f"{issue.id:<10} {issue.status:<15} {title:<35} @{issue.assignee:<14}")

    print("=" * 80)
    print(f"Total issues: {len(issues)}\n")


# Example usage
if __name__ == "__main__":
    # Print all issues
    print_issues()

    # Demonstrate individual lookups
    print("\nSearching for 'i-002':")
    issue = get_issue_by_id("i-002")
    if issue:
        print(f"  Found: {issue.title} (Status: {issue.status})")

    print("\nAll 'todo' issues:")
    todo_issues = get_issues_by_status("todo")
    for iss in todo_issues:
        print(f"  - {iss.id}: {iss.title}")

    print("\nAll 'in_progress' issues:")
    in_progress = get_issues_by_status("in_progress")
    for iss in in_progress:
        print(f"  - {iss.id}: {iss.title}")
