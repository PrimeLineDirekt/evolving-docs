---
title: confidence-scoring-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# confidence-scoring-pattern


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
```json
{
  "id": "assumption-file-exists-20260202",
  "status": "candidate",
  "confidence": 30,
  "observations": []
}
```


#### Example



**Code:**
```bash
confidence = min(90, confidence + 5)
```


#### Example



**Code:**
```bash
confidence = max(0, confidence - 8)
```


#### Example



**Code:**
```bash
                    ┌─────────────────────┐
                    │                     │
                    ▼                     │
candidate (30) ─────────► trial (50+) ────┼──► stable (70+)
     │                        │           │
     │                        │           │
     ▼                        ▼           │
quarantine (<30) ◄────────────────────────┘
     │
     │ /rules-review restore
     ▼
candidate (50)
```


#### Example



**Code:**
```json
{
  "observations": [
    {"ts": "2026-02-02T10:00:00Z", "outcome": "success"},
    {"ts": "2026-02-02T14:30:00Z", "outcome": "failure", "context": "User korrigierte"}
  ]
}
```


#### Example



**Code:**
```bash
# Quarantined Rules anzeigen
/rules-review quarantine

# Rule wiederherstellen (setzt auf candidate mit confidence 50)
/rules-review restore {rule_id}
```


#### Example



**Code:**
```json
{
  "config": {
    "confidence": {
      "initial": 30,
      "trial_threshold": 50,
      "stable_threshold": 70,
      "max_confidence": 90,
      "quarantine_threshold": 30,
      "success_increment": 5,
      "failure_decrement": 8
    }
  }
}
```


#### Example



**Code:**
```bash
1. User korrigiert Claude → Rule "scope-only-one-file" erstellt
   confidence: 30, status: candidate

2. /rules-review promote scope-only-one-file
   confidence: 50, status: trial

3. Rule angewendet, User zufrieden
   confidence: 55, status: trial

4. Nochmal angewendet, erfolgreich
   confidence: 60, status: trial

5. Wieder erfolgreich
   confidence: 65, status: trial

6. Wieder erfolgreich
   confidence: 70, status: stable (auto-promoted!)

7. Später: Failure
   confidence: 62, status: trial (auto-demoted)

8. Mehrere Failures
   confidence: 28, status: quarantine (auto-quarantined!)
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/patterns/confidence-scoring-pattern.md`</small>
