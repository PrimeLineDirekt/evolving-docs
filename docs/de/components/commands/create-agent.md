---
title: create-agent
type: command
tags: []
lang: en
confidence: 100
---

# create-agent


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

Erstellt neuen Agent aus Template


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Specialist: .claude/templates/agents/specialist-agent.md
Research: .claude/templates/agents/research-agent.md
Orchestrator: .claude/templates/agents/orchestrator-agent.md (if exists)
```


#### Example



**Code:**
```bash
✓ {DOMAIN} Agent erfolgreich erstellt!

Datei: .claude/agents/{domain}-agent.md
Typ: {Specialist|Research|Orchestrator} Agent
Domain: {DOMAIN}
Expertise-Bereiche: {LIST_OF_AREAS}
Tools: {LIST_OF_TOOLS}

Nächste Schritte:
→ Aktiviere den Agent mit @{domain}-agent in deinen Prompts
→ Teste mit: "{EXAMPLE_PROMPT}"
→ Passe Expertise-Bereiche an falls nötig in der Agent-Datei

Dokumentation: Siehe .claude/templates/agents/{type}-agent.md für Template-Details
```


#### Example



**Code:**
```bash
1. Read template file
2. Replace all placeholders
3. Validate output
4. Write agent file
5. Confirm to user
```


#### Example



**Code:**
```bash
IF template_not_found:
  Liste verfügbare Templates:
    ls .claude/templates/agents/
  Frage User welcher Template genutzt werden soll
  Retry mit korrektem Pfad
```


#### Example



**Code:**
```bash
IF required_info_missing:
  Frage gezielt nach fehlenden Informationen
  Gib Beispiele zur Orientierung
  Retry Placeholder-Replacement
```


#### Example



**Code:**
```bash
IF domain_too_generic OR domain_invalid:
  Erkläre Problem
  Gib Beispiele für gute Domain-Namen
  Frage nach spezifischerer Domain
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/create-agent.md`</small>
