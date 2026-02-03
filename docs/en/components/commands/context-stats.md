---
title: /context-stats
type: command
tags: []
lang: en
confidence: 100
---

# /context-stats


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Shows current context window usage with visual progress bar. |
| **Complexity** | medium |
| **Model** | haiku |
| **Category** | workflow |</div>


## What It Does

Displays context window usage as visual bar with recommendations based on usage level.


## System Impact

- Helps prevent degradation at high usage
- Suggests /clear or /whats-next when needed
- Reads from statusline temp files


## Architecture

Reads `/tmp/claude-context-pct-*.txt` for current percentage, renders 30-char bar with status indicators.


## Usage

No arguments. Shows percentage, visual bar, status, and recommendations.

### Examples

#### Basic Usage

**Code:**
```bash
/context-stats
```

**Output**: 38% filled bar, "Healthy" status

## Configuration

Thresholds:
- 0-59%: Healthy
- 60-79%: Warning
- 80-100%: Critical

## Best Practices

- Check before starting complex tasks
- Run /whats-next at 80%+ before /clear
- Monitor during multi-step operations




## Related


---

<small>Source: `.claude/commands/context-stats.md`</small>
