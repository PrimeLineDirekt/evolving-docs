---
title: sub-agent-delegation-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# sub-agent-delegation-pattern


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
Keywords: "wichtig", "kritisch", "muss perfekt", "production",
          "security", "auth", "final", "Architektur"
Domains:  security, payment, legal, authentication
```


#### Example



**Code:**
```bash
Keywords: "finde", "suche", "zeig mir", "wie viele", "gibt es",
          "schau mal", "check mal", "analysiere [große Menge]"
Intent:   Information Discovery, Bulk Processing
```


#### Example



**Code:**
```bash
❌ "lass uns", "wir", "sollen wir"
   = Reine Sprachweise, kein Kritikalitäts-Indikator!
```


#### Example



**Code:**
```json
{
  "success": true/false,
  "partial": true/false,
  "completed": ["file1", "file2"],
  "failed": [{"path": "file3", "error": "..."}],
  "result": "Analyse basiert auf 2/3 Quellen..."
}
```


#### Example



**Code:**
```json
{
  "type": "delegation_eval",
  "content": {
    "task_type": "codebase_search",
    "agent": "Explore",
    "mode": "FULL",
    "success": true,
    "user_correction": false,
    "info_loss": false
  }
}
```


#### Example



**Code:**
```bash
User: "Finde alle Stellen mit veralteten Referenzen"

Intent-Analyse:
  Signal: "finde" → EXPLORATIV
  Task: Bulk-Suche
  → FULL DELEGATE zu Explore Agent

Ergebnis:
  - 5 Inkonsistenzen gefunden
  - 0 False Positives
  - ~500 Tokens statt ~5000

Experience: exp-2026-001 (success, effectiveness=100%)
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

<small>Source: `knowledge/patterns/sub-agent-delegation-pattern.md`</small>
