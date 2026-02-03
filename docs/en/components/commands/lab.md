---
title: /lab
type: command
tags: []
lang: en
confidence: 100
---

# /lab


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Lab orchestrator - creates complex projects using Perplexity Labs: reports, dashboards, spreadsheets, or code prototypes |
| **Complexity** | high |
| **Model** | opus |
| **Category** | memory |</div>


## What It Does

Orchestrates Perplexity Labs projects via Chrome automation. Creates reports, dashboards, spreadsheets, or code prototypes through guided workflow with asset generation.


## System Impact

- Requires Claude-in-Chrome extension
- Creates project files in designated output directory
- May download generated assets
- Logs project metadata to knowledge base


## Architecture

Uses Opus for complex project orchestration. Implements browser automation for Labs interaction with multi-step workflow management.


## Usage

Describe project type and requirements. System guides through Labs workflow and manages asset creation.

### Examples

#### Basic Usage



**Code:**
```bash
/lab
```




## Configuration

Uses Opus model. Requires Claude-in-Chrome extension and Perplexity Labs access.

## Best Practices

- Define clear project requirements upfront
- Review generated assets before saving
- Organize output in project-specific folders
- Document Labs project parameters
- Iterate on complex projects
- Save intermediate results

## Related

- [`/deep-research`](#deep-research) - Für reine Recherche ohne Assets
- [`/knowledge-add`](#knowledge-add) - Manuell Wissen hinzufügen
- [`/think`](#think) - Für Analyse der Lab-Ergebnisse


---

<small>Source: `.claude/commands/lab.md`</small>
