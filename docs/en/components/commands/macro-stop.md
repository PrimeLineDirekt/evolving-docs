---
title: /macro-stop
type: command
tags: []
lang: en
confidence: 100
---

# /macro-stop


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Stops complete macro analysis dashboard (backend + frontend) cleanly |
| **Complexity** | low |
| **Model** | claude-sonnet-4-5 |
| **Category** | general |</div>


## What It Does

Cleanly stops the macro analysis dashboard. Shuts down backend services and closes frontend, ensuring proper cleanup and data persistence.


## System Impact

- Terminates backend services
- Closes frontend interfaces
- Saves any pending data
- Frees system resources


## Architecture

Uses Sonnet for clean shutdown orchestration. Implements graceful termination with timeout handling.


## Usage

Run without arguments to stop full dashboard stack.

### Examples

#### Basic Usage



**Code:**
```bash
/macro-stop
```




## Configuration

Uses Sonnet model. Shutdown timeout and cleanup behavior are configurable.

## Best Practices

- Save work before stopping
- Wait for clean shutdown confirmation
- Check logs if shutdown hangs
- Don't force quit unless necessary
- Verify services actually stopped
- Use before system maintenance

## Related

- `/macro-start` - Start dashboard
- Service management patterns


---

<small>Source: `.claude/commands/macro-stop.md`</small>
