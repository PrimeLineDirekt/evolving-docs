---
title: Swarm Orchestration
type: rule
tags: []
lang: en
confidence: 100
---

# Swarm Orchestration


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Coordinate multi-step tasks with agent dependencies using Task Tool |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

Swarm Orchestration unifies task coordination (session-scoped via Task Tool) with domain memory (project-scoped persistence). For multi-step work (≥3 steps), it uses Task Tool with blockedBy dependencies to coordinate parallel and sequential agents. At session end, completed tasks sync to domain memory via handoff. The delegation-request pattern enables sub-agents to recommend further task breakdown.


## System Impact

**When It Triggers:**
Multi-step tasks (≥3 steps), parallel agent work, task dependencies

**Behavior Enforced:**
- Use Task Tool for ≥3 step tasks
- Set blockedBy dependencies where logical
- Enable parallel execution (fan-out/fan-in patterns)
- Sync completed tasks to memory at session end
- Support delegation-request pattern from sub-agents
- Persist tasks via CLAUDE_CODE_TASK_LIST_ID

**Integration Points:**
- Task Tool (coordination)
- Domain memory (persistence)
- delegation.md (sub-agent spawning)
- session-task-sync.sh hook (auto-sync)


## Architecture

**Trigger:** Tasks with ≥3 steps or agent dependencies

**Dependencies:**
- Task Tool
- Domain memory
- session-task-sync.sh hook

**Coordination Patterns:**

| Pattern | Example | blockedBy |
|---------|---------|-----------|
| Sequential | Build → Test → Deploy | Test blockedBy Build |
| Fan-out/Fan-in | A,B parallel → C | C blockedBy [A,B] |
| Prerequisite | Setup → all others | all blockedBy Setup |

**Delegation-Request (Layer 2 Workaround):**
Sub-agents can't spawn tasks, so they return JSON requests that Layer 1 executes.


## Usage

**Decision Matrix:**

| Situation | Use |
|-----------|-----|
| ≥3 steps in session | Tasks |
| Parallel agents | Tasks (blockedBy) |
| Session end | Memory |
| Failure documentation | Memory |
| Project state | Memory |
| Active work feedback | Tasks |

**Task Creation:**
```javascript
// Create independent tasks
TaskCreate({ subject: "Schema definition", ... })  // Task #1
TaskCreate({ subject: "API endpoint", ... })  // Task #2

// Create dependent task
TaskCreate({ subject: "Frontend component", ... })  // Task #3
TaskUpdate({ taskId: "3", addBlockedBy: ["1", "2"] })
```

**Delegation-Request Pattern:**
```json
{
  "delegation_request": true,
  "reason": "Task involves 3 independent modules",
  "recommended_tasks": [
    {
      "subject": "Auth module refactor",
      "model": "sonnet",
      "agent": "general-purpose",
      "traits": ["engineer", "precise"],
      "blockedBy": []
    },
    {
      "subject": "Integration tests",
      "model": "haiku",
      "blockedBy": ["Auth module refactor"]
    }
  ]
}
```


## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| Task Threshold | ≥3 steps | When to use Task Tool |
| Task Persistence | CLAUDE_CODE_TASK_LIST_ID=evolving | Survive terminal close |
| Session Sync | Automatic | session-task-sync.sh hook |
| Parallel Support | Yes | Multiple TaskCreate in one message |
| Layer 2 Workaround | Delegation-request pattern | Sub-agents recommend tasks |


## Best Practices

**Do:**
- Use Tasks for ≥3 step work
- Set blockedBy for real dependencies
- Execute parallel tasks simultaneously
- Sync to memory at session end
- Use delegation-request pattern for sub-agent recommendations

**Don't:**
- Use Tasks for trivial work (1-2 steps)
- Create artificial dependencies (force sequential)
- Leave tasks uncompleted (orphaned)
- Use memory for session-local work


## Related


---

<small>Source: `.claude/rules/swarm-orchestration.md`</small>
