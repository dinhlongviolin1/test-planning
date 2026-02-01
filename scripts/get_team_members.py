"""
Team Members Utility Script

This script provides functions to read and parse team member information
from the team.md file in the planning repository.
"""

import os
import re
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

    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary."""
        return {
            "username": self.username,
            "name": self.name,
            "role": self.role,
            "capacity": self.capacity
        }


def get_repo_root() -> Path:
    """Get the root directory of the repository."""
    # Go up from this file's location to find repo root
    current = Path(__file__).resolve()
    # Assuming script is in a scripts/ folder at repo root
    return current.parent.parent


def get_team_file_path() -> Path:
    """Get the path to the team.md file."""
    return get_repo_root() / "team.md"


def parse_markdown_table(table_text: str) -> List[List[str]]:
    """
    Parse a markdown table and return a list of rows.
    
    Args:
        table_text: The markdown table text
        
    Returns:
        List of rows, where each row is a list of cell values
    """
    lines = table_text.strip().split('\n')
    rows = []
    
    for line in lines:
        # Skip separator lines (like |---|)
        if re.match(r'^[\s\|]*[-:]+[\s\|]*$', line):
            continue
            
        # Extract cells from the line
        cells = []
        for cell in line.strip('|').split('|'):
            cells.append(cell.strip())
        rows.append(cells)
    
    return rows


def get_team_members(file_path: Optional[str] = None) -> List[TeamMember]:
    """
    Read and parse team members from team.md file.
    
    Args:
        file_path: Optional path to team.md file. If not provided,
                   uses the default location in the repo.
    
    Returns:
        List of TeamMember objects
    """
    if file_path is None:
        file_path = str(get_team_file_path())
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the team members table section
    # Look for lines that start with | and contain data
    lines = content.split('\n')
    
    # Find the header row (first row with |username|)
    header_idx = None
    separator_idx = None
    data_start_idx = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('|') and 'username' in stripped.lower():
            header_idx = i
        elif header_idx is not None and separator_idx is None:
            if re.match(r'^[\s\|]*[-:]+[\s\|]*$', line):
                separator_idx = i
                # Data starts after separator
                data_start_idx = i + 1
                break
    
    if header_idx is None or separator_idx is None:
        return []
    
    members = []
    
    # Parse data rows
    for line in lines[data_start_idx:]:
        stripped = line.strip()
        if not stripped or not stripped.startswith('|'):
            break
            
        cells = [cell.strip() for cell in stripped.strip('|').split('|')]
        
        # Expecting: username, name, role, capacity (4 columns)
        if len(cells) >= 4:
            username = cells[0].lstrip('@')  # Remove @ prefix
            name = cells[1]
            role = cells[2]
            capacity = cells[3]
            
            members.append(TeamMember(
                username=username,
                name=name,
                role=role,
                capacity=capacity
            ))
    
    return members


def get_team_members_dict(file_path: Optional[str] = None) -> List[Dict[str, str]]:
    """
    Get team members as a list of dictionaries.
    
    Args:
        file_path: Optional path to team.md file
        
    Returns:
        List of dictionaries with team member info
    """
    members = get_team_members(file_path)
    return [m.to_dict() for m in members]


def get_member_by_username(username: str, file_path: Optional[str] = None) -> Optional[TeamMember]:
    """
    Get a specific team member by username.
    
    Args:
        username: The username to search for (without @)
        file_path: Optional path to team.md file
        
    Returns:
        TeamMember if found, None otherwise
    """
    members = get_team_members(file_path)
    for member in members:
        if member.username.lower() == username.lower():
            return member
    return None


def get_members_by_role(role: str, file_path: Optional[str] = None) -> List[TeamMember]:
    """
    Get team members filtered by role.
    
    Args:
        role: The role to filter by
        file_path: Optional path to team.md file
        
    Returns:
        List of TeamMember objects with matching role
    """
    members = get_team_members(file_path)
    return [m for m in members if m.role.lower() == role.lower()]


def print_team_members(members: Optional[List[TeamMember]] = None):
    """
    Print team members in a formatted table.
    
    Args:
        members: List of TeamMember objects. If None, fetches all members.
    """
    if members is None:
        members = get_team_members()
    
    print("\n" + "=" * 70)
    print(f"{'Username':<15} {'Name':<20} {'Role':<25} {'Capacity':<10}")
    print("=" * 70)
    
    for member in members:
        print(f"@{member.username:<13} {member.name:<20} {member.role:<25} {member.capacity:<10}")
    
    print("=" * 70)
    print(f"Total team members: {len(members)}\n")


# CLI Entry Point
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Get team members from team.md")
    parser.add_argument('--username', '-u', type=str, help="Filter by username")
    parser.add_argument('--role', '-r', type=str, help="Filter by role")
    parser.add_argument('--json', action='store_true', help="Output as JSON")
    
    args = parser.parse_args()
    
    members = get_team_members()
    
    if args.username:
        member = get_member_by_username(args.username)
        if member:
            members = [member]
        else:
            print(f"Member not found: {args.username}")
            members = []
    
    if args.role:
        members = get_members_by_role(args.role)
    
    if args.json:
        import json
        print(json.dumps([m.to_dict() for m in members], indent=2))
    else:
        print_team_members(members)