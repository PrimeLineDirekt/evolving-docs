---
title: scenario-edit
type: command
tags: []
lang: en
confidence: 100
---

# scenario-edit


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

Bearbeitet ein Szenario (Components hinzufügen/entfernen)


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
## Szenario: {display_name}

### Agents ({count})
{Liste aller Agents mit kurzer Beschreibung}

### Commands ({count})
{Liste aller Commands mit kurzer Beschreibung}

### Skills ({count})
{Liste aller Skills}

### Knowledge ({count})
{Liste der Knowledge-Dateien}

### Status
{status} | Tech: {tech_stack kurz}
```


#### Example



**Code:**
```bash
Szenario "{name}" aktualisiert!

## Änderungen
{Liste der vorgenommenen Änderungen}

Nutze /scenario {name} zum Aktivieren.
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/scenario-edit.md`</small>
