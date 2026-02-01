# Team Members Script

A Python utility script for reading and parsing team member information from the `team.md` file in the planning repository.

## Features

- **Parse team.md**: Read and parse markdown tables containing team member data
- **Filter by username**: Look up specific team members
- **Filter by role**: Get all members with a specific role
- **Multiple output formats**: Table display or JSON output
- **CLI interface**: Run from command line with arguments

## Installation

```bash
# No external dependencies required (uses Python standard library)
```

## Usage

### Basic Usage - Get All Team Members

```python
from get_team_members import get_team_members, print_team_members

# Get all team members as a list of TeamMember objects
members = get_team_members()
for member in members:
    print(f"@{member.username}: {member.name} - {member.role}")

# Print a formatted table
print_team_members()
```

### Get Members by Username

```python
from get_team_members import get_member_by_username

member = get_member_by_username("dinhlongviolin1")
if member:
    print(f"Found: {member.name} ({member.role})")
```

### Get Members by Role

```python
from get_team_members import get_members_by_role

engineers = get_members_by_role("Software Engineer")
for eng in engineers:
    print(f"{eng.name}: {eng.role}")
```

### Get JSON Output

```python
from get_team_members import get_team_members_dict

data = get_team_members_dict()
import json
print(json.dumps(data, indent=2))
```

## Command Line Interface

```bash
# Get all team members
python scripts/get_team_members.py

# Get specific member
python scripts/get_team_members.py --username dinhlongviolin1
python scripts/get_team_members.py -u dinhlongviolin1

# Get members by role
python scripts/get_team_members.py --role "Senior Software Engineer"
python scripts/get_team_members.py -r Developer

# Output as JSON
python scripts/get_team_members.py --json
python scripts/get_team_members.py -u dinhlongviolin1 --json
```

## Output Examples

### Table Output
```
======================================================================
Username          Name                 Role                      Capacity
======================================================================
@dinhlongviolin1   Dinh Long            Software Engineer         10 pts
@faisal            Faisal               Frontend Engineer/UI...   10 pts
@louis             Louis                Senior Software Engineer  10 pts
...
======================================================================
Total team members: 9
```

### JSON Output
```json
[
  {
    "username": "dinhlongviolin1",
    "name": "Dinh Long",
    "role": "Software Engineer",
    "capacity": "10 pts"
  }
]
```

## TeamMember Class

```python
@dataclass
class TeamMember:
    username: str      # Without @ prefix
    name: str
    role: str
    capacity: str
```

## File Structure

```
scripts/
├── get_team_members.py    # Main script
├── README.md              # This file
└── requirements.txt       # Dependencies
```