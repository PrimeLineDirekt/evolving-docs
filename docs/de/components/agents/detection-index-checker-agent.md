---
title: detection-index-checker-agent
type: agent
tags: []
lang: en
confidence: 100
---

# detection-index-checker-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents |</div>


## What It Does

Validiert Command Detection Index - Keywords, Coverage, Context-Router Sync, _stats.json


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
.claude/commands/*.md (Actual Files)
         ↓
    _stats.json.components.commands (Count)
         ↓
    detection-index.json (Entries)
         ↓
    COMMANDS.md (Documentation)
         ↓
    context-router.json (Graph Integration)

ALLE müssen synchron sein!
```


#### Example



**Code:**
```bash
Für jeden Command in .claude/commands/:
- Existiert Entry in detection-index.json?
- Hat Entry mindestens 3 Keywords?
- Ist Confidence >= 50?

Coverage = (Commands with Detection) / (Total Commands) * 100
Target: >= 95%
```


#### Example



**Code:**
```bash
Für jeden Entry in detection-index.json:
- Existiert Command-Datei (.claude/commands/{name}.md)?
- Ist Command in COMMANDS.md dokumentiert?

Orphan = Entry ohne existierende Datei
```


#### Example



**Code:**
```bash
Über alle Entries:
- Keyword nur einmal verwendet?
- Bei Überlappung: Anti-Keywords vorhanden?
- Bei Konflikt: Höherer Confidence gewinnt?

High-Conflict Keywords:
- "erstellen" → /create-agent, /create-command, /create-skill...
- "audit" → /full-audit, /quick-audit, /audit-security...
- "idee" → /idea-new, /idea-list, /idea-work...
```


#### Example



**Code:**
```bash
Confidence-Levels:
- 80-100: High → Auto-trigger möglich
- 50-79: Medium → User fragen
- 0-49: Low → Wahrscheinlich nicht gemeint

Prüfe:
- Haupt-Keywords (Verb + Objekt) haben >= 70?
- Generische Keywords haben < 60?
- Anti-Keywords reduzieren Confidence?
```


#### Example



**Code:**
```bash
Vergleiche mit context-router.json:
- Commands in beiden Systemen?
- Konsistente Keywords?
- Router-Routes haben gültige primary_nodes?
```


#### Example



**Code:**
```bash
Prüfe:
- Actual commands: count(.claude/commands/*.md)
- detection-index entries: length(detection-index.json)
- _stats.json: components.commands

Alle drei sollten identisch sein!
```


#### Example



**Code:**
```bash
Für jeden Command:
- In detection-index.json?
- In COMMANDS.md dokumentiert?
- Description konsistent?
```


#### Example



**Code:**
```python
def validate_detection_index():
    issues = []
    recommendations = []

    # Load data
    detection = read_json(".claude/detection-index.json")
    router = read_json("_graph/cache/context-router.json")
    stats = read_json("_stats.json")
    commands_md = read_file(".claude/COMMANDS.md")

    # Count actual files
    cmd_files = list_files(".claude/commands/*.md")
    actual_count = len(cmd_files)
    cmd_names = [extract_name(f) for f in cmd_files]

    detection_entries = detection.get("commands", detection)  # Handle both formats
    detection_names = [e["command"] for e in detection_entries]
    detection_count = len(detection_entries)

    # 1. _stats.json Sync
    stats_count = stats["components"]["commands"]
    if actual_count != stats_count:
        issues.append({
            "type": "stats_mismatch",
            "actual": actual_count,
            "stats_json": stats_count,
            "severity": "HIGH"
        })

    if detection_count != actual_count:
        issues.append({
            "type": "detection_coverage_mismatch",
            "actual_commands": actual_count,
            "detection_entries": detection_count,
            "severity": "MEDIUM"
        })

    # 2. Coverage Check
    missing = set(cmd_names) - set(detection_names)
    for cmd in missing:
        issues.append({
            "type": "missing_detection",
            "command": cmd,
            "severity": "MEDIUM"
        })

    # 3. Orphan Entries
    orphans = set(detection_names) - set(cmd_names)
    for cmd in orphans:
        issues.append({
            "type": "orphan_entry",
            "command": cmd,
            "severity": "MEDIUM"
        })

    # 4. Duplicate Keywords
    all_keywords = {}
    for entry in detection_entries:
        cmd = entry["command"]
        for kw in entry.get("keywords", []):
            kw_lower = kw.lower()
            if kw_lower in all_keywords:
                issues.append({
                    "type": "duplicate_keyword",
                    "keyword": kw,
                    "commands": [all_keywords[kw_lower], cmd],
                    "severity": "LOW"
                })
            else:
                all_keywords[kw_lower] = cmd

    # 5. Confidence Check
    for entry in detection_entries:
        conf = entry.get("confidence", 0)
        if conf < 50:
            issues.append({
                "type": "low_confidence",
                "command": entry["command"],
                "confidence": conf,
                "severity": "LOW"
            })

        if len(entry.get("keywords", [])) < 3:
            issues.append({
                "type": "insufficient_keywords",
                "command": entry["command"],
                "keyword_count": len(entry.get("keywords", [])),
                "minimum": 3,
                "severity": "LOW"
            })

    # 6. COMMANDS.md Check
    for cmd in cmd_names:
        if f"/{cmd}" not in commands_md and f"## {cmd}" not in commands_md:
            issues.append({
                "type": "missing_in_commands_md",
                "command": cmd,
                "severity": "MEDIUM"
            })

    # Calculate coverage
    coverage = (detection_count - len(orphans)) / actual_count * 100 if actual_count > 0 else 0

    return issues, recommendations, coverage
```


#### Example



**Code:**
```markdown
# Detection Index Validation Report

## Summary
- **Actual Commands**: {n}
- **Detection Entries**: {n}
- **Coverage**: {pct}%
- **Duplicate Keywords**: {n}
- **Detection Accuracy Score**: {score}/100

## _stats.json Sync Status

| Metric | Actual | _stats.json | Detection | Status |
|--------|--------|-------------|-----------|--------|
| Commands | 63 | 58 | 60 | ❌ ALL DIFFER |

**Root Cause**: _stats.json outdated, detection-index incomplete

## Coverage Analysis

| Category | Commands | In Detection | Coverage |
|----------|----------|--------------|----------|
| Model Switchers | 4 | 4 | 100% |
| Idea Management | 4 | 4 | 100% |
| Audit Suite | 5 | 4 | 80% |
| Creation Tools | 5 | 5 | 100% |
| NEW (this week) | 5 | 0 | 0% |

**Overall Coverage**: 92% (target: 95%)

## Issues Found

### HIGH: Stats Mismatch
- **Actual commands**: 63
- **_stats.json**: 58
- **Fix**: Update `_stats.json.components.commands = 63`

### MEDIUM: Missing Detection Entries
1. `/evolving-audit` - Neu erstellt, keine Keywords
2. `/new-command-2` - Vergessen
3. `/renamed-cmd` - Nach Umbenennung nicht aktualisiert

### MEDIUM: Orphan Entries
1. `/old-deprecated` - Datei gelöscht am 2026-01-03
2. `/renamed-old` - Wurde zu /renamed-cmd

### MEDIUM: Missing in COMMANDS.md
1. `/evolving-audit` - Neu, nicht dokumentiert
2. `/file-hygiene` - Fehlt in Liste

### LOW: Duplicate Keywords
| Keyword | Commands | Resolution |
|---------|----------|------------|
| "erstellen" | create-agent, create-command | Use anti-keywords |
| "audit" | full-audit, quick-audit | Confidence-based |
| "liste" | idea-list, project-list | Use "idee liste" vs "projekt liste" |

### LOW: Low Confidence
1. `/obscure-feature` - Confidence 35, add more keywords
2. `/rarely-used` - Confidence 42, consider deprecation

### LOW: Insufficient Keywords
1. `/quick-cmd` - Only 2 keywords (min 3)
2. `/simple-action` - Only 1 keyword

## Keyword Distribution

### High-Conflict Keywords (need disambiguation)
| Keyword | Used by | Recommendation |
|---------|---------|----------------|
| "erstellen" | 5 commands | Add object: "agent erstellen", "command erstellen" |
| "audit" | 3 commands | Add modifier: "full audit", "quick audit" |
| "zeige" | 4 commands | Add object: "zeige ideen", "zeige projekte" |

### Under-Keyworded Commands
| Command | Keywords | Should Add |
|---------|----------|------------|
| /evolving-audit | 0 | "system audit", "evolving prüfen" |
| /quick-cmd | 2 | Add 1 more unique keyword |

## Context Router Comparison

| Dimension | Detection | Router | Sync |
|-----------|-----------|--------|------|
| Total entries | 60 | 35 routes | Partial |
| Shared keywords | 156 | 89 | Overlap |
| Unique to detection | 223 | - | OK |
| Unique to router | - | 67 | OK |

## Auto-Sync Recommendations

### Current Problem
- Neue Commands haben keine Detection-Entries
- Hook erinnert, aber fügt nicht hinzu
- COMMANDS.md manuell gepflegt

### Recommended Solution

```


#### Example



**Code:**
```bash

## Cleanup Roadmap

### Phase 1: Fix Stats (2 min)
1. Update _stats.json.components.commands = 63

### Phase 2: Add Missing (10 min)
2. Add 5 missing detection entries
3. Add keywords for each (min 3)

### Phase 3: Remove Orphans (5 min)
4. Remove 2 orphan entries

### Phase 4: Resolve Duplicates (15 min)
5. Add anti-keywords for conflicts
6. Adjust confidence levels

### Phase 5: Update COMMANDS.md (10 min)
7. Add 2 missing command docs
8. Verify all entries match
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/detection-index-checker-agent.md`</small>
