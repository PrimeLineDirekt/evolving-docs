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
                   YES        NO
                    │         │
                    ▼         └──→ Weiter
         ┌─────────────────────┐
         │   Existiert Rule?   │
         └─────────────────────┘
               │         │
              YES        NO
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
  → YES: Rule erstellen/erweitern
  → NO: Weitermachen

"Gab es dazu schon mal Review-Feedback?"
  → YES: Rule erstellen
  → NO: Notieren für später
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

<small>Source: `knowledge/patterns/self-improving-rules-pattern.md`</small>
