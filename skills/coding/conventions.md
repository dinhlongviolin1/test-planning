# Coding Conventions

## Language & Framework

[Specify your tech stack here]

- **Language**: TypeScript / Python / etc.
- **Runtime**: Node.js / Python 3.11+ / etc.
- **Testing**: Jest / pytest / etc.

## File Structure

```
src/
├── api/              # Route handlers
├── services/         # Business logic
├── models/           # Data models
├── utils/            # Shared utilities
└── __tests__/        # Test files
```

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Files | kebab-case | `user-service.ts` |
| Classes | PascalCase | `UserService` |
| Functions | camelCase | `getUserById` |
| Constants | SCREAMING_SNAKE | `MAX_RETRIES` |

## Code Style

### Imports
- Group imports: external, then internal
- Sort alphabetically within groups

### Error Handling
- Use custom error classes
- Include error codes and messages
- Log errors with context

### Logging
- Use structured logging
- Include relevant context (IDs, etc.)

## Git Commits

Format: `type(scope): message`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(auth): add Google OAuth login`
- `fix(api): handle null user in profile endpoint`
