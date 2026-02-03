---
title: Context Monitor
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Context Monitor


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Context Monitor v2 - StatusLine with Context Budget Awareness  Format: 145K 72% | Evolving | Opus | main *3 | ✓ Last → Current Colors: Green (<60%) | Yellow (60-79%) | Red (≥80%) Writes context % to / |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

Context Monitor v2 - StatusLine with Context Budget Awareness  Format: 145K 72% | Evolving | Opus | main *3 | ✓ Last → Current Colors: Green (<60%) | Yellow (60-79%) | Red (≥80%) Writes context % to /tmp for hooks

### Key Features

- Type: general
- Language: bash

## System Impact

Displays real-time status line with context budget awareness. Shows:
- Context usage with color coding (green <60%, yellow 60-79%, red ≥80%)
- Current project/directory
- Active model (Opus/Sonnet/Haiku)
- Git status and change count
- Current focus from ledger

Writes context percentage to `/tmp/claude-context-pct-{session}.txt` for other hooks.

## Architecture

**Hook Type:** StatusLine (continuous)
**Language:** Bash
**Dependencies:** jq for JSON parsing
**Bug Workaround:** Applies 1.2x correction factor for Claude Code's cumulative token reporting

## Usage

### Examples

#### Status format
```
~145K 72% | Evolving | Opus | main *3 | → Current task
```

#### Color coding
- **Green (<60%):** Normal operation
- **Yellow (60-79%):** Context warning threshold
- **Red (≥80%):** Critical - consider handoff

#### Git indicators
- `main ✓` - Clean branch
- `main *3` - 3 changes (staged + unstaged + untracked)

## Configuration

**Context File:** `/tmp/claude-context-pct-{session}.txt`
**Token Calculation:** `(cache_read + cache_creation) × 1.2`
**Default Context Size:** 200K tokens

## Best Practices

**Do:**
- Monitor percentage throughout session
- Act on yellow/red warnings
- Use git indicator to track uncommitted work

**Don't:**
- Ignore red warnings (>80% context)
- Rely on token count alone (use percentage)
- Delete context percentage file (breaks other hooks)




## Related


---

<small>Source: `.claude/hooks/context-monitor.sh`</small>
