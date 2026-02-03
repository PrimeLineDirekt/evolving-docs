---
title: explicit-identity-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# explicit-identity-pattern


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

**Capabilities Provided:**
- Structured approach to component creation
- Automated validation and best practices
- Standardized output format
- Integration with system architecture

**When to Use:**
- Creating new system components
- Standardizing component structure
- Ensuring consistency across codebase
- Automating repetitive creation tasks



## Architecture

**Key Components:**

```
# DON'T - race at session boundaries
spawn_agent('analyzer', ['--learn'])  # defaults to "most recent"
```

**Data Flow:**
1. Controller analyzes current state
2. Selects appropriate agent based on context
3. Agent processes and contributes to shared state
4. Iterate until completion criteria met




## Usage


### Examples

#### Example



**Code:**
```bash
FALSCH: Race Condition

Main Agent → Spawn Worker("process latest session")
                    ↓
             Worker starts
                    ↓
    [NEW SESSION STARTS]
                    ↓
             Worker queries "latest"
                    ↓
             Gets WRONG session!
```


#### Example



**Code:**
```bash
RICHTIG: Explicit IDs

Main Agent → Spawn Worker("process session-abc123")
                    ↓
             Worker starts
                    ↓
    [NEW SESSION STARTS - irrelevant]
                    ↓
             Worker uses session-abc123
                    ↓
             Correct result!
```


#### Example



**Code:**
```python
# DON'T - race at session boundaries
spawn_agent('analyzer', ['--learn'])  # defaults to "most recent"
```


#### Example



**Code:**
```python
# DO - explicit identity
spawn_agent('analyzer', [
    '--learn',
    '--session-id', context.session_id
])
```


#### Example



**Code:**
```python
def save_state(session_id: str, data: dict):
    state_file = f"state/{session_id}.json"
    write_json(state_file, {
        'session_id': session_id,
        'data': data,
        'timestamp': now()
    })

def load_state(session_id: str):
    # Explicit ID, no "latest" query
    state_file = f"state/{session_id}.json"
    return read_json(state_file)
```


#### Example



**Code:**
```bash
□ Wird ein Prozess/Agent gestartet?
  → ID explizit durchreichen

□ Gibt es await/async Boundaries?
  → ID vorher speichern, nicht nach await queryen

□ Werden mehrere ID-Typen verwendet?
  → Klar trennen, nicht mischen

□ Wird "latest" oder "current" queryed?
  → Durch explizite ID ersetzen
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

<small>Source: `knowledge/patterns/explicit-identity-pattern.md`</small>
