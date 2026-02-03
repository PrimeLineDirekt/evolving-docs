---
title: /idea-connect
type: command
tags: []
lang: en
confidence: 100
---

# /idea-connect


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Connection engine and innovation catalyst - finds synergies between ideas and discovers new possibilities |
| **Complexity** | high |
| **Model** | opus |
| **Category** | workflow |</div>


## What It Does

Finds connections and synergies between ideas using AI analysis. Identifies complementary concepts, shared patterns, and potential integration opportunities across your idea collection.


## System Impact

- Reads from `_memory/ideas/` directory
- Creates connection maps in knowledge graph
- Updates idea metadata with discovered relationships


## Architecture

Uses Opus model for deep semantic analysis. Employs pattern matching and conceptual bridging to identify non-obvious connections between disparate ideas.


## Usage

Run without arguments to analyze all ideas, or specify idea IDs to focus analysis.

### Examples

#### Basic Usage



**Code:**
```bash
/idea-connect
```




## Configuration

Uses high complexity settings with Opus model for maximum insight depth. No special configuration required.

## Best Practices

- Run periodically as new ideas accumulate
- Review connection suggestions before accepting
- Use to identify promising idea combinations for development
- Helpful when deciding which idea to work on next

## Related

- `/idea-list` - View all ideas
- `/idea-work` - Develop a specific idea
- `/idea-new` - Capture new ideas


---

<small>Source: `.claude/commands/idea-connect.md`</small>
