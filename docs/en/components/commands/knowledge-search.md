---
title: /knowledge-search
type: command
tags: []
lang: en
confidence: 100
---

# /knowledge-search


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Knowledge base search engine - finds relevant knowledge and summarizes it contextually |
| **Complexity** | high |
| **Model** | haiku |
| **Category** | memory |</div>


## What It Does

Semantic search through knowledge base. Finds relevant content based on meaning not just keywords, summarizes results contextually, and suggests related knowledge paths.


## System Impact

- Searches across all `knowledge/` content
- Uses graph relationships for enhanced relevance
- Read-only operations
- Updates search usage metrics


## Architecture

Uses Haiku for fast semantic search. Implements multi-strategy retrieval combining keyword, semantic, and graph-based search for comprehensive results.


## Usage

Describe what you're looking for in natural language. System will find and summarize relevant knowledge.

### Examples

#### Basic Usage



**Code:**
```bash
/knowledge-search
```




## Configuration

Uses Haiku model. Search scope and result count are configurable.

## Best Practices

- Use natural language queries
- Be specific about context
- Review full results not just summaries
- Explore suggested related knowledge
- Combine with graph traversal for deep dives
- Refine queries if results too broad

## Related

- `/knowledge-add` - Add new knowledge
- `/recall` - Memory-specific search
- `/deep-research` - External research


---

<small>Source: `.claude/commands/knowledge-search.md`</small>
