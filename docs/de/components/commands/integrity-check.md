---
title: integrity-check
type: command
tags: []
lang: en
confidence: 100
---

# integrity-check


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

"Quick integrity validation without fixes"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
agents:    _stats.json (67) vs ls .claude/agents/*.md (67) ✅
commands:  _stats.json (71) vs ls .claude/commands/*.md (71) ✅
```


#### Example



**Code:**
```bash
INTEGRITY CHECK (2026-01-15)
============================

Counts:
├── agents:     67/67 ✅
├── commands:   71/71 ✅
├── skills:      7/7  ✅
├── hooks:      18/18 ✅
├── patterns:   56/56 ✅
├── learnings:  47/47 ✅
└── templates:  12/12 ✅

Graph:
├── Nodes: 520 ✅
├── Edges: 380 ✅
├── Broken refs: 0 ✅
└── Orphan nodes: 2 ⚠️

Registrations:
├── Complete: 298/300
└── Incomplete: 2 ⚠️
    ├── knowledge/decisions/decision-2026-01-14.md (missing: edges)
    └── .claude/agents/new-agent.md (missing: router)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORE: 95/100

Recommendation: Run /tool-map --fix to repair 2 issues
```


#### Example



**Code:**
```bash
# Quick check
/integrity-check

# Detailed output
/integrity-check --verbose

# For CI/CD integration
/integrity-check --json

# Auto-heal SAFE issues (broken edges, duplicates, expired)
/integrity-check --auto-heal

# Full healing with CAUTION-level detection
/integrity-check --heal-all
```


#### Example



**Code:**
```bash
Edge Partitions:
├── edges-by-type.json: 9 types ✅
├── edges-by-source.json: 12 sources ✅
├── edges-index.json: 614 total ✅
└── Sync: edges.json matches ✅
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/integrity-check.md`</small>
