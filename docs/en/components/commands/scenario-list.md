---
title: scenario-list
type: command
tags: []
lang: en
confidence: 100
---

# scenario-list


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

Zeigt alle verfügbaren Szenarien


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
## Verfügbare Szenarien

| Szenario | Beschreibung | Status | Agents | Commands |
|----------|--------------|--------|--------|----------|
| evolving-dashboard | Web Dashboard mit Terminal | active | 5 | 4 |
| ... | ... | ... | ... | ... |

**Aktives Szenario**: {active_scenario oder "Keins"}

## Commands
- /scenario {name} - Szenario aktivieren
- /scenario-create {name} - Neues Szenario erstellen
- /scenario-edit {name} - Szenario bearbeiten
```


#### Example



**Code:**
```bash
Keine Szenarien gefunden.

Erstelle ein neues Szenario mit:
/scenario-create {name}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/scenario-list.md`</small>
