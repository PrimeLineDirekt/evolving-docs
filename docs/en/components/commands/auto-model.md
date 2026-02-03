---
title: /auto-model
type: command
tags: []
lang: en
confidence: 100
---

# /auto-model


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Analysiere die Task-Beschreibung und empfehle das optimale Model. |
| **Complexity** | low |
| **Model** | haiku |
| **Category** | workflow |</div>


## What It Does

Analyzes task description and recommends optimal model (haiku/sonnet/opus) based on complexity scoring (1-10).


## System Impact

- Helps optimize cost/performance tradeoff
- Prevents over-engineering with expensive models
- Guides model selection for delegated tasks


## Architecture

Uses metacognitive analysis to score:
- Multi-step requirements
- Domain expertise depth
- Reasoning complexity
- Output requirements


## Usage

Provide task description as argument or it will prompt for details.

### Examples

#### Basic Usage

**Code:**
```bash
/auto-model "Analyze user feedback and suggest product improvements"
```

**Result**: Sonnet (complexity: 5/10)

## Configuration

Score thresholds:
- 1-3: Haiku
- 4-6: Sonnet
- 7-10: Opus

## Best Practices

- Use for unfamiliar tasks
- Trust high-confidence recommendations
- Consider budget when score is borderline




## Related


---

<small>Source: `.claude/commands/auto-model.md`</small>
