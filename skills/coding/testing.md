# Testing Requirements

## Coverage Requirements

- Minimum 80% code coverage
- 100% coverage for critical paths

## Test Structure

```
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

## Mocking

- Use mocks for external services
- Use factories for test data
- Never mock what you don't own

## Integration Tests

- Test API endpoints end-to-end
- Use test database (reset between tests)
- Test error scenarios

## When to Test

- [ ] New feature → Unit + Integration tests
- [ ] Bug fix → Regression test
- [ ] Refactor → Existing tests must pass
