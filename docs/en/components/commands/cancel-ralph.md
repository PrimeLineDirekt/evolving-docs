---
title: /cancel-ralph
type: command
tags: []
lang: en
confidence: 100
---

# /cancel-ralph


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Cancels a running Ralph Loop. |
| **Complexity** | low |
| **Model** | claude-sonnet-4-5 |
| **Category** | workflow |</div>


## What It Does

Aborts a running Ralph Loop by deleting its state file.


## System Impact

- Stops automated iteration immediately
- Cleans up loop state
- Prevents further iterations


## Architecture

Removes `/Users/neoforce/Buisiness/Evolving/.claude/ralph-loop.local.md` state file.


## Usage

No arguments needed. Reports iteration count if loop was active.

### Examples

#### Basic Usage

**Code:**
```bash
/cancel-ralph
```

**Output**: "Ralph Loop aborted after 3 iterations."

## Configuration

None required.

## Best Practices

- Use when loop behaves unexpectedly
- Check iteration count before canceling
- Safe to run even if no loop active




## Related


---

<small>Source: `.claude/commands/cancel-ralph.md`</small>
