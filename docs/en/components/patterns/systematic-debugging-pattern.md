---
title: systematic-debugging-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# systematic-debugging-pattern


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




## Usage


### Examples

#### Example



**Code:**
```bash
1. READ error messages completely
2. REPRODUCE the issue (get exact steps)
3. CHECK recent changes (git diff, git log)
4. GATHER evidence (logs, stack traces, state)
```


#### Example



**Code:**
```bash
1. FIND similar working code in codebase
2. COMPARE broken vs working
3. IDENTIFY the key differences
4. UNDERSTAND why working code works
```


#### Example



**Code:**
```bash
1. FORM a single, testable hypothesis
2. PREDICT what you'll see if hypothesis is correct
3. TEST with minimal change
4. VERIFY - was prediction correct?
```


#### Example



**Code:**
```bash
1. WRITE failing test that captures the bug
2. MAKE single, focused fix
3. VERIFY test passes
4. CHECK no regressions
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

<small>Source: `knowledge/patterns/systematic-debugging-pattern.md`</small>
