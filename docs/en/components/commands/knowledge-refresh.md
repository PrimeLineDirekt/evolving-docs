---
title: /knowledge-refresh
type: command
tags: []
lang: en
confidence: 100
---

# /knowledge-refresh


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Validates and updates existing learnings and patterns for accuracy and relevance |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Validates and refreshes existing knowledge. Checks learnings for accuracy, updates patterns based on new information, removes obsolete content, and ensures consistency across knowledge base.


## System Impact

- Scans `knowledge/` directory for learnings and patterns
- Updates content based on validation
- Archives deprecated knowledge
- Refreshes timestamps and metadata


## Architecture

Uses Sonnet for efficient validation logic. Implements decay-aware filtering and relevance scoring to identify knowledge needing refresh.


## Usage

Run without arguments to check all knowledge, or specify domains to refresh specific areas.

### Examples

#### Basic Usage



**Code:**
```bash
/knowledge-refresh
```




## Configuration

Uses Sonnet model. Refresh frequency and validation rules are configurable.

## Best Practices

- Run monthly for maintenance
- Validate before major projects
- Review suggested changes before applying
- Archive rather than delete obsolete knowledge
- Update related edges in knowledge graph
- Document why knowledge was updated

## Related

- [`update-check.md` Command](#update-check.md`-command) - Neue Features finden
- [`knowledge-refresh-cycle.md` Rule](#knowledge-refresh-cycle.md`-rule) - Refresh-Logik
- [`memory-decay.md` Rule](#memory-decay.md`-rule) - Experience Decay


---

<small>Source: `.claude/commands/knowledge-refresh.md`</small>
