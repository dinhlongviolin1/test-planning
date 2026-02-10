#!/usr/bin/env python3
"""
List all users/team members from the team.md file.
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from team_members import get_team_members, print_team_roster


def main():
    """List all team members."""
    print_team_roster()


if __name__ == "__main__":
    main()