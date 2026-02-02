---
title: scenario-create
type: command
tags: []
lang: en
confidence: 100
---

# scenario-create


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

Erstellt ein neues Szenario mit Agents, Commands und Konfiguration


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
mkdir -p .claude/scenarios/{name}/{commands,agents,skills,knowledge}
```


#### Example



**Code:**
```bash
Szenario "{name}" erstellt!

## Erstellt
- scenario.json
- README.md
- {x} Agents: {liste}
- {x} Commands: {liste}

## Nächste Schritte
1. /scenario {name} - Szenario aktivieren
2. Projekt-Pfad in scenario.json setzen
3. Agents nach Bedarf anpassen
4. Mit Development starten

Soll ich das Szenario jetzt aktivieren?
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/scenario-create.md`</small>
