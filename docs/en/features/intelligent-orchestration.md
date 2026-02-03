# Intelligent Orchestration

Evolving's orchestration layer automatically delegates tasks to specialized agents, composes traits for optimal performance, and selects the right model for each job.

![Intelligent Orchestration Architecture](/shared/assets/infographics/intelligent-orchestration.png)

---

## Smart Delegation

### What It Does

Automatically determines whether to handle a task directly or delegate to a specialized agent based on a scoring system.

### How It Works

```
User Task
    │
    ▼
┌─────────────────────────┐
│ Score Calculation       │
│                         │
│ +2  Scope > 2 files     │
│ +2  Bulk operation      │
│ +2  Research/learn      │
│ +2  Code review         │
│ +3  Exploration         │
│ -10 Critical keywords   │
│ -5  User wants to see   │
└──────────┬──────────────┘
           │
     Score ≥ 3?
      /        \
    YES         NO
     │           │
     ▼           ▼
  Delegate    Execute
             Directly
```

### Configuration

**Location**: `_graph/cache/delegation-config.json`

```json
{
  "task_types": {
    "exploration": {
      "agent": "Explore",
      "model": "haiku",
      "auto_delegate": true
    },
    "bug_fix": {
      "traits": ["engineer", "precise", "iterative"],
      "model": "sonnet"
    }
  }
}
```

### Example

```
User: "Find all uses of the auth function"

System:
  → Keywords: ["find", "search"]
  → Score: +3 (exploration)
  → Delegates to Explore Agent (haiku)
  → Completes in fresh context
```

**Related**: `.claude/rules/delegation.md`

---

## Agent Swarm

### What It Does

Coordinates multiple specialized agents working in parallel on independent subtasks.

### How It Works

```
Complex Task
     │
     ▼
┌─────────────────────────────┐
│ Task Decomposition          │
│                             │
│ Task A → Agent 1 (haiku)    │
│ Task B → Agent 2 (sonnet)   │
│ Task C → Agent 3 (sonnet)   │
│   (blockedBy: [A, B])       │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│ Parallel Execution          │
│                             │
│ ┌─────┐  ┌─────┐            │
│ │  A  │  │  B  │ (parallel) │
│ └──┬──┘  └──┬──┘            │
│    └────┬────┘              │
│         ▼                   │
│      ┌─────┐                │
│      │  C  │ (waits)        │
│      └─────┘                │
└──────────┬──────────────────┘
           │
           ▼
    Result Synthesis
```

### Configuration

Uses Task Tool with dependencies:

```javascript
// Create tasks
TaskCreate({ subject: "Analyze backend", ... })  // Task #1
TaskCreate({ subject: "Analyze frontend", ... }) // Task #2
TaskCreate({ subject: "Integration test", ... }) // Task #3

// Set dependency
TaskUpdate({ taskId: "3", addBlockedBy: ["1", "2"] })
```

### Example

```
User: "Refactor the auth module"

System decomposes:
  1. Explore current implementation (haiku, parallel)
  2. Review dependencies (haiku, parallel)
  3. Generate refactor plan (sonnet, after 1+2)
  4. Execute changes (sonnet, after 3)

Result: 2x faster through parallelization
```

**Related**: `.claude/rules/swarm-orchestration.md`

---

## Trait Composition

### What It Does

Builds specialized agent profiles by combining 480 possible trait combinations (8 expertise × 10 personality × 6 approach).

### How It Works

**Trait Categories**:
- **Expertise**: engineer, researcher, architect, security, analyst, etc.
- **Personality**: precise, direct, cautious, thorough, skeptical, etc.
- **Approach**: systematic, iterative, exploratory, adversarial, etc.

**Composition**:
```
Task: Fix subtle bug
  → Traits: ["engineer", "precise", "iterative"]
  → Profile: Engineering-focused, detail-oriented, step-by-step

Task: Security audit
  → Traits: ["security", "skeptical", "adversarial"]
  → Profile: Security-focused, distrusting, attack-minded
```

### Configuration

**Location**: `knowledge/rules/delegation/trait-system.md`

Traits are automatically selected based on task type via `delegation-config.json`.

### Example

```json
{
  "task_type": "bug_fix",
  "traits": ["engineer", "precise", "iterative"],
  "profile": {
    "focus": "Code correctness",
    "approach": "Systematic debugging",
    "mindset": "Detail-oriented"
  }
}
```

**Output**:
```
Agent behavior:
  ✓ Checks diagnostics before editing
  ✓ Tests after each change
  ✓ Documents assumptions
  ✓ Verifies with build
```

