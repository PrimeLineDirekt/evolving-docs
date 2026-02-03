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
| **Purpose** | Execute a workflow from the workflows/definitions/ directory |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | workflow |</div>


## What It Does

Executes predefined workflows with steps, permissions, and checkpoints. Supports resume from checkpoint.

## System Impact

Loads workflow definition, validates permissions, executes steps sequentially. Logs progress, creates checkpoints.

## Architecture

Workflow engine with state management. Supports permissions, preferences, logging, and checkpoints.

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
