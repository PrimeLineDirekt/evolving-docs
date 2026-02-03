---
title: plan-execution-enforcement
type: rule
tags: []
lang: en
confidence: 100
---

# plan-execution-enforcement


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```markdown
### Task 1.1: Codebase analysieren `[EXPLORE]`
### Task 1.2: Auth-Service implementieren `[DELEGATE]`
### Task 1.3: Type-System designen `[DELEGATE:code-architect]`
### Task 1.4: Typo fixen `[DIRECT]`
### Task 1.5: Phase 1 Review `[DELEGATE:code-reviewer]`
```


#### Example



**Code:**
```bash
Für jeden Task:
         │
         ▼
┌─────────────────────────────────┐
│ 1. HINT EXTRAHIEREN             │
│                                 │
│ Regex: `\[(\w+)(?::[\w-]+)?\]`  │
└──────────────┬──────────────────┘
               │
         Hint gefunden?
         /           \
       JA            NEIN
        │              │
        ▼              ▼
   Hint folgen    Score-Fallback
        │         (siehe unten)
        │
        ▼
┌─────────────────────────────────┐
│ 2. AGENT AUSWÄHLEN              │
│                                 │
│ [EXPLORE] → Explore Agent       │
│ [DELEGATE] → Traits-basiert     │
│ [DELEGATE:X] → Agent X          │
│ [DIRECT] → Selbst               │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 3. TASK TOOL AUFRUFEN           │
│                                 │
│ - subagent_type: Agent          │
│ - model: haiku/sonnet           │
│ - prompt: Task-Beschreibung     │
└─────────────────────────────────┘
```


#### Example



**Code:**
```markdown
### Task 1.5: Phase 1 Review `[DELEGATE:code-reviewer]`
**Scope:** All changes from Phase 1
**Focus:** Code quality, conventions, bugs
**Action:** Fix critical issues (>90% confidence) before Phase 2
```


#### Example



**Code:**
```bash
Parallel starten:
├─ feature-dev:code-reviewer (immer)
├─ pr-review-toolkit:type-design-analyzer (bei neuen Types)
├─ pr-review-toolkit:silent-failure-hunter (bei Error Handling)
├─ pr-review-toolkit:pr-test-analyzer (bei Tests)
└─ pr-review-toolkit:comment-analyzer (bei Docs/Comments)
```


#### Example



**Code:**
```bash
📊 Delegation Summary: 2/5 [DELEGATE] hints not followed

  - [DELEGATE] Implement auth service...
  - [DELEGATE:code-reviewer] Phase 2 Review...

💡 Tip: Use Task tool with appropriate subagent_type for [DELEGATE] tasks
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/rules/plan-execution-enforcement.md`</small>
