---
title: tool-inventory-agent
type: agent
tags: []
lang: en
confidence: 100
---

# tool-inventory-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2026-01-15 |</div>


## What It Does

"Discovers tools, finds orphans, generates Tool-Map"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
FÜR JEDE Kategorie in storage_locations:
  1. SCAN: Zähle Dateien im Pfad
  2. COMPARE: Prüfe gegen _stats.json Count
  3. VERIFY: Für jede Datei, prüfe Registrierungspunkte:
     - Node existiert in knowledge-nodes.json?
     - Eintrag in SYSTEM-MAP.md?
     - Route in context-router.json? (wenn applicable)
  4. REPORT: Liste Orphans mit fehlenden Registrierungen
```


#### Example



**Code:**
```bash
EVOLVING SYSTEM TOOL-MAP (2026-01-15)
=====================================

├── Core System
│   ├── Agents (64) ✅
│   ├── Commands (69) ✅
│   ├── Skills (7) ✅
│   └── Hooks (18) ✅
├── Knowledge Base
│   ├── Patterns (56) ✅
│   ├── Learnings (47) ✅
│   └── Decisions (11) ⚠️ 2 orphans
├── Graph
│   ├── Nodes (500)
│   └── Edges (344)
└── Templates & Blueprints
    ├── Templates (12) ✅
    └── Blueprints (9) ✅

ORPHANS FOUND: 2
INTEGRITY SCORE: 97/100
```


#### Example



**Code:**
```json
{
  "timestamp": "2026-01-15T10:00:00Z",
  "summary": {
    "total_components": 300,
    "registered": 298,
    "orphans": 2,
    "integrity_score": 97
  },
  "orphans": [
    {
      "file": "knowledge/decisions/decision-2026-01-14.md",
      "category": "decisions",
      "missing_registrations": ["_graph/edges.json", "_graph/knowledge-nodes.json"]
    }
  ],
  "count_mismatches": [
    {
      "category": "agents",
      "stats_count": 64,
      "actual_count": 66,
      "diff": 2
    }
  ]
}
```


#### Example



**Code:**
```bash
# Count agents
ls -1 .claude/agents/*.md | grep -v README | wc -l

# Check if node exists
grep -c "agent-new-agent" _graph/knowledge-nodes.json
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/tool-inventory-agent.md`</small>
