---
title: /project-analyze
type: command
tags: []
lang: en
confidence: 100
---

# /project-analyze


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Expert codebase analysis with specialized support for n8n workflows. Systematically analyze external projects, persist context, and collaborate with specialized agents |
| **Complexity** | high |
| **Model** | opus |
| **Category** | workflow |</div>


## What It Does

Analysiere externe Codebase mit Context-Management und n8n-Support


## System Impact

Analyzes external codebase, creates project context, delegates to specialized agents (n8n-expert for workflows). Persists findings for future sessions.

## Architecture

Orchestration layer: analyzes structure → detects project type → delegates to specialists → persists context → generates summary.

## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/project-analyze
```




## Configuration



## Best Practices

- Run analysis before making changes to external projects
- Review specialist agent findings before proceeding
- Use persisted context for efficiency in subsequent sessions
- Validate approval gates for safety

## Related

- [Upstream**:](#upstream**:)
- [User Input → Plain Text Detection → This Command](#user-input-→-plain-text-detection-→-this-command)
- [Downstream**:](#downstream**:)
- [This Command → @codebase-analyzer-agent → @n8n-expert-agent (conditional)](#this-command-→-@codebase-analyzer-agent-→-@n8n-expert-agent-(conditional))
- [Related Commands**:](#related-commands**:)
- [`/project-work {slug}`](#project-work-{slug}) - An Projekt arbeiten (nach Analyse)
- [`/project-list`](#project-list) - Alle analysierten Projekte anzeigen
- [`/n8n-analyze {path}`](#n8n-analyze-{path}) - Nur n8n Workflows analysieren (ohne Codebase)
- [Command Philosophy**: Understand external codebases deeply, persist context for efficiency, orchestrate specialists (n8n-Expert), maintain safety with explicit approval gates. Enable long-term project relationships.](#command-philosophy**:-understand-external-codebases-deeply,-persist-context-for-efficiency,-orchestrate-specialists-(n8n-expert),-maintain-safety-with-explicit-approval-gates.-enable-long-term-project-relationships.)


---

<small>Source: `.claude/commands/project-analyze.md`</small>
