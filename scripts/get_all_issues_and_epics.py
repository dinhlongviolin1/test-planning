#!/usr/bin/env python3
"""
Get all issues and epics from the planning repository.

Reads all .md files from issues/ and epics/ directories and extracts
metadata from the markdown meta table format.
"""

import argparse
import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Optional


def get_repo_root() -> Path:
    """Get the root directory of the repository."""
    current = Path(__file__).resolve()
    return current.parent.parent


def parse_meta_table(content: str) -> Optional[Dict[str, str]]:
    """
    Parse a markdown meta table (Field|Value pairs) from content.

    Args:
        content: The markdown content to parse.

    Returns:
        Dictionary of field names to values, or None if no valid table found.
    """
    lines = content.split('\n')

    # Find the meta table (starts with | Field | Value |)
    in_table = False
    table_started = False

    for line in lines:
        stripped = line.strip()

        # Look for the meta table header
        if '| Field | Value |' in stripped:
            in_table = True
            table_started = True
            continue

        # Skip separator line |-------|-------|
        if in_table and re.match(r'^\|[\s\-:]+\|[\s\-:]+\|$', stripped):
            continue

        # End of table (line doesn't start with |)
        if in_table and not stripped.startswith('|'):
            break

        # Parse data row
        if in_table and stripped.startswith('|'):
            cells = [cell.strip() for cell in stripped.strip('|').split('|')]
            if len(cells) >= 2:
                field = cells[0].strip()
                value = cells[1].strip()
                return field, value

    return None


def parse_frontmatter(content: str) -> Dict[str, str]:
    """
    Parse frontmatter from markdown content.

    Args:
        content: The markdown content to parse.

    Returns:
        Dictionary of metadata fields.
    """
    metadata = {}
    lines = content.split('\n')

    # Find the meta table (starts with | Field | Value |)
    in_table = False

    for line in lines:
        stripped = line.strip()

        # Look for the meta table header
        if '| Field | Value |' in stripped:
            in_table = True
            continue

        # Skip separator line |-------|-------|
        if in_table and re.match(r'^\|[\s\-:]+\|[\s\-:]+\|$', stripped):
            continue

        # End of table (line doesn't start with |)
        if in_table and not stripped.startswith('|'):
            break

        # Parse data row
        if in_table and stripped.startswith('|'):
            cells = [cell.strip() for cell in stripped.strip('|').split('|')]
            if len(cells) >= 2:
                field = cells[0].strip()
                value = cells[1].strip()
                metadata[field] = value

    return metadata


def parse_markdown_file(file_path: Path) -> Optional[Dict[str, str]]:
    """
    Parse a markdown file and extract metadata.

    Args:
        file_path: Path to the markdown file.

    Returns:
        Dictionary of metadata fields, or None if parsing fails.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        metadata = parse_frontmatter(content)

        # Also extract title from ## Title section
        title_match = re.search(r'^##\s+Title\s*\n(.+)$', content, re.MULTILINE)
        if title_match:
            metadata['Title'] = title_match.group(1).strip()

        return metadata

    except Exception as e:
        print(f"Warning: Failed to parse {file_path}: {e}", file=sys.stderr)
        return None


def get_files_from_directory(directory: Path, exclude_index: bool = True) -> List[Path]:
    """
    Get all markdown files from a directory.

    Args:
        directory: The directory to search.
        exclude_index: Whether to exclude _index.md files.

    Returns:
        List of markdown file paths.
    """
    if not directory.exists():
        return []

    files = []
    for file_path in sorted(directory.glob("*.md")):
        if exclude_index and file_path.name == "_index.md":
            continue
        files.append(file_path)

    return files


def filter_by_status(items: List[Dict[str, str]], status: Optional[str]) -> List[Dict[str, str]]:
    """
    Filter items by status (case-insensitive).

    Args:
        items: List of item dictionaries.
        status: Status to filter by (case-insensitive).

    Returns:
        Filtered list of items.
    """
    if status is None:
        return items

    status_lower = status.lower()
    return [item for item in items if item.get('Status', '').lower() == status_lower]


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Get all issues and epics from the planning repository."
    )
    parser.add_argument(
        '--status', '-s',
        type=str,
        help="Filter by status (case-insensitive)"
    )
    parser.add_argument(
        '--issues-dir',
        type=str,
        help="Custom issues directory path"
    )
    parser.add_argument(
        '--epics-dir',
        type=str,
        help="Custom epics directory path"
    )

    args = parser.parse_args()

    repo_root = get_repo_root()

    # Determine directories
    issues_dir = Path(args.issues_dir) if args.issues_dir else repo_root / "issues"
    epics_dir = Path(args.epics_dir) if args.epics_dir else repo_root / "epics"

    # Parse issues
    issues = []
    issue_files = get_files_from_directory(issues_dir)

    for file_path in issue_files:
        metadata = parse_markdown_file(file_path)
        if metadata:
            issues.append(metadata)
        else:
            print(f"Warning: Skipping malformed file: {file_path}", file=sys.stderr)

    # Parse epics
    epics = []
    epic_files = get_files_from_directory(epics_dir)

    for file_path in epic_files:
        metadata = parse_markdown_file(file_path)
        if metadata:
            epics.append(metadata)
        else:
            print(f"Warning: Skipping malformed file: {file_path}", file=sys.stderr)

    # Filter by status if requested
    if args.status:
        issues = filter_by_status(issues, args.status)
        epics = filter_by_status(epics, args.status)

    # Output as JSON
    result = {
        "issues": issues,
        "epics": epics
    }

    print(json.dumps(result, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())