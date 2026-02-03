---
title: /context
type: command
tags: []
lang: en
confidence: 100
---

# /context


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Loads relevant context from Knowledge Graph based on keywords. |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Queries context router with keywords, returns primary/secondary entities and related files.


## System Impact

- Reduces main context load
- On-demand knowledge loading
- Smart node prioritization


## Architecture

Uses `_graph/cache/context-router.json` for keyword→node mapping, loads entity details from `_graph/nodes.json`.


## Usage

Provide keywords to find relevant patterns, templates, rules, and documentation.

### Examples

#### Basic Usage

**Code:**
```bash
/context agent-creation
```

**Output**: Templates, patterns, and related docs for agents

## Configuration

Routes defined in context-router.json

## Best Practices

- Use for unfamiliar domains
- Review primary nodes first
- Load secondary only if needed




## Related


---

<small>Source: `.claude/commands/context.md`</small>