**Related**: `knowledge/rules/delegation/trait-system.md`

---

## Model Selection

### What It Does

Automatically selects the optimal model (haiku/sonnet/opus) based on task complexity.

### How It Works

**Decision Matrix**:

| Complexity | Model | Cost | Use Case |
|------------|-------|------|----------|
| 1-3 | Haiku | $ | Search, list, simple edits |
| 4-6 | Sonnet | $$ | Refactoring, reviews, design |
| 7+ | Opus (self) | $$$ | Architecture, complex logic |

**Complexity Factors**:
- +1 per file involved
- +2 for logic changes
- +1 for new patterns
- -1 for read-only tasks

### Configuration

**Location**: `.claude/rules/smart-model-delegation.md`

```json
{
  "thresholds": {
    "haiku_max": 3,
    "sonnet_max": 6,
    "opus_min": 7
  }
}
```

### Example

```
Task: "List all commands"
  → Complexity: 1 (read-only)
  → Model: haiku
  → Cost: $0.001

Task: "Refactor auth service"
  → Complexity: 5 (3 files + logic)
  → Model: sonnet
  → Cost: $0.015

Task: "Design new architecture"
  → Complexity: 8 (multi-system)
  → Model: opus (don't delegate)
  → Cost: $0.075
```

**Related**: `.claude/rules/smart-model-delegation.md`

---

## Parallel Execution

### What It Does

Executes independent tasks simultaneously using multiple tool calls in a single message.

### How It Works

**Sequential** (slow):
```
Call Agent 1 → Wait → Call Agent 2 → Wait → Combine
```

**Parallel** (fast):
```
Call Agent 1 ┐
Call Agent 2 ├─ Wait → Combine
Call Agent 3 ┘
```

### Configuration

No configuration needed - just make multiple Task Tool calls in one response.

### Example

**Sequential (❌ inefficient)**:
```
Task({ prompt: "Analyze backend" })
[wait for result]
Task({ prompt: "Analyze frontend" })
[wait for result]
```

**Parallel (✅ optimal)**:
```
Task({ prompt: "Analyze backend" })
Task({ prompt: "Analyze frontend" })
Task({ prompt: "Check tests" })
[all execute simultaneously]
```

**Result**: 3x faster execution

**Related**: `.claude/rules/swarm-orchestration.md`

---

## Delegation Request Pattern

### What It Does

Allows Layer 2 agents (without Task Tool) to request further delegation back to Layer 1 orchestrator.

### How It Works

**Problem**: Sub-agents can't spawn more agents (no Task Tool access).

**Solution**: Sub-agent returns structured JSON request.

```
Layer 1 (Orchestrator)
    │
    │ Delegates complex task
    ▼
Layer 2 (Sub-Agent)
    │
    │ Realizes needs more specialization
    │
    ▼
┌──────────────────────────┐
│ Delegation Request JSON  │
│                          │
│ {                        │
│   "delegation_request": true,
│   "reason": "...",       │
│   "recommended_tasks": [ │
│     {                    │
│       "subject": "...",  │
│       "model": "haiku",  │
│       "agent": "Explore" │
│     }                    │
│   ]                      │
│ }                        │
└──────────┬───────────────┘
           │
           ▼
Layer 1 (Orchestrator)
    │
    │ Creates & executes tasks
    │
    ▼
  Results combined
```

### Configuration

No configuration - pattern is convention-based.

### Example

**Sub-agent output**:
```json
{
  "delegation_request": true,
  "reason": "Auth module spans 3 files with complex dependencies",
  "recommended_tasks": [
    {
      "subject": "Map auth dependencies",
      "model": "haiku",
      "agent": "Explore",
      "blockedBy": []
    },
    {
      "subject": "Refactor auth.ts",
      "model": "sonnet",
      "agent": "general-purpose",
      "traits": ["engineer", "precise"],
      "blockedBy": ["Map auth dependencies"]
    }
  ]
}
```

**Layer 1 executes**:
1. Creates Task #1 (Explore)
2. Creates Task #2 (Engineer)
3. Sets Task #2 blockedBy Task #1
4. Runs both (sequentially due to dependency)
5. Combines results

**Related**: `knowledge/patterns/delegation-request-pattern.md`

---

## Summary

Intelligent Orchestration automatically:
- **Delegates** tasks when score ≥ 3
- **Coordinates** multiple agents in parallel
- **Composes** 480 trait combinations
- **Selects** optimal model by complexity
- **Executes** independent tasks simultaneously
- **Handles** Layer 2 delegation requests

**Result**: Faster execution, lower costs, better specialization.
