---
title: /create-skill
type: command
tags: []
lang: en
confidence: 100
---

# /create-skill


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Creates new skill from templates (simple or progressive). |
| **Complexity** | high |
| **Model** | haiku |
| **Category** | memory |</div>


## What It Does

Interactive skill creation wizard. Generates simple (<500 lines) or progressive (multi-file) skills with auto-detection.


## System Impact

- Adds skill to .claude/skills/
- Enables auto-activation on keywords
- Provides domain expertise on-demand


## Architecture

Uses templates from `.claude/templates/skills/`:
- simple-skill/SKILL.md (single file)
- progressive-skill/ (SKILL.md + reference.md + examples.md)


## Usage

Optionally provide skill name, otherwise prompts for configuration.

### Examples

#### Simple Skill

**Code:**
```bash
/create-skill api-rate-limiting
```

**Result**: Single-file skill for rate limiting patterns

## Configuration



## Best Practices



### Tips

!!! tip "Do's**"
    - Wähle richtigen Komplexitäts-Level (Simple vs. Progressive)
    - Include Trigger-Keywords in Description
    - Gib konkrete Beispiele in Fragen
    - Validiere vor dem Schreiben
    - Für Progressive: Achte auf gute Separation (Entry/Details/Examples)
    - Dokumentiere related Skills

!!! tip "Don'ts**"
    - Erstelle keinen Skill ohne User-Bestätigung
    - Überkompliziere nicht (Simple reicht oft)
    - Lasse keine Placeholders im Output
    - Vergiss nicht Directory zu erstellen
    - (Progressive) Erstelle nicht nur 1 oder 2 Files - alle 3 oder Simple wählen


## Related

- [`/create-agent`](#create-agent) - Agent erstellen
- [`/create-command`](#create-command) - Command erstellen
- [`/create-hook`](#create-hook) - Hook erstellen
- [Template-Creator Skill**: Dieser Command kann auch durch den `template-creator` Skill getriggert werden.](#template-creator-skill**:-dieser-command-kann-auch-durch-den-`template-creator`-skill-getriggert-werden.)
- [Wichtig**:](#wichtig**:)
- [Wähle richtige Komplexität (Simple vs. Progressive)](#wähle-richtige-komplexität-(simple-vs.-progressive))
- [Include Trigger-Keywords in Description](#include-trigger-keywords-in-description)
- [Für Progressive: Erstelle ALLE 3 Files](#für-progressive:-erstelle-alle-3-files)
- [Nutze Progressive Disclosure richtig](#nutze-progressive-disclosure-richtig)
- [Dokumentiere Auto-Activation Pattern](#dokumentiere-auto-activation-pattern)


---

<small>Source: `.claude/commands/create-skill.md`</small>
