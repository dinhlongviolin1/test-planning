# CLAUDE.md - AI Agent Guide

This file provides documentation for AI coding agents working in this repository.

## Project Overview

This is a **markdown-based project management repository** used to track epics, issues, tasks, sprints, and team members. The project management data lives entirely in markdown files, making it version-controlled and human-readable.

**Key Characteristics:**
- All project data stored as markdown files
- AI agents generate JSON data for frontend views (they don't render views directly)
- Code implementation tasks target external repositories
- Git-based workflow with structured commit messages

## Directory Structure

```
/workspace/repo/
├── epics/              # Large features spanning multiple sprints (e-001, e-002, etc.)
├── issues/             # Individual work items and user stories (i-001, i-002, etc.)
├── tasks/              # AI coding tasks for automated implementation (t-001, t-002, etc.)
├── milestones/         # Milestone tracking (m-001, m-002, etc.)
├── sprints/            # Sprint planning and tracking (s-001, s-002, etc.)
│   └── current.md      # Points to the active sprint
├── skills/             # Instructions and conventions for AI agents
│   ├── coding/
│   │   ├── conventions.md   # Coding standards and git conventions
│   │   └── testing.md       # Testing requirements
│   └── views/           # View styling guidelines
├── scripts/            # Automation scripts
├── project.md          # Project overview with linked code repos
├── team.md             # Team member details (9 members with various roles)
└── README.md           # Agent navigation guide
```

### Directory Details

- **epics/**: Large features that span multiple sprints. Each epic contains multiple issues.
- **issues/**: Individual work items, user stories, and bug reports. Each issue can link to one or more tasks.
- **tasks/**: AI coding tasks that generate code for external repositories. Tasks link back to their parent issue.
- **milestones/**: Long-term release targets that group epics.
- **sprints/**: Time-boxed work periods (typically 2 weeks). Contains issue assignments and velocity tracking.
- **skills/**: Instructions for AI agents on how to write code, test, and generate views.
- **scripts/**: Automation scripts for project management tasks.

## Key Conventions

### Git Commit Format

Format: `type(scope): message`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:
- `feat(auth): add Google OAuth login`
- `fix(api): handle null user in profile endpoint`
- `docs(readme): update installation instructions`

### File Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Files | kebab-case | `user-service.ts` |
| Classes | PascalCase | `UserService` |
| Functions | camelCase | `getUserById` |
| Constants | SCREAMING_SNAKE | `MAX_RETRIES` |

### Import Organization

Group imports in this order:
1. External imports (npm packages)
2. Internal imports (project modules)

Sort alphabetically within each group.

### File ID System

- **Epics**: e-001, e-002, etc.
- **Issues**: i-001, i-002, etc.
- **Tasks**: t-001, t-002, etc.
- **Milestones**: m-001, m-002, etc.
- **Sprints**: s-001, s-002, etc.

Always read `_index.md` to get the next available ID before creating new files.

## Testing Requirements

### Coverage Requirements
- **Minimum 80% code coverage**
- **100% coverage** for critical paths

### Test Structure (AAA Pattern)

```typescript
describe('ServiceName', () => {
  describe('methodName', () => {
    it('should do expected behavior', async () => {
      // Arrange - Set up test data and mocks
      // Act - Execute the function being tested
      // Assert - Verify the expected outcome
    });
  });
});
```

### Mocking Guidelines
- Use mocks for external services (APIs, databases)
- Use factories for test data creation
- Never mock what you don't own

### When to Test
- **New feature**: Write unit tests + integration tests
- **Bug fix**: Write regression test
- **Refactor**: Ensure existing tests pass

## Team Information

See `team.md` for complete team member details. The team consists of 9 members:

| Username | Name | Role |
|----------|------|------|
| @dinhlongviolin1 | Dinh Long | Software Engineer |
| @faisal | Faisal | Frontend Engineer/UI Designer |
| @louis | Louis | Senior Software Engineer |
| @nguyen | Nguyen | Senior Software Engineer |
| @vanalite | Van Alite | Senior Software Engineer |
| @bach | Bach | Researcher |
| @alan | Alan | Researcher |
| @alex | Alex | Researcher |
| @thinhle | Thinh Le | Researcher |

## Important Guidelines for Agents

### Core Principles
1. **This is a markdown-based PM system** - Work with the file structure, not a database
2. **Follow commit format strictly** - Always use `type(scope): message`
3. **Write tests for any code created** - Follow the testing requirements above
4. **Check existing conventions first** - Always read `skills/coding/` before implementing

### Common Workflows

**Creating a new issue:**
1. Read `issues/_index.md` to get the NEXT_ID
2. Create `issues/i-{NEXT_ID}.md` using the issue template
3. Update `issues/_index.md` to increment NEXT_ID

**Implementing a coding task:**
1. Read `issues/i-X.md` thoroughly
2. Note the `Target Repo` field - that's where code goes
3. Read `skills/coding/` for project conventions
4. Create `tasks/t-{NEXT_ID}.md` with full context
5. Submit task to the coding queue

### Critical Rules
- **Never delete files** - Mark as archived/cancelled instead
- **Never modify IDs** - IDs are permanent
- **Always update timestamps** - Update `Updated` field on every change
- **Link everything** - Cross-references help navigation (issue ↔ task, issue ↔ sprint)

### Status Values

| Entity | Valid Statuses |
|--------|---------------|
| Issue | backlog, todo, in_progress, in_review, done, blocked |
| Task | pending, queued, running, completed, failed, cancelled |
| Sprint | planning, active, completed |
| Epic | draft, active, completed |
| Milestone | planned, in_progress, completed, missed |

### View Generation

When users request views (e.g., kanban board), agents:
1. Read the relevant markdown files (sprint, issues, etc.)
2. Parse and extract the data
3. Generate JSON matching the requested view schema
4. The frontend handles the actual rendering