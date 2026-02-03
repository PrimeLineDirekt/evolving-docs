---
title: /compose-agent
type: command
tags: []
lang: en
confidence: 100
---

# /compose-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Creates a dynamic agent from the Trait System (480 combinations). |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | workflow |</div>


## What It Does

Composes custom agents by combining expertise (10), personality (8), and approach (6) traits.


## System Impact

- 480 unique agent combinations available
- On-demand agent creation without files
- Customized tone, tools, and execution pattern


## Architecture

Uses trait taxonomy from `knowledge/agents/trait-taxonomy.json`:
- Voice mappings for personality
- Tool allowlists for expertise
- Execution patterns for approach

## Usage

`/compose-agent <expertise> [personality] [approach]`

Defaults: personality=direct, approach=systematic

### Examples

#### Basic







## Configuration



## Best Practices




## Related

- [**Agent Factory**: `.claude/agents/agent-factory.md`](#**agent-factory**:-`.claude/agents/agent-factory.md)
- [**Template**: `.claude/templates/agents/dynamic-agent.md`](#**template**:-`.claude/templates/agents/dynamic-agent.md)
- [**Trait System**: `knowledge/agents/trait-taxonomy.json`](#**trait-system**:-`knowledge/agents/trait-taxonomy.json)
- [**Voice Mappings**: `knowledge/agents/voice-mappings.json`](#**voice-mappings**:-`knowledge/agents/voice-mappings.json)
- [**Disclaimers**: `knowledge/agents/disclaimers.json`](#**disclaimers**:-`knowledge/agents/disclaimers.json)


---

<small>Source: `.claude/commands/compose-agent.md`</small>
