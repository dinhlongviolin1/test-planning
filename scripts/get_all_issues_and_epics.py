"""
Issues and Epics Utility Script

This script provides functions to read and parse all issues and epics
from the planning repository's markdown files.
"""

import os
import re
import sys
import json
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Optional, Any

logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
logger = logging.getLogger(__name__)


def get_repo_root() -> Path:
    """Get the root directory of the repository."""
    current = Path(__file__).resolve()
    return current.parent.parent


def parse_meta_table(content: str) -> Dict[str, str]:
    """
    Parse the Meta table from markdown content.

    Looks for a table after a '# Meta' or '## Meta' heading and extracts
    key-value pairs from it.

    Args:
        content: The full markdown file content

    Returns:
        Dict of field names to values
    """
    meta = {}
    lines = content.split('\n')

    # Find the Meta heading (# Meta or ## Meta)
    meta_start = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped in ('# Meta', '## Meta'):
            meta_start = i + 1
            break

    if meta_start is None:
        return meta

    # Parse table rows until next section or end of content
    for line in lines[meta_start:]:
        stripped = line.strip()
        # Stop at next heading
        if stripped.startswith('#') and not stripped.startswith('#|'):
            break
        # Skip empty lines, header row detection, and separator lines
        if not stripped or not stripped.startswith('|'):
            continue
        if re.match(r'^\|[\s]*[-:]+[\s]*(\|[\s]*[-:]+[\s]*)*\|$', stripped):
            continue

        cells = [cell.strip() for cell in stripped.strip('|').split('|')]
        if len(cells) >= 2:
            key = cells[0]
            value = cells[1]
            # Skip the header row
            if key.lower() == 'field' and value.lower() == 'value':
                continue
            meta[key] = value

    return meta


def parse_sections(content: str) -> Dict[str, Any]:
    """
    Extract markdown ## sections and their content.

    Args:
        content: The full markdown file content

    Returns:
        Dict keyed by snake_case section name with parsed content
    """
    sections: Dict[str, Any] = {}

    # Split by ## headings (but not # Meta)
    parts = re.split(r'^## ', content, flags=re.MULTILINE)

    for part in parts[1:]:  # Skip everything before the first ##
        heading_end = part.find('\n')
        if heading_end == -1:
            heading = part.strip()
            body = ''
        else:
            heading = part[:heading_end].strip()
            body = part[heading_end + 1:].strip()

        # Skip Meta section
        if heading.lower() == 'meta':
            continue

        # Normalize heading to snake_case
        key = heading.lower().replace(' ', '_')

        # Parse based on section type
        if key == 'tasks':
            sections[key] = _parse_tasks(body)
        elif key in ('linked_epics', 'related_issues', 'linked_sprint', 'linked_milestone'):
            sections[key] = _parse_link_list(body)
        else:
            sections[key] = body

    return sections


def _parse_tasks(body: str) -> List[Dict[str, Any]]:
    """Parse a Tasks section with checkbox items."""
    tasks = []
    for line in body.split('\n'):
        line = line.strip()
        match = re.match(r'^- \[([ x])\] (.+)$', line)
        if match:
            done = match.group(1) == 'x'
            task_text = match.group(2).strip()
            tasks.append({"task": task_text, "done": done})
    return tasks


def _parse_link_list(body: str) -> List[Dict[str, str]]:
    """Parse a section with markdown link items or '- None'."""
    links = []
    for line in body.split('\n'):
        line = line.strip()
        if line == '- None' or line == '- none':
            return []
        match = re.match(r'^- \[([^\]]+)\]\(([^)]+)\)\s*-\s*(.+)$', line)
        if match:
            links.append({
                "id": match.group(1),
                "link": match.group(2),
                "description": match.group(3).strip()
            })
    return links


def parse_markdown_file(file_path: Path) -> Dict[str, Any]:
    """
    Parse a single markdown issue or epic file.

    Args:
        file_path: Path to the markdown file

    Returns:
        Dict with all meta fields and section content merged
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    meta = parse_meta_table(content)
    sections = parse_sections(content)

    # Merge: meta fields with lowercased keys + sections + source file
    result: Dict[str, Any] = {}
    for k, v in meta.items():
        result[k.lower()] = v
    result.update(sections)
    result['_source_file'] = file_path.name

    return result


def get_all_items(directory: str, status_filter: Optional[str] = None) -> List[Dict]:
    """
    Get all parsed items from a directory of markdown files.

    Args:
        directory: Directory name relative to repo root (e.g. 'issues', 'epics')
        status_filter: Optional status to filter by (case-insensitive)

    Returns:
        List of parsed item dicts
    """
    dir_path = get_repo_root() / directory

    if not dir_path.exists():
        return []

    items = []
    for md_file in sorted(dir_path.glob('*.md')):
        # Skip index files
        if md_file.name == '_index.md':
            continue

        try:
            item = parse_markdown_file(md_file)
            items.append(item)
        except Exception as e:
            logger.warning("Failed to parse %s: %s", md_file, e)
            continue

    if status_filter is not None:
        items = [
            item for item in items
            if item.get('status', '').lower() == status_filter.lower()
        ]

    return items


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Get all issues and epics')
        parser.add_argument('--status', '-s', type=str, help='Filter by status (case-insensitive)')
        args = parser.parse_args()

        issues = get_all_items('issues', args.status)
        epics = get_all_items('epics', args.status)
        result = {'issues': issues, 'epics': epics}
        print(json.dumps(result, indent=2))
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
