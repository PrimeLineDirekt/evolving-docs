---
title: post-todo-review
type: rule
tags: []
lang: en
confidence: 100
---

# post-todo-review


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
Todo-Liste completed (alle Items ✅)
         │
         ▼
┌─────────────────────────────────┐
│ 1. CODE-CHECK                   │
│                                 │
│ Wurden Code-Files geändert?     │
│ (.ts, .tsx, .py, .js, .jsx,     │
│  .go, .rs, .java, .rb, etc.)    │
└──────────────┬──────────────────┘
               │
         Code geändert?
         /           \
       JA            NEIN
        │              │
        ▼              ▼
    Weiter         SKIP Review
                   (nur Docs/Config)
        │
        ▼
┌─────────────────────────────────┐
│ 2. CHANGE-ANALYSE               │
│                                 │
│ Was wurde geändert?             │
│ • Neue Types/Interfaces?        │
│ • Neue Strukturen/Patterns?     │
│ • Error Handling?               │
│ • Tests?                        │
│ • Kommentare?                   │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 3. AGENT-SELECTION              │
│                                 │
│ Base: feature-dev:code-reviewer │
│ + Zusätzliche nach Matrix       │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 4. PARALLEL REVIEW              │
│                                 │
│ Alle ausgewählten Agents        │
│ PARALLEL starten mit Task Tool  │
│ (ein Message-Block)             │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 5. ERGEBNIS-SYNTHESE            │
│                                 │
│ Findings zusammenfassen:        │
│ • Critical Issues (fix now)     │
│ • Warnings (consider fixing)    │
│ • Suggestions (optional)        │
└─────────────────────────────────┘
```


#### Example



**Code:**
```bash
Todo-Liste war:
[x] AuthService Klasse erstellen
[x] Login-Methode implementieren
[x] Session-Handling hinzufügen

→ Review-Agents:
  • feature-dev:code-reviewer (IMMER)
```


#### Example



**Code:**
```bash
Todo-Liste war:
[x] User Interface definieren
[x] AuthResponse Type erstellen
[x] Login-Logik implementieren
[x] Type-Guards hinzufügen

→ Review-Agents:
  • feature-dev:code-reviewer (IMMER)
  • pr-review-toolkit:type-design-analyzer (neue Types)
```


#### Example



**Code:**
```bash
Todo-Liste war:
[x] API-Struktur entwerfen
[x] DTOs definieren
[x] Service-Layer implementieren
[x] Error-Handling hinzufügen
[x] Unit-Tests schreiben
[x] JSDoc-Kommentare ergänzen

→ Review-Agents (PARALLEL):
  • feature-dev:code-reviewer (IMMER)
  • feature-dev:code-architect (neue Strukturen)
  • pr-review-toolkit:type-design-analyzer (DTOs)
  • pr-review-toolkit:silent-failure-hunter (Error Handling)
  • pr-review-toolkit:pr-test-analyzer (Tests)
  • pr-review-toolkit:comment-analyzer (Kommentare)
```


#### Example



**Code:**
```markdown
## Task
Review the code changes from the completed todo list.

## Scope
Files modified in this session (check git diff or recent edits).

## Focus
- Code quality and best practices
- Adherence to project conventions (check CLAUDE.md)
- Potential bugs or logic errors
- Performance considerations

## Output
Confidence-filtered findings (only report issues with confidence > 70%).
```


#### Example



**Code:**
```markdown
## Task
Analyze newly created types/interfaces for design quality.

## Focus
- Encapsulation and invariant expression
- Type safety and proper constraints
- Naming conventions
- Documentation completeness

## Output
Ratings for each type (encapsulation, invariants, usefulness).
```


#### Example



**Code:**
```markdown
## Task
Review new structures and patterns for architectural soundness.

## Focus
- Consistency with existing codebase patterns
- Separation of concerns
- Dependency management
- Scalability considerations

## Output
Architectural assessment with recommendations.
```


#### Example



**Code:**
```markdown
## ⚠️ PENDING REVIEW

Die Todo-Liste wurde abgeschlossen, aber der Code-Review konnte wegen
hohem Context (>85%) nicht durchgeführt werden.

**Nächste Session MUSS starten mit:**
1. `feature-dev:code-reviewer` auf folgende Files:
   - [Liste der geänderten Files]

2. Falls Types erstellt: `pr-review-toolkit:type-design-analyzer`
3. Falls Strukturen erstellt: `feature-dev:code-architect`

**Änderungen die reviewt werden müssen:**
- [Kurze Beschreibung was implementiert wurde]
```


#### Example



**Code:**
```markdown
## Post-Todo Review Complete

### Agents Used
- feature-dev:code-reviewer
- pr-review-toolkit:type-design-analyzer

### Findings

**Critical (0)**
(none)

**Warnings (2)**
1. `src/auth.ts:42` - Missing null check on user object
2. `src/types.ts:15` - UserRole type could be more restrictive

**Suggestions (1)**
1. Consider adding JSDoc to public methods
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/rules/post-todo-review.md`</small>
