---
title: system-architect-agent
type: agent
tags: []
lang: en
confidence: 100
---

# system-architect-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2025-12-14 |</div>


## What It Does

"Designt die Architektur des zu generierenden Systems"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "blueprint": "object - Selected blueprint configuration",
  "analysis": "object - Output from system-analyzer-agent",
  "user_customization": {
    "domain": "string",
    "project_name": "string",
    "specialist_count": "number",
    "include_validator": "boolean",
    "include_kb": "boolean"
  },
  "target_path": "string"
}
```


#### Example



**Code:**
```bash
1. Load full blueprint JSON
2. Extract component templates
3. Identify mandatory vs optional components
4. Check model_tiering configuration
```


#### Example



**Code:**
```bash
Für jeden Agent im Blueprint:
1. Ersetze generische Rolle mit Domain-spezifischer
2. Definiere konkrete Expertise-Bereiche
3. Setze Model-Tier basierend auf Kritikalität
4. Dokumentiere Dependencies
```


#### Example



**Code:**
```bash
1. Load knowledge_injection from blueprint
2. Match domain gegen context-router
3. Add domain-specific patterns
4. Plan pattern copying strategy
```


#### Example



**Code:**
```json
{
  "architecture": {
    "name": "string - Project name",
    "domain": "string",
    "pattern": "string - Architecture pattern",
    "description": "string"
  },
  "agents": [
    {
      "id": "string - agent filename (ohne .md)",
      "role": "string - Human-readable role",
      "type": "orchestrator|specialist|reporter",
      "tier": 1|2|3,
      "model": "opus|sonnet|haiku",
      "expertise": ["array of expertise areas"],
      "dependencies": ["array of agent IDs this depends on"],
      "template": "string - Source template path"
    }
  ],
  "commands": [
    {
      "id": "string - command filename (ohne .md)",
      "name": "string - Display name",
      "description": "string",
      "model": "opus|sonnet|haiku",
      "uses_agents": ["array of agent IDs"],
      "template": "string - Source template path"
    }
  ],
  "knowledge_injection": {
    "patterns": [
      {
        "source": "string - Path in Evolving",
        "target": "string - Path in generated system",
        "inject_mode": "copy|reference|summary"
      }
    ],
    "learnings": ["array of learning references"],
    "agent_prompt_references": ["array of reference prompts"]
  },
  "flow_diagram": "string - ASCII art diagram",
  "model_distribution": {
    "opus": "number - count",
    "sonnet": "number - count",
    "haiku": "number - count"
  },
  "estimated_complexity": "low|medium|high"
}
```


#### Example



**Code:**
```json
{
  "architecture": {
    "name": "Steuer-Beratungs-System",
    "domain": "steuer",
    "pattern": "multi-agent-advisory",
    "description": "Experten-Team für umfassende Steuerberatung"
  },
  "agents": [
    {
      "id": "steuer-koordinator-agent",
      "role": "Steuer-Koordinator",
      "type": "orchestrator",
      "tier": 2,
      "model": "sonnet",
      "expertise": ["Team-Koordination", "Anfrage-Routing", "Synthese"],
      "dependencies": [],
      "template": ".claude/templates/agents/orchestrator-agent.md"
    },
    {
      "id": "steuerberater-agent",
      "role": "Steuerberater",
      "type": "specialist",
      "tier": 1,
      "model": "opus",
      "expertise": ["Einkommensteuer", "Werbungskosten", "Sonderausgaben", "Optimierung"],
      "dependencies": ["steuer-koordinator-agent"],
      "template": ".claude/templates/agents/specialist-agent.md"
    },
    {
      "id": "steueranwalt-agent",
      "role": "Steueranwalt",
      "type": "specialist",
      "tier": 1,
      "model": "opus",
      "expertise": ["Steuerrecht", "Risiko-Bewertung", "Rechtssicherheit"],
      "dependencies": ["steuerberater-agent"],
      "template": ".claude/templates/agents/specialist-agent.md"
    },
    {
      "id": "software-experte-agent",
      "role": "Software-Experte",
      "type": "specialist",
      "tier": 2,
      "model": "sonnet",
      "expertise": ["SteuerSparErklärung", "ELSTER", "Software-Bedienung"],
      "dependencies": ["steuer-koordinator-agent"],
      "template": ".claude/templates/agents/specialist-agent.md"
    },
    {
      "id": "steuer-reporter-agent",
      "role": "Report-Generator",
      "type": "reporter",
      "tier": 3,
      "model": "haiku",
      "expertise": ["Zusammenfassung", "Checklisten", "Action Items"],
      "dependencies": ["steuerberater-agent", "steueranwalt-agent"],
      "template": ".claude/templates/agents/specialist-agent.md"
    }
  ],
  "flow_diagram": "
   ┌──────────────────────┐
   │  Steuer-Koordinator  │
   │      (Sonnet)        │
   └──────────┬───────────┘
              │
   ┌──────────┼──────────┐
   │          │          │
   ▼          ▼          ▼
┌─────────┐ ┌─────────┐ ┌─────────────┐
│Steuer-  │ │Steuer-  │ │Software-    │
│berater  │ │anwalt   │ │Experte      │
│(Opus)   │ │(Opus)   │ │(Sonnet)     │
└────┬────┘ └────┬────┘ └─────────────┘
     │           │
     └─────┬─────┘
           │
           ▼
   ┌───────────────┐
   │   Reporter    │
   │   (Haiku)     │
   └───────────────┘
  ",
  "model_distribution": {
    "opus": 2,
    "sonnet": 2,
    "haiku": 1
  }
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/system-architect-agent.md`</small>
