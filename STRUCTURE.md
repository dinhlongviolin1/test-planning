# Structure

This document describes the directory layout, entity schemas, and linking conventions for the markdown-based planning system. For the tech stack and system architecture, see [ARCHITECTURE.md](ARCHITECTURE.md). For agent instructions and critical rules, see [CLAUDE.md](CLAUDE.md).

## Directory Layout

| Directory | Description |
|-----------|-------------|
| `epics/` | Large features spanning multiple sprints (`e-XXX.md` files) |
| `issues/` | Individual work items (`i-XXX.md` files) |
| `sprints/` | Time-boxed work periods (`s-XXX.md` files); `current.md` points to the active sprint |
| `milestones/` | Long-term release targets (`m-XXX.md` files) |
| `tasks/` | AI coding tasks (`t-XXX.md` files) |
| `skills/` | Agent instructions (e.g., `coding/conventions.md`, `coding/testing.md`) |
| `scripts/` | Utility scripts (e.g., `get_all_issues_and_epics.py`, `get_team_members.py`) |
| `docs/` | Project documentation |

## Entity File Naming

| Entity | File Pattern | Example |
|--------|--------------|---------|
| Epic | `e-XXX.md` | `e-001.md` |
| Issue | `i-XXX.md` | `i-001.md` |
| Sprint | `s-XXX.md` | `s-001.md` |
| Milestone | `m-XXX.md` | `m-001.md` |
| Task | `t-XXX.md` | `t-001.md` |

## Entity Meta Tables

Every entity file has a `## Meta` section with a markdown table:

```
## Meta
| Field | Value |
|-------|-------|
| ID    | x-001 |
| Status | active |
```

### Epic Meta Fields

| Field | Description |
|-------|-------------|
| ID | Entity identifier (e.g., `e-001`) |
| Status | Current state (see Valid Status Values) |
| Created | ISO 8601 creation timestamp |
| Updated | Date of last modification |

### Issue Meta Fields

| Field | Description |
|-------|-------------|
| ID | Entity identifier (e.g., `i-001`) |
| Status | Current state (see Valid Status Values) |
| Created | Date of creation |
| Updated | Date of last modification |
| Points | Estimated effort (story points) |
| Assignee | GitHub username of assigned person |

### Sprint Meta Fields

| Field | Description |
|-------|-------------|
| ID | Entity identifier (e.g., `s-001`) |
| Status | Current state (see Valid Status Values) |
| Created | Date of creation |
| Updated | Date of last modification |
| Start Date | Sprint start date |
| End Date | Sprint end date |

### Milestone Meta Fields

| Field | Description |
|-------|-------------|
| ID | Entity identifier (e.g., `m-001`) |
| Status | Current state (see Valid Status Values) |
| Created | Date of creation |
| Updated | Date of last modification |
| Target Date | Target completion date |

### Task Meta Fields

| Field | Description |
|-------|-------------|
| ID | Entity identifier (e.g., `t-001`) |
| Status | Current state (see Valid Status Values) |
| Created | Date of creation |
| Updated | Date of last modification |
| Issue | Linked issue ID (or `-` if none) |
| Priority | Priority level (e.g., low, medium, high) |
| Complexity | Estimated complexity (numeric scale) |

## Valid Status Values

| Entity | Valid Statuses |
|--------|----------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

## Bidirectional Linking

Links between entities are always bidirectional. If an issue links to an epic, the epic must also list that issue. This maintains referential integrity across the planning system.

Common link section names used in entity files:

| Source | Section | Target |
|--------|---------|--------|
| Issue | Linked Epics | Epic |
| Issue | Linked Sprint | Sprint |
| Issue | Linked Milestone | Milestone |
| Epic | Related Issues | Issue |
| Sprint | Linked Epics | Epic |
| Sprint | Linked Milestone | Milestone |
| Sprint | Issues (Todo/In Progress/In Review/Done) | Issue |
| Milestone | Linked Epics | Epic |
| Milestone | Linked Sprints | Sprint |

## Sequential ID Allocation

Each entity directory contains an `_index.md` file that tracks the next available ID:

```markdown
**NEXT_ID: 13**
```

When creating a new entity:
1. Read the `_index.md` file for the relevant entity directory
2. Use the current `NEXT_ID` as the new entity's ID
3. Increment `NEXT_ID` in `_index.md` and commit the change

This ensures IDs are unique and monotonically increasing.

## Entity Relationship Hierarchy

```
Milestone → Epic → Issue → Task → PR
```

Milestones contain sprints and epics; epics span sprints and group issues; issues belong to sprints and can generate tasks; tasks represent AI coding work linked to issues.