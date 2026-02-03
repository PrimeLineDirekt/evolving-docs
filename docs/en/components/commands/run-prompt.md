---
title: /run-prompt
type: command
tags: []
lang: en
confidence: 100
---

# /run-prompt


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Execute saved prompts from the prompts/ folder. Main advantage: execution in fresh sub-agent context without context bleeding from planning |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | workflow |</div>


## What It Does

Führe gespeicherte Prompts in frischem Sub-Agent Kontext aus


## System Impact

Loads prompt, spawns sub-agent with fresh context, executes in isolation. No context bleeding.

## Architecture

Prompt loader + sub-agent spawner. Ensures clean execution context for specialized tasks.

## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/run-prompt
```




## Configuration



## Best Practices

- Use for complex, self-contained tasks
- Create prompts with Prompt Pro Framework
- Leverage fresh context for better results
- Store reusable prompts in prompts/ directory

## Related

- [`/create-prompt`](#create-prompt) - Prompts erstellen
- [`@prompt-pro-framework`](#@prompt-pro-framework) - Framework Referenz
- [`prompts/`](#prompts) - Prompt Storage


---

<small>Source: `.claude/commands/run-prompt.md`</small>
