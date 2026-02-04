---
title: API Design
type: skill
tags: [api, rest, graphql, design, backend]
lang: en
confidence: 95
---

# API Design

![API Design Skill](../../shared/assets/infographics/skills/api-design.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Workflow Skill |
| **Purpose** | Guide REST and GraphQL API design decisions |
| **Complexity** | Medium |
| **Source** | claude-workflow |
| **Plugin** | external |
</div>

## What It Does

The API Design skill provides comprehensive guidance for designing robust APIs, covering endpoint structure, HTTP methods, status codes, response formats, versioning strategies, authentication patterns, and OpenAPI documentation. It helps create consistent, maintainable APIs following industry best practices.

## Key Principles

- **Resource-based URLs** - Use nouns, not verbs in endpoints
- **Proper HTTP methods** - GET, POST, PUT, PATCH, DELETE for semantic operations
- **Consistent status codes** - 2xx success, 4xx client errors, 5xx server errors
- **Clear response formats** - Structured data, meta information, pagination
- **API versioning** - URL-based or header-based versioning strategies
- **Security first** - Authentication, authorization, rate limiting, input validation

## REST API Patterns

### URL Structure
```
GET    /users              # List users
GET    /users/:id          # Get user
POST   /users              # Create user
PUT    /users/:id          # Replace user
PATCH  /users/:id          # Update user
DELETE /users/:id          # Delete user

# Nested resources
GET    /users/:id/orders   # User's orders
POST   /users/:id/orders   # Create order for user

# Query parameters for filtering/pagination
GET    /users?role=admin&status=active
GET    /users?page=2&limit=20&sort=-createdAt
```

### Response Formats

**Success Response**
```json
{
  "data": {
    "id": "123",
    "type": "user",
    "attributes": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  },
  "meta": {
    "requestId": "abc-123"
  }
}
```

**Error Response**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Must be a valid email address"
      }
    ]
  },
  "meta": {
    "requestId": "abc-123",
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

## GraphQL Patterns

### Schema Design
```graphql
type Query {
  user(id: ID!): User
  users(filter: UserFilter, pagination: Pagination): UserConnection!
}

type Mutation {
  createUser(input: CreateUserInput!): UserPayload!
  updateUser(id: ID!, input: UpdateUserInput!): UserPayload!
}

type User {
  id: ID!
  name: String!
  email: String!
  orders(first: Int, after: String): OrderConnection!
}

type UserPayload {
  user: User
  errors: [Error!]
}
```

## Authentication & Security

### JWT Bearer Token
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

### API Key
```
X-API-Key: your-api-key
```

### Rate Limiting Headers
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1609459200
Retry-After: 60
```

## Usage

The skill is automatically triggered when:
- Designing new API endpoints
- Implementing authentication
- Creating error handling
- Defining response formats
- Setting up API versioning

Or use naturally with phrases like:
- "Design an API for..."
- "How should I structure this endpoint?"
- "What's the best way to handle API errors?"

## Output

The skill provides:

1. **URL structure recommendations** - RESTful endpoint design
2. **Response format templates** - Consistent JSON structures
3. **Status code guidance** - Appropriate HTTP codes
4. **Security patterns** - Authentication and authorization
5. **OpenAPI specs** - Documentation templates
6. **Best practices** - Industry-standard conventions

## API Security Checklist

- ✓ HTTPS only
- ✓ Authentication on all endpoints
- ✓ Authorization checks
- ✓ Input validation
- ✓ Rate limiting
- ✓ Request size limits
- ✓ CORS properly configured
- ✓ No sensitive data in URLs
- ✓ Audit logging

## Related Skills

- [Architecture Patterns](architecture-patterns.md) - System design decisions
- [Testing Strategy](testing-strategy.md) - API testing approaches
- [Performance Optimization](performance-optimization.md) - API performance

---

<small>Source: `external/claude-workflow:api-design`</small>
