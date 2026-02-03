---
title: /whats-next
type: command
tags: []
lang: en
confidence: 100
---

# /whats-next


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Du erstellst ein strukturiertes Handoff-Dokument via spezialisierten Agent. |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | memory |</div>


## What It Does

Session-Handoff erstellen für Kontextwechsel oder Pause


## System Impact

Creates session handoff in `_handoffs/`. Updates memory with progress. Auto-triggers at 85% context. Can run in background with --background flag.

## Architecture

Delegates to specialized whats-next agent with fresh context. Agent reads memory, analyzes plans, writes structured handoff, updates project memory. Returns handoff path to user.




## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/whats-next
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/commands/whats-next.md`</small>
