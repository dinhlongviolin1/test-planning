"""Tests for the Issue model."""

from datetime import datetime, timezone

import pytest

from issues.models import Issue


class TestIssue:
    """Tests for the Issue dataclass."""

    def test_from_github_api_with_all_fields(self):
        """Test creating an Issue from complete GitHub API response."""
        data = {
            "number": 123,
            "title": "Test Issue",
            "state": "open",
            "created_at": "2026-01-15T10:30:00Z",
            "updated_at": "2026-01-16T14:20:00Z",
            "closed_at": None,
            "body": "This is a test issue body",
            "html_url": "https://github.com/user/repo/issues/123",
            "user": {"login": "testuser"},
            "labels": [{"name": "bug"}, {"name": "enhancement"}],
            "assignees": [{"login": "developer1"}, {"login": "developer2"}],
            "comments": 5,
        }

        issue = Issue.from_github_api(data)

        assert issue.number == 123
        assert issue.title == "Test Issue"
        assert issue.state == "open"
        assert issue.body == "This is a test issue body"
        assert issue.html_url == "https://github.com/user/repo/issues/123"
        assert issue.user_login == "testuser"
        assert issue.labels == ["bug", "enhancement"]
        assert issue.assignees == ["developer1", "developer2"]
        assert issue.comments_count == 5
        assert issue.closed_at is None

    def test_from_github_api_with_closed_issue(self):
        """Test creating an Issue for a closed issue."""
        data = {
            "number": 456,
            "title": "Closed Issue",
            "state": "closed",
            "created_at": "2026-01-10T08:00:00Z",
            "updated_at": "2026-01-12T16:00:00Z",
            "closed_at": "2026-01-12T16:00:00Z",
            "body": None,
            "html_url": "https://github.com/user/repo/issues/456",
            "user": {"login": "anotheruser"},
            "labels": [],
            "assignees": [],
            "comments": 0,
        }

        issue = Issue.from_github_api(data)

        assert issue.number == 456
        assert issue.state == "closed"
        assert issue.closed_at == datetime(2026, 1, 12, 16, 0, 0, tzinfo=timezone.utc)
        assert issue.body is None
        assert issue.labels == []
        assert issue.assignees == []

    def test_from_github_api_with_minimal_fields(self):
        """Test creating an Issue with minimal fields."""
        data = {
            "number": 789,
            "title": "Minimal Issue",
            "state": "open",
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-01T00:00:00Z",
            "closed_at": None,
            "body": None,
            "html_url": "",
            "user": {"login": ""},
            "labels": [],
            "assignees": [],
            "comments": 0,
        }

        issue = Issue.from_github_api(data)

        assert issue.number == 789
        assert issue.title == "Minimal Issue"
        assert issue.user_login == ""