---
title: /doc-gen
type: command
tags: []
lang: en
confidence: 100
---

# /doc-gen


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Generates/updates Auswanderungs-KI product documentation for ReadTheDocs. |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | workflow |</div>


## What It Does

Multi-wave documentation generation using specialized agents (writers, analysts, translators) with security gates.


## System Impact

- Generates complete ReadTheDocs site
- Enforces security constraints (no leaks)
- Incremental updates via state tracking


## Architecture

5-wave process:
- Wave 0: Orchestrator planning
- Wave 1-2: Parallel content generation
- Wave 3: Security gate (blocking)
- Wave 4: Translation (DE→EN)
- Wave 5: Assembly + publish


## Usage

Modes: full (complete rebuild), update (changed sections), section (single), publish (build only).

### Examples

#### Basic Usage

**Code:**
```bash
/doc-gen full
```

**Result**: Complete documentation generated + pushed

## Configuration

Options: --section, --lang, --dry-run, --skip-security

## Best Practices

- Use update mode for incremental changes
- Never skip security gate in production
- Test with --dry-run first
- Review state file after updates




## Related

- [Plan: `~/.claude/plans/misty-enchanting-tiger.md`](#plan:-`~/.claude/plans/misty-enchanting-tiger.md)
- [Docs Repo: `/Users/neoforce/Buisiness/auswanderungs-ki-docs/`](#docs-repo:-`/users/neoforce/buisiness/auswanderungs-ki-docs)


---

<small>Source: `.claude/commands/doc-gen.md`</small>
