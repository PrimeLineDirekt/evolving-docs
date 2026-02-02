---
title: tool-map
type: command
tags: []
lang: en
confidence: 100
---

# tool-map


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

"Generate visual Tool-Map of the Evolving System"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
# Nur Tool-Map anzeigen
/tool-map

# Tool-Map generieren und Orphans automatisch fixen
/tool-map --fix

# Storage-Locations neu analysieren
/tool-map --refresh

# Als Markdown exportieren für Dokumentation
/tool-map --export md
```


#### Example



**Code:**
```bash
EVOLVING SYSTEM TOOL-MAP (2026-01-15)
=====================================

├── Core System
│   ├── Agents (67) ✅
│   ├── Commands (71) ✅
│   ├── Skills (7) ✅
│   └── Hooks (18) ✅
├── Knowledge Base
│   ├── Patterns (56) ✅
│   ├── Learnings (47) ✅
│   └── Decisions (14) ✅
├── Graph
│   ├── Nodes (520)
│   └── Edges (380)
└── Templates & Blueprints
    ├── Templates (12) ✅
    └── Blueprints (9) ✅

ORPHANS FOUND: 0
INTEGRITY SCORE: 100/100
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/tool-map.md`</small>
