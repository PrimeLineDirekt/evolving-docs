---
title: self-improving-rules-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# self-improving-rules-pattern


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
```bash
┌─────────────────────────────────────────────────────┐
│                  Code Review / Usage                 │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Pattern erkannt?   │
              │  (3+ Occurrences)   │
              └─────────────────────┘
                    │         │
                   JA        NEIN
                    │         │
                    ▼         └──→ Weiter
         ┌─────────────────────┐
         │   Existiert Rule?   │
         └─────────────────────┘
               │         │
              JA        NEIN
               │         │
               ▼         ▼
    ┌──────────────┐  ┌──────────────┐
    │  Rule Update │  │ Neue Rule    │
    │  (Ergänzen)  │  │  erstellen   │
    └──────────────┘  └──────────────┘
                         │
                         ▼
         ┌─────────────────────────────┐
         │  Rule mit echten Beispielen │
         │  aus dem aktuellen Code     │
         └─────────────────────────────┘
```


#### Example



**Code:**
```bash
"Habe ich das schon 3x gemacht?"
  → JA: Rule erstellen/erweitern
  → NEIN: Weitermachen

"Gab es dazu schon mal Review-Feedback?"
  → JA: Rule erstellen
  → NEIN: Notieren für später
```


#### Example



**Code:**
```markdown
# .claude/rules/example-rule.md

---
paths: src/**/*.ts  # Optional: Scope begrenzen
---

# [Rule Name]

**Trigger**: [Wann gilt diese Rule?]

## Pattern

[Was ist das Pattern?]

## Beispiel (aus Code)

```


#### Example



**Code:**
```bash

## Anti-Pattern

```


#### Example



**Code:**
```bash

## Related

- [Andere Rule](andere-rule.md)
```


#### Example



**Code:**
```bash
Session 1: cn() Utility für Tailwind Classes genutzt
Session 2: cn() wieder genutzt
Session 3: cn() wieder genutzt, neuer Dev fragt "was ist cn()?"
```


#### Example



**Code:**
```markdown
# .claude/rules/tailwind-cn-utility.md

**Trigger**: Bei Tailwind Class-Kombinationen

## Pattern

Nutze `cn()` für conditional Tailwind Classes:

```


#### Example



**Code:**
```bash

## Anti-Pattern

```


#### Example



**Code:**
```markdown
## Ergänzung: cva() für Varianten

Bei Components mit vielen Varianten, nutze `cva()`:

```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/patterns/self-improving-rules-pattern.md`</small>
