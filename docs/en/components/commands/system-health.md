---
title: /system-health
type: command
tags: []
lang: en
confidence: 100
---

# /system-health


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Du bist der System Health Analyzer für Evolving. Führe eine umfassende Diagnose der Knowledge Base und Project-Struktur durch. |
| **Complexity** | high |
| **Model** | haiku |
| **Category** | memory |</div>


## What It Does

System-Diagnostik für Knowledge Base


## System Impact

Performs 4-8 diagnostic checks depending on mode (quick/full). Validates master document sync, file structure, frontmatter, cross-references, and more. Offers auto-fix for common issues.

## Architecture

Two modes: Quick (4 checks, <30s) and Full (8 checks, <3min). Samples files for validation, calculates health score 0-100, provides actionable recommendations.




## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/system-health
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/commands/system-health.md`</small>
