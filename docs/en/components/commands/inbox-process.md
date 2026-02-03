---
title: /inbox-process
type: command
tags: []
lang: en
confidence: 100
---

# /inbox-process


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Inbox processing engine - analyzes, categorizes, and integrates files from `_inbox/` into the knowledge system |
| **Complexity** | high |
| **Model** | haiku |
| **Category** | memory |</div>


## What It Does

Automatically processes files from the `_inbox/` directory. Extracts key information, determines appropriate storage location, updates knowledge graph, and archives processed files.

### Key Features

- Auto-detects file type and content
- Extracts metadata and key concepts
- Categorizes by domain and relevance
- Links to existing knowledge
- Supports documents, code, images, and data files

## System Impact

- Reads from `_inbox/` directory
- Creates entries in knowledge base
- Updates graph with new nodes/edges
- Moves processed files to appropriate locations
- Logs processing history


## Architecture

Uses Haiku for fast processing of multiple files. Implements content analysis pipeline with classification, extraction, and integration stages.




## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/inbox-process
```




## Configuration

Configurable categorization rules and storage paths. Auto-processing can be scheduled or manual.

## Best Practices

- Drop files in `_inbox/` as they arrive
- Run regularly to keep inbox clean
- Review categorization suggestions
- Add custom processing rules for common file types
- Archive important files separately

## Related

- `/knowledge-add` - Manually add knowledge
- `/onboard-process` - Process onboarding data
- `/knowledge-search` - Find processed content


---

<small>Source: `.claude/commands/inbox-process.md`</small>
