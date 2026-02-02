---
title: inventory-report
type: command
tags: []
lang: en
confidence: 100
---

# inventory-report


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

Generiert vollständiges Tool-Inventar für aktuelles Projekt


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
1. .claude/ Directory scannen
   → commands/, agents/, skills/, scenarios/, hooks/, blueprints/, templates/, rules/

2. _memory/ scannen
   → projects/*.json (ohne Backups)

3. _graph/ scannen
   → Nodes count, Edges count, Routes count

4. CLAUDE.md Hierarchie
   → Global, Symlinks, Projekt

5. Output generieren
   → Markdown Tables + Mermaid + ASCII
```


#### Example



**Code:**
```bash
# Standard-Inventar generieren
/inventory-report

# Nur JSON-Index aktualisieren
/inventory-report --format json

# Vergleich mit Template
/inventory-report --compare /Buisiness/Evolving-Template
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/inventory-report.md`</small>
