---
title: Context Warning
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Context Warning


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Context Warning Hook - PreToolUse (v4 - Progressive Escalation) Warnt bei hohem Context % mit progressiver Eskalation  ESKALATIONSSTUFEN: - 70%: Warnung (continue: true) - 85%: Auto-Trigger Agent im B |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

Context Warning Hook - PreToolUse (v4 - Progressive Escalation) Warnt bei hohem Context % mit progressiver Eskalation  ESKALATIONSSTUFEN: - 70%: Warnung (continue: true) - 85%: Auto-Trigger Agent im Background (continue: true) - 88%: FORCE Handoff - muss erst reagieren (continue: false) - 90%: BLOCK - nur Handoff-Tools erlaubt  FEATURES: - Debouncing: warnt nur alle 120 Sekunden (außer ≥85%) - Einmaliger Trigger pro Session (handoff_triggered_file)

### Key Features

- Type: general
- Language: bash

## System Impact

Progressive escalation system preventing context overflow. Four escalation levels:
- **70%:** Warning (continues work)
- **85%:** Auto-triggers whats-next agent in background
- **88%:** Forces handoff before continuing
- **90%:** Blocks heavy tools, only handoff-actions allowed

## Architecture

**Hook Type:** PreToolUse
**Language:** Bash
**Debouncing:** 120 seconds between warnings (bypassed at ≥85%)
**Session Files:** `/tmp/claude-context-{warn,handoff-triggered}-{session}.txt`

## Usage

### Examples

#### 70% Warning
```
⚠️ Context at 70% - Consider handoff with /whats-next
```

#### 85% Auto-trigger
```
⚠️ AUTO-HANDOFF: Context at 85%. Starting whats-next agent in background...
```

#### 88% Force handoff
```
🚨 HANDOFF REQUIRED: Context at 88%. Must start whats-next agent NOW!
```
**Blocks:** All tools until handoff agent completes

#### 90% Critical block
```
🛑 Context at 90% - ONLY handoff-actions allowed!
```
**Allowed Tools:** Read, Write, Bash, Skill, Glob, Grep, TodoWrite, Task
**Blocked:** Edit, heavy operations

## Configuration

**Thresholds:**
- Warning: 70%
- Auto-handoff: 85%
- Force handoff: 88%
- Block: 90%

**Debounce:** 120 seconds (2 minutes) for warnings <85%
**One-shot:** Handoff agent only triggered once per session

## Best Practices

**Do:**
- Act on 70% warnings before they escalate
- Let auto-handoff complete at 85%
- Create handoff immediately at 88%
- Use /clear after handoff at 90%

**Don't:**
- Ignore escalating warnings
- Try to continue heavy work at 90%
- Manually delete trigger files (breaks one-shot protection)
- Force through blocks (defeats safety)




## Related


---

<small>Source: `.claude/hooks/context-warning.sh`</small>
