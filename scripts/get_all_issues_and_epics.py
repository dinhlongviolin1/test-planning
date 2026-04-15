"""
Issues and Epics Utility Script

This script provides functions to read and parse all issue and epic files
from the planning repository. Issues are stored in issues/i-XXX.md and
epics in epics/e-XXX.md, using markdown meta tables for metadata.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field


def get_repo_root() -> Path:
    """Get the root directory of the repository."""
    current = Path(__file__).resolve()
    return current.parent.parent


def parse_meta_table(content: str) -> Dict[str, str]:
    """
    Extract all key-value pairs from a # Meta markdown table.

    Finds the '# Meta' heading, then reads the '| Field | Value |' table rows.
    Skips the header row and separator lines.

    Args:
        content: Full file content as a string.

    Returns:
        Dict mapping field names to their values.
    """
    meta = {}
    lines = content.split('\n')

    in_meta = False
    header_seen = False

    for line in lines:
        stripped = line.strip()

        # Detect start of meta section (supports both '# Meta' and '## Meta')
        if stripped in ('# Meta', '## Meta'):
            in_meta = True
            continue

        if not in_meta:
            continue

        # Stop at next heading
        if re.match(r'^#{1,6}\s+', stripped) and stripped not in ('# Meta', '## Meta'):
            break

        # Skip empty lines within the meta section
        if not stripped:
            if header_seen:
                break
            continue

        # Skip separator lines (e.g., |-------|-------|)
        if re.match(r'^[\s|:-]+$', stripped) and '-' in stripped:
            continue

        # Must be a table row
        if stripped.startswith('|'):
            cells = [cell.strip() for cell in stripped.strip('|').split('|')]
            if len(cells) >= 2:
                field_name = cells[0].strip()
                value = cells[1].strip()

                # Skip the header row
                if field_name.lower() == 'field' and value.lower() == 'value':
                    header_seen = True
                    continue

                if field_name:
                    meta[field_name] = value

    return meta


def parse_sections(content: str) -> Dict[str, str]:
    """
    Split file content by ## headings and return a dict of heading -> body text.

    Args:
        content: Full file content as a string.

    Returns:
        Dict mapping section heading names to their body text (stripped).
    """
    sections = {}
    lines = content.split('\n')
    current_heading = None
    current_lines: List[str] = []

    for line in lines:
        stripped = line.strip()
        # Match ## headings but not # Meta or ### subheadings
        match = re.match(r'^##\s+(.+)$', stripped)
        if match:
            # Save the previous section
            if current_heading is not None:
                sections[current_heading] = '\n'.join(current_lines).strip()
            current_heading = match.group(1).strip()
            current_lines = []
        elif current_heading is not None:
            current_lines.append(line.rstrip())

    # Save the last section
    if current_heading is not None:
        sections[current_heading] = '\n'.join(current_lines).strip()

    return sections


def parse_list_items(text: str) -> List[str]:
    """
    Extract bullet list items from section text.

    Args:
        text: Section body text.

    Returns:
        List of item strings (with leading '- ' removed).
    """
    items = []
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('- '):
            items.append(stripped[2:].strip())
    return items


def parse_tasks(text: str) -> List[Dict[str, Any]]:
    """
    Parse task checkboxes from a section.

    Args:
        text: Section body text containing '- [ ]' or '- [x]' items.

    Returns:
        List of dicts with 'task' (str) and 'done' (bool) keys.
    """
    tasks = []
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('- [x] ') or stripped.startswith('- [X] '):
            tasks.append({"task": stripped[6:].strip(), "done": True})
        elif stripped.startswith('- [ ] '):
            tasks.append({"task": stripped[6:].strip(), "done": False})
    return tasks


@dataclass
class Issue:
    """Represents a parsed issue file."""
    id: str = ""
    status: str = ""
    created: str = ""
    updated: str = ""
    points: Optional[str] = None
    assignee: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    linked_epics: List[str] = field(default_factory=list)
    linked_sprint: List[str] = field(default_factory=list)
    linked_milestone: List[str] = field(default_factory=list)
    target_repo: Optional[str] = None
    tasks: List[Dict[str, Any]] = field(default_factory=list)
    notes: Optional[str] = None
    raw_meta: Dict[str, str] = field(default_factory=dict)
    raw_sections: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        result: Dict[str, Any] = {}
        result["id"] = self.id
        result["status"] = self.status
        result["created"] = self.created
        result["updated"] = self.updated
        result["points"] = self.points
        result["assignee"] = self.assignee
        result["title"] = self.title
        result["description"] = self.description
        result["linked_epics"] = self.linked_epics
        result["linked_sprint"] = self.linked_sprint
        result["linked_milestone"] = self.linked_milestone
        result["target_repo"] = self.target_repo
        result["tasks"] = self.tasks
        result["notes"] = self.notes
        # Include any extra meta fields not explicitly modeled
        excluded = {k.lower() for k in result.keys()}
        for key, value in self.raw_meta.items():
            if key.lower() not in excluded:
                result[key] = value
        return result


@dataclass
class Epic:
    """Represents a parsed epic file."""
    id: str = ""
    status: str = ""
    created: str = ""
    updated: str = ""
    owner: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    related_issues: List[str] = field(default_factory=list)
    raw_meta: Dict[str, str] = field(default_factory=dict)
    raw_sections: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        result: Dict[str, Any] = {}
        result["id"] = self.id
        result["status"] = self.status
        result["created"] = self.created
        result["updated"] = self.updated
        result["owner"] = self.owner
        result["title"] = self.title
        result["description"] = self.description
        result["related_issues"] = self.related_issues
        # Include any extra meta fields not explicitly modeled
        excluded = {k.lower() for k in result.keys()}
        for key, value in self.raw_meta.items():
            if key.lower() not in excluded:
                result[key] = value
        return result


@dataclass
class Agent:
    """Represents a parsed agents.md file."""
    id: str = ""
    title: Optional[str] = None
    description: Optional[str] = None
    status: str = ""
    created: str = ""
    updated: str = ""
    capabilities: List[str] = field(default_factory=list)
    instructions: Optional[str] = None
    raw_meta: Dict[str, str] = field(default_factory=dict)
    raw_sections: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        result: Dict[str, Any] = {}
        result["id"] = self.id
        result["title"] = self.title
        result["description"] = self.description
        result["status"] = self.status
        result["created"] = self.created
        result["updated"] = self.updated
        result["capabilities"] = self.capabilities
        result["instructions"] = self.instructions
        # Include any extra meta fields not explicitly modeled
        excluded = {k.lower() for k in result.keys()}
        for key, value in self.raw_meta.items():
            if key.lower() not in excluded:
                result[key] = value
        return result


def parse_issue_file(file_path: Path) -> Optional[Issue]:
    """
    Read an issue file and parse its meta table and content sections.

    Args:
        file_path: Path to the issue markdown file.

    Returns:
        Issue object if successfully parsed, None if malformed.
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except OSError as e:
        print(f"Warning: could not read {file_path}: {e}", file=sys.stderr)
        return None

    meta = parse_meta_table(content)
    if not meta:
        print(f"Warning: malformed or missing meta table in {file_path}", file=sys.stderr)
        return None

    sections = parse_sections(content)

    issue = Issue(
        id=meta.get("ID", ""),
        status=meta.get("Status", ""),
        created=meta.get("Created", ""),
        updated=meta.get("Updated", ""),
        points=meta.get("Points"),
        assignee=meta.get("Assignee"),
        title=sections.get("Title"),
        description=sections.get("Description"),
        linked_epics=parse_list_items(sections.get("Linked Epics", "")),
        linked_sprint=parse_list_items(sections.get("Linked Sprint", "")),
        linked_milestone=parse_list_items(sections.get("Linked Milestone", "")),
        target_repo=sections.get("Target Repo"),
        tasks=parse_tasks(sections.get("Tasks", "")),
        notes=sections.get("Notes"),
        raw_meta=meta,
        raw_sections=sections,
    )
    return issue


