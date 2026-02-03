---
title: /inventory-report
type: command
tags: []
lang: en
confidence: 100
---

# /inventory-report


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Generates or updates complete tool inventory for the current project |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Generates comprehensive tool inventory for current project. Scans all components, documents relationships, tracks versions, and produces structured report.


## System Impact

- Scans `.claude/` directory structure
- Reads all commands, agents, skills, hooks
- Updates `_stats.json` with current counts
- Creates or updates inventory report file


## Architecture

Uses Sonnet for efficient scanning and cataloging. Implements recursive directory traversal with metadata extraction and relationship mapping.


## Usage

Run without arguments to generate full inventory for current project.

### Examples

#### Basic Usage



**Code:**
```bash
/inventory-report
```




## Configuration

Uses Sonnet model. Report format and detail level are configurable.

## Best Practices

- Run after adding new components
- Review before major refactoring
- Use for documentation updates
- Compare across projects for consistency
- Include in project health checks

## Related

- `/tool-map` - Interactive system map
- `/integrity-check` - Validate system health
- `/system-audit` - Deep system analysis


---

<small>Source: `.claude/commands/inventory-report.md`</small>
