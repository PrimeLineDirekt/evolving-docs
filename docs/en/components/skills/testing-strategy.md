---
title: Testing Strategy
type: skill
tags: [testing, quality, coverage, test-driven]
lang: en
confidence: 95
---

# Testing Strategy

![Testing Strategy Skill](../../shared/assets/infographics/skills/testing-strategy.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Workflow Skill |
| **Purpose** | Design comprehensive testing strategies |
| **Complexity** | High |
| **Source** | claude-workflow |
| **Plugin** | external |
</div>

## What It Does

The Testing Strategy skill designs comprehensive testing strategies for any codebase. It provides framework recommendations, test structure templates, coverage strategies, and mocking patterns following the testing pyramid approach.

## Key Principles

- **Testing pyramid** - 70% unit, 20% integration, 10% E2E
- **Fast feedback** - Unit tests run quickly and frequently
- **Isolation** - Tests don't depend on each other
- **Meaningful coverage** - Focus on business logic
- **Clear structure** - Arrange, Act, Assert pattern

## Testing Pyramid Approach

```
        /\
       /  \     E2E Tests (10%)
      /----\    - Critical user journeys
     /      \   - Slow but comprehensive
    /--------\  Integration Tests (20%)
   /          \ - Component interactions
  /------------\ - API contracts
 /              \ Unit Tests (70%)
/________________\ - Fast, isolated
                   - Business logic focus
```

## Framework Selection

### JavaScript/TypeScript

| Type | Recommended | Alternative |
|------|-------------|-------------|
| Unit | Vitest | Jest |
| Integration | Vitest + MSW | Jest + SuperTest |
| E2E | Playwright | Cypress |
| Component | Testing Library | Enzyme |

### Python

| Type | Recommended | Alternative |
|------|-------------|-------------|
| Unit | pytest | unittest |
| Integration | pytest + httpx | pytest + requests |
| E2E | Playwright | Selenium |
| API | pytest + FastAPI TestClient | - |

### Go

| Type | Recommended |
|------|-------------|
| Unit | testing + testify |
| Integration | testing + httptest |
| E2E | testing + chromedp |

## Test Structure Templates

### Unit Test
```javascript
describe('[Unit] ComponentName', () => {
  describe('methodName', () => {
    it('should [expected behavior] when [condition]', () => {
      // Arrange
      const input = createTestInput();

      // Act
      const result = methodName(input);

      // Assert
      expect(result).toEqual(expectedOutput);
    });

    it('should throw error when [invalid condition]', () => {
      expect(() => methodName(invalidInput)).toThrow(ExpectedError);
    });
  });
});
```

### Integration Test
```javascript
describe('[Integration] API /users', () => {
  beforeAll(async () => {
    await setupTestDatabase();
  });

  afterAll(async () => {
    await teardownTestDatabase();
  });

  it('should create user and return 201', async () => {
    const response = await request(app)
      .post('/users')
      .send({ name: 'Test', email: 'test@example.com' });

    expect(response.status).toBe(201);
    expect(response.body.id).toBeDefined();
  });
});
```

### E2E Test
```javascript
describe('[E2E] User Registration Flow', () => {
  it('should complete registration successfully', async ({ page }) => {
    await page.goto('/register');

    await page.fill('[data-testid="email"]', 'new@example.com');
    await page.fill('[data-testid="password"]', 'SecurePass123!');
    await page.click('[data-testid="submit"]');

    await expect(page.locator('.welcome-message')).toBeVisible();
    await expect(page).toHaveURL('/dashboard');
  });
});
```

## Coverage Strategy

### What to Cover
- Business logic (100%)
- Edge cases and error handling (90%+)
- API contracts (100%)
- Critical user paths (E2E)
- UI components (snapshot + interaction)
- **NOT**: Third-party library internals
- **NOT**: Simple getters/setters

### Coverage Thresholds
```json
{
  "coverageThreshold": {
    "global": {
      "branches": 80,
      "functions": 80,
      "lines": 80,
      "statements": 80
    },
    "src/core/": {
      "branches": 95,
      "functions": 95
    }
  }
}
```

## Test Data Management

### Factories/Builders
```javascript
// factories/user.js
export const userFactory = (overrides = {}) => ({
  id: faker.string.uuid(),
  name: faker.person.fullName(),
  email: faker.internet.email(),
  createdAt: new Date(),
  ...overrides,
});

// Usage
const admin = userFactory({ role: 'admin' });
```

### Fixtures
```javascript
// fixtures/users.json
{
  "validUser": { "name": "Test", "email": "test@example.com" },
  "invalidUser": { "name": "", "email": "invalid" }
}
```

## Mocking Strategy

### When to Mock
- External APIs and services
- Database in unit tests
- Time/Date for determinism
- Random values
- **NOT**: Internal modules (usually)
- **NOT**: The code under test

### Mock Examples
```javascript
// API mocking with MSW
import { http, HttpResponse } from 'msw';

export const handlers = [
  http.get('/api/users', () => {
    return HttpResponse.json([
      { id: 1, name: 'John' },
    ]);
  }),
];

// Time mocking
vi.useFakeTimers();
vi.setSystemTime(new Date('2024-01-01'));
```

## Usage

The skill is triggered when:
- Adding tests
- Improving coverage
- Setting up testing infrastructure
- Designing test strategies

Or use naturally with phrases like:
- "How should I test this?"
- "Create a testing strategy for..."
- "Set up testing for..."

## Output

The skill provides:

1. **Framework recommendations** - Tool selection
2. **Test structure templates** - Code examples
3. **Coverage strategies** - What and how to test
4. **Mocking patterns** - Test doubles
5. **Best practices** - Testing conventions

## Related Skills

- [API Design](api-design.md) - API testing strategies
- [Architecture Patterns](architecture-patterns.md) - Testing architectural components
- [Project Analysis](project-analysis.md) - Understanding existing test setup

---

<small>Source: `external/claude-workflow:testing-strategy`</small>
