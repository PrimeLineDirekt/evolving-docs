---
title: Dispatching Parallel Agents
type: skill
tags: [agents, parallel, orchestration]
lang: en
confidence: 95
---

# Dispatching Parallel Agents

![Dispatching Parallel Agents Skill](../../shared/assets/infographics/skills/dispatching-parallel-agents.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Run multiple agents concurrently for independent tasks |
| **Complexity** | High |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The Parallel Agents skill spawns multiple sub-agents simultaneously when tasks have no dependencies on each other. This dramatically reduces total execution time compared to sequential processing.

## When to Use

✅ **Good for parallel:**
- Multiple independent file analyses
- Separate module implementations
- Different aspects of code review
- Research across multiple sources

❌ **Not for parallel:**
- Tasks with dependencies
- Sequential operations (build → test → deploy)
- Shared state modifications

## The Pattern

```
┌─────────────────────────┐
│    Main Agent           │
│    (Orchestrator)       │
└──────────┬──────────────┘
           │ Parallel dispatch
    ┌──────┼──────┐
    ▼      ▼      ▼
┌──────┐┌──────┐┌──────┐
│Task A││Task B││Task C│
│Agent ││Agent ││Agent │
└──────┘└──────┘└──────┘
    │      │      │
    └──────┼──────┘
           ▼
┌─────────────────────────┐
│    Result Aggregation   │
└─────────────────────────┘
```

## Model Selection

| Task Complexity | Model | Use Case |
|-----------------|-------|----------|
| Simple/Fast | haiku | Exploration, simple analysis |
| Balanced | sonnet | Implementation, reviews |
| Complex | opus | Architecture decisions |

## Key Principles

- **Zero Dependencies** - Only parallelize independent tasks
- **Fresh Context** - Each agent gets clean context
- **Result Synthesis** - Aggregate findings after completion
- **Efficient Models** - Use haiku for simple tasks

## Usage

Automatically applied when multiple `[DELEGATE]` tasks have no blockedBy.

## Related Skills

- [Subagent-Driven Development](subagent-driven-development.md) - General sub-agent patterns
- [Executing Plans](executing-plans.md) - Plan execution with parallel tasks

---

<small>Source: `superpowers:dispatching-parallel-agents`</small>
