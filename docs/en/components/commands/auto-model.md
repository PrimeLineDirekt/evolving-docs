---
title: auto-model
type: command
tags: []
lang: en
confidence: 100
---

# auto-model


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

Automatische Model-Auswahl basierend auf Task-Komplexität


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```xml
<task_analysis>
  <complexity_indicators>
    Multi-step erforderlich: [ja/nein]
    Domain-Expertise nötig: [keine/etwas/tief]
    Reasoning-Tiefe: [flach/mittel/tief]
    Output-Komplexität: [einfach/strukturiert/umfassend]
    Ambiguität: [klar/mittel/hoch]
  </complexity_indicators>

  <requirements_check>
    □ Code-Generierung
    □ Research/Recherche
    □ Kreative Ideation
    □ Risiko-Bewertung
    □ Multi-Perspektiven
    □ Strategische Planung
  </requirements_check>
</task_analysis>
```


#### Example



**Code:**
```bash
Complexity Score: {X}/10
Empfohlenes Model: {haiku|sonnet|opus}
Confidence: {high|medium|low}

Begründung: {Warum dieses Model}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/auto-model.md`</small>
