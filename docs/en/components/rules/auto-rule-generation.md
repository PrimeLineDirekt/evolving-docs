---
title: auto-rule-generation
type: rule
tags: []
lang: en
confidence: 100
---

# auto-rule-generation


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
User korrigiert Claude
         │
         ▼
┌─────────────────────────────────┐
│ HOOK: correction-detector.py    │
│                                 │
│ Erkennt Correction-Pattern      │
│ → Kategorisiert (assumption,    │
│   scope, over_engineering, etc.)│
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ HOOK: Suggestion anzeigen       │
│                                 │
│ "💡 Das könnte eine Rule sein!  │
│  Kategorie: {category}          │
│  Soll ich eine Rule erstellen?" │
└──────────────┬──────────────────┘
               │
         User bestätigt?
         /           \
       JA            NEIN
        │              │
        ▼              ▼
    Weiter         STOP
                   (keine Rule)
        │
        ▼
┌─────────────────────────────────┐
│ 1. SPAM CHECK                   │
│                                 │
│ • Gleiche Kategorie in staging? │
│   → Letzte 24h? → Skip          │
│ • Schon Rule diese Session?     │
│   → Skip                        │
└──────────────┬──────────────────┘
               │ OK
               ▼
┌─────────────────────────────────┐
│ 2. CONTEXT EXTRACTION           │
│                                 │
│ • Letzte 3-5 Turns lesen        │
│ • original_action identifizieren│
│ • corrected_to identifizieren   │
│ • Kategorie aus Hook übernehmen │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 3. RULE GENERATION              │
│                                 │
│ Template: knowledge/rules/      │
│           staging/_template.md  │
│                                 │
│ Felder ausfüllen:               │
│ • title (prägnant, <50 Zeichen) │
│ • category (aus Hook)           │
│ • pattern (was vermeiden)       │
│ • anti_pattern (was nicht)      │
│ • example (konkretes Beispiel)  │
│                                 │
│ ID: {category}-{slug}-{YYYYMMDD}│
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 4. SPEICHERN                    │
│                                 │
│ Datei: knowledge/rules/staging/ │
│        {id}.md                  │
│                                 │
│ Status: "candidate"             │
│ Confidence: 30 (initial)        │
│                                 │
│ _index.json aktualisieren:      │
│ • rules[] += neue Rule          │
│ • by_status.candidate += 1      │
│ • stats.total_generated += 1    │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 5. INFORM                       │
│                                 │
│ "✓ Rule erstellt: {title}"      │
│ "(Kategorie: {category})"       │
└─────────────────────────────────┘
```


#### Example



**Code:**
```markdown
# {Title}

**Category**: {category}
**Created**: {YYYY-MM-DD}
**Status**: candidate
**Confidence**: 30

## Pattern

{Was Claude tun sollte}

## Anti-Pattern

{Was Claude NICHT tun sollte}

## Example

**Situation**: {Konkrete Situation}
**Wrong**: {Was falsch gemacht wurde}
**Right**: {Was richtig wäre}

## Context

{Zusätzlicher Kontext, wann die Regel gilt}
```


#### Example



**Code:**
```bash
/rules-review list --status=CANDIDATE

# Zeigt alle neuen candidate-Rules mit Metriken:
# - Applied count (Nutzungshäufigkeit)
# - Success rate (Erfolgsquote)
# - Age (Alter seit Erstellung)

# Promotion zu trial:
/rules-review promote {rule_id}
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/rules/auto-rule-generation.md`</small>
