---
title: /create-system
type: command
tags: []
lang: en
confidence: 100
---

# /create-system


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Generates complete multi-agent system with agents, commands, knowledge injection, and CLAUDE.md. |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | memory |</div>


## What It Does

Blueprint-based system generation. Analyzes requirements, matches blueprint, customizes architecture, generates all files.


## System Impact

- Creates standalone project with .claude/ structure
- Configures domain-specific agents
- Sets up memory and knowledge base


## Architecture

5-wave generation:
1. Orchestrator (planning)
2. Builder agents (parallel file creation)
3. Security gate
4. Validation
5. Assembly


## Usage

Provide target path, optionally blueprint. Interactive customization follows.

### Examples

#### Basic Usage

**Code:**
```bash
/create-system ~/projects/tax-advisor
```

**Result**: Complete system with specialized agents

## Configuration

Blueprints in `.claude/blueprints/`

## Best Practices

- Use blueprints for common patterns
- Validate before external path
- Review generated CLAUDE.md




## Related

- [`.claude/blueprints/`](#.claude/blueprints) - Blueprint-Definitionen
- [`.claude/agents/system-*-agent.md`](#.claude/agents/system-*-agent.md) - Builder-Agents
- [`.claude/templates/generated-system/`](#.claude/templates/generated-system) - Generation Templates
- [`knowledge/patterns/system-generation-pattern.md`](#knowledge/patterns/system-generation-pattern.md) - Pattern-Dokumentation


---

<small>Source: `.claude/commands/create-system.md`</small>
