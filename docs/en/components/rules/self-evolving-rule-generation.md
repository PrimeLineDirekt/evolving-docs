---
title: self-evolving-rule-generation
type: rule
tags: []
lang: en
confidence: 100
---

# self-evolving-rule-generation


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
│ 1. ANALYSE                      │
│                                 │
│ • Was wurde korrigiert?         │
│ • Warum war es falsch?          │
│ • Was ist das gewünschte        │
│   Verhalten?                    │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 2. KATEGORISIERUNG              │
│                                 │
│ Correction-Typ bestimmen:       │
│ • assumption (false assumption) │
│ • scope (task scope issue)      │
│ • over_engineering (too complex)│
│ • misunderstanding (wrong goal) │
│ • preference (user preference)  │
│ • automation (proactive action) │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 3. GENERALISIERUNG              │
│                                 │
│ • Abstract Pattern extrahieren  │
│ • Konkrete Beispiele sammeln    │
│ • Anti-Patterns identifizieren  │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 4. RULE GENERATION              │
│                                 │
│ Template laden:                 │
│ knowledge/rules/staging/        │
│ _template.md                    │
│                                 │
│ Felder ausfüllen:               │
│ • title, category, trigger      │
│ • rule, do_examples, dont's     │
│ • context, related              │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 5. STAGING                      │
│                                 │
│ • Rule in staging/ speichern    │
│ • _index.json aktualisieren     │
│ • User informieren              │
└─────────────────────────────────┘
```


#### Example



**Code:**
```markdown
# {Title}

**Category**: {assumption|scope|over_engineering|misunderstanding|preference|automation}
**Trigger**: {When to apply this rule}
**Created**: {YYYY-MM-DD}

## Rule

{Core rule statement - what Claude should do differently}

## Do

{Positive examples - what TO do}

## Don't

{Negative examples - what NOT to do}

## Context

{Additional context, edge cases, exceptions}

## Related

{Links to related rules, patterns, or documentation}
```


#### Example



**Code:**
```bash
knowledge/rules/staging/{category}-{slug}-{YYYYMMDD}.md

Beispiele:
- assumption-file-exists-20260201.md
- scope-only-specific-file-20260201.md
- over_engineering-simple-solution-20260201.md
```


#### Example



**Code:**
```json
{
  "rules": [
    {
      "id": "assumption-file-exists-20260201",
      "title": "Don't assume file exists without checking",
      "category": "assumption",
      "created": "2026-02-01",
      "status": "draft",
      "activation_count": 0,
      "effectiveness": null
    }
  ]
}
```


#### Example



**Code:**
```bash
User: "Die Datei existiert nicht - prüf das vorher!"

Claude analysiert:
  → Category: assumption
  → Pattern: Datei-Existenz vor Read prüfen

Generierte Rule:
  Title: "Verify file existence before reading"
  Rule: "Always use ls or glob to verify file exists before Read"
  Do: "Use ls {path} to check, handle not-found gracefully"
  Don't: "Assume file exists based on memory or context"
```


#### Example



**Code:**
```bash
User: "Ich wollte nur die eine Funktion refactorn, nicht die ganze Datei!"

Claude analysiert:
  → Category: scope
  → Pattern: Scope zu weit interpretiert

Generierte Rule:
  Title: "Respect explicit scope boundaries"
  Rule: "When user says 'refactor function X', only touch function X"
  Do: "Ask if scope unclear, confirm before expanding scope"
  Don't: "Automatically refactor related code without permission"
```


#### Example



**Code:**
```bash
"✅ Rule erstellt: {title}
   Kategorie: {category}
   Gespeichert in: knowledge/rules/staging/{filename}

   Die Rule ist jetzt im Staging-Bereich und wird bei Bedarf
   automatisch aktiviert wenn ähnliche Situationen auftreten."
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/rules/self-evolving-rule-generation.md`</small>
