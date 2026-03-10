#!/usr/bin/env python3
"""
List all users/team members from the team.md file.
"""

import sys
from pathlib import Path

# Add parent directory to path so we can import team_members
sys.path.insert(0, str(Path(__file__).parent.parent))

from team_members import print_team_roster


def main():
    """List all team members."""
    print_team_roster()


if __name__ == "__main__":
    main()
