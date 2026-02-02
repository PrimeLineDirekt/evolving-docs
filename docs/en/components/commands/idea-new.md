---
title: idea-new
type: command
tags: []
lang: en
confidence: 100
---

# idea-new


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

Erfasse eine neue Idee mit KI-Analyse


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```markdown
---
id: {id}
title: "{Titel}"
category: {kategorie}
tags: [{automatisch generierte Tags basierend auf Analyse}]
status: draft
potential: {score}
created: {heutiges Datum}
updated: {heutiges Datum}
required_skills: [{skill1, skill2, ...}]
related_ideas: [{ids verwandter Ideen}]
related_projects: [{namen verwandter Projekte}]
monetization: {direct|indirect|none}
effort: {low|medium|high}
---

# {Titel}

## Beschreibung

{User's Ideen-Beschreibung hier einfügen}

## Analyse

{Deine Analyse mit Potential-Score Begründung}

## Skills

**Vorhanden:**
{Liste mit ✓}

**Zu entwickeln:**
{Liste mit ○}

## Nächste Schritte

- [ ] Idee weiter ausarbeiten
- [ ] Marktforschung durchführen
- [ ] {weitere spezifische Schritte}

## Erkenntnisse

_Wird gefüllt während du an der Idee arbeitest_

## Verbindungen

{Liste verwandter Ideen/Projekte mit kurzer Erklärung warum}
```


#### Example



**Code:**
```bash
✓ Idee erfasst: {Titel}
  ID: {id}
  Kategorie: {kategorie}
  Potential: {score}/10

{Kurze Zusammenfassung der Analyse}

Nächste Schritte:
- /idea-work {id} - An der Idee arbeiten
- /idea-list - Alle Ideen anzeigen
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/idea-new.md`</small>
