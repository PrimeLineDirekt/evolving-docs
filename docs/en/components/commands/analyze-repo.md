---
title: /analyze-repo
type: command
tags: []
lang: en
confidence: 100
---

# /analyze-repo


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | **Natürliche Sprache funktioniert:** |
| **Complexity** | high |
| **Model** | opus |
| **Category** | memory |</div>


## What It Does

Five-phase repository analysis with relevance extraction and template abstraction. Analyzes external repos for Claude Code components and integrates valuable findings into the Evolving system.

## System Impact

Creates entries in `external/{repo}/`, generates templates, updates knowledge graph and SYSTEM-MAP. Can significantly expand system capabilities by importing proven patterns.

## Architecture

**Phase 1:** Remote relevance check (README + structure)
**Phase 2:** Deep dive (local clone, code extraction)
**Phase 3:** REL extraction (EXT/TPL/SKIP decisions)
**Phase 3.5:** Compatibility check
**Phase 4:** Archive to `_archive/repos/`
**Phase 5:** Full system integration


## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/analyze-repo
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/commands/analyze-repo.md`</small>
