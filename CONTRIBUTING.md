# Contributing to This Project

This is a test-planning repository that manages all project data as markdown files. This guide helps external contributors understand how to contribute effectively.

## How to Submit Issues

### Issue Tracking Workflow

All issues are tracked as markdown files in the `issues/` directory. Each issue is a separate file with the format `i-XXX.md` (e.g., `i-001.md`, `i-002.md`).

### Meta Table Format

Every issue file must include a Meta table at the top with the following fields:

```markdown
## Meta
| Field | Value |
|-------|-------|
| ID | i-001 |
| Status | todo |
| Created | 2026-01-29 |
| Updated | 2026-01-29 |
```

### ID Conventions

Issue IDs follow the format `i-XXX` where XXX is a sequential number:
- Example: `i-001`, `i-002`, `i-003`

### Valid Issue Statuses

| Status | Description |
|--------|-------------|
| `backlog` | Issue is recorded but not yet planned |
| `todo` | Issue is ready to be worked on |
| `in_progress` | Issue is actively being worked on |
| `in_review` | Work is complete and under review |
| `done` | Issue has been completed |
| `blocked` | Issue cannot proceed due to a dependency |

## Pull Request Conventions

### Commit Format

All commits should follow this format:

```
type(scope): message
```

### Commit Types

| Type | Description |
|------|-------------|
| `feat` | New feature or functionality |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Code style changes (formatting, no logic change) |
| `refactor` | Code refactoring |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks, dependencies, etc. |

### Commit Examples

```
docs(readme): update setup instructions
fix(issue): resolve status update bug
feat(auth): add OAuth login support
refactor(api): simplify error handling
```

### General Guidelines

- All changes should be committed with clear, descriptive messages
- Include the relevant scope (file, module, or feature area)
- Keep commits atomic and focused on a single change

## Coding Standards

For detailed coding conventions, see [skills/coding/conventions.md](skills/coding/conventions.md).

### File Naming

| Type | Convention | Example |
|------|------------|---------|
| Files | kebab-case | `user-service.ts` |
| Classes | PascalCase | `UserService` |
| Functions | camelCase | `getUserById` |
| Constants | SCREAMING_SNAKE | `MAX_RETRIES` |

### Import Organization

- Group imports: external libraries first, then internal modules
- Sort alphabetically within each group

### Error Handling

- Use custom error classes
- Include error codes and messages
- Log errors with relevant context

### Logging

- Use structured logging
- Include relevant context (IDs, timestamps, etc.)

## Testing Requirements

For detailed testing guidelines, see [skills/coding/testing.md](skills/coding/testing.md).

### Coverage Requirements

- Minimum 80% code coverage required
- 100% coverage for critical paths

### Test Structure

```typescript
describe('ServiceName', () => {
  describe('methodName', () => {
    it('should do expected behavior', async () => {
      // Arrange
      // Act
      // Assert
    });
  });
});
```

### Mocking Guidelines

- Use mocks for external services
- Use factories for test data
- Never mock what you don't own

## Team-Specific Conventions

### Repository Structure

```
/
├── milestones/        # Long-term release targets (m-XXX.md)
├── epics/            # Large features spanning sprints (e-XXX.md)
├── sprints/          # Time-boxed work periods (s-XXX.md)
├── issues/           # Individual work items (i-XXX.md)
├── tasks/            # AI coding tasks (t-XXX.md)
└── skills/           # Instructions for AI assistants
    ├── coding/       # Code conventions and patterns
    └── views/        # View styling preferences
```

### Critical Rules

1. **Never delete files** - Mark as archived/cancelled instead
2. **Never modify IDs** - IDs are permanent once assigned
3. **Always update timestamps** - Update the `Updated` field on every change
4. **Check target repo** - Issues specify which repository receives code changes
5. **Read skills first** - Before coding tasks, read `skills/coding/`

### Bidirectional Linking

- Issue → Task: When creating a task for an issue, the task must link back to the issue
- Issue → Sprint: Sprint files must list all issues assigned to them
- Always maintain both directions of links to ensure traceability

### Before Implementing Issues

1. Read the issue file thoroughly
2. Note the `Target Repo` field - this specifies where the code should be implemented
3. Create a task file in `tasks/` if this requires code changes in another repository