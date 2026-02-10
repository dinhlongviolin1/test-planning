#!/usr/bin/env python3
"""
Get All Users - Enhanced User Retrieval Script

This script demonstrates how to retrieve all users from the team.md data source
using the existing team_members.py module. It provides a clean, educational
example of user retrieval patterns.

Usage:
    PYTHONPATH=/workspace/repo python3 scripts/get_all_users.py

The script shows:
    - Getting all users
    - Getting a specific user by username
    - Filtering users by role
    - Working with TeamMember dataclass
"""

import sys
from pathlib import Path

# Add the repository root to the Python path for imports
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from team_members import (
    get_team_members,
    get_member_by_username,
    get_members_by_role,
    get_all_roles,
    TeamMember
)


def get_all_users(file_path: str | None = None) -> list[TeamMember]:
    """
    Retrieve all users from the team.md data source.

    This function serves as the primary entry point for fetching user data.
    It wraps the underlying team_members.get_team_members() function with
    clear documentation and error handling.

    Args:
        file_path: Optional path to the team.md file. If not provided,
                   uses the default location in the repository root.

    Returns:
        A list of TeamMember objects representing all users in the data source.

    Raises:
        FileNotFoundError: If the team.md file cannot be found.
        ValueError: If the file contains invalid data.

    Example:
        >>> users = get_all_users()
        >>> for user in users:
        ...     print(f"{user.name} (@{user.username})")
    """
    members = get_team_members(file_path)
    return members


def get_user(username: str, file_path: str | None = None) -> TeamMember | None:
    """
    Retrieve a specific user by their username.

    Args:
        username: The username to search for (without @ prefix).
        file_path: Optional path to the team.md file.

    Returns:
        The TeamMember object if found, None otherwise.

    Example:
        >>> user = get_user("alice")
        >>> if user:
        ...     print(f"Found: {user.name}")
    """
    return get_member_by_username(username, file_path)


def get_users_by_role(role: str, file_path: str | None = None) -> list[TeamMember]:
    """
    Retrieve all users with a specific role.

    Args:
        role: The role to filter by (case-insensitive).
        file_path: Optional path to the team.md file.

    Returns:
        A list of TeamMember objects matching the specified role.

    Example:
        >>> engineers = get_users_by_role("Software Engineer")
        >>> for eng in engineers:
        ...     print(f"{eng.name}: {eng.role}")
    """
    return get_members_by_role(role, file_path)


def format_user(user: TeamMember) -> str:
    """
    Format a user for display.

    Args:
        user: The TeamMember object to format.

    Returns:
        A formatted string representation of the user.

    Example:
        >>> user = get_user("alice")
        >>> print(format_user(user))
    """
    return f"@{user.username} | {user.name} | {user.role} | Capacity: {user.capacity}"


def print_users_table(users: list[TeamMember]) -> None:
    """
    Print a formatted table of users.

    Args:
        users: List of TeamMember objects to display.
    """
    if not users:
        print("No users found.")
        return

    print("\n" + "=" * 70)
    print(f"{'Username':<15} {'Name':<20} {'Role':<25} {'Capacity':<10}")
    print("=" * 70)

    for user in users:
        print(f"@{user.username:<13} {user.name:<20} {user.role:<25} {user.capacity:<10}")

    print("=" * 70)
    print(f"Total users: {len(users)}\n")


def main():
    """
    Main entry point demonstrating user retrieval patterns.

    This function showcases various ways to retrieve and display user data
    using the team_members.py module.
    """
    print("=" * 70)
    print("GET ALL USERS - Example Script")
    print("=" * 70)

    try:
        # Example 1: Get all users
        print("\n[1] Getting all users...")
        all_users = get_all_users()

        if all_users:
            print_users_table(all_users)
        else:
            print("No users found in the data source.")

        # Example 2: Get a specific user
        print("\n[2] Getting a specific user (alice)...")
        user = get_user("alice")
        if user:
            print(f"Found: {format_user(user)}")
        else:
            print("User 'alice' not found.")

        # Example 3: Filter by role
        print("\n[3] Filtering users by role (Engineer)...")
        engineers = get_users_by_role("Engineer")
        if engineers:
            print(f"Found {len(engineers)} engineers:")
            for eng in engineers:
                print(f"  - {eng.name} (@{eng.username})")
        else:
            print("No engineers found.")

        # Example 4: Get all unique roles
        print("\n[4] All unique roles in the team...")
        roles = get_all_roles()
        if roles:
            print(f"Roles: {', '.join(roles)}")
        else:
            print("No roles found.")

        # Example 5: Display summary statistics
        print("\n[5] Team Summary...")
        print(f"  Total users: {len(all_users)}")
        role_counts = {}
        for user in all_users:
            role_counts[user.role] = role_counts.get(user.role, 0) + 1
        for role, count in sorted(role_counts.items()):
            print(f"  {role}: {count}")

    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print("Please ensure team.md exists in the repository root.")
    except ValueError as e:
        print(f"\nError: {e}")
        print("The team.md file may have an invalid format.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()