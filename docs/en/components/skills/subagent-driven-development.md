---
title: Subagent-Driven Development
type: skill
tags: [agents, orchestration, delegation]
lang: en
confidence: 95
---

# Subagent-Driven Development

![Subagent-Driven Development Skill](../../shared/assets/infographics/skills/subagent-driven-development.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Orchestrate sub-agents for complex implementations |
| **Complexity** | High |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The Subagent-Driven Development skill uses specialized sub-agents to handle independent tasks within a larger implementation. The main agent orchestrates while sub-agents execute, each with fresh context optimized for their specific task.

## Why Sub-Agents?

| Aspect | Main Agent | Sub-Agent |
|--------|------------|-----------|
| **Context** | Full history | Fresh, task-focused |
| **Focus** | Multi-task orchestration | Single specialized task |
| **Cost** | Higher (Opus + context) | Lower (Haiku/Sonnet) |

## Agent Types

| Type | Use Case | Model |
|------|----------|-------|
| **Explore** | Codebase discovery | haiku |
| **Implement** | Feature development | sonnet |
| **Review** | Code quality checks | sonnet |
| **Debug** | Bug investigation | sonnet |

## Orchestration Pattern

```
┌─────────────────────────────────┐
│         Main Agent              │
│       (Orchestrator)            │
└──────────────┬──────────────────┘
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│Explore │ │Implement│ │Review │
│ Agent  │ │ Agent   │ │ Agent │
└────────┘ └────────┘ └────────┘
    │          │          │
    └──────────┼──────────┘
               ▼
┌─────────────────────────────────┐
│      Result Aggregation         │
└─────────────────────────────────┘
```

## Key Principles

- **Fresh Context** - Each agent starts clean
- **Specialized Agents** - Right agent for the job
- **Parallel Execution** - Independent tasks run together
- **Result Synthesis** - Aggregate findings at end

## Model Selection

| Task Complexity | Model | Examples |
|-----------------|-------|----------|
| 1-3 (Simple) | haiku | Exploration, simple analysis |
| 4-6 (Medium) | sonnet | Implementation, reviews |
| 7+ (Complex) | Don't delegate | Architecture decisions |

## Usage

Applied automatically when using `[DELEGATE]` hints in plans.

## Related Skills

- [Dispatching Parallel Agents](dispatching-parallel-agents.md) - Parallel execution
- [Executing Plans](executing-plans.md) - Hint-based delegation

---

<small>Source: `superpowers:subagent-driven-development`</small>
