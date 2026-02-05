"""
Tests for get_all_users() function.
"""

import os
import tempfile
from pathlib import Path
from team_members import get_all_users, TeamMember


class TestGetAllUsers:
    """Test cases for get_all_users function."""

    def test_get_all_users_returns_list(self):
        """Test that get_all_users returns a list."""
        result = get_all_users()
        assert isinstance(result, list)

    def test_get_all_users_returns_team_members(self):
        """Test that get_all_users returns TeamMember objects."""
        result = get_all_users()
        assert len(result) > 0
        for member in result:
            assert isinstance(member, TeamMember)

    def test_get_all_users_has_required_fields(self):
        """Test that each user has all required fields."""
        result = get_all_users()
        for member in result:
            assert hasattr(member, 'username')
            assert hasattr(member, 'name')
            assert hasattr(member, 'role')
            assert hasattr(member, 'capacity')
            assert member.username  # Not empty
            assert member.name  # Not empty
            assert member.role  # Not empty

    def test_get_all_users_handles_custom_file_path(self):
        """Test that get_all_users works with a custom file path."""
        # Create a temporary team.md file
        test_content = """| Username | Name | Role | Capacity/Sprint |
|----------|------|------|-----------------|
| @testuser | Test User | Developer | 10 pts |
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(test_content)
            temp_path = f.name

        try:
            result = get_all_users(temp_path)
            assert len(result) == 1
            assert result[0].username == 'testuser'
            assert result[0].name == 'Test User'
            assert result[0].role == 'Developer'
        finally:
            os.unlink(temp_path)

    def test_get_all_users_raises_file_not_found(self):
        """Test that get_all_users raises FileNotFoundError for missing file."""
        try:
            get_all_users('/nonexistent/path/team.md')
            assert False, "Expected FileNotFoundError"
        except FileNotFoundError as e:
            assert "not found" in str(e).lower()

    def test_get_all_users_raises_value_error_for_empty_file(self):
        """Test that get_all_users raises ValueError for file with no users."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("# Team\n\n| Username | Name | Role | Capacity/Sprint |\n|----------|------|------|-----------------|\n")
            temp_path = f.name

        try:
            get_all_users(temp_path)
            assert False, "Expected ValueError"
        except ValueError as e:
            assert "no users" in str(e).lower() or "not found" in str(e).lower()
        finally:
            os.unlink(temp_path)

    def test_get_all_users_with_actual_team_data(self):
        """Test get_all_users with the actual team.md file."""
        result = get_all_users()
        assert len(result) >= 1  # At least one user exists

        # Check that known team members are present
        usernames = [m.username for m in result]
        assert 'dinhlongviolin1' in usernames
        assert 'faisal' in usernames