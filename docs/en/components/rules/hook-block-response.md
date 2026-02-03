---
title: Hook Block Response
type: rule
tags: []
lang: en
confidence: 100
---

# Hook Block Response


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Enforce mandatory compliance when hooks return "block" decision |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

When any hook returns `"decision": "block"`, this rule enforces that Claude MUST stop, analyze the issue, fix the underlying problem, and retry - not ignore the warning or work around it. Hook blocks are instructions, not recommendations. The rule prevents common bypass attempts like deleting files, ignoring warnings, or superficially acknowledging without fixing.


## System Impact

**When It Triggers:**
When any hook returns `{"decision": "block", "message": "..."}`

**Behavior Enforced:**
1. **STOP** - No further tool calls until problem is resolved
2. **ANALYZE** - Understand what the hook flagged
3. **FIX** - Address the root cause (not symptoms)
4. **VERIFY** - Retry Write/Edit must pass hook validation

**Forbidden Actions:**
- Ignore warning and continue
- Delete file to bypass hook
- Acknowledge ("I saw it") without fixing
- Write same problematic code again

**Integration Points:**
- All hooks that can return "block" decision
- Write/Edit tools (where blocks occur)
- Code quality enforcement (check-comments.py, todo-enforcer.sh)


## Architecture

**Trigger:** Hook response with `"decision": "block"`

**Dependencies:**
- Hooks that can block (check-comments.py, todo-enforcer.sh, etc.)
- Write/Edit tools

**Response Flow:**
1. **Hook blocks** → Claude receives block message
2. **STOP** → No more tool calls
3. **ANALYZE** → Understand hook's complaint
4. **FIX** → Refactor/improve code
5. **RETRY** → New Write/Edit attempt
6. **VERIFY** → Must pass hook or escalate to user


## Usage

**Example: check-comments.py (>25% comments):**

**WRONG:**
```
Hook: "Blocked: 75% comments"
Claude: "I see the issue" → Deletes file → Continues
Claude: "Noted" → Writes same code again
```

**RIGHT:**
```
Hook: "Blocked: 75% comments"
Claude:
  1. Analyze: Which comments are redundant?
  2. Refactor: Use self-explanatory names instead
  3. Rewrite: Keep only "why" comments, not "what"
  4. Retry: Write/Edit with improved code
```

**Example: todo-enforcer.sh (open todos):**

**WRONG:**
```
Hook: "Blocked: 3 open todos"
Claude: Marks todos "completed" without doing them
Claude: Tries to bypass hook
```

**RIGHT:**
```
Hook: "Blocked: 3 open todos"
Claude:
  1. Actually complete the todos
  2. OR remove irrelevant todos with justification
  3. THEN proceed with session end
```


## Configuration

| Hook Type | Block Trigger | Required Fix |
|-----------|---------------|--------------|
| check-comments.py | >25% comments | Reduce to self-documenting code |
| todo-enforcer.sh | Open todos at session end | Complete or remove with reason |
| (any hook) | decision: "block" | Address root cause |


## Best Practices

**Do:**
- Stop immediately when hook blocks
- Understand what the hook is enforcing
- Fix the root cause (not just symptoms)
- Retry with improved code
- Escalate to user if hook requirement is impossible

**Don't:**
- Ignore block and continue
- Delete file to bypass
- Acknowledge without fixing
- Work around the hook
- Request user exception without trying to fix first


## Related


---

<small>Source: `.claude/rules/hook-block-response.md`</small>
