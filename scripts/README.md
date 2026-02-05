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

# Repository Users Script

A Python utility script for fetching users (collaborators, contributors, and members) from a GitHub repository using the GitHub REST API.

## Features

- **Get collaborators**: Fetch users with direct access to the repository
- **Get contributors**: Fetch users who have contributed to the repository
- **Get organization members**: Fetch members if the repo is owned by an organization
- **Multiple output formats**: Table display or JSON output
- **CLI interface**: Run from command line with arguments

## Installation

```bash
# Requires the 'requests' library
pip install requests
```

## Usage

### Basic Usage - Get All Users

```python
from get_repo_users import get_all_users, print_users

# Get all users
all_users = get_all_users("dinhlongviolin1", "test-planning")
print_users(all_users["collaborators"], "Collaborators")
```

### Get Only Collaborators

```python
from get_repo_users import get_all_collaborators

collaborators = get_all_collaborators("dinhlongviolin1", "test-planning")
for user in collaborators:
    print(f"{user.login}: {user.type}")
```

### Get JSON Output

```python
from get_repo_users import get_all_users

result = get_all_users("dinhlongviolin1", "test-planning")
import json
print(json.dumps({k: [u.to_dict() for u in v] for k, v in result.items()}, indent=2))
```

## Command Line Interface

```bash
# Set GitHub token (required for private repos)
export GITHUB_TOKEN="your-token-here"

# Get all users from repository
python scripts/get_repo_users.py

# Get only collaborators
python scripts/get_repo_users.py --collaborators

# Get only contributors
python scripts/get_repo_users.py --contributors

# Get only organization members
python scripts/get_repo_users.py --members

# Output as JSON
python scripts/get_repo_users.py --json

# Specify a different repository
python scripts/get_repo_users.py --repo owner/repo

# Specify token directly
python scripts/get_repo_users.py --token "your-token-here"
```

## Output Examples

### Table Output
```
======================================================================
Collaborators
======================================================================
Login                Type      Admin  URL
----------------------------------------------------------------------
dinhlongviolin1      User      No     https://github.com/dinhlongviolin1
faisal               User      Yes    https://github.com/faisal
...
======================================================================
Total: 5
```

### JSON Output
```json
{
  "collaborators": [
    {
      "login": "dinhlongviolin1",
      "id": 123456,
      "avatar_url": "https://avatars...",
      "html_url": "https://github.com/dinhlongviolin1",
      "type": "User",
      "site_admin": false
    }
  ],
  "contributors": [...],
  "members": [...]
}
```

## GitHubUser Class

```python
@dataclass
class GitHubUser:
    login: str           # Username
    id: int              # GitHub user ID
    avatar_url: str      # Profile picture URL
    html_url: str        # Profile URL
    type: str            # "User" or "Bot"
    site_admin: bool     # Is GitHub admin
```

# Repository Issues Script

A Python utility script for fetching issues (open and closed) from a GitHub repository using the GitHub REST API.

## Features

- **Get all issues**: Fetch both open and closed issues
- **Filter by state**: Get only open, only closed, or all issues
- **Rich issue details**: Title, body, labels, assignees, comments, dates
- **Multiple output formats**: Table display or JSON output
- **CLI interface**: Run from command line with arguments

## Installation

```bash
# Requires the 'requests' library
pip install requests
```

## Usage

### Basic Usage - Get All Issues

```python
from get_repo_issues import get_all_issues, print_issues

# Get all issues (open and closed)
all_issues = get_all_issues("dinhlongviolin1", "test-planning")
print_issues(all_issues, "All Issues")
```

### Get Only Open Issues

```python
from get_repo_issues import get_all_issues

open_issues = get_all_issues("dinhlongviolin1", "test-planning", state="open")
```

### Get JSON Output

```python
from get_repo_issues import get_all_issues

issues = get_all_issues("dinhlongviolin1", "test-planning")
import json
print(json.dumps([i.to_dict() for i in issues], indent=2))
```

## Command Line Interface

```bash
# Set GitHub token (required for private repos)
export GITHUB_TOKEN="your-token-here"

# Get all issues from repository
python scripts/get_repo_issues.py

# Get only open issues
python scripts/get_repo_issues.py --state open

# Get only closed issues
python scripts/get_repo_issues.py --state closed

# Output as JSON
python scripts/get_repo_issues.py --json

# Specify a different repository
python scripts/get_repo_issues.py --repo owner/repo
```

## Output Examples

### Table Output
```
================================================================================
dinhlongviolin1/test-planning - All Issues (Open and Closed)
================================================================================
#     State      Title                                    Labels
--------------------------------------------------------------------------------
#1    [OPEN]     Initial project setup                   enhancement
#2    [OPEN]     Add user authentication feature         feature,prio-high
#3    [CLOSED]   Fix login bug                           bug,urgent
...
================================================================================
Total: 25
```

### JSON Output
```json
{
  "repository": "dinhlongviolin1/test-planning",
  "state_filter": "all",
  "total_count": 25,
  "issues": [
    {
      "number": 1,
      "title": "Initial project setup",
      "state": "open",
      "body": "Description of the issue...",
      "html_url": "https://github.com/dinhlongviolin1/test-planning/issues/1",
      "user_login": "dinhlongviolin1",
      "user_type": "User",
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-16T14:20:00Z",
      "closed_at": null,
      "labels": ["enhancement"],
      "assignees": ["dinhlongviolin1"],
      "comments": 3,
      "id": 1234567890
    }
  ]
}
```

## GitHubIssue Class

```python
@dataclass
class GitHubIssue:
    number: int              # Issue number
    title: str               # Issue title
    state: str               # "open" or "closed"
    body: str                # Issue description
    html_url: str            # Issue URL
    user_login: str          # Creator username
    user_type: str           # "User" or "Bot"
    created_at: str          # ISO timestamp
    updated_at: str          # ISO timestamp
    closed_at: Optional[str] # ISO timestamp or None
    labels: List[str]        # Label names
    assignees: List[str]     # Assignee usernames
    comments: int            # Comment count
    id: int                  # GitHub issue ID
```

## File Structure

```
scripts/
├── get_team_members.py    # Team member parsing script
├── get_repo_users.py      # Repository users fetching script
├── get_repo_issues.py     # Repository issues fetching script
├── list_users.py          # List all users (from team.md)
└── README.md              # This file
```