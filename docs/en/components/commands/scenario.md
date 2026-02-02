---
title: scenario
type: command
tags: []
lang: en
confidence: 100
---

# scenario


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | commands |</div>


## What It Does

Aktiviert ein Szenario und zeigt verfügbare Komponenten


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "active_scenario": "{name}"
}
```


#### Example



**Code:**
```bash
Szenario "{display_name}" aktiviert!

## Projekt
- Name: {project.name}
- Tech Stack: {tech_stack}
- Deployment: {project.deployment.platform}

## Verfügbare Agents
{Für jeden Agent in scenario: Name + kurze Beschreibung aus Agent-Datei}

## Verfügbare Commands
{Für jeden Command in scenario: Name + kurze Beschreibung}

## Quick Start
{Zeige die wichtigsten Commands für dieses Szenario}

Nutze @{agent-name} um einen spezialisierten Agent zu involvieren.
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/scenario.md`</small>
