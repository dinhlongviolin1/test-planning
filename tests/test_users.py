"""
Tests for the team_members.py module.
"""

import pytest
from pathlib import Path
import sys

# Add repo root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from team_members import (
    TeamMember,
    get_team_members,
    get_member_by_username,
    get_members_by_role,
    get_all_roles,
    parse_team_table
)


class TestTeamMember:
    """Test the TeamMember dataclass."""

    def test_team_member_creation(self):
        """Test creating a TeamMember object."""
        member = TeamMember(
            username="testuser",
            name="Test User",
            role="Software Engineer",
            capacity="10 pts"
        )

        assert member.username == "testuser"
        assert member.name == "Test User"
        assert member.role == "Software Engineer"

    def test_team_member_to_dict(self):
        """Test converting TeamMember to dictionary."""
        member = TeamMember(
            username="testuser",
            name="Test User",
            role="Software Engineer",
            capacity="10 pts"
        )

        result = member.to_dict()

        assert result["username"] == "testuser"
        assert result["name"] == "Test User"
        assert result["role"] == "Software Engineer"


class TestParseTeamTable:
    """Test parse_team_table function."""

    def test_parse_valid_table(self):
        """Test parsing a valid team table."""
        content = """# Team Members

| Username | Name | Role | Capacity |
|----------|------|------|----------|
| @john | John Doe | Engineer | 10 pts |
| @jane | Jane Smith | Designer | 8 pts |
"""
        members = parse_team_table(content)

        assert len(members) == 2
        assert members[0].username == "john"
        assert members[1].username == "jane"


class TestGetTeamMembers:
    """Test get_team_members function."""

    def test_get_all_members(self):
        """Test retrieving all team members."""
        members = get_team_members()

        assert len(members) > 0
        assert all(isinstance(m, TeamMember) for m in members)

    def test_members_have_required_fields(self):
        """Test that all members have required fields."""
        members = get_team_members()

        for member in members:
            assert member.username
            assert member.name
            assert member.role


class TestGetMemberByUsername:
    """Test get_member_by_username function."""

    def test_get_existing_member(self):
        """Test retrieving an existing member."""
        member = get_member_by_username("dinhlongviolin1")

        assert member is not None
        assert member.username == "dinhlongviolin1"

    def test_get_nonexistent_member(self):
        """Test retrieving a non-existent member."""
        member = get_member_by_username("nonexistent")

        assert member is None


class TestGetMembersByRole:
    """Test get_members_by_role function."""

    def test_filter_by_role(self):
        """Test filtering members by role."""
        members = get_members_by_role("Researcher")

        assert all(m.role == "Researcher" for m in members)
        assert len(members) > 0


class TestGetAllRoles:
    """Test get_all_roles function."""

    def test_get_all_roles(self):
        """Test getting all unique roles."""
        roles = get_all_roles()

        assert len(roles) > 0
        assert all(isinstance(r, str) for r in roles)