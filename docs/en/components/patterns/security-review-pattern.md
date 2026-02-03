---
title: security-review-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# security-review-pattern


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
1. Repository-Struktur verstehen
2. Bestehende Security-Patterns identifizieren
3. Framework/Library-spezifische Schutzmechanismen erkennen
4. Coding Standards und Conventions erfassen
```


#### Example



**Code:**
```bash
1. Diff/Changes analysieren (git diff main..HEAD)
2. Gegen bestehende Patterns vergleichen
3. Abweichungen von etablierten Praktiken identifizieren
4. Data Flow tracing für sensitive Daten
```


#### Example



**Code:**
```bash
1. OWASP Top 10 Kategorien prüfen
2. Confidence Score pro Finding (1-10)
3. Nur Findings mit Score ≥ 8 reporten
4. False-Positive Filtering anwenden
```


#### Example



**Code:**
```markdown
## Security Finding: {TITLE}

**Location:** `{file}:{line}`
**Severity:** CRITICAL | HIGH | MEDIUM | LOW
**Category:** {OWASP Category}
**Confidence:** {8-10}/10

### Description
{Was das Problem ist}

### Vulnerable Code
```


#### Example



**Code:**
```bash

### Exploit Scenario
{Wie ein Angreifer das ausnutzen könnte}

### Recommendation
{Wie es gefixt werden sollte}

### Fixed Code
```


#### Example



**Code:**
```bash
1. Git Diff holen
   └─ git diff main..HEAD --name-only
   └─ git diff main..HEAD -- {files}

2. Pro geänderte Datei
   └─ Context verstehen (was macht die Datei?)
   └─ Changes analysieren
   └─ Security-relevante Änderungen identifizieren

3. Pro potentielles Finding
   └─ Confidence Score vergeben
   └─ Gegen Hard Exclusions prüfen
   └─ Falls Score ≥ 8: Dokumentieren

4. Report erstellen
   └─ Findings nach Severity sortieren
   └─ Recommendations hinzufügen
```


#### Example



**Code:**
```bash
User: /security-review feature/user-auth

Claude:
1. Analysiere Branch feature/user-auth vs main
2. Finde 12 geänderte Dateien
3. Identifiziere 3 potentielle Issues
4. Nach False-Positive Filter: 1 Finding

## Security Report: feature/user-auth

### Finding 1: SQL Injection in User Search

**Location:** `src/api/users.py:45`
**Severity:** CRITICAL
**Category:** Injection (A03:2021)
**Confidence:** 9/10

**Description:**
User input wird direkt in SQL Query interpoliert ohne Parameterisierung.

**Vulnerable Code:**
```


#### Example



**Code:**
```bash

**Exploit Scenario:**
Angreifer kann `'; DROP TABLE users; --` als search_term senden.

**Recommendation:**
Parameterisierte Queries verwenden.

**Fixed Code:**
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

<small>Source: `knowledge/patterns/security-review-pattern.md`</small>
