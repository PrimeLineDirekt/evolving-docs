---
title: system-analyzer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# system-analyzer-agent


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

"Analysiert Anforderungen und matcht sie mit passenden Blueprints"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "user_request": "string - User's Beschreibung des gewünschten Systems",
  "target_path": "string - Ziel-Pfad für das System",
  "context": {
    "available_blueprints": ["array of blueprint IDs"],
    "domain_hints": "optional domain keywords"
  }
}
```


#### Example



**Code:**
```bash
1. Tokenize user_request
2. Remove stop words
3. Identify domain-specific terms
4. Map to known domains (steuer, legal, finance, medical, etc.)
```


#### Example



**Code:**
```bash
1. Read .claude/blueprints/index.json
2. For each blueprint:
   - Load blueprint JSON
   - Match keywords gegen detection_patterns
   - Calculate fit_score (0-100)
3. Sort by fit_score descending
```


#### Example



**Code:**
```bash
fit_score = (
  keyword_matches * 10 +
  domain_hint_matches * 20 +
  complexity_match * 15 +
  use_case_match * 25
) / max_possible * 100
```


#### Example



**Code:**
```json
{
  "analysis": {
    "detected_domain": "string",
    "detected_keywords": ["array"],
    "complexity_estimate": "low|medium|high",
    "agent_count_estimate": "number"
  },
  "blueprint_matches": [
    {
      "blueprint_id": "string",
      "blueprint_name": "string",
      "fit_score": "number (0-100)",
      "match_reasons": ["array of reasons"],
      "recommended": "boolean"
    }
  ],
  "customization_needed": {
    "domain": "string - detected or ask user",
    "project_name": "string - suggested name",
    "specialists": ["suggested specialist roles"],
    "questions": ["array of clarification questions if needed"]
  },
  "recommendation": "string - top blueprint with reasoning"
}
```


#### Example



**Code:**
```bash
"Ich brauche ein System für Steuerberatung mit mehreren Experten"
```


#### Example



**Code:**
```json
{
  "analysis": {
    "detected_domain": "steuer",
    "detected_keywords": ["steuer", "beratung", "experten", "system"],
    "complexity_estimate": "high",
    "agent_count_estimate": 4
  },
  "blueprint_matches": [
    {
      "blueprint_id": "multi-agent-advisory",
      "blueprint_name": "Multi-Agent Advisory System",
      "fit_score": 95,
      "match_reasons": [
        "Keyword 'steuer' matched domain_hints.steuer",
        "Keyword 'beratung' matched type advisory",
        "Keyword 'experten' matched multi-agent pattern",
        "Complexity high matches advisory systems"
      ],
      "recommended": true
    }
  ],
  "customization_needed": {
    "domain": "steuer",
    "project_name": "steuer-beratungs-system",
    "specialists": ["steuerberater", "steueranwalt", "software-experte"],
    "questions": []
  },
  "recommendation": "multi-agent-advisory Blueprint empfohlen (95% Match). Das System braucht ca. 4 Agents für umfassende Steuerberatung."
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/system-analyzer-agent.md`</small>
