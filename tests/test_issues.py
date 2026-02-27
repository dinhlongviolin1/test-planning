"""
Tests for the issues.py module.
"""

from pathlib import Path
import sys

# Add repo root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from issues import (
    Issue,
    get_issues,
    get_issue_by_id,
    get_issues_by_status,
    get_issues_by_assignee,
    parse_markdown_meta,
    parse_title_section,
    parse_description_section,
)


class TestIssue:
    """Test the Issue dataclass."""

    def test_issue_creation(self):
        """Test creating an Issue object."""
        issue = Issue(
            id="i-001",
            status="todo",
            created="2026-01-30",
            updated="2026-01-30",
            points="5",
            assignee="dinhlongviolin1",
            title="Test Issue",
            description="Test description",
        )

        assert issue.id == "i-001"
        assert issue.status == "todo"
        assert issue.assignee == "dinhlongviolin1"

    def test_issue_to_dict(self):
        """Test converting Issue to dictionary."""
        issue = Issue(
            id="i-001",
            status="todo",
            created="2026-01-30",
            updated="2026-01-30",
            points="5",
            assignee="dinhlongviolin1",
            title="Test Issue",
            description="Test description",
        )

        result = issue.to_dict()

        assert result["id"] == "i-001"
        assert result["status"] == "todo"
        assert result["title"] == "Test Issue"


class TestParseFunctions:
    """Test parsing functions."""

    def test_parse_markdown_meta(self):
        """Test parsing Meta table from markdown."""
        content = """# Meta
| Field | Value |
|-------|-------|
| ID | i-001 |
| Status | todo |
| Created | 2026-01-30 |

## Title
Test Title
"""
        meta = parse_markdown_meta(content)

        assert meta["ID"] == "i-001"
        assert meta["Status"] == "todo"
        assert meta["Created"] == "2026-01-30"

    def test_parse_title_section(self):
        """Test parsing Title section."""
        content = """## Title
Design database architecture

## Description
Some description
"""
        title = parse_title_section(content)
        assert "Design database architecture" in title

    def test_parse_description_section(self):
        """Test parsing Description section."""
        content = """## Description
This is a test description.

## Linked Epics
- epic 1
"""
        desc = parse_description_section(content)
        assert "test description" in desc


class TestGetIssues:
    """Test get_issues function."""

    def test_get_all_issues(self):
        """Test retrieving all issues."""
        issues = get_issues()

        assert len(issues) > 0
        assert all(isinstance(i, Issue) for i in issues)

    def test_issues_have_required_fields(self):
        """Test that all issues have required fields."""
        issues = get_issues()

        for issue in issues:
            assert issue.id.startswith("i-")
            assert issue.status
            assert issue.title


class TestGetIssueById:
    """Test get_issue_by_id function."""

    def test_get_existing_issue(self):
        """Test retrieving an existing issue by ID."""
        issue = get_issue_by_id("i-001")

        assert issue is not None
        assert issue.id == "i-001"

    def test_get_nonexistent_issue(self):
        """Test retrieving a non-existent issue."""
        issue = get_issue_by_id("i-999")

        assert issue is None


class TestGetIssuesByStatus:
    """Test get_issues_by_status function."""

    def test_get_todo_issues(self):
        """Test filtering issues by todo status."""
        issues = get_issues_by_status("todo")

        assert all(i.status == "todo" for i in issues)

    def test_get_in_progress_issues(self):
        """Test filtering issues by in_progress status."""
        issues = get_issues_by_status("in_progress")

        assert all(i.status == "in_progress" for i in issues)


class TestGetIssuesByAssignee:
    """Test get_issues_by_assignee function."""

    def test_filter_by_assignee(self):
        """Test filtering issues by assignee."""
        issues = get_issues_by_assignee("dinhlongviolin1")

        assert all(i.assignee == "dinhlongviolin1" for i in issues)
        assert len(issues) > 0
