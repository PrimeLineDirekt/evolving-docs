---
title: /system-audit
type: command
tags: []
lang: en
confidence: 100
---

# /system-audit


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Du bist der System Audit Orchestrator. Führe einen umfassenden Integritäts-Check durch. |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | memory |</div>


## What It Does

System-Integritäts-Audit mit 4 spezialisierten Validatoren


## System Impact

Orchestrates 4 parallel validation agents. Checks detection index, knowledge graph, memory schema, and cross-references. Can auto-fix issues with user approval.

## Architecture

Spawns 4 haiku agents in parallel (detection validator, graph validator, memory validator, stats validator), aggregates scores, generates visual audit report with fix recommendations.




## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/system-audit
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/commands/system-audit.md`</small>
