# Agent Coordination

Evolving coordinates specialized agents through built-in tools, plugin integrations, dependency management, automated reviews, and intelligent failure recovery.

---

## Built-in Agents

### What It Does

Provides three core agents optimized for specific workflows: exploration, planning, and debugging.

### Agent Types

| Agent | Purpose | Model | Auto-Delegate |
|-------|---------|-------|---------------|
| **Explore** | Codebase search, file discovery | haiku | Keywords: find, search, explore |
| **Plan** | Architecture planning, task breakdown | sonnet | Keywords: plan, design, architect |
| **debugger** | Systematic bug investigation | sonnet | Keywords: debug, error, fix |

### How It Works

**Explore Agent**:
```
User: "Find all authentication files"
     │
     ▼
┌──────────────────────────┐
│ 1. Keyword Detection     │
│    ["find", "files"]     │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 2. Auto-Delegate         │
│    subagent_type: Explore│
│    model: haiku          │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 3. Fresh Context         │
│    • No history bloat    │
│    • Focused search      │
│    • Fast execution      │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 4. Result Return         │
│    Files: [auth.ts,      │
│           authService.ts,│
│           login.tsx]     │
└──────────────────────────┘
```

**Plan Agent**:
```
User: "Create implementation plan for auth feature"
     │
     ▼
Plan Agent (sonnet):
  → Analyzes requirements
  → Breaks into phases
  → Creates task hierarchy
  → Assigns delegation hints
  → Returns structured plan
```

**debugger Agent**:
```
User: "Debug login failure"
     │
     ▼
debugger Agent (sonnet):
  → Reads error messages
  → Traces execution flow
  → Identifies root cause
  → Suggests fixes with confidence
  → Verifies proposed solution
```

### Configuration

**Location**: Built-in to Claude Code (no config needed)

**Invocation**:
```javascript
Task({
  subagent_type: "Explore",  // or "Plan", "debugger"
  model: "haiku",             // or "sonnet"
  prompt: "Your task description"
})
```

### Example

```
User: "How is routing implemented?"

System:
  → Detects: exploration task
  → Delegates: Explore Agent (haiku)
  → Agent searches codebase
  → Returns: "Routing uses React Router v6..."

Cost: $0.001 (haiku vs $0.015 for sonnet)
Speed: 2 seconds (fresh context)
```

**Related**: `.claude/rules/delegation.md`

---

## Plugin Agents

### What It Does

Extends core capabilities with specialized agents from Claude Code plugins: feature-dev and pr-review-toolkit.

### Available Plugins

**feature-dev Plugin**:
| Agent | Purpose |
|-------|---------|
| `feature-dev:code-reviewer` | General code quality review |
| `feature-dev:code-architect` | Architecture and structure review |
| `feature-dev:code-explorer` | Deep codebase analysis |

**pr-review-toolkit Plugin**:
| Agent | Purpose |
|-------|---------|
| `pr-review-toolkit:code-reviewer` | PR-focused code review |
| `pr-review-toolkit:type-design-analyzer` | Type/interface quality |
| `pr-review-toolkit:silent-failure-hunter` | Error handling gaps |
| `pr-review-toolkit:pr-test-analyzer` | Test coverage & quality |
| `pr-review-toolkit:comment-analyzer` | Comment accuracy |
| `pr-review-toolkit:code-simplifier` | Complexity reduction |

### How It Works

```
Code Changed
     │
     ▼
┌──────────────────────────┐
│ 1. Trigger Detection     │
│    • Todo completed?     │
│    • Plan phase done?    │
│    • Manual review?      │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 2. Agent Selection       │
│                          │
│ Base: code-reviewer      │
│                          │
│ +type-design-analyzer    │
│   (if new types)         │
│                          │
│ +silent-failure-hunter   │
│   (if error handling)    │
│                          │
│ +pr-test-analyzer        │
│   (if tests added)       │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 3. Parallel Execution    │
│                          │
│ All selected agents run  │
│ simultaneously           │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 4. Finding Synthesis     │
│                          │
│ • Critical (must fix)    │
│ • Warnings (should fix)  │
│ • Suggestions (optional) │
└──────────────────────────┘
```

