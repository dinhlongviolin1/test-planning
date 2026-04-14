"""
Issues and Epics Utility Script

This script reads issue and epic markdown files and outputs them as JSON.
"""

import re
import json
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class IssueOrEpic:
    """Represents an issue or epic with its details."""
    data: Dict[str, str]

    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary."""
        return self.data


def get_repo_root() -> Path:
    """Get the root directory of the repository."""
    current = Path(__file__).resolve()
    return current.parent.parent


def parse_frontmatter_table(table_text: str) -> Dict[str, str]:
    """
    Parse a two-column markdown table from the frontmatter.

    Args:
        table_text: The markdown table text (rows like | Field | Value |)

    Returns:
        Dictionary of field -> value pairs
    """
    result = {}
    lines = table_text.strip().split('\n')

    for line in lines:
        # Skip separator lines (like |-------|-------|)
        if re.match(r'^\s*\|[\s\-:]*\|[\s\-:]*\|\s*$', line):
            continue

        # Extract cells
        cells = []
        for cell in line.strip('|').split('|'):
            cells.append(cell.strip())

        # Expecting exactly 2 columns: Field and Value
        if len(cells) >= 2:
            key = cells[0]
            value = cells[1]
            if key and key not in ('Field', ''):
                result[key] = value

    return result


def parse_section(content: str, section_header: str) -> str:
    """
    Extract content from a section like '## Title' or '## Description'.

    Args:
        content: Full file content
        section_header: The section header to find (e.g., '## Title')

    Returns:
        The content of the section, stripped
    """
    pattern = re.escape(section_header) + r'\s*\n(.*?)(?=\n## |\n# |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ''


def parse_file(file_path: Path) -> Optional[Dict[str, str]]:
    """
    Parse a single markdown file and extract all fields.

    Args:
        file_path: Path to the markdown file

    Returns:
        Dictionary with all extracted fields, or None if parsing fails
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None

    # Skip _index.md files
    if file_path.name == '_index.md':
        return None

    result = {}

    # Find the # Meta section
    meta_match = re.search(r'# Meta\s*\n((?:\|.*\|\n)+)', content)
    if not meta_match:
        return None

    table_text = meta_match.group(1)
    fields = parse_frontmatter_table(table_text)
    result.update(fields)

    # Extract Title
    title = parse_section(content, '## Title')
    if title:
        result['title'] = title

    # Extract Description
    description = parse_section(content, '## Description')
    if description:
        result['description'] = description

    return result


def get_items_from_directory(directory: Path, item_type: str) -> List[Dict[str, str]]:
    """
    Get all items (issues or epics) from a directory.

    Args:
        directory: Path to the issues/ or epics/ directory
        item_type: 'issues' or 'epics' for logging

    Returns:
        List of dictionaries representing each item
    """
    if not directory.exists() or not directory.is_dir():
        return []

    items = []
    for file_path in sorted(directory.iterdir()):
        if file_path.is_file() and file_path.suffix == '.md':
            if file_path.name == '_index.md':
                continue

            result = parse_file(file_path)
            if result:
                items.append(result)
            else:
                print(f"Warning: Skipping malformed file: {file_path}", file=sys.stderr)

    return items


def filter_by_status(items: List[Dict[str, str]], status: str) -> List[Dict[str, str]]:
    """
    Filter items by status (case-insensitive).

    Args:
        items: List of item dictionaries
        status: Status to filter by

    Returns:
        Filtered list of items
    """
    return [
        item for item in items
        if item.get('Status', '').lower() == status.lower()
    ]


def get_all_issues_and_epics(status_filter: Optional[str] = None) -> Dict[str, List[Dict[str, str]]]:
    """
    Get all issues and epics as JSON-serializable dictionaries.

    Args:
        status_filter: Optional status to filter by (case-insensitive)

    Returns:
        Dictionary with 'issues' and 'epics' keys, each containing a list of items
    """
    repo_root = get_repo_root()
    issues_dir = repo_root / 'issues'
    epics_dir = repo_root / 'epics'

    issues = get_items_from_directory(issues_dir, 'issues')
    epics = get_items_from_directory(epics_dir, 'epics')

    if status_filter:
        issues = filter_by_status(issues, status_filter)
        epics = filter_by_status(epics, status_filter)

    return {
        'issues': issues,
        'epics': epics
    }


# CLI Entry Point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get all issues and epics from markdown files"
    )
    parser.add_argument(
        '--status', '-s',
        type=str,
        help="Filter by status (case-insensitive)"
    )

    args = parser.parse_args()

    try:
        result = get_all_issues_and_epics(status_filter=args.status)
        print(json.dumps(result, indent=2))
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)