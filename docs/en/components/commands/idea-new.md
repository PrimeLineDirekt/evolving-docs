---
title: /idea-new
type: command
tags: []
lang: en
confidence: 100
---

# /idea-new


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Personal idea analyst - captures and intelligently analyzes new ideas with AI assistance |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | memory |</div>


## What It Does

Captures new ideas with AI analysis. Automatically extracts key concepts, suggests tags, identifies potential challenges, and recommends related existing ideas.


## System Impact

- Creates new file in `_memory/ideas/`
- Updates knowledge graph with new node and edges
- Triggers connection analysis with existing ideas


## Architecture

Uses Sonnet for balanced analysis speed and depth. Implements structured idea capture with automatic enrichment and classification.


## Usage

Describe your idea in natural language. The system will guide you through clarifying questions and perform analysis.

### Examples

#### Basic Usage



**Code:**
```bash
/idea-new
```




## Configuration

Uses Sonnet model for analysis. Automatic tagging and categorization enabled by default.

## Best Practices

- Capture ideas immediately when they occur
- Provide context about why the idea matters
- Review AI suggestions but validate before saving
- Link to related ideas when prompted
- Use tags consistently for better filtering

## Related

- `/idea-list` - View all ideas
- `/idea-work` - Develop the idea further
- `/idea-connect` - Find related concepts


---

<small>Source: `.claude/commands/idea-new.md`</small>