### Configuration

**Location**: `_graph/cache/delegation-config.json`

```json
{
  "task_types": {
    "code_review_feature_dev": {
      "agent": "feature-dev:code-reviewer",
      "model": "sonnet",
      "inline_hints": ["[review]", "[cr]"]
    },
    "type_design_review": {
      "agent": "pr-review-toolkit:type-design-analyzer",
      "model": "sonnet",
      "inline_hints": ["[types]", "[interface]"]
    }
  }
}
```

### Example

**Post-Todo Review**:
```
Todo completed:
  ✓ Create User interface
  ✓ Implement AuthService
  ✓ Add error handling
  ✓ Write tests

System triggers review:
  → feature-dev:code-reviewer (base)
  → type-design-analyzer (User interface)
  → silent-failure-hunter (error handling)
  → pr-test-analyzer (tests)

Parallel execution → Results in 15 seconds

Findings:
  Critical: 0
  Warnings: 2 (missing null checks)
  Suggestions: 1 (consider JSDoc)
```

**Related**: `knowledge/references/claude-code-plugins-guide.md`

---

## Task Dependencies

### What It Does

Manages execution order through blockedBy relationships, ensuring prerequisites complete before dependent tasks start.

### How It Works

```
Task Creation with Dependencies:

┌──────────────────────────┐
│ Task 1: Schema           │
│ blockedBy: []            │
└──────────┬───────────────┘
           │
┌──────────▼───────────────┐
│ Task 2: API              │
│ blockedBy: []            │
└──────────┬───────────────┘
           │
           ├──► Both run in parallel
           │
┌──────────▼───────────────┐
│ Task 3: Frontend         │
│ blockedBy: [1, 2]        │
│                          │
│ ⏸ WAITS for 1 & 2       │
└──────────┬───────────────┘
           │
           └──► Runs after both complete
```

### Configuration

**Setting Dependencies**:
```javascript
// Create tasks
TaskCreate({ subject: "Define schema" })        // → Task #1
TaskCreate({ subject: "Create API endpoint" })  // → Task #2
TaskCreate({ subject: "Build frontend" })       // → Task #3

// Set dependencies
TaskUpdate({
  taskId: "3",
  addBlockedBy: ["1", "2"]
})
```

**Dependency Patterns**:

| Pattern | Structure | Use Case |
|---------|-----------|----------|
| **Sequential** | A → B → C | Steps must be in order |
| **Fan-out/Fan-in** | A,B → C | Parallel work, then combine |
| **Prerequisite** | Setup → all others | Common foundation needed |

### Example

**Feature Implementation**:
```
Tasks:
1. Schema design           (no dependencies)
2. API implementation      (no dependencies)
3. Frontend component      (depends on 1, 2)
4. Integration test        (depends on 3)

Execution:
  Time 0s:  Start 1 & 2 (parallel)
  Time 15s: Both complete → Start 3
  Time 30s: 3 completes → Start 4
  Time 40s: All done

Total: 40s (vs 70s if sequential)
```

**Related**: `.claude/rules/swarm-orchestration.md`

---

## Review Pipeline

### What It Does

Automatically triggers code reviews by specialized agents after todo completion or phase boundaries.

### How It Works

