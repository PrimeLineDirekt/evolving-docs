---
title: /interview-plan
type: command
tags: []
lang: en
confidence: 100
---

# /interview-plan


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Interviews user about a plan file to validate assumptions, identify gaps, and refine details before implementation |
| **Complexity** | low |
| **Model** | opus |
| **Category** | workflow |</div>


## What It Does

Conducts detailed interview about a plan before implementation. Asks clarifying questions, identifies assumptions, validates feasibility, and ensures all edge cases are considered.


## System Impact

- Reads plan file from specified path
- Creates interview transcript
- Updates plan with clarifications
- May generate refined plan version


## Architecture

Uses Opus for deep analysis and strategic questioning. Implements structured interview protocol covering assumptions, risks, dependencies, and success criteria.


## Usage

Provide path to plan file. System will analyze and conduct interactive interview session.

### Examples

#### Basic Usage



**Code:**
```bash
/interview-plan
```




## Configuration

Uses Opus model for thorough questioning. Interview depth and focus areas are configurable.

## Best Practices

- Run before executing any complex plan
- Answer questions honestly, even if uncertain
- Challenge interviewer's assumptions too
- Document all clarifications
- Update plan file with discoveries
- Use after `/think` for comprehensive planning

## Related

- `/think` - Deep thinking mode
- `/review-plan` - Final plan validation
- `/verify-plan` - Technical verification


---

<small>Source: `.claude/commands/interview-plan.md`</small>
