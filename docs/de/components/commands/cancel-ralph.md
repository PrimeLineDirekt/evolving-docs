---
title: cancel-ralph
type: command
tags: []
lang: en
confidence: 100
---

# cancel-ralph


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

Aktiven Ralph Loop abbrechen


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
# Prüfen und löschen
if [ -f "/Users/neoforce/Buisiness/Evolving/.claude/ralph-loop.local.md" ]; then
  rm "/Users/neoforce/Buisiness/Evolving/.claude/ralph-loop.local.md"
  echo "Loop abgebrochen"
fi
```


#### Example



**Code:**
```bash
🛑 Ralph Loop abgebrochen nach {N} Iterationen.
```


#### Example



**Code:**
```bash
ℹ️ Kein aktiver Ralph Loop gefunden.
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/cancel-ralph.md`</small>