```
Todo List Completed
     │
     ▼
┌──────────────────────────┐
│ 1. Trigger Check         │
│                          │
│ • All todos completed?   │
│ • Code files changed?    │
│ • Not just docs?         │
└──────────┬───────────────┘
           │ YES
           ▼
┌──────────────────────────┐
│ 2. Change Analysis       │
│                          │
│ What changed?            │
│ • New types?             │
│ • Error handling?        │
│ • Tests?                 │
│ • Comments?              │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 3. Agent Selection       │
│                          │
│ Always:                  │
│ • code-reviewer          │
│                          │
│ Conditional:             │
│ • type-design-analyzer   │
│ • silent-failure-hunter  │
│ • pr-test-analyzer       │
│ • comment-analyzer       │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 4. Parallel Review       │
│                          │
│ All agents execute       │
│ simultaneously           │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ 5. Synthesized Report    │
│                          │
│ Critical: Must fix now   │
│ Warnings: Should fix     │
│ Suggestions: Consider    │
└──────────────────────────┘
```

### Configuration

**Review Matrix**:

| Change Type | Additional Agents |
|-------------|-------------------|
| New types/interfaces | type-design-analyzer |
| Error handling code | silent-failure-hunter |
| Test files | pr-test-analyzer |
| Comments/docs | comment-analyzer |
| New structures | code-architect |

### Example

**Simple Feature**:
```
Todos completed:
  ✓ Implement login method
  ✓ Add validation

Review agents:
  → code-reviewer only

Findings: 1 warning (missing error case)
```

**Complex Feature**:
```
Todos completed:
  ✓ Define User interface
  ✓ Create AuthService class
  ✓ Add error handling
  ✓ Write unit tests
  ✓ Add JSDoc comments

Review agents (parallel):
  → code-reviewer
  → type-design-analyzer (User interface)
  → code-architect (AuthService class)
  → silent-failure-hunter (error handling)
  → pr-test-analyzer (tests)
  → comment-analyzer (JSDoc)

Findings:
  Critical: 0
  Warnings: 3
  Suggestions: 2
```

**Related**: `.claude/rules/post-todo-review.md`

---

## Failure Recovery

### What It Does

Implements a 3-attempt escalation strategy with mandatory sub-agent analysis after repeated failures.

### How It Works

```
Problem Detected
     │
     ▼
┌──────────────────────────┐
│ Attempt 1-2: Self Fix    │
│                          │
│ • Diagnose with evidence │
│ • Identify root cause    │
│ • Fix & verify           │
└──────────┬───────────────┘
           │
      Still failing?
           │
           ▼
┌──────────────────────────┐
│ Attempt 3: SUB-AGENTS    │
│ (MANDATORY)              │
│                          │
│ STOP self-fixing!        │
│                          │
│ Launch agents:           │
│ • Explore: Backend API   │
│ • Explore: Frontend code │
│ • debugger: E2E flow     │
│                          │
│ → Gather FACTS           │
└──────────┬───────────────┘
           │
      Still unclear?
           │
           ▼
┌──────────────────────────┐
│ Attempt 4: USER          │
│                          │
│ Present:                 │
│ • Agent findings         │
│ • Contradictions         │
│ • Proposed options       │
│                          │
│ Request guidance         │
└──────────┬───────────────┘
           │
      Can't help?
           │
           ▼
┌──────────────────────────┐
│ BLOCKED: Document        │
│                          │
│ • Log in memory          │
│ • Create experience      │
│ • Continue other work    │
└──────────────────────────┘
```

### Configuration

**No configuration** - enforced by rule system.

**Loop Detection**:
- Same change reversed and re-applied
- Conflicting information sources
- Ping-pong between two states

### Example

**Typical Bug Fix**:
```
Attempt 1:
  → Read error message
  → Fix missing import
  → Verify: Still fails

Attempt 2:
  → Check type definitions
  → Add type annotation
  → Verify: Still fails

Attempt 3 (MANDATORY SUB-AGENTS):
  → Explore Agent: Check API contract
  → Explore Agent: Check caller code
  → debugger Agent: Trace request/response

  Findings:
    - API expects 'email' field
    - Code sends 'username' field
    - Handoff was wrong (outdated)

  Fix with confidence:
  → Change 'username' to 'email'
  → Verify: ✓ PASSES

No more attempts needed!
```

