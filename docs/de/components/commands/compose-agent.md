---
title: compose-agent
type: command
tags: []
lang: en
confidence: 100
---

# compose-agent


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

Execution pattern (systematic, iterative, etc.)


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
/compose-agent <expertise> [personality] [approach]
```


#### Example



**Code:**
```bash
# Vollständig spezifiziert
/compose-agent researcher skeptical systematic
/compose-agent engineer precise iterative
/compose-agent strategist empathetic consultative

# Mit Defaults (personality=direct, approach=systematic)
/compose-agent analyst
/compose-agent creative

# Teilweise spezifiziert
/compose-agent security cautious    # approach=systematic (default)
/compose-agent architect thorough exploratory
```


#### Example



**Code:**
```bash
1. Parse Arguments
   └─ expertise (required)
   └─ personality (default: direct)
   └─ approach (default: systematic)

2. Validate Traits
   └─ Check against valid options
   └─ Return error with suggestions if invalid

3. Load Trait Data
   └─ knowledge/agents/trait-taxonomy.json
   └─ knowledge/agents/voice-mappings.json
   └─ knowledge/agents/disclaimers.json (if needed)

4. Compose Agent
   └─ Fill .claude/templates/agents/dynamic-agent.md
   └─ Apply all placeholders

5. Output Agent Prompt
   └─ Complete markdown agent definition
   └─ Ready for immediate use
```


#### Example



**Code:**
```bash
Fehler: Ungültige Expertise "{input}"

Gültige Optionen:
researcher, architect, engineer, analyst, strategist,
legal, creative, security, communications, medical

Beispiel: /compose-agent researcher skeptical systematic
```


#### Example



**Code:**
```bash
Fehler: Ungültige Personality "{input}"

Gültige Optionen:
precise, creative, cautious, direct, thorough,
contrarian, empathetic, skeptical

Default ist "direct" wenn nicht angegeben.
```


#### Example



**Code:**
```bash
Fehler: Ungültiger Approach "{input}"

Gültige Optionen:
systematic, exploratory, iterative, parallel,
adversarial, consultative

Default ist "systematic" wenn nicht angegeben.
```


#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────────────┐
│  /compose-agent <expertise> [personality] [approach]        │
├─────────────────────────────────────────────────────────────┤
│  EXPERTISE (10)     PERSONALITY (8)     APPROACH (6)        │
│  ─────────────      ──────────────      ────────────        │
│  researcher         precise             systematic          │
│  architect          creative            exploratory         │
│  engineer           cautious            iterative           │
│  analyst            direct (default)    parallel            │
│  strategist         thorough            adversarial         │
│  legal*             contrarian          consultative        │
│  creative           empathetic                              │
│  security*          skeptical                               │
│  communications                                             │
│  medical*                                                   │
│                                                             │
│  * = includes disclaimer                                    │
├─────────────────────────────────────────────────────────────┤
│  480 unique combinations available                          │
└─────────────────────────────────────────────────────────────┘
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/compose-agent.md`</small>
