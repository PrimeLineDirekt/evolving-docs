---
title: /create-hook
type: command
tags: []
lang: en
confidence: 100
---

# /create-hook


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Du bist mein Hook Creation Assistant. Deine Aufgabe ist es, einen neuen Hook aus Templates zu erstellen. |
| **Complexity** | high |
| **Model** | haiku |
| **Category** | workflow |</div>


## What It Does

Erstellt neuen Hook aus Template


## System Impact




## Architecture




## Usage


### Examples

#### Examples



**Code:**
```

### Post-Tool-Use Beispiel

```




## Configuration



## Best Practices



### Tips

!!! tip "Do's**"
    - IMMER `trap 'exit 0' ERR` einbauen
    - IMMER mit `exit 0` enden
    - Background execution nutzen: `(long_task &)`
    - Logging implementieren
    - Pfad-Patterns validieren
    - Testing-Instructions geben

!!! tip "Don'ts**"
    - NIEMALS ohne exit 0 enden
    - Keine blocking operations ohne &
    - Keine unvalidierten User-Inputs in Bash
    - Keine Hooks ohne chmod +x
    - Keine komplexe Logic ohne Error-Handling


## Related

- [`/create-agent`](#create-agent) - Agent erstellen
- [`/create-command`](#create-command) - Command erstellen
- [`/create-skill`](#create-skill) - Skill erstellen
- [Template-Creator Skill**: Dieser Command kann auch durch den `template-creator` Skill getriggert werden.](#template-creator-skill**:-dieser-command-kann-auch-durch-den-`template-creator`-skill-getriggert-werden.)
- [Wichtig**:](#wichtig**:)
- [Hooks MÜSSEN mit `exit 0` enden](#hooks-müssen-mit-`exit-0`-enden)
- [chmod +x MUSS ausgeführt werden](#chmod-+x-muss-ausgeführt-werden)
- [Background execution für lange Tasks: `(task &)`](#background-execution-für-lange-tasks:-`(task-&))
- [Validiere Bash-Syntax](#validiere-bash-syntax)
- [Teste nach Erstellung](#teste-nach-erstellung)


---

<small>Source: `.claude/commands/create-hook.md`</small>
