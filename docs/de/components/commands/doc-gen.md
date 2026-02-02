---
title: doc-gen
type: command
tags: []
lang: en
confidence: 100
---

# doc-gen


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

"--section=X, --lang=X, --dry-run, --skip-security"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Mode: full
    │
    ├─ Wave 0: Orchestrator
    │   └─ Plant Sections, erstellt Assignments
    │
    ├─ Wave 1: Core Content (PARALLEL)
    │   ├─ Feature Writer → features/, use-cases/
    │   ├─ Technical Writer → api/, integration/
    │   ├─ KB Analyst → knowledge-base/
    │   └─ FAQ Agent → faq/
    │
    ├─ Wave 2: Business Content (PARALLEL)
    │   ├─ Whitelabel Writer → whitelabel/
    │   ├─ Legal Agent → legal/
    │   ├─ Competitor Agent → comparison/
    │   └─ Diagram Generator → assets/diagrams/
    │
    ├─ Wave 3: Security Gate (BLOCKING)
    │   └─ Scannt ALLE Inhalte auf Leaks
    │
    ├─ Wave 4: Translation
    │   └─ DE → EN (marktadaptiert)
    │
    └─ Wave 5: Assembly
        └─ MkDocs Build, Link-Check, Publish
```


#### Example



**Code:**
```bash
# Initiale Erstellung
/doc-gen full

# Nach KB-Update (neue Länder)
/doc-gen update --section=kb

# Nur API-Docs
/doc-gen section --section=api

# Nur deutsch
/doc-gen update --lang=de

# Dry-Run
/doc-gen full --dry-run
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/doc-gen.md`</small>
