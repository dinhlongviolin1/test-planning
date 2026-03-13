# CLAUDE.md - AI Agent Project Guide

This file provides comprehensive guidance for AI assistants working with this project planning repository.

## Project Overview

This is a **project planning repository** that uses markdown files to manage issues, sprints, epics, milestones, and tasks. It serves as a "game world" for AI agents to manage software projects without directly modifying code in target repositories.

**Key Characteristics:**
- All project management data lives as markdown files
- AI agents can read/write files in this repository
- Code changes go to target repositories via coding tasks (spawning agents)
- All changes are committed to git with version control

## Directory Structure

```
/workspace/repo/
├── README.md              # Agent navigation guide - ALWAYS READ THIS FIRST
├── project.md             # Project overview, linked code repositories
├── team.md                # Team members with roles and capacity
├── CLAUDE.md              # This file - AI agent guidance
│
├── milestones/            # Long-term release targets
│   ├── _index.md          # Overview + ID counter
│   └── m-XXX.md           # Individual milestones
│
├── epics/                 # Large features spanning multiple sprints
│   ├── _index.md          # Overview + ID counter
│   └── e-XXX.md           # Individual epics
│
├── sprints/               # Time-boxed work periods
│   ├── _index.md          # Overview + ID counter
│   ├── current.md         # Points to active sprint (always check this)
│   └── s-XXX.md           # Individual sprints
│
├── issues/                # Individual work items
│   ├── _index.md          # Overview + NEXT_ID COUNTER
│   └── i-XXX.md           # One file per issue (self-contained)
│
├── tasks/                 # AI coding tasks that spawn agents to target repos
│   ├── _index.md          # Overview + NEXT_ID COUNTER
│   └── t-XXX.md           # One file per task
│
├── skills/                # Instructions for AI agents
│   ├── coding/            # Coding conventions and testing requirements
│   │   ├── conventions.md # Naming, file structure, code style
│   │   └── testing.md     # Coverage requirements, test structure
│   └── views/             # View styling guidelines (if applicable)
│
└── scripts/               # Python utilities
    ├── get_team_members.py # Retrieves team members from team.md
    ├── list_users.py       # Lists all users
    └── README.md           # Scripts documentation
```

## Important Configuration

### .gitignore

```gitignore
# tokamak ephemeral worktrees
.tokamak/worktrees/
```

This repository excludes ephemeral worktrees created by the tokamak orchestrator to avoid cluttering the git history with temporary development environments.

## Coding Conventions

Refer to `skills/coding/conventions.md` for detailed coding standards:

### File Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Files | kebab-case | `user-service.ts` |
| Classes | PascalCase | `UserService` |
| Functions | camelCase | `getUserById` |
| Constants | SCREAMING_SNAKE | `MAX_RETRIES` |

### Import Organization

- Group imports: external packages first, then internal modules
- Sort alphabetically within each group

### Git Commit Format

```
type(scope): message
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples:**
- `feat(auth): add Google OAuth login`
- `fix(api): handle null user in profile endpoint`
- `docs: add CLAUDE.md for agent guidance`

## Project Skills

### skills/coding/conventions.md

Contains detailed guidelines for:
- Language and framework specifications
- File structure recommendations
- Naming conventions (files, classes, functions, constants)
- Import grouping and sorting
- Error handling patterns
- Logging standards
- Git commit message format

### skills/coding/testing.md

Specifies the testing approach:
- **Minimum 80% code coverage** required
- **100% coverage** for critical paths
- Test structure using `describe`/`it` blocks
- Arrange/Act/Assert pattern
- Mock external services only (never mock what you don't own)
- Integration tests for API endpoints
- Test database reset between tests

## Python Scripts

### scripts/get_team_members.py

A utility script for reading and parsing team member information from `team.md`:

```python
from get_team_members import get_team_members, print_team_members

# Get all team members
members = get_team_members()

# Get specific member by username
member = get_member_by_username("dinhlongviolin1")

# Get members by role
engineers = get_members_by_role("Software Engineer")

