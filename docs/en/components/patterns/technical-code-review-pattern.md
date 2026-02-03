---
title: technical-code-review-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# technical-code-review-pattern


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
WHEN receiving code review feedback:

1. READ: Complete feedback without reacting
2. UNDERSTAND: Restate requirement in own words (or ask)
3. VERIFY: Check against codebase reality
4. EVALUATE: Technically sound for THIS codebase?
5. RESPOND: Technical acknowledgment or reasoned pushback
6. IMPLEMENT: One item at a time, test each
```


#### Example



**Code:**
```bash
IF any item is unclear:
  STOP - do not implement anything yet
  ASK for clarification on ALL unclear items

WHY: Items may be related. Partial understanding = wrong implementation.
```


#### Example



**Code:**
```bash
Feedback: "Fix items 1-6"
You understand 1,2,3,6. Unclear on 4,5.

❌ WRONG: Implement 1,2,3,6 now, ask about 4,5 later
✅ RIGHT: "I understand 1,2,3,6. Need clarification on 4 and 5."
```


#### Example



**Code:**
```bash
BEFORE implementing:
  1. Technically correct for THIS codebase?
  2. Breaks existing functionality?
  3. Reason for current implementation?
  4. Works on all platforms/versions?
  5. Does reviewer understand full context?

IF suggestion seems wrong:
  Push back with technical reasoning

IF conflicts with prior decisions:
  Stop and discuss first
```


#### Example



**Code:**
```bash
1. grep codebase for actual usage
2. IF unused: "This isn't called. Remove it (YAGNI)?"
3. IF used: Then implement properly
```


#### Example



**Code:**
```bash
✅ "Fixed. [Brief description]"
✅ "Good catch - [issue]. Fixed in [location]."
✅ [Just fix it and show in the code]

❌ "You're absolutely right!"
❌ "Thanks for [anything]"
❌ ANY gratitude expression
```


#### Example



**Code:**
```bash
1. Clarify anything unclear FIRST
2. Then implement:
   - Blocking issues (breaks, security)
   - Simple fixes (typos, imports)
   - Complex fixes (refactoring, logic)
3. Test each fix individually
4. Verify no regressions
```


#### Example



**Code:**
```bash
✅ "You were right - I checked [X]. Implementing now."
✅ "Verified and you're correct. Fixing."

❌ Long apology
❌ Defending why you pushed back
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

<small>Source: `knowledge/patterns/technical-code-review-pattern.md`</small>
