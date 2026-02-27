"""
Team Member Retrieval Module

This module provides functionality to retrieve and parse team member
information from the team.md file in the planning repository.
"""

from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class TeamMember:
    """Represents a team member with their details."""

    username: str
    name: str
    role: str
    capacity: str

    def __repr__(self) -> str:
        return f"TeamMember(username='{self.username}', name='{self.name}', role='{self.role}', capacity='{self.capacity}')"

    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary."""
        return {
            "username": self.username,
            "name": self.name,
            "role": self.role,
            "capacity": self.capacity,
        }


def get_team_members(file_path: Optional[str] = None) -> List[TeamMember]:
    """
    Retrieve all team members from the team.md file.

    Args:
        file_path: Optional path to the team.md file. If not provided,
                   will look for team.md in the current directory.

    Returns:
        List of TeamMember objects representing all team members.

    Raises:
        FileNotFoundError: If the team.md file is not found.
        ValueError: If the file format is invalid.
    """
    team_file: Path
    if file_path is None:
        team_file = Path(__file__).parent / "team.md"
    else:
        team_file = Path(file_path)

    if not team_file.exists():
        raise FileNotFoundError(f"Team file not found: {team_file}")

    with open(team_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse the markdown table for team members
    members = parse_team_table(content)

    return members


def parse_team_table(markdown_content: str) -> List[TeamMember]:
    """
    Parse team member information from markdown table format.

    Args:
        markdown_content: The raw markdown content containing the team table.

    Returns:
        List of TeamMember objects.
    """
    members = []

    # Split content into lines
    lines = markdown_content.split("\n")

    # Find the table and parse it
    in_table = False

    for line in lines:
        stripped = line.strip()

        # Detect table start (looking for | at start and end)
        if stripped.startswith("|") and stripped.endswith("|"):
            # Skip header separator line (contains |---|)
            if "---" in stripped and not in_table:
                in_table = True
                # Parse headers from previous line
                continue

            if in_table and "---" not in stripped:
                # Parse data row
                cells = [cell.strip() for cell in stripped.strip("|").split("|")]

                if len(cells) >= 4:
                    # Remove @ symbol from username if present
                    username = cells[0].lstrip("@")
                    name = cells[1]
                    role = cells[2]
                    capacity = cells[3]

                    member = TeamMember(
                        username=username, name=name, role=role, capacity=capacity
                    )
                    members.append(member)
        elif in_table and not stripped.startswith("|"):
            # Table ended
            break

    return members


def get_member_by_username(
    username: str, file_path: Optional[str] = None
) -> Optional[TeamMember]:
    """
    Get a specific team member by their username.

    Args:
        username: The username to search for (without @ symbol).
        file_path: Optional path to the team.md file.

    Returns:
        TeamMember object if found, None otherwise.
    """
    members = get_team_members(file_path)

    for member in members:
        if member.username.lower() == username.lower():
            return member

    return None


def get_members_by_role(role: str, file_path: Optional[str] = None) -> List[TeamMember]:
    """
    Get all team members with a specific role.

    Args:
        role: The role to filter by.
        file_path: Optional path to the team.md file.

    Returns:
        List of TeamMember objects with the specified role.
    """
    members = get_team_members(file_path)

    return [member for member in members if member.role.lower() == role.lower()]


def get_all_roles(file_path: Optional[str] = None) -> List[str]:
    """
    Get all unique roles in the team.

    Args:
        file_path: Optional path to the team.md file.

    Returns:
        List of unique role names.
    """
    members = get_team_members(file_path)

    roles = set()
    for member in members:
        roles.add(member.role)

    return sorted(list(roles))


def print_team_roster(file_path: Optional[str] = None) -> None:
    """
    Print a formatted roster of all team members.

    Args:
        file_path: Optional path to the team.md file.
    """
    members = get_team_members(file_path)

    print("\n" + "=" * 60)
    print("TEAM ROSTER")
    print("=" * 60)
    print(f"{'Username':<15} {'Name':<20} {'Role':<25} {'Capacity'}")
    print("-" * 60)

    for member in members:
        print(
            f"@{member.username:<14} {member.name:<20} {member.role:<25} {member.capacity}"
        )

    print("-" * 60)
    print(f"Total Members: {len(members)}")
    print("=" * 60 + "\n")


# Example usage
if __name__ == "__main__":
    # Print the full team roster
    print_team_roster()

    # Demonstrate individual lookups
    print("\nSearching for 'dinhlongviolin1':")
    member = get_member_by_username("dinhlongviolin1")
    if member:
        print(f"  Found: {member}")

    print("\nAll Engineers:")
    engineers = get_members_by_role("Software Engineer")
    for eng in engineers:
        print(f"  - {eng.name} (@{eng.username})")

    print("\nAll unique roles:")
    for role in get_all_roles():
        print(f"  - {role}")
