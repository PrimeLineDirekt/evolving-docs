---
title: create-command
type: command
tags: []
lang: en
confidence: 100
---

# create-command


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | commands |</div>


## What It Does

Erstellt neuen Command aus Template


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Wenn Command Dateien erstellt/updatet → Workflow
Wenn Command Daten analysiert/auswertet → Analysis
```


#### Example



**Code:**
```bash
Workflow: .claude/templates/commands/workflow-command.md
Analysis: .claude/templates/commands/analysis-command.md
```


#### Example



**Code:**
```markdown
### /{COMMAND_NAME}

**Trigger-Keywords**:
- {KEYWORD_1}
- {KEYWORD_2}
- {KEYWORD_3}

**Pattern-Beispiele**:
```


#### Example



**Code:**
```bash

**Anti-Patterns**:
```


#### Example



**Code:**
```bash

**Confirmation Template**:
"Ich erkenne dass du {intent}. Soll ich `/{COMMAND_NAME}` nutzen?"
```


#### Example



**Code:**
```bash
✓ Command erfolgreich erstellt!

Datei: .claude/commands/{name}.md
Typ: {Workflow|Analysis} Command
Purpose: {BRIEF_DESCRIPTION}

{Falls Pattern hinzugefügt}
Auto-Detection Pattern hinzugefügt zu workflow-patterns.md
Trigger-Keywords: {LIST}

Nächste Schritte:
→ Teste mit: /{name} {example-argument}
→ {SPECIFIC_NEXT_STEP_1}
→ {SPECIFIC_NEXT_STEP_2}

Related: {RELATED_COMMANDS}
```


#### Example



**Code:**
```bash
✓ Command erfolgreich erstellt!

Datei: .claude/commands/project-init.md
Typ: Workflow Command
Purpose: Initialisiert neue Projekte mit Standardstruktur

Auto-Detection Pattern hinzugefügt zu workflow-patterns.md
Trigger-Keywords: "neues projekt", "projekt erstellen", "initialize project"

Nächste Schritte:
→ Teste mit: /project-init my-new-project
→ Passe Directory-Struktur an falls nötig
→ Erweitere Validation-Logic in Step 1

Related: /project-add (für bestehende Projekte)
```


#### Example



**Code:**
```bash
1. Read template file
2. Replace all placeholders
3. Validate output
4. Write command file
5. (Optional) Read workflow-patterns
6. (Optional) Edit workflow-patterns
7. Confirm to user
```


#### Example



**Code:**
```bash
IF template_not_found:
  Liste verfügbare Templates
  Frage User welcher Template
  Retry mit korrektem Pfad
```


#### Example



**Code:**
```bash
IF command_exists:
  Frage: "Command existiert bereits. Überschreiben? (Y/N)"
  IF no: Frage nach alternativem Namen
  IF yes: Backup erstellen (optional), dann überschreiben
```


#### Example



**Code:**
```bash
IF name_invalid:
  Erkläre Naming-Konventionen
  Gib Beispiele
  Frage nach korrektem Namen
```


#### Example



**Code:**
```bash
IF pattern_update_fails:
  Warne User
  Command wurde trotzdem erstellt
  User kann Pattern manuell hinzufügen
  Gib Anleitung
```


#### Example



**Code:**
```bash
User: /create-command project-init

Typ: Workflow
Beschreibung: "Initialisiert neue Projekte mit Standardstruktur"
Argument: "optional: projekt-name"
Input: Projektname, Typ (web/cli/library), Beschreibung
Datenquelle: projects/
Index: projects/index.json

→ Erstellt: .claude/commands/project-init.md
→ Pattern: "neues projekt", "projekt erstellen"
```


#### Example



**Code:**
```bash
User: /create-command idea-stats

Typ: Analysis
Analyse-Typ: Ideas
Datenquellen: ideas/, ideas/index.json
Metriken: Total, By Category, Avg Potential, Status Distribution
Patterns: High-potential ideas, Underutilized skills

→ Erstellt: .claude/commands/idea-stats.md
→ Pattern: "ideen statistik", "analyse ideen"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/create-command.md`</small>
