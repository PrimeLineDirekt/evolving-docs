---
title: metacognitive-orchestrator
type: rule
tags: []
lang: en
confidence: 100
---

# metacognitive-orchestrator


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
```bash
I notice [observation]. This might cause [problem] because [reason].
Alternative: [your suggestion].
Should I proceed with your original request, or try the alternative?
```


#### Example



**Code:**
```bash
User-Input
    │
    ▼
┌─────────────────────────────────────┐
│ 1. USER OVERRIDE CHECK              │
│    _graph/cache/task-types.json     │
│    → user_overrides section         │
│    Match? → Force Pattern           │
└──────────────────┬──────────────────┘
                   │ Kein Override
                   ▼
┌─────────────────────────────────────┐
│ 2. KEYWORD EXTRACTION               │
│    Aus User-Input Keywords ziehen   │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ 3. TASK-TYPE MATCHING               │
│    _graph/cache/task-types.json     │
│    → task_types section             │
│    Confidence berechnen             │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ 4. MUTEX CHECK                      │
│    _graph/cache/pattern-mutex.json  │
│    → Konflikt mit aktivem Pattern?  │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ 5. CONTEXT BUDGET CHECK             │
│    _graph/cache/orchestration-config│
│    → Context > 70%? → summary_only  │
│    → Context > 90%? → no_pattern    │
└──────────────────┬──────────────────┘
                   │
                   ▼
         CONFIDENCE LEVEL?
         /       |       \
      HIGH    MEDIUM    LOW
     (≥80)   (50-79)   (<50)
       │        │        │
       ▼        ▼        ▼
    AUTO     FRAGEN    SKIP
    LOAD    "Meinst   Pattern
            du...?"
                   │
                   ▼
┌─────────────────────────────────────┐
│ 6. DELEGATION CHECK                 │
│    _graph/cache/delegation-config   │
│                                     │
│    Task delegierbar?                │
│    → JA: Agent/Traits + Model       │
│    → NEIN: Selbst bearbeiten        │
│                                     │
│    Details: auto-delegation.md      │
└─────────────────────────────────────┘
```


#### Example



**Code:**
```bash
base_confidence = 50

FOR keyword IN user_input:
    IF keyword IN task_type.keywords:
        confidence += 10
    IF keyword IN task_type.anti_keywords:
        confidence -= 15

confidence += task_type.confidence_boost

FINAL = min(100, max(0, confidence))
```


#### Example



**Code:**
```bash
1. Summary laden: .claude/summaries/patterns/{pattern}.json
2. Key Points internalisieren
3. Pattern anwenden (ohne explizite Ankündigung)
4. Bei Unsicherheit: Full MD nachladen
```


#### Example



**Code:**
```bash
User: "Ich möchte das optimieren"

Claude: "Das klingt nach einem kreativen Verbesserungs-Task.
         Soll ich das Reflection Pattern nutzen für iterative
         Selbst-Kritik und Verfeinerung?"

[Ja → Summary laden, anwenden]
[Nein → Normal fortfahren]
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/rules/metacognitive-orchestrator.md`</small>
