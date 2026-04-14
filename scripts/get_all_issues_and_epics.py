"""
Issues and Epics Utility Script

This script provides functions to read and parse all issues and epics
from the planning repository's markdown files, with optional status filtering.
"""

import json
import logging
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def get_repo_root() -> Path:
    """Get the root directory of the repository."""
    current = Path(__file__).resolve()
    return current.parent.parent


def to_snake_case(name: str) -> str:
    """Convert a field name to snake_case.

    Args:
        name: The field name to convert (e.g., 'Linked Epics', 'ID', 'Target Repo')

    Returns:
        The snake_case version of the name
    """
    name = name.strip().lower()
    name = re.sub(r'\s+', '_', name)
    return name


def parse_meta_table(content: str) -> Dict[str, str]:
    """Parse the # Meta markdown table into a dict.

    Args:
        content: The full markdown file content

    Returns:
        Dict with snake_case keys and string values from the Meta table

    Raises:
        ValueError: If no Meta section or table is found
    """
    lines = content.split('\n')

    # Find the Meta header (# Meta or ## Meta)
    meta_start = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '# Meta' or stripped == '## Meta':
            meta_start = i
            break

    if meta_start is None:
        raise ValueError("No Meta section found")

    # Parse table rows after # Meta
    result = {}
    in_table = False
    header_seen = False
    separator_seen = False

    for line in lines[meta_start + 1:]:
        stripped = line.strip()

        # Stop at next section header
        if stripped.startswith('#') and not stripped.startswith('|'):
            break

        if not stripped.startswith('|'):
            if in_table:
                break
            continue

        in_table = True

        # Skip header row (first | row)
        if not header_seen:
            header_seen = True
            continue

        # Skip separator row (e.g., |-------|-------|)
        if not separator_seen and re.match(r'^[|\s\-:]+$', stripped) and '-' in stripped:
            separator_seen = True
            continue

        # Parse data row
        cells = [cell.strip() for cell in stripped.strip('|').split('|')]
        if len(cells) >= 2:
            key = to_snake_case(cells[0])
            value = cells[1].strip()
            if key:
                result[key] = value

    if not result:
        raise ValueError("No data rows found in Meta table")

    return result


def parse_sections(content: str) -> Dict[str, str]:
    """Parse ## Section headers and their content.

    Splits the content by ## headers and captures each section's text.
    Only captures sections that appear after the Meta table.

    Args:
        content: The full markdown file content

    Returns:
        Dict with snake_case section names as keys and stripped content as values
    """
    # Find all ## sections using regex
    section_pattern = re.compile(r'^## (.+)$', re.MULTILINE)
    matches = list(section_pattern.finditer(content))

    result = {}
    for i, match in enumerate(matches):
        section_name = to_snake_case(match.group(1))
        if section_name == 'meta':
            continue
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        section_content = content[start:end].strip()
        if section_name:
            result[section_name] = section_content

    return result


def parse_markdown_file(filepath: Path) -> Dict[str, Any]:
    """Parse a single issue or epic markdown file.

    Reads the file, extracts Meta table fields and section content,
    and returns them as a flat dictionary.

    Args:
        filepath: Path to the markdown file

    Returns:
        Dict containing all meta fields and section content

    Raises:
        ValueError: If the file cannot be parsed
    """
    content = filepath.read_text(encoding='utf-8')

    meta = parse_meta_table(content)
    sections = parse_sections(content)

    # Merge meta and sections into a flat dict (meta takes precedence for conflicts)
    result = {}
    result.update(sections)
    result.update(meta)

    return result


def get_all_items(directory: Path) -> List[Dict[str, Any]]:
    """Get all parsed items from a directory.

    Scans for *.md files (excluding _index.md), parses each one,
    and returns the list of parsed items sorted by filename.

    Args:
        directory: Path to the directory to scan (e.g., issues/ or epics/)

    Returns:
        List of dicts, one per successfully parsed file
    """
    if not directory.exists():
        return []

    items = []
    md_files = sorted(directory.glob('*.md'))

    for filepath in md_files:
        if filepath.name == '_index.md':
            continue

        try:
            item = parse_markdown_file(filepath)
            items.append(item)
        except (ValueError, OSError) as e:
            logger.warning("Skipping %s: %s", filepath, e)

    return items


def main() -> None:
    """Main entry point for the CLI."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Get all issues and epics from the planning repository"
    )
    parser.add_argument(
        '--status', '-s',
        type=str,
        help="Filter by status (case-insensitive)"
    )

    args = parser.parse_args()

    try:
        repo_root = get_repo_root()
    except Exception as e:
        logger.error("Cannot determine repo root: %s", e)
        sys.exit(1)

    issues = get_all_items(repo_root / 'issues')
    epics = get_all_items(repo_root / 'epics')

    if args.status:
        status_filter = args.status.lower()
        issues = [
            item for item in issues
            if item.get('status', '').lower() == status_filter
        ]
        epics = [
            item for item in epics
            if item.get('status', '').lower() == status_filter
        ]

    result = {"issues": issues, "epics": epics}
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
