---
title: /idea-list
type: command
tags: []
lang: en
confidence: 100
---

# /idea-list


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Idea dashboard manager - provides clear overview of all ideas with filtering and organization |
| **Complexity** | high |
| **Model** | haiku |
| **Category** | memory |</div>


## What It Does

Displays all ideas with filters and organizational views. Shows status, tags, creation dates, and relationships between ideas.


## System Impact

- Reads from `_memory/ideas/*.json`
- Queries knowledge graph for idea relationships
- No write operations - read-only dashboard


## Architecture

Uses Haiku for fast retrieval and formatting. Implements filtering logic and sorting capabilities for large idea collections.


## Usage

Run to see full list, or use filters like status, tags, or date ranges.

### Examples

#### Basic Usage



**Code:**
```bash
/idea-list
```




## Configuration

Uses Haiku model for speed. Configurable display format and filter options.

## Best Practices

- Use filters to focus on active or high-priority ideas
- Review regularly to track idea development progress
- Combine with `/idea-connect` to discover relationships
- Export filtered lists for planning sessions

## Related

- `/idea-new` - Add new ideas
- `/idea-connect` - Find connections
- `/idea-work` - Work on specific idea


---

<small>Source: `.claude/commands/idea-list.md`</small>
