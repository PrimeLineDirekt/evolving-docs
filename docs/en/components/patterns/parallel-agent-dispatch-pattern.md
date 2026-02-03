---
title: parallel-agent-dispatch-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# parallel-agent-dispatch-pattern


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | When facing multiple independent problems, dispatch specialized agents in parallel rather than solving sequentially.

```
Sequential (slow):
  Problem A → Solve → Problem B → Solve → Problem C → Solve |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does




## System Impact

**When to Apply:**
**Good candidates:**
- Multiple independent features
- Parallel test fixes
- Multi-file refactoring with clear boundaries
- Research across different domains

**Poor candidates:**
- Sequential dependencies
- Shared state modifications
- Single-file changes
- Tightly coupled components

---

**Integration Points:**
- Can be combined with multi-agent orchestration patterns
- Integrates with task coordination systems
- Requires proper state management




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Sequential (slow):
  Problem A → Solve → Problem B → Solve → Problem C → Solve
  Total time: 3x

Parallel (fast):
  Problem A → Agent A ─┐
  Problem B → Agent B ─┼→ Integrate Results
  Problem C → Agent C ─┘
  Total time: 1x + integration
```


#### Example



**Code:**
```markdown
## Agent Task: {Domain Name}

**Scope**: Only files in {path}
**Goal**: {Specific outcome}
**Constraints**:
- Do not modify files outside scope
- {Other boundaries}

**Expected Output**:
- {Deliverable 1}
- {Deliverable 2}
```


#### Example



**Code:**
```bash
<task 1: Agent for Domain A>
<task 2: Agent for Domain B>
<task 3: Agent for Domain C>
```


#### Example



**Code:**
```bash
User: "Add authentication, logging, and caching"

Orchestrator:
  1. Identify: 3 independent concerns
  2. Create tasks:
     - Auth Agent: src/auth/, middleware
     - Logging Agent: src/logging/, config
     - Cache Agent: src/cache/, redis setup
  3. Dispatch parallel
  4. Integrate: wire together in main app
```


#### Example



**Code:**
```markdown
**Agent A Boundary**: src/feature-a/**
**Agent B Boundary**: src/feature-b/**
**Shared Interface**: src/types/shared.ts (read-only)
```


#### Example



**Code:**
```bash
Multiple failures/tasks?
    │
    ├─ No → Single agent handles all
    │
    └─ Yes → Are they independent?
              │
              ├─ No (related) → Single agent investigates all
              │
              └─ Yes → Can they work in parallel?
                        │
                        ├─ No (shared state) → Sequential agents
                        │
                        └─ Yes → PARALLEL DISPATCH
```


#### Example



**Code:**
```markdown
Fix the 3 failing tests in src/agents/agent-tool-abort.test.ts:

1. "should abort tool with partial output" - expects 'interrupted at'
2. "should handle mixed completed and aborted" - fast tool aborted
3. "should properly track pendingToolCount" - expects 3, gets 0

These are timing/race condition issues. Your task:

1. Read the test file and understand what each test verifies
2. Identify root cause - timing issues or actual bugs?
3. Fix by:
   - Replacing arbitrary timeouts with event-based waiting
   - Fixing bugs in abort implementation if found

Do NOT just increase timeouts - find the real issue.

Return: Summary of what you found and what you fixed.
```


#### Example



**Code:**
```bash
Agent 1 → Fix agent-tool-abort.test.ts
Agent 2 → Fix batch-completion.test.ts
Agent 3 → Fix race-conditions.test.ts
```




## Configuration



## Best Practices

**Do:**
- Use for multi-expert coordination requiring diverse perspectives
- Apply when problem benefits from iterative refinement
- Combine with proper state management and validation
- Monitor blackboard size to prevent context overflow

**Don't:**
- Use for simple single-agent tasks
- Apply to strictly sequential workflows
- Ignore controller bottleneck risks
- Forget to handle write conflicts in concurrent scenarios




## Related


---

<small>Source: `knowledge/patterns/parallel-agent-dispatch-pattern.md`</small>