def parse_epic_file(file_path: Path) -> Optional[Epic]:
    """
    Read an epic file and parse its meta table and content sections.

    Args:
        file_path: Path to the epic markdown file.

    Returns:
        Epic object if successfully parsed, None if malformed.
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except OSError as e:
        print(f"Warning: could not read {file_path}: {e}", file=sys.stderr)
        return None

    meta = parse_meta_table(content)
    if not meta:
        print(f"Warning: malformed or missing meta table in {file_path}", file=sys.stderr)
        return None

    sections = parse_sections(content)

    epic = Epic(
        id=meta.get("ID", ""),
        status=meta.get("Status", ""),
        created=meta.get("Created", ""),
        updated=meta.get("Updated", ""),
        owner=meta.get("Owner"),
        title=sections.get("Title"),
        description=sections.get("Description"),
        related_issues=parse_list_items(sections.get("Related Issues", "")),
        raw_meta=meta,
        raw_sections=sections,
    )
    return epic


def get_all_issues(status_filter: Optional[str] = None) -> List[Issue]:
    """
    Read and parse all issue files from the issues/ directory.

    Args:
        status_filter: If provided, only return issues matching this status
                       (case-insensitive).

    Returns:
        List of Issue objects.
    """
    issues_dir = get_repo_root() / "issues"
    if not issues_dir.is_dir():
        return []

    issues = []
    for file_path in sorted(issues_dir.glob("i-*.md")):
        issue = parse_issue_file(file_path)
        if issue is None:
            continue
        if status_filter and issue.status.lower() != status_filter.lower():
            continue
        issues.append(issue)

    return issues


def get_all_epics(status_filter: Optional[str] = None) -> List[Epic]:
    """
    Read and parse all epic files from the epics/ directory.

    Args:
        status_filter: If provided, only return epics matching this status
                       (case-insensitive).

    Returns:
        List of Epic objects.
    """
    epics_dir = get_repo_root() / "epics"
    if not epics_dir.is_dir():
        return []

    epics = []
    for file_path in sorted(epics_dir.glob("e-*.md")):
        epic = parse_epic_file(file_path)
        if epic is None:
            continue
        if status_filter and epic.status.lower() != status_filter.lower():
            continue
        epics.append(epic)

    return epics


def parse_agents_file(file_path: Path) -> Optional[Agent]:
    """
    Read an agents.md file and parse its meta table and content sections.

    Args:
        file_path: Path to the agents.md file.

    Returns:
        Agent object if successfully parsed, None if malformed.
    """
    try:
        content = file_path.read_text(encoding='utf-8')
    except OSError as e:
        print(f"Warning: could not read {file_path}: {e}", file=sys.stderr)
        return None

    meta = parse_meta_table(content)
    if not meta:
        print(f"Warning: malformed or missing meta table in {file_path}", file=sys.stderr)
        return None

    sections = parse_sections(content)

    agent = Agent(
        id=meta.get("ID", ""),
        status=meta.get("Status", ""),
        created=meta.get("Created", ""),
        updated=meta.get("Updated", ""),
        title=sections.get("Title"),
        description=sections.get("Description"),
        capabilities=parse_list_items(sections.get("Capabilities", "")),
        instructions=sections.get("Instructions"),
        raw_meta=meta,
        raw_sections=sections,
    )
    return agent


def get_all_agents(status_filter: Optional[str] = None) -> List[Agent]:
    """
    Read and parse the agents.md file from the repo root.

    Args:
        status_filter: If provided, only return agents matching this status
                       (case-insensitive).

    Returns:
        List of Agent objects.
    """
    repo_root = get_repo_root()
    agents_file = repo_root / "agents.md"
    if not agents_file.is_file():
        return []

    agent = parse_agents_file(agents_file)
    if agent is None:
        return []
    if status_filter and agent.status.lower() != status_filter.lower():
        return []

    return [agent]


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Get all issues and epics")
    parser.add_argument('--status', '-s', type=str, help="Filter by status (case-insensitive)")
    args = parser.parse_args()

    try:
        issues = get_all_issues(status_filter=args.status)
        epics = get_all_epics(status_filter=args.status)
        agents = get_all_agents(status_filter=args.status)

        output = {
            "issues": [i.to_dict() for i in issues],
            "epics": [e.to_dict() for e in epics],
            "agents": [a.to_dict() for a in agents],
        }
        print(json.dumps(output, indent=2))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
