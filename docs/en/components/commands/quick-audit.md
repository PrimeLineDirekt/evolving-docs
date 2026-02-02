---
title: quick-audit
type: command
tags: []
lang: en
confidence: 100
---

# quick-audit


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | commands |</div>


## What It Does

Schneller Security & Quality Check mit 5 Core-Agents (5-8 Minuten)


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
$ARGUMENTS: path (default: .)

1. Direkt starten (kein Intake-Profiling)
2. Alle 5 Agents PARALLEL
3. Kurzer Summary-Report
```


#### Example



**Code:**
```markdown
# Quick Audit: {project}

**Duration**: {time}
**Health Score**: {score}/100

## Critical Issues ({count})
{list_critical_only}

## High Priority ({count})
{list_high_only}

## Quick Wins
{top_3_quick_wins}

---
Für vollständigen Audit: `/full-audit --deep`
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/quick-audit.md`</small>
