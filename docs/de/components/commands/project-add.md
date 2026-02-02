---
title: project-add
type: command
tags: []
lang: en
confidence: 100
---

# project-add


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

Dokumentiere ein Projekt in der Knowledge Base

### Key Features

- {Feature 1}
- {Feature 2}
- {Feature 3}

## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Welches Projekt möchtest du dokumentieren?

Optionen:
[1] README importieren - Gib Pfad zu einer bestehenden README an
[2] Neues Projekt - Ich führe dich durch die Dokumentation
[3] Bestehendes updaten - Update ein bereits dokumentiertes Projekt
```


#### Example



**Code:**
```markdown
---
project_name: "{Name}"
status: {in_development|live|paused|completed}
started: {datum oder YYYY-MM}
completed: {datum oder leer}
tags: [{tag1, tag2, tag3}]
tech_stack: [{tech1, tech2, tech3}]
skills_used: [{skill1, skill2}]
skills_developed: [{skill1, skill2}]
related_ideas: [{idea-ids}]
monetization: {yes|no|planned}
---

# {Projekt-Name}

## Übersicht
{Kurzbeschreibung + Zweck}

## Features
- {Feature 1}
- {Feature 2}
- {Feature 3}

## Tech-Stack
- **{Kategorie}**: {Tools}
- **{Kategorie}**: {Tools}

## Architektur
{Beschreibung wie es aufgebaut ist - optional Diagramm}

## Use-Cases
{Wie wird es verwendet}

## Learnings

### Was gut funktioniert hat
- {Learning 1}
- {Learning 2}

### Herausforderungen
- {Challenge 1} → {Lösung}
- {Challenge 2} → {Lösung}

### Was ich anders machen würde
- {Improvement 1}
- {Improvement 2}

## Wiederverwendbare Patterns
{Links zu extrahierten Patterns in knowledge/}

## Skills entwickelt
{Liste mit Beschreibung}

## Nächste Schritte
{Falls in Entwicklung}

## Links
- Repository: {falls vorhanden}
- Live-URL: {falls vorhanden}
- Dokumentation: {falls vorhanden}
```


#### Example



**Code:**
```markdown
---
title: "{Pattern Name}"
type: pattern
category: {technical|process|business}
difficulty: {beginner|intermediate|advanced}
tags: [{tags}]
source_project: {projekt-name}
created: {datum}
---

# {Pattern Name}

## Problem
{Welches Problem löst dieses Pattern}

## Lösung
{Wie funktioniert es}

## Implementation
{Code/Prozess-Beschreibung}

## Wann verwenden
{Use-Cases}

## Beispiel
{Aus dem Quell-Projekt}
```


#### Example



**Code:**
```bash
✓ Projekt dokumentiert: {Name}
  Status: {status}
  Skills entwickelt: {anzahl}
  Patterns extrahiert: {anzahl}

Key Learnings:
- {Learning 1}
- {Learning 2}
- {Learning 3}

Neue Skills:
{Liste neuer Skills}

Wiederverwendbare Patterns:
{Liste der Patterns}

Verbindungen:
{Verwandte Ideen falls vorhanden}

Empfehlungen:
{Basierend auf diesem Projekt könntest du Ideen entwickeln für...}

Nächste Schritte:
- /idea-new - Neue Idee basierend auf diesem Projekt
- /knowledge-search - Verwandte Projekte finden
- /project-add - Weiteres Projekt dokumentieren
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/project-add.md`</small>
