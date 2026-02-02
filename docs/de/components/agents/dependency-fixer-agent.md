---
title: dependency-fixer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# dependency-fixer-agent


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

"Repairs broken registrations with tiered autonomy"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
FÜR JEDEN Orphan aus Findings:
  1. IDENTIFY: Welche Registrierungen fehlen?
  2. CLASSIFY: Auto/Batch/Individual basierend auf:
     - Anzahl der fehlenden Registrierungen
     - Risiko-Level (Edge-Konflikte = HIGH)
  3. PREPARE: Änderungen vorbereiten:
     - Node-Definition generieren
     - _stats Count erhöhen
     - SYSTEM-MAP Eintrag formatieren
  4. CONFIRM: Bei Batch/Individual → User fragen
  5. EXECUTE: Registrierungen durchführen
  6. VERIFY: Prüfen ob erfolgreich
```


#### Example



**Code:**
```json
{
  "id": "{type}-{filename}",
  "type": "{category}",
  "name": "{Human Readable Name}",
  "path": "{relative/path/to/file.md}",
  "domain": ["evolving-system"],
  "tags": ["{category}", "auto-created"],
  "summary": "Auto-generated node for {filename}",
  "created": "{ISO-timestamp}"
}
```


#### Example



**Code:**
```bash
DEPENDENCY FIXER REPORT
=======================

Processed: 5 orphans
Fixed: 4
Skipped: 1 (edge conflict)

Changes Made:
├── _stats.json: +4 agents
├── knowledge-nodes.json: +4 nodes
├── edges.json: +8 edges
├── SYSTEM-MAP.md: +4 entries
└── context-router.json: +2 routes

Remaining Issues:
└── .claude/agents/conflict-agent.md: Manual review needed (duplicate ID)
```


#### Example



**Code:**
```json
{
  "timestamp": "2026-01-15T10:00:00Z",
  "summary": {
    "processed": 5,
    "fixed": 4,
    "skipped": 1
  },
  "changes": [
    {
      "file": ".claude/agents/new-agent.md",
      "registrations_added": ["_stats.json", "knowledge-nodes.json", "SYSTEM-MAP.md"]
    }
  ],
  "remaining_issues": [
    {
      "file": ".claude/agents/conflict-agent.md",
      "reason": "duplicate_id",
      "recommendation": "manual_review"
    }
  ]
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/dependency-fixer-agent.md`</small>
