---
title: delegation
type: rule
tags: []
lang: en
confidence: 100
---

# delegation


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
Komplexität 1-3  →  HAIKU   (schnell, günstig)
Komplexität 4-6  →  SONNET  (balanced)
Komplexität 7+   →  Nicht delegieren, selbst machen
```


#### Example



**Code:**
```bash
User-Input
    │
    ▼
┌─────────────────────────────────┐
│ 1. SCORE BERECHNEN              │
│    Score ≥ 3? → Delegieren      │
│    Score < 3? → Selbst machen   │
└──────────────┬──────────────────┘
               │ Score ≥ 3
               ▼
┌─────────────────────────────────┐
│ 2. AGENT SELECTION              │
│                                 │
│ Priorität:                      │
│ 1. Built-in (Explore, debugger) │
│ 2. Plugin (feature-dev:*, etc.) │
│ 3. Trait-basiert                │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 3. MODEL SELECTION              │
│                                 │
│ Komplexität → Model (siehe oben)│
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 4. EXECUTE mit Task Tool        │
└─────────────────────────────────┘
```


#### Example



**Code:**
```markdown
## 1. TASK
Atomic, specific goal

## 2. EXPECTED OUTCOME
Konkrete Deliverables

## 3. REQUIRED TOOLS
Explizite Tool-Whitelist

## 4. MUST DO
Exhaustive Requirements

## 5. MUST NOT DO
Verbotene Aktionen

## 6. CONTEXT
File paths, Patterns, Constraints
```


#### Example



**Code:**
```json
{
  "delegation_request": true,
  "reason": "Kurze Begründung warum Delegation sinnvoll",
  "recommended_tasks": [
    {
      "subject": "Task-Beschreibung",
      "model": "haiku|sonnet",
      "agent": "Explore|debugger|general-purpose",
      "traits": ["engineer", "precise"],
      "blockedBy": []
    }
  ]
}
```


#### Example



**Code:**
```bash
Sub-Agent gibt Delegation-Request zurück
                │
                ▼
┌─────────────────────────────────┐
│ 1. REQUEST VALIDIEREN           │
│    • Sinnvolle Tasks?           │
│    • Richtige Models?           │
│    • Dependencies logisch?      │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 2. TASKS ERSTELLEN              │
│    TaskCreate für jeden Task    │
│    TaskUpdate für blockedBy     │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 3. PARALLEL AUSFÜHREN           │
│    Nicht-blockierte Tasks       │
│    gleichzeitig starten         │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 4. ERGEBNISSE ZUSAMMENFÜHREN    │
│    Alle Task-Ergebnisse         │
│    zu einem Result              │
└─────────────────────────────────┘
```


#### Example



**Code:**
```json
{
  "delegation_request": true,
  "reason": "Refactoring betrifft 3 unabhängige Module",
  "recommended_tasks": [
    {
      "subject": "Auth-Modul refactoren",
      "model": "sonnet",
      "agent": "general-purpose",
      "traits": ["engineer", "precise", "iterative"],
      "blockedBy": []
    },
    {
      "subject": "API-Modul refactoren",
      "model": "sonnet",
      "agent": "general-purpose",
      "traits": ["engineer", "precise", "iterative"],
      "blockedBy": []
    },
    {
      "subject": "Integration Tests anpassen",
      "model": "haiku",
      "agent": "general-purpose",
      "blockedBy": ["Auth-Modul refactoren", "API-Modul refactoren"]
    }
  ]
}
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/rules/delegation.md`</small>