**Without Escalation** (anti-pattern):
```
Attempt 1: Try fix A → Fails
Attempt 2: Try fix B → Fails
Attempt 3: Try fix C → Fails
Attempt 4: Try fix A again → Fails (loop!)
...
Token waste, no progress
```

**Related**: `.claude/rules/failure-recovery.md`

---

## Delegation Enforcer

### What It Does

Monitors plan execution to ensure delegation hints are followed, providing gap tracking and session summaries.

### How It Works

```
Plan Execution Starts
     │
     ▼
┌──────────────────────────┐
│ For Each Task:           │
│                          │
│ Extract hint from title: │
│ • [EXPLORE]              │
│ • [DELEGATE]             │
│ • [DELEGATE:agent]       │
│ • [DIRECT]               │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ Enforcement Check        │
│                          │
│ Was hint followed?       │
│                          │
│ [EXPLORE] → Explore used?│
│ [DELEGATE] → Task used?  │
│ [DIRECT] → Self executed?│
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ Gap Tracking             │
│                          │
│ If hint NOT followed:    │
│ • Log to JSONL           │
│ • Count for summary      │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│ Session-End Summary      │
│                          │
│ "2/5 [DELEGATE] hints    │
│  not followed"           │
│                          │
│ Shows which tasks        │
└──────────────────────────┘
```

### Configuration

**Location**: `.claude/hooks/delegation-enforcer.py`

**Inline Hints** (in plan):
```markdown
### Task 1.1: Analyze codebase `[EXPLORE]`
### Task 1.2: Implement auth `[DELEGATE]`
### Task 1.3: Phase review `[DELEGATE:code-reviewer]`
### Task 1.4: Fix typo `[DIRECT]`
```

**Agent Mapping**:
```json
{
  "[EXPLORE]": {
    "agent": "Explore",
    "model": "haiku"
  },
  "[DELEGATE]": {
    "agent": "general-purpose",
    "model": "sonnet",
    "traits": ["based on task type"]
  },
  "[DELEGATE:code-reviewer]": {
    "agent": "feature-dev:code-reviewer",
    "model": "sonnet"
  }
}
```

### Example

**Plan with Hints**:
```markdown
### Task 1.1: Find auth files `[EXPLORE]`
### Task 1.2: Review auth logic `[DELEGATE:code-reviewer]`
### Task 1.3: Fix import statement `[DIRECT]`
```

**Execution**:
```
Task 1.1:
  → Hint: [EXPLORE]
  → Used: Task(subagent_type="Explore") ✓
  → Gap: None

Task 1.2:
  → Hint: [DELEGATE:code-reviewer]
  → Used: Task(subagent_type="feature-dev:code-reviewer") ✓
  → Gap: None

Task 1.3:
  → Hint: [DIRECT]
  → Used: Edit tool directly ✓
  → Gap: None
```

**Session-End Summary**:
```
📊 Delegation Summary: 3/3 hints followed ✓

No gaps detected - excellent execution!
```

**With Gaps**:
```
📊 Delegation Summary: 1/3 hints not followed

  - [DELEGATE] Implement auth service...
    (executed directly instead of delegating)

💡 Tip: Use Task tool with appropriate subagent_type for [DELEGATE] tasks
```

**Related**: `.claude/rules/plan-execution-enforcement.md`

---

## Summary

Agent Coordination provides:
- **Built-in Agents**: Explore, Plan, debugger (optimized)
- **Plugin Agents**: 9 specialized reviewers from 2 plugins
- **Task Dependencies**: blockedBy coordination (parallel + sequential)
- **Review Pipeline**: Automatic post-todo reviews
- **Failure Recovery**: 3-attempt escalation with sub-agents
- **Delegation Enforcer**: Hint tracking + session summaries

**Result**: Specialized work goes to specialists, coordination happens automatically.
