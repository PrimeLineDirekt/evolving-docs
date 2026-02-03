---
title: four-bucket-context-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# four-bucket-context-pattern


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
┌─────────────────────────────────────────────────────────────────┐
│                    CONTEXT MANAGEMENT                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐       │
│   │  WRITE  │   │ SELECT  │   │COMPRESS │   │ ISOLATE │       │
│   │         │   │         │   │         │   │         │       │
│   │Authorita│   │ Gezielt │   │Zusammen-│   │Sub-Agent│       │
│   │tive     │   │ einsch- │   │fassen   │   │auslagern│       │
│   │setzen   │   │ leusen  │   │         │   │         │       │
│   └─────────┘   └─────────┘   └─────────┘   └─────────┘       │
│        │             │             │             │             │
│        ▼             ▼             ▼             ▼             │
│   Kritische     Task-       Lange        Spezialisierte       │
│   Constraints   relevanter  Historien    Tasks                │
│                 Kontext                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```markdown
# KRITISCH: Sicherheitsregeln

Diese Regeln dürfen NIEMALS ignoriert werden:
- Keine API-Keys im Code
- Keine SQL-Injections
- Immer Input validieren
```


#### Example



**Code:**
```bash
User: "Erstelle einen neuen Agent"

SELECT:
- .claude/templates/specialist-agent.md
- knowledge/patterns/agent-orchestration-pattern.md
- Ein Beispiel-Agent als Referenz

NICHT laden:
- Alle 17 Agents
- Alle Patterns
- Gesamte Knowledge Base
```


#### Example



**Code:**
```markdown
## Quick Resume (COMPRESS)

> Ledger System implementiert. PreCompact Hook erstellt.
> Nächster Schritt: Four-Bucket Pattern dokumentieren.
```


#### Example



**Code:**
```bash
Haupt-Session:
  "Analysiere dieses Repository"

ISOLATE → research-analyst-agent:
  - Bekommt: Repo-URL, spezifische Fragen
  - Arbeitet: Mit frischem Kontext
  - Liefert: Strukturierte Findings

Haupt-Session:
  Verarbeitet Findings weiter
```


#### Example



**Code:**
```bash
Welche Strategie?
       │
       ▼
┌──────────────────┐
│ Darf NIEMALS     │──YES──▶ WRITE
│ ignoriert werden?│
└────────┬─────────┘
         │ NO
         ▼
┌──────────────────┐
│ Nur für diesen   │──YES──▶ SELECT
│ Task relevant?   │
└────────┬─────────┘
         │ NO
         ▼
┌──────────────────┐
│ Zu lang/         │──YES──▶ COMPRESS
│ historisch?      │
└────────┬─────────┘
         │ NO
         ▼
┌──────────────────┐
│ Spezialisiert/   │──YES──▶ ISOLATE
│ eigenständig?    │
└──────────────────┘
```


#### Example



**Code:**
```bash
1. WRITE: CLAUDE.md + Rules laden (authoritative)
2. SELECT: Domain Memory für aktives Projekt
3. COMPRESS: Ledger Quick Resume lesen
4. (Bei Bedarf) ISOLATE: Spezial-Tasks an Agents
```


#### Example



**Code:**
```bash
1. SELECT: Neuen Task-relevanten Kontext laden
2. COMPRESS: Vorherigen Task kurz zusammenfassen
3. (Optional) WRITE: Neue Constraints definieren
```


#### Example



**Code:**
```bash
1. COMPRESS: Aktuellen Stand zusammenfassen
2. /clear: Frischen Kontext holen
3. WRITE + SELECT: Nur Notwendiges neu laden
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

<small>Source: `knowledge/patterns/four-bucket-context-pattern.md`</small>
