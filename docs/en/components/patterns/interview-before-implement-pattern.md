---
title: interview-before-implement-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# interview-before-implement-pattern


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

Pläne werden oft ohne tiefgehende Prüfung implementiert. Wichtige Details, Edge Cases und Tradeoffs werden erst während der Implementierung entdeckt - wenn Änderungen teuer sind.

**Solution**: **Strukturiertes Interview VOR Implementation:**

```
Plan erstellt
    ↓
Interview-Session (Opus)
    ↓
Probing Questions zu:
- Technical Implementation
- UI/UX Details
- Risks & Concerns
- Tradeoffs
- Edge Cases
- Dependencies
    ↓
Plan aktualisiert mit Erkenntnissen
    ↓
Implementation mit klarerem Scope
```



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
---
description: Interview me about the plan
model: opus
---

Read plan file and interview about:
- Technical implementation
- UI & UX
- Concerns & tradeoffs
- Edge cases

Continue until complete, then update plan.
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
Plan erstellt
    ↓
Interview-Session (Opus)
    ↓
Probing Questions zu:
- Technical Implementation
- UI/UX Details
- Risks & Concerns
- Tradeoffs
- Edge Cases
- Dependencies
    ↓
Plan aktualisiert mit Erkenntnissen
    ↓
Implementation mit klarerem Scope
```


#### Example



**Code:**
```markdown
---
description: Interview me about the plan
model: opus
---

Read plan file and interview about:
- Technical implementation
- UI & UX
- Concerns & tradeoffs
- Edge cases

Continue until complete, then update plan.
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

<small>Source: `knowledge/patterns/interview-before-implement-pattern.md`</small>
