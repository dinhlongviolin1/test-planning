#!/usr/bin/env python3
"""
User Retrieval Script

This script demonstrates how to fetch all users from the team.md data source.
It provides both a programmatic API and a command-line interface.

Usage:
    python get_users.py              # Print all users
    python get_users.py --json       # Output as JSON
    python get_users.py --username alice  # Get specific user
    python get_users.py --role "Engineer"  # Filter by role
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass


# Default path to the team data source
DEFAULT_TEAM_FILE = Path(__file__).parent.parent / "team.md"


@dataclass
class User:
    """
    Represents a user with their details.

    Attributes:
        username: Unique identifier for the user (without @ prefix).
        name: Full name of the user.
        role: Job role or title of the user.
        capacity: Work capacity or points allocation per sprint.
    """
    username: str
    name: str
    role: str
    capacity: str

    def to_dict(self) -> Dict[str, str]:
        """Convert the User object to a dictionary."""
        return {
            "username": self.username,
            "name": self.name,
            "role": self.role,
            "capacity": self.capacity
        }

    def __str__(self) -> str:
        return f"@{self.username} ({self.name}) - {self.role}"


class UserNotFoundError(Exception):
    """Raised when a requested user is not found."""
    pass


class InvalidDataError(Exception):
    """Raised when the data source has invalid format."""
    pass


def get_users(file_path: Optional[str] = None) -> List[User]:
    """
    Retrieve all users from the team.md data source.

    This function reads the team.md file and parses the markdown table
    to extract user information. It demonstrates how to fetch users
    from a structured data source.

    Args:
        file_path: Optional path to the team.md file. If not provided,
                   uses the default location in the repository root.

    Returns:
        List of User objects representing all users in the data source.

    Raises:
        FileNotFoundError: If the data source file does not exist.
        InvalidDataError: If the file format is invalid or unparseable.
    """
    # Determine the file path to use
    if file_path is None:
        data_path = DEFAULT_TEAM_FILE
    else:
        data_path = Path(file_path)

    # Validate that the file exists
    if not data_path.exists():
        raise FileNotFoundError(
            f"User data source not found: {data_path}. "
            "Please ensure team.md exists in the repository root."
        )

    # Read and parse the data source
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except IOError as e:
        raise IOError(f"Failed to read user data source: {e}")

    # Parse markdown table format
    users = _parse_user_table(content)

    if not users:
        raise InvalidDataError(
            f"No users found in {data_path}. "
            "Please ensure the file contains a valid user table."
        )

    return users


def get_user_by_username(username: str, file_path: Optional[str] = None) -> User:
    """
    Retrieve a specific user by their username.

    Demonstrates how to fetch a single user from the data source
    with case-insensitive username matching.

    Args:
        username: The username to search for (without @ prefix).
        file_path: Optional path to the team.md file.

    Returns:
        The User object matching the username.

    Raises:
        UserNotFoundError: If no user with the given username exists.
        FileNotFoundError: If the data source file does not exist.
    """
    users = get_users(file_path)

    # Case-insensitive search for the user
    for user in users:
        if user.username.lower() == username.lower():
            return user

    raise UserNotFoundError(
        f"User '{username}' not found in the data source. "
        f"Available users: {', '.join(u.username for u in users)}"
    )


def get_users_by_role(role: str, file_path: Optional[str] = None) -> List[User]:
    """
    Retrieve all users with a specific role.

    Demonstrates how to filter users from the data source
    by their role attribute.

    Args:
        role: The role to filter by (case-insensitive).
        file_path: Optional path to the team.md file.

    Returns:
        List of User objects with the specified role.
    """
    users = get_users(file_path)
    return [user for user in users if user.role.lower() == role.lower()]


def _parse_user_table(markdown_content: str) -> List[User]:
    """
    Parse user information from markdown table format.

    Internal helper function that extracts user records from
    the markdown table structure in the team.md file.

    Args:
        markdown_content: The raw markdown content containing the user table.

    Returns:
        List of User objects parsed from the table.

    Raises:
        InvalidDataError: If the table format is invalid.
    """
    users = []
    lines = markdown_content.split('\n')

    # State machine to track table parsing
    in_table = False
    header_found = False

    for line in lines:
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            continue

        # Detect table start by looking for | at start and end
        if stripped.startswith('|') and stripped.endswith('|'):
            # Check for header separator line (contains ---)
            if '---' in stripped and not header_found:
                # This is the separator line after headers
                in_table = True
                header_found = True
                continue

            if in_table and header_found:
                # Parse a data row
                cells = [cell.strip() for cell in stripped.strip('|').split('|')]

                # Expecting: username, name, role, capacity (4 columns)
                if len(cells) >= 4:
                    # Remove @ prefix from username if present
                    username = cells[0].lstrip('@')
                    name = cells[1]
                    role = cells[2]
                    capacity = cells[3]

                    users.append(User(
                        username=username,
                        name=name,
                        role=role,
                        capacity=capacity
                    ))
        elif in_table and not stripped.startswith('|'):
            # We've exited the table
            break

    return users


def print_users(users: Optional[List[User]] = None,
                file_path: Optional[str] = None) -> None:
    """
    Print users in a formatted table.

    Args:
        users: List of User objects. If None, fetches all users.
        file_path: Optional path to the team.md file.
    """
    if users is None:
        users = get_users(file_path)

    if not users:
        print("No users found.")
        return

    # Print formatted table
    print("\n" + "=" * 70)
    print(f"{'Username':<15} {'Name':<20} {'Role':<25} {'Capacity':<10}")
    print("=" * 70)

    for user in users:
        print(f"@{user.username:<13} {user.name:<20} {user.role:<25} {user.capacity:<10}")

    print("=" * 70)
    print(f"Total users: {len(users)}\n")


def main():
    """Main entry point for the command-line interface."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Get all users from the team.md data source",
        epilog="Examples:\n"
               "  python get_users.py                  # List all users\n"
               "  python get_users.py --json           # Output as JSON\n"
               "  python get_users.py --username alice # Get specific user\n"
               "  python get_users.py --role Engineer  # Filter by role",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--username', '-u',
        type=str,
        help='Filter users by username (case-insensitive)'
    )

    parser.add_argument(
        '--role', '-r',
        type=str,
        help='Filter users by role (case-insensitive)'
    )

    parser.add_argument(
        '--json',
        action='store_true',
        help='Output users as JSON format'
    )

    parser.add_argument(
        '--file', '-f',
        type=str,
        help='Path to custom user data file'
    )

    args = parser.parse_args()

    try:
        # Fetch users from the data source
        users = get_users(args.file)

        # Apply filters if specified
        if args.username:
            user = get_user_by_username(args.username, args.file)
            users = [user]

        if args.role:
            users = get_users_by_role(args.role, args.file)

        # Output results
        if args.json:
            print(json.dumps([u.to_dict() for u in users], indent=2))
        else:
            print_users(users)

    except FileNotFoundError as e:
        print(f"Error: {e}", file=__import__('sys').stderr)
        __import__('sys').exit(1)
    except InvalidDataError as e:
        print(f"Error: {e}", file=__import__('sys').stderr)
        __import__('sys').exit(1)
    except UserNotFoundError as e:
        print(f"Error: {e}", file=__import__('sys').stderr)
        __import__('sys').exit(1)


if __name__ == "__main__":
    # Run the main function when script is executed
    main()