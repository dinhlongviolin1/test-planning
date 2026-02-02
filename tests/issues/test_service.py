"""Tests for the GitHub service."""

import time
from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

from issues.models import Issue
from issues.service import GitHubAPIError, GitHubService, RateLimitError


class TestGitHubService:
    """Tests for the GitHubService class."""

    @pytest.fixture
    def mock_session(self):
        """Create a mock requests session."""
        with patch("issues.service.requests.Session") as mock:
            session = MagicMock()
            mock.return_value = session
            yield session

    @pytest.fixture
    def service(self, mock_session):
        """Create a GitHubService with mocked session."""
        return GitHubService(token="test-token")

    def test_init_with_token(self, mock_session):
        """Test initialization with a token."""
        mock_session.headers = {}
        service = GitHubService(token="my-token")
        assert service.session.headers["Authorization"] == "token my-token"

    def test_init_from_env(self, mock_session):
        """Test initialization falling back to environment variable."""
        mock_session.headers = {}
        with patch.dict("os.environ", {"GITHUB_TOKEN": "env-token"}):
            service = GitHubService()
            assert service.session.headers["Authorization"] == "token env-token"

    def test_make_request_success(self, service, mock_session):
        """Test successful API request."""
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {"key": "value"}
        mock_session.get.return_value = mock_response

        response = service._make_request("https://api.github.com/test")

        assert response == mock_response
        mock_session.get.assert_called_once_with(
            "https://api.github.com/test", params=None
        )

    def test_make_request_rate_limit(self, service, mock_session):
        """Test handling of rate limit error."""
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.headers = {"X-RateLimit-Reset": str(int(time.time()) + 60)}
        mock_session.get.return_value = mock_response

        with pytest.raises(RateLimitError) as exc_info:
            service._make_request("https://api.github.com/test")

        assert "retry after" in str(exc_info.value).lower()

    def test_make_request_unauthorized(self, service, mock_session):
        """Test handling of unauthorized error."""
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_session.get.return_value = mock_response

        with pytest.raises(GitHubAPIError) as exc_info:
            service._make_request("https://api.github.com/test")

        assert "unauthorized" in str(exc_info.value).lower()

    def test_make_request_not_found(self, service, mock_session):
        """Test handling of not found error."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_session.get.return_value = mock_response

        with pytest.raises(GitHubAPIError) as exc_info:
            service._make_request("https://api.github.com/test")

        assert exc_info.value.status_code == 404

    def test_get_issues_success(self, service, mock_session):
        """Test fetching issues from a repository."""
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = [
            {
                "number": 1,
                "title": "Issue 1",
                "state": "open",
                "created_at": "2026-01-01T00:00:00Z",
                "updated_at": "2026-01-01T00:00:00Z",
                "closed_at": None,
                "body": None,
                "html_url": "https://github.com/user/repo/issues/1",
                "user": {"login": "user1"},
                "labels": [],
                "assignees": [],
                "comments": 0,
            },
            {
                "number": 2,
                "title": "Issue 2",
                "state": "closed",
                "created_at": "2026-01-02T00:00:00Z",
                "updated_at": "2026-01-02T00:00:00Z",
                "closed_at": "2026-01-03T00:00:00Z",
                "body": "Fixed",
                "html_url": "https://github.com/user/repo/issues/2",
                "user": {"login": "user2"},
                "labels": [{"name": "bug"}],
                "assignees": [{"login": "dev1"}],
                "comments": 3,
            },
        ]
        mock_response.links = {}
        mock_session.get.return_value = mock_response

        issues = service.get_issues("dinhlongviolin1", "test-planning")

        assert len(issues) == 2
        assert isinstance(issues[0], Issue)
        assert issues[0].number == 1
        assert issues[1].number == 2

    def test_get_issues_pagination(self, service, mock_session):
        """Test handling of paginated results."""
        # First page
        page1_response = MagicMock()
        page1_response.ok = True
        page1_response.json.return_value = [
            {"number": 1, "title": "Issue 1", "state": "open",
             "created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-01T00:00:00Z",
             "closed_at": None, "body": None, "html_url": "",
             "user": {"login": ""}, "labels": [], "assignees": [], "comments": 0}
        ]
        page1_response.links = {
            "next": {"url": "https://api.github.com/repos/user/repo/issues?page=2"}
        }

        # Second page
        page2_response = MagicMock()
        page2_response.ok = True
        page2_response.json.return_value = [
            {"number": 2, "title": "Issue 2", "state": "open",
             "created_at": "2026-01-02T00:00:00Z", "updated_at": "2026-01-02T00:00:00Z",
             "closed_at": None, "body": None, "html_url": "",
             "user": {"login": ""}, "labels": [], "assignees": [], "comments": 0}
        ]
        page2_response.links = {}

        mock_session.get.side_effect = [page1_response, page2_response]

        issues = service.get_issues("user", "repo")

        assert len(issues) == 2
        assert mock_session.get.call_count == 2

    def test_get_issues_invalid_state(self, service):
        """Test that invalid state raises ValueError."""
        with pytest.raises(ValueError):
            service.get_issues("user", "repo", state="invalid")

    def test_get_issue_success(self, service, mock_session):
        """Test fetching a single issue."""
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "number": 42,
            "title": "Specific Issue",
            "state": "open",
            "created_at": "2026-01-15T10:30:00Z",
            "updated_at": "2026-01-16T14:20:00Z",
            "closed_at": None,
            "body": "Issue details",
            "html_url": "https://github.com/user/repo/issues/42",
            "user": {"login": "testuser"},
            "labels": [{"name": "help wanted"}],
            "assignees": [{"login": "dev1"}],
            "comments": 10,
        }
        mock_session.get.return_value = mock_response

        issue = service.get_issue("user", "repo", 42)

        assert issue.number == 42
        assert issue.title == "Specific Issue"
        assert issue.comments_count == 10