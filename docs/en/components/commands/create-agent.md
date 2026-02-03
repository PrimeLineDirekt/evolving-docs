---
title: /create-agent
type: command
tags: []
lang: en
confidence: 100
---

# /create-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Du bist mein Agent Creation Assistant. Deine Aufgabe ist es, einen neuen Agent aus Templates zu erstellen. |
| **Complexity** | high |
| **Model** | haiku |
| **Category** | workflow |</div>


## What It Does

Erstellt neuen Agent aus Template


## System Impact




## Architecture




## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/create-agent
```




## Configuration



## Best Practices



### Tips

!!! tip "Do's**"
    - Frage nur nach essentiellen Informationen
    - Generiere sinnvolle Defaults wo möglich
    - Validiere vor dem Schreiben
    - Gib klare Beispiele in Fragen
    - Bestätige mit hilfreichen Next Steps

!!! tip "Don'ts**"
    - Erstelle keinen Agent ohne User-Bestätigung
    - Lasse keine Placeholders im Output
    - Überschreibe nicht ohne zu fragen
    - Verwende keine generischen Namen (agent1, test-agent)
    - Überspringe keine Validation


## Related

- [`/create-command`](#create-command) - Command erstellen
- [`/create-hook`](#create-hook) - Hook erstellen
- [`/create-skill`](#create-skill) - Skill erstellen
- [Template-Creator Skill**: Dieser Command kann auch durch den `template-creator` Skill getriggert werden bei Auto-Detection.](#template-creator-skill**:-dieser-command-kann-auch-durch-den-`template-creator`-skill-getriggert-werden-bei-auto-detection.)
- [Wichtig**:](#wichtig**:)
- [Nutze Read/Write Tools korrekt](#nutze-read/write-tools-korrekt)
- [Erstelle IMMER das agents/ Directory falls es nicht existiert](#erstelle-immer-das-agents/-directory-falls-es-nicht-existiert)
- [Sei präzise bei Placeholder-Replacement](#sei-präzise-bei-placeholder-replacement)
- [Validiere gründlich vor dem Schreiben](#validiere-gründlich-vor-dem-schreiben)


---

<small>Source: `.claude/commands/create-agent.md`</small>
