---
title: ralph-wiggum-loop-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# ralph-wiggum-loop-pattern


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────┐
│                  Ralph Loop                          │
│                                                      │
│  /ralph-loop "Task" --completion-promise "DONE"     │
│                         │                            │
│                         ▼                            │
│               ┌─────────────────┐                   │
│               │  Claude Works   │◄──────────────┐   │
│               │   on Task       │               │   │
│               └────────┬────────┘               │   │
│                        │                         │   │
│                        ▼                         │   │
│               ┌─────────────────┐               │   │
│               │  Tries to Exit  │               │   │
│               └────────┬────────┘               │   │
│                        │                         │   │
│                        ▼                         │   │
│               ┌─────────────────┐               │   │
│               │   Stop Hook     │               │   │
│               │   Intercepts    │               │   │
│               └────────┬────────┘               │   │
│                        │                         │   │
│           ┌────────────┴────────────┐           │   │
│           ▼                         ▼           │   │
│   ┌──────────────┐         ┌──────────────┐    │   │
│   │ Promise Found │         │ No Promise   │────┘   │
│   │ (COMPLETE)    │         │ Re-prompt    │        │
│   └──────┬───────┘         └──────────────┘        │
│          │                                          │
│          ▼                                          │
│   ┌──────────────┐                                 │
│   │  Exit Loop   │                                 │
│   │  Task Done   │                                 │
│   └──────────────┘                                 │
└─────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```bash
/ralph-loop "PROMPT" --completion-promise "TEXT" --max-iterations N
```


#### Example



**Code:**
```bash
# 1. Check if loop active
if [ ! -f ".claude/ralph-loop.local.md" ]; then
  exit 0  # No loop, allow exit
fi

# 2. Extract completion promise from state
completion_promise=$(get_frontmatter "completion_promise")

# 3. Check last message for promise
last_message=$(extract_last_assistant_message)
if echo "$last_message" | grep -q "<promise>$completion_promise</promise>"; then
  rm ".claude/ralph-loop.local.md"
  exit 0  # Promise found, allow exit
fi

# 4. Increment iteration, re-prompt
iteration=$((iteration + 1))
if [ $iteration -gt $max_iterations ]; then
  exit 0  # Safety limit reached
fi

# 5. Block exit, return re-prompt
echo '{"decision": "block", "reason": "ORIGINAL_PROMPT"}'
```


#### Example



**Code:**
```bash
/ralph-loop "Build a REST API for todos. Requirements:
- CRUD operations
- Input validation
- Unit tests with >80% coverage
- Documentation

When ALL requirements are met and tests pass,
output <promise>COMPLETE</promise>" \
  --completion-promise "COMPLETE" \
  --max-iterations 50
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/ralph-wiggum-loop-pattern.md`</small>
