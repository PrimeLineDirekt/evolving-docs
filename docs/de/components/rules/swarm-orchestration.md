---
title: swarm-orchestration
type: rule
tags: []
lang: en
confidence: 100
---

# swarm-orchestration


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
┌─────────────────────────────────────────────────────────┐
│                    ZEITLICHE TRENNUNG                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  TASKS (Session-Scope)          MEMORY (Projekt-Scope)  │
│  ─────────────────────          ────────────────────── │
│  • Multi-Step Arbeit            • Projekt-State         │
│  • Agent Koordination           • Progress History      │
│  • Aktive Dependencies          • Failures/Learnings    │
│  • Real-time Feedback           • Cross-Session         │
│                                                         │
│           ◄──── HANDOFF ────►                          │
│              (Bridge)                                   │
└─────────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```bash
User-Request
     │
     ▼
 Multi-Step?
 (3+ Schritte)
   /     \
  JA     NEIN
   │       │
   ▼       ▼
TASKS   Direkt
   │    ausführen
   │
   ▼
blockedBy
setzen wo
sinnvoll
```


#### Example



**Code:**
```bash
Task 1: Schema definieren         (kein blockedBy)
Task 2: API Endpoint              (kein blockedBy - parallel zu 1)
Task 3: Frontend Component        (blockedBy: [1, 2])
Task 4: Integration Test          (blockedBy: [3])
```


#### Example



**Code:**
```javascript
// Task erstellen
TaskCreate({ subject: "API Endpoint", ... })  // → Task #2

// Dependency setzen
TaskUpdate({ taskId: "3", addBlockedBy: ["1", "2"] })
```


#### Example



**Code:**
```bash
Layer 1 (Orchestrator)
     │
     │ Task mit komplexem Scope
     ▼
Layer 2 (Sub-Agent)
     │
     │ Analysiert, findet weitere Arbeit
     │
     ▼
┌─────────────────────────────────┐
│ DELEGATION-REQUEST              │
│                                 │
│ "Ich empfehle folgende Tasks:  │
│  1. Task A (Haiku)              │
│  2. Task B (Sonnet)             │
│  3. Task C blockedBy [A, B]"    │
└─────────────────────────────────┘
     │
     │ JSON zurückgeben
     ▼
Layer 1 (Orchestrator)
     │
     │ Prüft, erstellt Tasks
     │ Führt delegierte Arbeit aus
     ▼
Ergebnis
```


#### Example



**Code:**
```json
{
  "delegation_request": true,
  "reason": "Task zu komplex für einzelnen Agent",
  "recommended_tasks": [
    {
      "subject": "Schema validieren",
      "model": "haiku",
      "agent": "Explore",
      "blockedBy": []
    },
    {
      "subject": "Tests schreiben",
      "model": "sonnet",
      "agent": "general-purpose",
      "blockedBy": ["Schema validieren"]
    }
  ]
}
```


#### Example



**Code:**
```bash
1. TaskList abrufen
2. Completed Tasks extrahieren
3. Progress-Entry für Memory generieren:
   {
     "date": "YYYY-MM-DD",
     "action": "Session completed",
     "tasks_done": ["Task 1", "Task 2", ...],
     "result": "Summary",
     "next": "Nächste Schritte"
   }
4. In aktives Projekt-Memory schreiben
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/rules/swarm-orchestration.md`</small>
