---
title: Writing Plans
type: skill
tags: [planning, architecture, organization]
lang: en
confidence: 95
---

# Writing Plans

![Writing Plans Skill](../../shared/assets/infographics/skills/writing-plans.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Create detailed implementation plans from specs |
| **Complexity** | High |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The Writing Plans skill transforms requirements and designs into executable implementation plans. Plans include phases, tasks with delegation hints, dependency graphs, and review gates.

## Plan Structure

### Phases
- Logical groupings of related work
- Clear boundaries between phases
- Review gate at end of each phase

### Tasks with Hints
Every task includes a delegation hint:

| Hint | Meaning | Execution |
|------|---------|-----------|
| `[EXPLORE]` | Research/discovery | Explore agent |
| `[DELEGATE]` | Implementation | Sub-agent |
| `[DELEGATE:agent]` | Specific agent | Named agent |
| `[DIRECT]` | Simple/critical | Self |

### Dependencies
- Tasks can block other tasks
- Parallel execution where possible
- Critical path identified

## Plan Template

```markdown
# Plan: Feature Name

## Phase 1: Setup
### Task 1.1: Analyze codebase [EXPLORE]
### Task 1.2: Create schema [DIRECT]
### Task 1.3: Phase 1 Review [DELEGATE:code-reviewer]

## Phase 2: Implementation
### Task 2.1: Build API [DELEGATE]
### Task 2.2: Build UI [DELEGATE]
...
```

## Key Principles

- **Phase Boundaries** - Clear separation between phases
- **Delegation Hints** - Every task has a hint
- **Review Gates** - Validate before moving on
- **Dependency Awareness** - Know what blocks what

## Usage

```
/writing-plans
```

## Related Skills

- [Brainstorming](brainstorming.md) - Create the design first
- [Executing Plans](executing-plans.md) - Run the plan
- [Dispatching Parallel Agents](dispatching-parallel-agents.md) - Parallel execution

---

<small>Source: `superpowers:writing-plans`</small>
