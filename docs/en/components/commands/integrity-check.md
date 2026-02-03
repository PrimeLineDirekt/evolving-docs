---
title: /integrity-check
type: command
tags: []
lang: en
confidence: 100
---

# /integrity-check


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Quick integrity validation of the Evolving system without automatic repairs |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Performs quick integrity validation without fixes. Checks graph consistency, file references, memory coherence, and system health metrics. Reports issues without modifying anything.


## System Impact

- Read-only validation of all system components
- Checks `_graph/`, `_memory/`, and `.claude/` structures
- Validates edges, nodes, and references
- No modifications to any files


## Architecture

Uses Sonnet for efficient validation logic. Implements parallel checks across multiple subsystems with comprehensive error reporting.


## Usage

Run without arguments for full check, or specify subsystems to validate specific areas.

### Examples

#### Basic Check







## Configuration

Uses Sonnet model. Validation depth and scope are configurable.

## Best Practices

- Run before major operations
- Check regularly for early issue detection
- Review full report even if summary looks good
- Use with `/tool-map --fix` for repairs
- Add to pre-commit hooks for automation

## Related

- [`/tool-map`](#tool-map) - Full inventory with optional auto-fix
- [`/tool-map --fix`](#tool-map---fix) - Repair found issues
- [`scripts/partition-edges.py`](#scripts/partition-edges.py) - Regenerate edge partitions
- [`scripts/self-heal.py`](#scripts/self-heal.py) - Auto-repair broken edges


---

<small>Source: `.claude/commands/integrity-check.md`</small>
