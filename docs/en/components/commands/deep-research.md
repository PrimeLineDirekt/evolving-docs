---
title: /deep-research
type: command
tags: []
lang: en
confidence: 100
---

# /deep-research


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Research orchestrator offering two paths: WebSearch or Perplexity Deep Research via Chrome. |
| **Complexity** | high |
| **Model** | opus |
| **Category** | memory |</div>


## What It Does

Multi-source research with two modes: conventional WebSearch or automated Perplexity via Chrome MCP.


## System Impact

- Token-efficient via Perplexity automation
- Deep analysis for complex topics
- Source credibility tracking


## Architecture

- Mode 1: WebSearch + research-orchestrator skill
- Mode 2: Chrome automation → Perplexity Research Mode → extract results


## Usage

Provide research topic. Choose conventional (fast) or Perplexity (deep, 2-5 min).

### Examples

#### Basic Usage

**Code:**
```bash
/deep-research "AI agents market trends 2026"
```

**Result**: Comprehensive research report with sources

## Configuration

Requires Chrome MCP for Perplexity mode

## Best Practices

- Use Perplexity for complex topics
- Enable Research Mode (not Search)
- Allow 2-5 minutes for deep research
- Save results to knowledge base




## Related

- [`/think`](#think) - Für Analyse nach der Recherche
- [`/sparring`](#sparring) - Für Diskussion der Ergebnisse
- [`/knowledge-add`](#knowledge-add) - Ergebnisse in KB speichern


---

<small>Source: `.claude/commands/deep-research.md`</small>
