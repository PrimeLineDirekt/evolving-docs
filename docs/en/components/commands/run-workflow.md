---
title: /run-workflow
type: command
tags: []
lang: en
confidence: 100
---

# /run-workflow


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Führt einen Workflow aus dem `workflows/definitions/` Verzeichnis aus. |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | workflow |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/run-workflow
```




## Configuration



## Best Practices



### Tips

!!! tip ""
    Workflows sind in `workflows/definitions/*.yaml` definiert

!!! tip ""
    Permissions in `workflows/permissions/*.yaml`

!!! tip ""
    Preferences in `workflows/preferences/*.yaml`

!!! tip ""
    Logs werden in `workflows/logs/` gespeichert

!!! tip ""
    Checkpoints in `workflows/checkpoints/` für Resume


## Related


---

<small>Source: `.claude/commands/run-workflow.md`</small>
