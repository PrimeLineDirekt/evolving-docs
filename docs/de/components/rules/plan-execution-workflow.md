---
title: plan-execution-workflow
type: rule
tags: []
lang: en
confidence: 100
---

# plan-execution-workflow


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
ExitPlanMode → User wählt Option 2
         │
         ▼
┌─────────────────────────────────┐
│ AUTOMATISCH: Interview starten  │
│                                 │
│ Claude sagt:                    │
│ "Plan genehmigt. Starte jetzt   │
│  Interview zur Finalisierung..." │
│                                 │
│ → /interview-plan {plan-path}   │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ INTERVIEW LÄUFT                 │
│                                 │
│ • Gaps identifizieren           │
│ • Schwachstellen aufzeigen      │
│ • Fragen stellen                │
│ • Plan finalisieren             │
│ • Phase Boundaries prüfen       │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ NACH INTERVIEW                  │
│                                 │
│ Claude fragt:                   │
│ "Interview abgeschlossen.       │
│  Plan finalisiert.              │
│                                 │
│  Execution starten?             │
│  1. Clear Context + Execute     │
│     (empfohlen bei >50% Context)│
│  2. Execute ohne Clear"         │
└──────────────┬──────────────────┘
               │
         User wählt
         /        \
       1.          2.
        │           │
        ▼           ▼
    /clear      Direkt
    + Execute   Execute
```


#### Example



**Code:**
```bash
[ExitPlanMode wird aufgerufen]

Claude: "Plan erstellt. Bereit für Genehmigung.

         1. Nein - Plan überarbeiten
         2. Ja - weitermachen
         3. Nein - abbrechen"

User: "2"

Claude: "Plan genehmigt. Starte jetzt Interview zur Finalisierung..."

[Interview läuft]
Claude: "Frage 1: Der Plan enthält keine expliziten Phase Boundaries.
         Soll ich diese aus der Task-Struktur ableiten?"

User: "Ja, mach das automatisch"

[Weitere Fragen...]

Claude: "Interview abgeschlossen. Plan finalisiert.

         Context-Nutzung: 62%

         Execution starten?
         1. Clear Context + Execute (empfohlen)
         2. Execute ohne Clear"

User: "1"

[Claude führt /clear aus]
[Execution startet mit finalisiertem Plan]
```


#### Example



**Code:**
```bash
Interview-Check für Hints:
         │
         ▼
┌─────────────────────────────────┐
│ Für jeden Task prüfen:          │
│                                 │
│ Hat Hint im Titel?              │
│ ([EXPLORE], [DELEGATE], [DIRECT])│
└──────────────┬──────────────────┘
               │
         Hint fehlt?
         /        \
       JA         NEIN
        │           │
        ▼           ▼
   "Task X.Y       Weiter
    hat keinen
    Hint. Soll
    ich ergänzen?"
        │
        ▼
   Hint hinzufügen
   oder User fragt
```


#### Example



**Code:**
```bash
Claude: "Ich sehe dass folgende Tasks keinen Delegation-Hint haben:
         - Task 2.1: API Endpoint implementieren
         - Task 3.2: Database Schema erstellen

         Soll ich Hints basierend auf dem Task-Typ ergänzen?
         (Empfehlung: [DELEGATE] für beide)"

User: "Ja"

Claude: [Ergänzt Hints im Plan]
```


#### Example



**Code:**
```bash
Claude: "Phase 2 hat keinen Review-Task am Ende.
         Soll ich 'Task 2.Y: Phase 2 Review [DELEGATE:code-reviewer]'
         hinzufügen?"

User: "Ja"

Claude: [Fügt Review-Task hinzu]
```


#### Example



**Code:**
```bash
Phase-Generierung:
1. Tasks gruppieren nach Abhängigkeiten
2. Natürliche Breakpoints identifizieren:
   - Nach Setup/Scaffold
   - Nach Core-Implementation
   - Vor Integration/Testing
3. Review-Agents pro Phase zuweisen:
   - Frühe Phasen: Quick-Check (code-reviewer)
   - Letzte Phase: Volle Analyse (alle relevanten Agents)
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/rules/plan-execution-workflow.md`</small>
