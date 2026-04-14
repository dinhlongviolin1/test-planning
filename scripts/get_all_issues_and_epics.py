"""
Issues and Epics Utility Script

This script provides functions to read and parse all issues and epics
from the issues/ and epics/ directories in the planning repository.
Outputs JSON with optional status filtering.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional


def get_repo_root() -> Path:
    """Get the root directory of the repository."""
    current = Path(__file__).resolve()
    return current.parent.parent


def parse_meta_table(content: str) -> Optional[Dict[str, str]]:
    """
    Parse the # Meta markdown table from file content.

    Returns a dict with lowercased keys, or None if no valid Meta section found.
    """
    lines = content.split('\n')

    # Find the Meta heading (# Meta or ## Meta)
    meta_start = None
    meta_level = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '# Meta':
            meta_start = i
            meta_level = 1
            break
        elif stripped == '## Meta':
            meta_start = i
            meta_level = 2
            break

    if meta_start is None:
        return None

    # Extract lines between Meta heading and the next heading of same or higher level
    meta_lines = []
    for line in lines[meta_start + 1:]:
        stripped = line.strip()
        if meta_level == 1 and stripped.startswith('## '):
            break
        if meta_level == 2 and stripped.startswith('## ') and not stripped.startswith('## Meta'):
            break
        meta_lines.append(line)

    # Parse table rows
    meta = {}
    for line in meta_lines:
        stripped = line.strip()
        if not stripped or not stripped.startswith('|'):
            continue
        # Skip separator rows (e.g., |-------|-------|)
        if re.match(r'^[|\s\-:]+$', stripped):
            continue
        # Skip header row
        if 'Field' in stripped and 'Value' in stripped:
            continue

        cells = [cell.strip() for cell in stripped.strip('|').split('|')]
        if len(cells) >= 2:
            key = cells[0].lower()
            value = cells[1]
            # Strip @ prefix from assignee/owner values
            if key in ('assignee', 'owner'):
                value = value.lstrip('@')
            meta[key] = value

    if not meta:
        return None

    return meta


def parse_sections(content: str) -> Dict[str, str]:
    """
    Parse ## sections from file content.

    Returns a dict mapping section heading (lowercase) to raw content string.
    """
    sections = {}
    parts = content.split('\n## ')

    for part in parts[1:]:  # Skip everything before the first ##
        lines = part.split('\n')
        heading = lines[0].strip()
        body = '\n'.join(lines[1:]).strip()
        sections[heading.lower()] = body

    return sections


def extract_link_references(text: str) -> List[str]:
    """Extract IDs from markdown links like [e-001](e-001.md)."""
    return re.findall(r'\[([^\]]+)\]', text)


def extract_single_link_reference(text: str) -> Optional[str]:
    """Extract a single link reference from text, handling '- None' cases."""
    stripped = text.strip()
    if not stripped or stripped == '- None':
        return None
    matches = re.findall(r'\[([^\]]+)\]', stripped)
    return matches[0] if matches else stripped


def parse_tasks(text: str) -> List[Dict]:
    """Parse checkbox task lines into list of dicts with text and done keys."""
    tasks = []
    for line in text.split('\n'):
        line = line.strip()
        match = re.match(r'^- \[([ xX])\] (.+)$', line)
        if match:
            done = match.group(1).lower() == 'x'
            tasks.append({"text": match.group(2).strip(), "done": done})
    return tasks


def parse_list_references(text: str) -> List[str]:
    """Parse a list of markdown link lines and extract references."""
    refs = []
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('- '):
            matches = re.findall(r'\[([^\]]+)\]', line)
            if matches:
                refs.append(matches[0])
    return refs


def parse_issue_file(file_path: Path) -> Optional[Dict]:
    """
    Parse a single issue markdown file.

    Returns a dict with all meta fields and section content, or None on error.
    """
    content = file_path.read_text(encoding='utf-8')

    meta = parse_meta_table(content)
    if meta is None:
        print(f"Warning: No valid Meta section in {file_path}", file=sys.stderr)
        return None

    sections = parse_sections(content)

    issue = dict(meta)

    # Extract section content
    issue['title'] = sections.get('title', '').strip() or None
    issue['description'] = sections.get('description', '').strip() or None
    issue['linked_epics'] = parse_list_references(sections.get('linked epics', ''))
    issue['linked_sprint'] = extract_single_link_reference(sections.get('linked sprint', ''))
    issue['linked_milestone'] = extract_single_link_reference(sections.get('linked milestone', ''))
    issue['target_repo'] = sections.get('target repo', '').strip() or None
    issue['tasks'] = parse_tasks(sections.get('tasks', ''))
    issue['notes'] = sections.get('notes', '').strip() or None

    return issue


def parse_epic_file(file_path: Path) -> Optional[Dict]:
    """
    Parse a single epic markdown file.

    Returns a dict with all meta fields and section content, or None on error.
    """
    content = file_path.read_text(encoding='utf-8')

    meta = parse_meta_table(content)
    if meta is None:
        print(f"Warning: No valid Meta section in {file_path}", file=sys.stderr)
        return None

    sections = parse_sections(content)

    epic = dict(meta)

    # Owner may not be present — ensure it's in the dict
    if 'owner' not in epic:
        epic['owner'] = None

    # Title is optional for epics (e.g., e-003 has no ## Title)
    epic['title'] = sections.get('title', '').strip() or None
    epic['description'] = sections.get('description', '').strip() or None
    epic['related_issues'] = parse_list_references(sections.get('related issues', ''))

    return epic


def get_all_issues(issues_dir: Path) -> List[Dict]:
    """Parse all issue files in the issues directory."""
    issues = []
    for file_path in sorted(issues_dir.glob('*.md')):
        if file_path.name == '_index.md':
            continue
        try:
            issue = parse_issue_file(file_path)
            if issue is not None:
                issues.append(issue)
        except Exception as e:
            print(f"Warning: Error parsing {file_path}: {e}", file=sys.stderr)
    return issues


def get_all_epics(epics_dir: Path) -> List[Dict]:
    """Parse all epic files in the epics directory."""
    epics = []
    for file_path in sorted(epics_dir.glob('*.md')):
        if file_path.name == '_index.md':
            continue
        try:
            epic = parse_epic_file(file_path)
            if epic is not None:
                epics.append(epic)
        except Exception as e:
            print(f"Warning: Error parsing {file_path}: {e}", file=sys.stderr)
    return epics


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Get all issues and epics")
    parser.add_argument('--status', '-s', type=str, help="Filter by status (case-insensitive)")
    args = parser.parse_args()

    repo_root = get_repo_root()
    issues_dir = repo_root / "issues"
    epics_dir = repo_root / "epics"

    issues_exist = issues_dir.is_dir()
    epics_exist = epics_dir.is_dir()

    if not issues_exist and not epics_exist:
        print("Error: Neither issues/ nor epics/ directory found", file=sys.stderr)
        sys.exit(1)

    if not issues_exist:
        print("Warning: issues/ directory not found", file=sys.stderr)
        issues = []
    else:
        issues = get_all_issues(issues_dir)

    if not epics_exist:
        print("Warning: epics/ directory not found", file=sys.stderr)
        epics = []
    else:
        epics = get_all_epics(epics_dir)

    # Apply status filtering
    if args.status:
        status_filter = args.status.lower()
        issues = [i for i in issues if i.get('status', '').lower() == status_filter]
        epics = [e for e in epics if e.get('status', '').lower() == status_filter]

    print(json.dumps({"issues": issues, "epics": epics}, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
