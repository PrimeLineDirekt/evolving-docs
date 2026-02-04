---
title: Project Analysis
type: skill
tags: [analysis, codebase, onboarding, tech-stack]
lang: en
confidence: 95
---

# Project Analysis

![Project Analysis Skill](../../shared/assets/infographics/skills/project-analysis.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Workflow Skill |
| **Purpose** | Analyze project structure and tech stack |
| **Complexity** | Medium |
| **Source** | claude-workflow |
| **Plugin** | external |
| **Context** | fork |
| **Isolation** | moderate |
| **Timeout** | 180s |
</div>

## What It Does

The Project Analysis skill systematically analyzes any project to understand its structure, tech stack, patterns, and conventions. It provides a comprehensive overview for onboarding to new codebases or understanding existing architecture.

## Key Principles

- **Systematic exploration** - Follow consistent analysis pattern
- **Tech stack detection** - Identify frameworks and tools
- **Pattern recognition** - Understand architectural decisions
- **Convention discovery** - Learn project standards
- **Quick onboarding** - Provide actionable overview

## Analysis Process

### 1. Quick Overview (30 seconds)
```bash
# Check for common project markers
ls -la
cat README.md 2>/dev/null | head -50
```

### 2. Tech Stack Detection

#### Package Managers & Dependencies
- `package.json` → Node.js/JavaScript/TypeScript
- `requirements.txt` / `pyproject.toml` / `setup.py` → Python
- `go.mod` → Go
- `Cargo.toml` → Rust
- `pom.xml` / `build.gradle` → Java
- `Gemfile` → Ruby

#### Frameworks (from dependencies)
- React, Vue, Angular, Next.js, Nuxt
- Express, FastAPI, Django, Flask, Rails
- Spring Boot, Gin, Echo

#### Infrastructure
- `Dockerfile`, `docker-compose.yml` → Containerized
- `kubernetes/`, `k8s/` → Kubernetes
- `terraform/`, `.tf` files → IaC
- `serverless.yml` → Serverless Framework
- `.github/workflows/` → GitHub Actions

### 3. Project Structure Analysis

Present as a tree with annotations:
```
project/
├── src/              # Source code
│   ├── components/   # UI components (React/Vue)
│   ├── services/     # Business logic
│   ├── models/       # Data models
│   └── utils/        # Shared utilities
├── tests/            # Test files
├── docs/             # Documentation
└── config/           # Configuration
```

### 4. Key Patterns Identification

Look for and report:
- **Architecture**: Monolith, Microservices, Serverless, Monorepo
- **API Style**: REST, GraphQL, gRPC, tRPC
- **State Management**: Redux, Zustand, MobX, Context
- **Database**: SQL, NoSQL, ORM used
- **Authentication**: JWT, OAuth, Sessions
- **Testing**: Jest, Pytest, Go test, etc.

### 5. Development Workflow

Check for:
- `.eslintrc`, `.prettierrc` → Linting/Formatting
- `.husky/` → Git hooks
- `Makefile` → Build commands
- `scripts/` in package.json → NPM scripts

## Output Format

```markdown
# Project: [Name]

## Overview
[1-2 sentence description]

## Tech Stack
| Category | Technology |
|----------|------------|
| Language | TypeScript |
| Framework | Next.js 14 |
| Database | PostgreSQL |
| ...      | ...        |

## Architecture
[Description with simple ASCII diagram if helpful]

## Key Directories
- `src/` - [purpose]
- `lib/` - [purpose]

## Entry Points
- Main: `src/index.ts`
- API: `src/api/`
- Tests: `npm test`

## Conventions
- [Naming conventions]
- [File organization patterns]
- [Code style preferences]

## Quick Commands
| Action | Command |
|--------|---------|
| Install | `npm install` |
| Dev | `npm run dev` |
| Test | `npm test` |
| Build | `npm run build` |
```

## Usage

The skill is triggered when:
- Starting work on a new codebase
- Onboarding to a project
- Understanding existing architecture

Or use naturally with phrases like:
- "Analyze this project"
- "How does this project work?"
- "What's the tech stack?"

## Output

The skill provides:

1. **Tech stack overview** - Languages, frameworks, tools
2. **Architecture description** - High-level system design
3. **Directory structure** - File organization patterns
4. **Conventions guide** - Naming, styling, patterns
5. **Quick commands** - Essential development tasks
6. **Entry points** - Where to start reading code

## Related Skills

- [Architecture Patterns](architecture-patterns.md) - Understanding architectural decisions
- [Git Workflow](git-workflow.md) - Understanding Git conventions
- [Testing Strategy](testing-strategy.md) - Understanding test setup

---

<small>Source: `external/claude-workflow:project-analysis`</small>
