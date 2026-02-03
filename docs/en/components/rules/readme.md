---
title: README
type: rule
tags: []
lang: en
confidence: 100
---

# README


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
.claude/rules/                    # CORE: Auto-load bei Session-Start (~2K Tokens)
├── core-principles.md            # Arbeitsweise
├── workflow-detection.md         # Command-Erkennung
├── domain-memory-bootup.md       # Session-Start
└── README.md                     # Diese Datei

knowledge/rules/                  # ON-DEMAND: Nur via Context Router (~0 Tokens default)
├── debugging/                    # observe-before-editing, evidence-before-claims
├── memory/                       # experience-suggest, memory-decay, auto-learning
├── creation/                     # command-creation, ultrathink
├── context/                      # context-optimization, clear-dont-compact
├── automation/                   # proactive-behavior, autonomy-classifier
├── workflow/                     # auto-archival, session-evaluation
├── sync/                         # cross-reference-sync, knowledge-linking
├── misc/                         # no-reference-only, relevance-extraction
└── scenarios/                    # auswanderungs-ki, evolving-dashboard
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/rules/README.md`</small>
