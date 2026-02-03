---
title: /recall
type: command
tags: []
lang: en
confidence: 100
---

# /recall


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Search the Experience Memory for relevant experiences |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Queries the Experience Memory system to retrieve relevant past experiences, solutions, and learnings based on keywords or context.

## System Impact

Reads experience memory with decay-aware filtering. Returns confidence-scored matches.

## Architecture




## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/recall
```




## Configuration



## Best Practices

- Use specific keywords for better matches
- Review confidence scores before applying solutions
- Update experiences when circumstances change

## Related


---

<small>Source: `.claude/commands/recall.md`</small>
