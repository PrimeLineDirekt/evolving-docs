---
title: /generate-image
type: command
tags: []
lang: en
confidence: 100
---

# /generate-image


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Generates images using FAL.ai Nano Banana Pro with ICS Framework. |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | workflow |</div>


## What It Does

AI image generation with intelligent prompt enhancement using ICS Framework (Image type + Content + Style).


## System Impact

- Auto-enhances vague prompts
- Adds photography layer for realistic images
- Handles style recommendations
- Integrates with FAL.ai API




## Architecture




## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/generate-image
```




## Configuration



## Best Practices




## Related

- [Agent: `.claude/agents/fal-image-generator-agent.md`](#agent:-`.claude/agents/fal-image-generator-agent.md)
- [Script: `.claude/scripts/fal_generate.py`](#script:-`.claude/scripts/fal_generate.py)
- [Stats: `python3 .claude/scripts/fal_generate.py --stats`](#stats:-`python3-.claude/scripts/fal_generate.py---stats)


---

<small>Source: `.claude/commands/generate-image.md`</small>
