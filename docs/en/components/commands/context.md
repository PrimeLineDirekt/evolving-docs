---
title: context
type: command
tags: []
lang: en
confidence: 100
---

# context


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




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
User Input: "Kontext für Agent-Erstellung"
Keywords: ["agent", "creation", "erstellen"]
```


#### Example



**Code:**
```markdown
## Relevanter Kontext für: {topic}

### Primary Entities (immer relevant)
- **{node-name}** ({type}) - {description}
  Path: {path}

### Secondary Entities (zusätzlich hilfreich)
- **{node-name}** ({type}) - {description}

### Aktiver Memory-Kontext
Aus: {context_file}
- {key info from memory}

### Verbundene Entities (via Graph)
- {related nodes from edges.json}
```


#### Example



**Code:**
```bash
## Relevanter Kontext für: Agent-Erstellung

### Primary Entities
- **Specialist Agent Template** (template) - Template für specialist agents
  Path: .claude/templates/agents/specialist-agent.md

- **Research Agent Template** (template) - Template für research agents
  Path: .claude/templates/agents/research-agent.md

- **Template Creator** (skill) - Template creation für Agents, Commands, etc.
  Path: .claude/skills/template-creator/

### Secondary Entities
- **Progressive Disclosure Pattern** (pattern) - reference.md + examples.md
- **Intake Gate Pattern** (pattern) - Input validation vor Ausführung
- **12-Factor Agents** (learning) - 12 Prinzipien für Agent Design

### Aktiver Memory-Kontext
Aus: _memory/projects/evolving-system.json
- Aktueller Focus: Domain Memory Implementation
- Features: 8 (6 passing, 1 planned)
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/context.md`</small>
