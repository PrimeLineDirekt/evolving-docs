---
title: Architecture Patterns
type: skill
tags: [architecture, patterns, design, system-design]
lang: en
confidence: 95
---

# Architecture Patterns

![Architecture Patterns Skill](../../shared/assets/infographics/skills/architecture-patterns.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Workflow Skill |
| **Purpose** | Guide software architecture and design decisions |
| **Complexity** | High |
| **Source** | claude-workflow |
| **Plugin** | external |
</div>

## What It Does

The Architecture Patterns skill provides guidance on software architecture patterns and design decisions. It helps choose appropriate architectural approaches based on project size, team size, and requirements, from simple layered architectures to complex distributed systems.

## Key Principles

- **Simplicity first** - Start simple, evolve when needed
- **Team alignment** - Match architecture to team capabilities
- **Requirements-driven** - Let business needs drive decisions
- **Scalability consideration** - Plan for growth trajectory
- **Maintainability focus** - Optimize for change

## Pattern Selection

### By Project Size

| Size | Recommended Pattern |
|------|---------------------|
| Small (<10K LOC) | Simple MVC/Layered |
| Medium (10K-100K) | Clean Architecture |
| Large (>100K) | Modular Monolith or Microservices |

### By Team Size

| Team | Recommended |
|------|-------------|
| 1-3 devs | Monolith with clear modules |
| 4-10 devs | Modular Monolith |
| 10+ devs | Microservices (if justified) |

## Common Patterns

### Layered Architecture
```
┌─────────────────────────────┐
│       Presentation          │  <- UI, API Controllers
├─────────────────────────────┤
│       Application           │  <- Use Cases, Services
├─────────────────────────────┤
│         Domain              │  <- Business Logic, Entities
├─────────────────────────────┤
│      Infrastructure         │  <- Database, External APIs
└─────────────────────────────┘
```
**Use when**: Simple CRUD apps, small teams, quick prototypes

### Clean Architecture
```
┌─────────────────────────────────────┐
│            Frameworks & Drivers      │
│  ┌─────────────────────────────┐    │
│  │     Interface Adapters       │    │
│  │  ┌─────────────────────┐    │    │
│  │  │   Application       │    │    │
│  │  │  ┌─────────────┐    │    │    │
│  │  │  │   Domain    │    │    │    │
│  │  │  └─────────────┘    │    │    │
│  │  └─────────────────────┘    │    │
│  └─────────────────────────────┘    │
└─────────────────────────────────────┘
```
**Use when**: Complex business logic, long-lived projects, testability is key

### Hexagonal (Ports & Adapters)
```
        ┌──────────┐
        │ HTTP API │
        └────┬─────┘
             │ Port
    ┌────────▼────────┐
    │                 │
    │   Application   │
    │     Core        │
    │                 │
    └────────┬────────┘
             │ Port
        ┌────▼─────┐
        │ Database │
        └──────────┘
```
**Use when**: Need to swap external dependencies, multiple entry points

### Event-Driven Architecture
```
Producer -> Event Bus -> Consumer
              │
              ├─-> Consumer
              │
              └─-> Consumer
```
**Use when**: Loose coupling needed, async processing, scalability

### CQRS (Command Query Responsibility Segregation)
```
┌─────────────┐      ┌─────────────┐
│  Commands   │      │   Queries   │
│  (Write)    │      │   (Read)    │
└──────┬──────┘      └──────┬──────┘
       │                    │
       ▼                    ▼
  Write Model          Read Model
       │                    │
       └────────┬───────────┘
                ▼
           Event Store
```
**Use when**: Different read/write scaling, complex domains, event sourcing

## Directory Structures

### Feature-Based (Recommended for medium+)
```
src/
├── features/
│   ├── users/
│   │   ├── api/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── types/
│   └── orders/
│       ├── api/
│       ├── components/
│       └── ...
├── shared/
│   ├── components/
│   ├── hooks/
│   └── utils/
└── app/
    └── ...
```

### Layer-Based (Simple apps)
```
src/
├── controllers/
├── services/
├── models/
├── repositories/
└── utils/
```

## Decision Framework

### Trade-off Analysis Template
```markdown
## Decision: [What we're deciding]

### Options Considered
1. Option A: [Description]
2. Option B: [Description]

### Trade-offs
| Criteria | Option A | Option B |
|----------|----------|----------|
| Complexity | Low | High |
| Scalability | Medium | High |
| Team familiarity | High | Low |

### Decision
We chose [Option] because [reasoning].

### Consequences
- [What this enables]
- [What this constrains]
```

## Usage

The skill is triggered when:
- Designing new systems
- Choosing architectural patterns
- Structuring projects
- Making technology decisions

Or use naturally with phrases like:
- "How should I structure this project?"
- "What architecture pattern should I use?"
- "Design the system architecture for..."

## Output

The skill provides:

1. **Pattern recommendations** - Based on project context
2. **Directory structures** - Organized code layouts
3. **Trade-off analysis** - Decision framework
4. **Best practices** - Industry conventions
5. **Migration paths** - Evolution strategies

## Related Skills

- [API Design](api-design.md) - API architectural decisions
- [Project Analysis](project-analysis.md) - Understanding existing architectures
- [Testing Strategy](testing-strategy.md) - Testing architectural components

---

<small>Source: `external/claude-workflow:architecture-patterns`</small>
