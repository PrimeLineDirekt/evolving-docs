---
title: intake-gate-pattern
type: pattern
tags: ["[user-interaction", " validation", " askuserquestion", " best-practice]"]
lang: en
confidence: 100
---

# intake-gate-pattern


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns || **Created** | 2025-12-01 |</div>

<div class="component-tags">
<span class="tag tag-[user-interaction">[user-interaction</span>
<span class="tag tag--validation"> validation</span>
<span class="tag tag--askuserquestion"> askuserquestion</span>
<span class="tag tag--best-practice]"> best-practice]</span>
</div>

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

**Key Components:**

```
## Schritt 0: Intake Gate

**Prüfe $ARGUMENTS**:

Falls leer oder vage:
→ Nutze AskUserQuestion mit strukturierten Optionen

Falls ausreichend:
→ Zeige Zusammenfassung, fahre fort
```

**Data Flow:**
1. Controller analyzes current state
2. Selects appropriate agent based on context
3. Agent processes and contributes to shared state
4. Iterate until completion criteria met




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────┐
│  User Input     │
└────────┬────────┘
         ▼
┌─────────────────┐
│  INTAKE GATE    │◄──── Ist Input ausreichend?
│  - Validate     │      - Nein → AskUserQuestion
│  - Clarify      │      - Ja → Proceed
│  - Confirm      │
└────────┬────────┘
         ▼
┌─────────────────┐
│  DECISION GATE  │◄──── User bestätigt
│  - Proceed      │
│  - Ask more     │
│  - Add context  │
└────────┬────────┘
         ▼
┌─────────────────┐
│  EXECUTION      │
└─────────────────┘
```


#### Example



**Code:**
```markdown
## Schritt 0: Intake Gate

**Prüfe $ARGUMENTS**:

Falls leer oder vage:
→ Nutze AskUserQuestion mit strukturierten Optionen

Falls ausreichend:
→ Zeige Zusammenfassung, fahre fort
```


#### Example



**Code:**
```markdown
**Analysiere den Input auf**:
- Komplexität (einfach vs. komplex)
- Scope (klar vs. unklar)
- Abhängigkeiten (standalone vs. vernetzt)
- Risiko (niedrig vs. hoch)

**Bei Unklarheiten, frage nach**:
- Scope: "Was genau soll enthalten sein?"
- Ziel: "Was ist das gewünschte Ergebnis?"
- Kontext: "Gibt es relevante Constraints?"
- Priorität: "Was ist am wichtigsten?"
```


#### Example



**Code:**
```markdown
**Vor Ausführung IMMER bestätigen**:

Ich habe verstanden:
- Task: {zusammenfassung}
- Scope: {scope}
- Output: {expected_output}

Wie möchtest du fortfahren?
1. **Proceed** - Starte Ausführung
2. **Ask more** - Ich habe weitere Fragen
3. **Add context** - Ich möchte mehr Kontext geben
```


#### Example



**Code:**
```json
{
  "questions": [{
    "question": "Um welche Art von Task handelt es sich?",
    "header": "Task Type",
    "options": [
      {"label": "Coding", "description": "Implementierung, Bug Fix, Feature"},
      {"label": "Analysis", "description": "Code Review, Architecture, Research"},
      {"label": "Documentation", "description": "Docs, Comments, READMEs"},
      {"label": "Planning", "description": "Roadmap, Architecture Decision"}
    ],
    "multiSelect": false
  }]
}
```


#### Example



**Code:**
```json
{
  "questions": [{
    "question": "Wie umfangreich soll die Lösung sein?",
    "header": "Scope",
    "options": [
      {"label": "Minimal", "description": "Schnellste Lösung, nur das Nötigste"},
      {"label": "Standard", "description": "Solide Lösung mit Best Practices"},
      {"label": "Comprehensive", "description": "Vollständig mit Edge Cases, Tests"}
    ],
    "multiSelect": false
  }]
}
```


#### Example



**Code:**
```json
{
  "questions": [{
    "question": "Was ist am wichtigsten?",
    "header": "Priority",
    "options": [
      {"label": "Speed", "description": "Schnell fertig, später verbessern"},
      {"label": "Quality", "description": "Sauber und wartbar"},
      {"label": "Learning", "description": "Verstehen wie es funktioniert"}
    ],
    "multiSelect": false
  }]
}
```


#### Example



**Code:**
```bash
User: /create-agent für API

Claude: *erstellt sofort einen generischen API Agent*
        *User wollte aber einen REST API Testing Agent*
        *Rework nötig*
```


#### Example



**Code:**
```bash
User: /create-agent für API

Claude: Ich erstelle einen Agent für API-Arbeit.

        Um den richtigen Agent zu erstellen:

        [AskUserQuestion]
        - API Type: REST / GraphQL / gRPC
        - Purpose: Testing / Integration / Documentation
        - Scope: Single API / Multiple APIs

User: REST, Testing, Single API

Claude: Verstanden! Ich erstelle einen REST API Testing Agent.

        - Name: rest-api-tester-agent
        - Focus: Endpoint Testing, Response Validation
        - Tools: WebFetch, Bash (curl)

        Proceed / Ask more / Add context?

User: Proceed

Claude: *erstellt genau den gewünschten Agent*
```


#### Example



**Code:**
```markdown
## Schritt 0: Intake Gate

**Input**: $ARGUMENTS

**Validation**:
- Falls leer → AskUserQuestion für {relevante Optionen}
- Falls vage → Clarifying Questions
- Falls klar → Zeige Zusammenfassung

**Decision Gate**:
Bestätige vor Ausführung:
- Proceed
- Ask more
- Add context

---
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

<small>Source: `knowledge/patterns/intake-gate-pattern.md`</small>
