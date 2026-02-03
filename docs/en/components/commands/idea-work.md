---
title: /idea-work
type: command
tags: []
lang: en
confidence: 100
---

# /idea-work


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Personal sparring partner for idea development - helps systematically develop ideas through structured dialogue |
| **Complexity** | high |
| **Model** | opus |
| **Category** | workflow |</div>


## What It Does

Interactive sparring session for idea development. Challenges assumptions, explores implications, identifies risks, and helps refine concepts through Socratic dialogue.


## System Impact

- Reads idea from `_memory/ideas/`
- Updates idea with development notes
- Creates session transcript in knowledge base
- May spawn new related ideas


## Architecture

Uses Opus for deep thinking and critical analysis. Implements structured progression through idea validation, refinement, and action planning phases.


## Usage

Specify idea ID or description. System engages in interactive session with probing questions and feedback.

### Examples

#### Basic Usage



**Code:**
```bash
/idea-work
```




## Configuration

Uses Opus model for maximum analytical depth. Session duration and focus areas are configurable.

## Best Practices

- Prepare to defend your assumptions
- Welcome critical feedback and challenges
- Take notes during session for later review
- Follow up with action items
- Revisit periodically as idea evolves
- Combine with `/think` for deep analysis

## Related

- `/idea-new` - Capture initial concept
- `/idea-connect` - Find synergies
- `/think` - Deep analytical thinking


---

<small>Source: `.claude/commands/idea-work.md`</small>
