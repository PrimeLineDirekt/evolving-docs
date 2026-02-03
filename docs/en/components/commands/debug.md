---
title: /debug
type: command
tags: []
lang: en
confidence: 100
---

# /debug


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Systematic debugging: understand symptoms, form hypotheses, gather evidence, find root cause. |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | analysis |</div>


## What It Does

Methodical debugging workflow: define problem, generate hypotheses, test systematically, document resolution.


## System Impact

- Structured problem-solving approach
- Evidence-based hypothesis testing
- Creates bug resolution docs


## Architecture

6-step process:
1. Intake gate
2. Problem definition
3. Hypothesis generation
4. Evidence gathering
5. Root cause analysis
6. Fix development + documentation


## Usage

Provide error description or symptoms. Guided through systematic debugging.

### Examples

#### Basic Usage

**Code:**
```bash
/debug "API returns 500 on user login"
```

**Result**: Hypotheses tested, root cause found, fix proposed

## Configuration

None required

## Best Practices

- Provide reproducible symptoms
- Include recent changes
- Test one hypothesis at a time
- Document learnings




## Related

- [`/project-analyze`](#project-analyze) - Für Codebase-Überblick
- [`/system-health`](#system-health) - System-Diagnostik
- [`/sparring problem-solving`](#sparring-problem-solving) - Für komplexe Probleme


---

<small>Source: `.claude/commands/debug.md`</small>
