---
title: /memory-stats
type: command
tags: []
lang: en
confidence: 100
---

# /memory-stats


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Displays statistics about the experience memory system |
| **Complexity** | low |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Shows comprehensive statistics about experience memory system. Displays counts, decay metrics, trust levels, and usage patterns across all memory types.


## System Impact

- Reads memory files and indices
- Calculates metrics and statistics
- Read-only operations
- No data modifications


## Architecture

Uses Sonnet for efficient metric calculation. Implements decay-aware analysis and temporal trending for memory health assessment.


## Usage

Run without arguments for full stats, or specify memory types for focused reports.

### Examples

#### Basic Usage



**Code:**
```bash
/memory-stats
```




## Configuration

Uses Sonnet model. Stat calculation and display format are configurable.

## Best Practices

- Review regularly to monitor system health
- Track memory growth over time
- Identify low-confidence experiences
- Clean up obsolete memory periodically
- Use before knowledge refresh
- Compare across projects

## Related

- `/learning-review` - Review learning effectiveness
- `/knowledge-refresh` - Update knowledge base
- Memory decay rules


---

<small>Source: `.claude/commands/memory-stats.md`</small>
