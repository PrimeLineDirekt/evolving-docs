---
title: /knowledge-add
type: command
tags: []
lang: en
confidence: 100
---

# /knowledge-add


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Knowledge base manager - structures, analyzes, and stores knowledge intelligently |
| **Complexity** | high |
| **Model** | haiku |
| **Category** | memory |</div>


## What It Does

Adds knowledge to the knowledge base with intelligent structuring. Extracts key concepts, creates appropriate categorization, links to related knowledge, and updates search indices.


## System Impact

- Creates new files in `knowledge/` directory
- Updates knowledge graph with new nodes and edges
- Refreshes search indices
- May update related documentation


## Architecture

Uses Haiku for efficient processing. Implements content analysis, categorization, and graph integration pipeline.


## Usage

Provide content to add. System will analyze, categorize, and prompt for clarifications if needed.

### Examples

#### Basic Usage



**Code:**
```bash
/knowledge-add
```




## Configuration

Uses Haiku model. Auto-categorization and linking enabled by default.

## Best Practices

- Add knowledge as you learn it
- Provide context about relevance
- Review suggested categorization
- Link to related concepts when prompted
- Use consistent naming conventions
- Tag appropriately for discovery

## Related

- `/knowledge-search` - Find knowledge
- `/knowledge-refresh` - Update existing knowledge
- `/inbox-process` - Auto-process inbox files


---

<small>Source: `.claude/commands/knowledge-add.md`</small>
