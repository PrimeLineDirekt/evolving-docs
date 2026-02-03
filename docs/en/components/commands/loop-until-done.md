---
title: /loop-until-done
type: command
tags: []
lang: en
confidence: 100
---

# /loop-until-done


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Iterates a task until success criteria is met (Ralph Wiggum pattern) |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | workflow |</div>


## What It Does

Executes task iteratively until completion criteria is met. Implements persistent retry loop with progress tracking and automatic failure recovery.


## System Impact

- May run for extended duration
- Logs each iteration attempt
- Updates task status in memory
- Creates completion report


## Architecture

Uses Sonnet for balanced iteration logic. Implements Ralph Wiggum pattern with evidence-based verification and automatic escalation on repeated failures.


## Usage

Define task and success criteria. System will iterate until criteria met or max attempts reached.

### Examples

#### Basic Usage



**Code:**
```bash
/loop-until-done
```




## Configuration

Uses Sonnet model. Max iterations and success criteria are configurable.

## Best Practices

- Define clear, measurable success criteria
- Set reasonable max iteration limit
- Monitor progress during execution
- Cancel if pattern suggests futility
- Review logs after completion
- Use for tasks with verification methods

## Related

- `/debug` - For debugging failed loops
- Failure recovery rules
- Ralph Wiggum pattern documentation


---

<small>Source: `.claude/commands/loop-until-done.md`</small>
