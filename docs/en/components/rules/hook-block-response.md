---
title: hook-block-response
type: rule
tags: []
lang: en
confidence: 100
---

# hook-block-response


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
FALSCH:
- "Ich sehe 75% Kommentare" → File löschen → weiter
- "Notiert" → gleichen Code nochmal

RICHTIG:
- Code analysieren: Welche Kommentare sind überflüssig?
- Refactor: Selbsterklärende Namen statt Kommentare
- Neu schreiben: Nur Kommentare die "warum" erklären, nicht "was"
- Write/Edit mit verbessertem Code
```


#### Example



**Code:**
```bash
FALSCH:
- Todos auf "completed" setzen ohne sie zu erledigen
- Hook umgehen

RICHTIG:
- Offene Todos tatsächlich abarbeiten
- ODER: Todos entfernen wenn nicht mehr relevant (mit Begründung)
- Erst dann Session beenden
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/rules/hook-block-response.md`</small>