# Output as JSON
data = get_team_members_dict()
```

**CLI Usage:**
```bash
python scripts/get_team_members.py
python scripts/get_team_members.py --username dinhlongviolin1
python scripts/get_team_members.py --role "Senior Software Engineer"
python scripts/get_team_members.py --json
```

### scripts/list_users.py

A simple wrapper script that imports from `get_team_members.py` to list all team members:

```bash
python scripts/list_users.py
```

## Planning System Workflow

### Step 1: Read README.md First

The `README.md` file is the agent navigation guide. Always read it before starting any work in this repository.

### Step 2: Understand the Meta Table Format

Every file in this repository uses a Meta table at the top:

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | x-001 |
| Status | active |
| Updated | 2026-03-13 |
```

### Step 3: Maintain ID Counters

- Read `_index.md` files to get the NEXT_ID before creating new items
- Increment NEXT_ID after creating any new item
- IDs are permanent - never modify existing IDs

### Step 4: Keep Bidirectional Links

- If an issue links to a task, the task must link back to the issue
- If an issue is assigned to a sprint, the sprint must list the issue
- Cross-references help navigate the project

### Step 5: Understand Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | `backlog`, `todo`, `in_progress`, `in_review`, `done`, `blocked` |
| Task | `pending`, `queued`, `running`, `completed`, `failed`, `cancelled` |
| Sprint | `planning`, `active`, `completed` |
| Epic | `draft`, `active`, `completed` |
| Milestone | `planned`, `in_progress`, `completed`, `missed` |

### Common Workflows

**Show current sprint:**
1. Read `sprints/current.md` to get the active sprint ID
2. Read `sprints/s-{id}.md` for full sprint details

**Create a new issue:**
1. Read `issues/_index.md` to get the NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using the issue template
3. Update `issues/_index.md` to increment NEXT_ID

**Move issue to Done:**
1. Read the issue file `issues/i-X.md`
2. Update Status to `done`
3. Update the `updated` timestamp

**Implement issue (create coding task):**
1. Read `issues/i-X.md` thoroughly
2. Note the `Target Repo` field
3. Read `skills/coding/` for conventions
4. Create `tasks/t-{NEXT_ID}.md` with full context
5. Update `tasks/_index.md` to increment NEXT_ID
6. Submit task to the coding queue

## Team Structure

From `team.md`, the team consists of 9 members:

| Username | Name | Role | Capacity/Sprint |
|----------|------|------|-----------------|
| @dinhlongviolin1 | Dinh Long | Software Engineer | 10 pts |
| @faisal | Faisal | Frontend Engineer/UI Designer | 10 pts |
| @louis | Louis | Senior Software Engineer | 10 pts |
| @nguyen | Nguyen | Senior Software Engineer | 10 pts |
| @vanalite | Van Alite | Senior Software Engineer | 10 pts |
| @bach | Bach | Researcher | 10 pts |
| @alan | Alan | Researcher | 10 pts |
| @alex | Alex | Researcher | 10 pts |
| @thinhle | Thinh Le | Researcher | 10 pts |

**Roles Defined:**
- **Lead Engineer**: Technical leadership and architecture decisions
- **Product Manager**: Requirements and prioritization
- **Developer**: Implementation and code review

## Git Workflow

### Commit Format

This project uses conventional commits following the format:

```
type: description
```

Where type is one of: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples:**
- `docs: add CLAUDE.md for agent guidance`
- `feat: add new sprint planning template`
- `fix: update issue status workflow`

### Making Commits

1. Stage specific files - never use `git add -A` or `git add .`
2. Include `.tokamak/` and `.claude/` files in commits (first-class project files)
3. Use clear, concise commit messages
4. Include attribution: `Authored-By: Tokamak Agent <agent@tokamak.sh>`

### Branch Strategy

- Current branch: `feature/main-task-iss_c8434156-98bb-40-1773390719-1773390727`
- Main branch: `main`
- Create new branches for feature work

## Tips for AI Agents

1. **Start by reading** - Always read relevant files before making changes
2. **Check current.md** - For sprints, always check `sprints/current.md` first
3. **Preserve IDs** - Never modify existing IDs, always use next available
4. **Update timestamps** - Always update the `Updated` field when modifying files
5. **Use skills** - Reference `skills/coding/` for project-specific instructions
6. **Link everything** - Maintain bidirectional references between related items
7. **Commit often** - Each meaningful change should be a separate commit
8. **Be conservative** - When unsure, ask the human for clarification