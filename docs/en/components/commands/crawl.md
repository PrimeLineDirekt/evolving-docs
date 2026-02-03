---
title: /crawl
type: command
tags: []
lang: en
confidence: 100
---

# /crawl


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Unified web crawling interface (Firecrawl MCP + Crawlee fallback). |
| **Complexity** | high |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Intelligently routes between Firecrawl (MCP) and Crawlee (Python) based on URL count and limits.


## System Impact

- Dynamic threshold based on remaining credits
- Tracks usage in project memory
- Auto-resets daily




## Architecture

Decision flow:
- URLs ≤ threshold + limits OK → Firecrawl
- URLs > threshold OR limits reached → Crawlee
- Special features (screenshot, PDF) → Firecrawl only


## Usage

Auto-mode by default. Explicit mode via `--mode=firecrawl|crawlee`.


### Examples

#### Usage



**Code:**
```

### Basic Crawl (Auto-routing)

```


#### Examples



**Code:**
```

### 1. Quick Single Page

```




## Configuration

Threshold tracked in `_memory/projects/evolving-system.json`

## Best Practices

- Use --dry-run to check routing
- Prefer Firecrawl for speed/features
- Use Crawlee for bulk operations




## Related

- [**Firecrawl Tools**: `mcp__firecrawl__*` MCP tools](#**firecrawl-tools**:-`mcp__firecrawl__*`-mcp-tools)
- [**Crawlee Script**: `scripts/crawlers/crawlee_template.py`](#**crawlee-script**:-`scripts/crawlers/crawlee_template.py)
- [**Memory Schema**: `_memory/projects/evolving-system.json`](#**memory-schema**:-`_memory/projects/evolving-system.json)
- [**Context Router**: `_graph/cache/context-router.json` (keywords: crawl, scrape, web)](#**context-router**:-`_graph/cache/context-router.json`-(keywords:-crawl,-scrape,-web))


---

<small>Source: `.claude/commands/crawl.md`</small>
