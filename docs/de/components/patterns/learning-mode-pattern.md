---
title: learning-mode-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# learning-mode-pattern


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
```python
def process_data(items):
    validated = []
    for item in items:
        # TODO(human): Implement validation logic
        # Consider: type checking, range validation, required fields
        pass
    return validated
```


#### Example



**Code:**
```markdown
## Learning Challenge

**Context:**
{Was der Code tut und warum diese Stelle wichtig ist}

**Your Task:**
Implementiere {spezifische Aufgabe} in 2-10 Zeilen.

**Guidance:**
- Bedenke: {Hinweis 1}
- Achte auf: {Hinweis 2}
- Vermeide: {Anti-Pattern}

**Code Location:**
```


#### Example



**Code:**
```bash

**When you're done:**
Teile deinen Code und ich gebe dir Feedback.
```


#### Example



**Code:**
```bash
✗ Mehrere TODOs → User überfordert
✓ Ein fokussierter TODO → Klares Lernziel
```


#### Example



**Code:**
```bash
Erst TODO platzieren, dann auf User warten.
Nicht: Code generieren und dann TODO erwähnen.
```


#### Example



**Code:**
```bash
User implementiert → Claude gibt Feedback:
- Was gut war
- Was verbessert werden könnte
- Alternative Ansätze
- Warum die Lösung funktioniert
```


#### Example



**Code:**
```bash
Zu wenig (1 Zeile) → Trivial, kein Lerneffekt
Zu viel (20+ Zeilen) → Überfordernd
Sweet Spot: 2-10 Zeilen mit klarem Fokus
```


#### Example



**Code:**
```markdown
## Learning Challenge: Input Validation

**Context:**
Wir bauen eine User-Registration. Die Validierung ist kritisch für Security.

**Your Task:**
Implementiere `validate_email()` die prüft ob eine Email gültig ist.

**Guidance:**
- Nutze Regex oder String-Methoden
- Prüfe: @ vorhanden, Domain vorhanden, keine Leerzeichen
- Return: True/False

**Code:**
```


#### Example



**Code:**
```markdown
## Learning Challenge: Error Handling

**Context:**
Die API-Funktion braucht robustes Error Handling.

**Your Task:**
Füge try/except hinzu für den API-Call.

**Guidance:**
- Fange spezifische Exceptions (nicht bare except)
- Logge den Fehler
- Gib sinnvollen Fallback zurück

**Code:**
```


#### Example



**Code:**
```markdown
## Learning Challenge: Debug This

**Context:**
Der folgende Code hat einen Bug. Users berichten dass die Summe falsch ist.

**Your Task:**
Finde und fixe den Bug.

**Guidance:**
- Trace durch mit Beispiel-Input
- Achte auf Edge Cases
- Prüfe Loop-Bedingungen

**Code:**
```


#### Example



**Code:**
```bash

**Hint:** Was passiert mit `i` in einer for-loop?
```


#### Example



**Code:**
```markdown
## Feedback

**Was du gut gemacht hast:**
- {Positives 1}
- {Positives 2}

**Verbesserungsvorschläge:**
- {Suggestion 1}
- {Suggestion 2}

**Warum das funktioniert:**
{Erklärung des Konzepts}

**Alternative Ansätze:**
```


#### Example



**Code:**
```bash

**Weiterführend:**
- {Link oder Konzept zum Vertiefen}
```


#### Example



**Code:**
```markdown
/learn {topic}

Aktiviert Learning Mode für das Thema.
Generiert Challenges statt fertigem Code.
```


#### Example



**Code:**
```bash
User fragt: "Implementiere X für mich"
Claude erkennt: Komplexe Logik, gute Lern-Opportunity

Claude: "Das ist eine gute Gelegenheit zum Lernen!
        Soll ich dir eine Challenge stellen statt
        den Code direkt zu generieren?"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/learning-mode-pattern.md`</small>
