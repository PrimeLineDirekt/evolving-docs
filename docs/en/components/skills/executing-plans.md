---
title: Executing Plans
type: skill
tags: [execution, workflow, automation]
lang: en
confidence: 95
---

# Executing Plans

![Executing Plans Skill](../../shared/assets/infographics/skills/executing-plans.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Execute implementation plans with hint-based delegation |
| **Complexity** | High |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The Executing Plans skill runs implementation plans created by the Writing Plans skill. It interprets delegation hints, dispatches to appropriate agents, tracks progress, and enforces review gates.

## Execution Flow

1. **Load Plan** - Read plan file
2. **Extract Tasks** - Parse phases and tasks
3. **Follow Hints** - Delegate based on hints
4. **Track Progress** - Update task status
5. **Review Gates** - Validate at phase boundaries
6. **Create Handoff** - Document session results

## Hint-Based Delegation

| Hint | Action |
|------|--------|
| `[EXPLORE]` | Spawn Explore agent (haiku) |
| `[DELEGATE]` | Spawn implementation agent (sonnet) |
| `[DELEGATE:agent]` | Spawn specific named agent |
| `[DIRECT]` | Execute directly (no delegation) |

## Review Gates

At each phase boundary:
1. Run code-reviewer agent
2. Fix critical issues (>90% confidence)
3. Continue to next phase only if clean

**Final Phase Review:**
- Full analysis with all relevant agents
- Type analyzer, test analyzer, etc.

## Progress Tracking

- Todo list with task IDs
- Mark in_progress when starting
- Mark completed when done
- Handoff at session end

## Usage

```
/executing-plans path/to/plan.md
```

## Related Skills

- [Writing Plans](writing-plans.md) - Create the plan first
- [Dispatching Parallel Agents](dispatching-parallel-agents.md) - Run tasks in parallel
- [Verification Before Completion](verification-before-completion.md) - Verify work

---

<small>Source: `superpowers:executing-plans`</small>
