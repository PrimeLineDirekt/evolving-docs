---
title: memory-schema-validator-agent
type: agent
tags: []
lang: en
confidence: 100
---

# memory-schema-validator-agent


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

Validiert Domain Memory Schema - Progress, Failures, Experiences, Backups, _stats.json Sync


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
// _stats.json enthält:
"memory": {
  "ideas": 1,        // count(ideas/*.md)
  "experiences": 16, // count(_memory/experiences/exp-*.json)
  "ledgers": 1       // count(_ledgers/*.md)
}
```


#### Example



**Code:**
```bash
Für jede Project-Memory Datei (_memory/projects/*.json):

Required Fields:
- name: string
- status: "active" | "paused" | "completed" | "archived"
- version: string (optional)
- phase: string
- goals: array
- features: array[{name, status, tests?}]
- state: object
- progress: array[{date, action, result, next?}]
- failures: array[{date, what, why, learned}]
```


#### Example



**Code:**
```bash
Für jeden Progress-Eintrag:

Required:
- date: "YYYY-MM-DD" format
- action: string (was getan)
- result: string (Ergebnis)

Optional:
- next: string (nächster Schritt)
- session_id: string

Validation:
- date nicht in Zukunft
- action mindestens 10 Zeichen
- result mindestens 5 Zeichen
```


#### Example



**Code:**
```bash
Für jeden Failure-Eintrag:

Required:
- date: "YYYY-MM-DD" format
- what: string (was ging schief)
- why: string (Root Cause)
- learned: string (Lesson Learned)

Validation:
- Alle 4 Felder ausgefüllt
- Keine leeren Strings
```


#### Example



**Code:**
```bash
Für jede Experience (_memory/experiences/exp-*.json):

Required Fields (aus SCHEMA.md):
- id: "exp-YYYY-NNN"
- type: "solution" | "pattern" | "decision" | "workaround" | "gotcha" | "preference"
- summary: string
- created: ISO date
- base_relevance: 0-100
- decay_factor: 0-1
- trust_level: 0-1
- effective_relevance: calculated

Decay Check:
- valid_until abgelaufen? → Cleanup Candidate
- effective_relevance < 30? → Low Priority
```


#### Example



**Code:**
```bash
Best Practices:
- Max 10 Einträge pro Projekt
- Älter als 30 Tage → sollte archiviert werden
- Nur letzte 5 für Quick-Load relevant

Prüfe:
- Projekte mit > 10 Progress-Einträgen
- Projekte mit Einträgen > 30 Tage alt
```


#### Example



**Code:**
```bash
Backup-Policy:
- Max 3 Backups pro Projekt
- Älter als 7 Tage → löschen
- Gesamtgröße < 5MB

Prüfe:
- Anzahl Backups pro Projekt
- Alter der Backups
- Gesamtgröße aller Backups
```


#### Example



**Code:**
```bash
Prüfe memory.* Werte:

experiences:
- Actual: count(_memory/experiences/exp-*.json)
- _stats.json: memory.experiences
- Match?

ideas:
- Actual: count(ideas/*.md)
- _stats.json: memory.ideas
- Match?
```


#### Example



**Code:**
```python
def validate_memory_schema():
    issues = []
    recommendations = []
    stats = read_json("_stats.json")

    # 1. Schema Validation
    for file in glob("_memory/projects/*.json"):
        if ".backup_" in file:
            continue

        try:
            data = read_json(file)
        except JSONDecodeError as e:
            issues.append({
                "type": "invalid_json",
                "file": file,
                "error": str(e),
                "severity": "CRITICAL"
            })
            continue

        # Required fields
        required = ["name", "status", "goals", "features", "state", "progress"]
        for field in required:
            if field not in data:
                issues.append({
                    "type": "missing_field",
                    "file": file,
                    "field": field,
                    "severity": "HIGH"
                })

        # Progress validation
        for i, entry in enumerate(data.get("progress", [])):
            for field in ["date", "action", "result"]:
                if field not in entry or not entry[field]:
                    issues.append({
                        "type": "invalid_progress_entry",
                        "file": file,
                        "index": i,
                        "missing": field,
                        "severity": "MEDIUM"
                    })

        # Progress hygiene
        progress_count = len(data.get("progress", []))
        if progress_count > 10:
            issues.append({
                "type": "progress_overflow",
                "file": file,
                "count": progress_count,
                "max": 10,
                "severity": "LOW"
            })

        # Failure validation
        for i, entry in enumerate(data.get("failures", [])):
            for field in ["date", "what", "why", "learned"]:
                if field not in entry or not entry[field]:
                    issues.append({
                        "type": "invalid_failure_entry",
                        "file": file,
                        "index": i,
                        "missing": field,
                        "severity": "MEDIUM"
                    })

    # 2. Experience Validation
    exp_files = glob("_memory/experiences/exp-*.json")
    actual_exp_count = len(exp_files)

    if actual_exp_count != stats["memory"]["experiences"]:
        issues.append({
            "type": "experience_count_mismatch",
            "actual": actual_exp_count,
            "stats_json": stats["memory"]["experiences"],
            "severity": "HIGH"
        })

    for exp_file in exp_files:
        exp = read_json(exp_file)

        # Check decay
        if "valid_until" in exp:
            if parse_date(exp["valid_until"]) < today():
                issues.append({
                    "type": "expired_experience",
                    "file": exp_file,
                    "expired": exp["valid_until"],
                    "severity": "LOW"
                })

        if exp.get("effective_relevance", 100) < 30:
            recommendations.append({
                "type": "low_relevance_experience",
                "file": exp_file,
                "relevance": exp["effective_relevance"],
                "action": "Consider archiving"
            })

    # 3. Backup Retention
    backup_groups = {}
    for backup in glob("_memory/projects/*.backup_*.json"):
        project = extract_project_name(backup)
        if project not in backup_groups:
            backup_groups[project] = []
        backup_groups[project].append(backup)

    total_backup_size = 0
    for project, backups in backup_groups.items():
        if len(backups) > 3:
            issues.append({
                "type": "excessive_backups",
                "project": project,
                "count": len(backups),
                "max": 3,
                "severity": "MEDIUM"
            })

        for backup in backups:
            age = get_file_age_days(backup)
            size = get_file_size(backup)
            total_backup_size += size

            if age > 7:
                issues.append({
                    "type": "stale_backup",
                    "file": backup,
                    "age_days": age,
                    "severity": "LOW"
                })

    if total_backup_size > 5 * 1024 * 1024:  # 5MB
        issues.append({
            "type": "backup_size_exceeded",
            "total_mb": total_backup_size / (1024 * 1024),
            "max_mb": 5,
            "severity": "MEDIUM"
        })

    return issues, recommendations
```


#### Example



**Code:**
```markdown
# Memory Schema Validation Report

## Summary
- **Project Files**: {n}
- **Experience Files**: {n}
- **Backup Files**: {n}
- **Schema Violations**: {n}
- **Memory Health Score**: {score}/100

## _stats.json Sync Status

| Metric | Actual | _stats.json | Status |
|--------|--------|-------------|--------|
| Experiences | 22 | 16 | ❌ OUTDATED |
| Ideas | 1 | 1 | ✅ OK |
| Ledgers | 1 | 1 | ✅ OK |

## Schema Validation Results

| Project | Valid JSON | Required Fields | Progress | Failures |
|---------|------------|-----------------|----------|----------|
| evolving-system | ✅ | ✅ | ⚠️ 15 entries | ✅ |
| auswanderungs-ki | ✅ | ✅ | ⚠️ 30 entries | ✅ |
| thrive-vibes | ✅ | ❌ features | ✅ | ✅ |

## Issues Found

### CRITICAL: Invalid JSON
- **File**: `_memory/projects/broken.json`
- **Error**: Unexpected token at line 42
- **Fix**: Repair JSON syntax manually

### HIGH: Missing Required Field
- **File**: `_memory/projects/thrive-vibes.json`
- **Missing**: `features` array
- **Fix**: Add empty features array: `"features": []`

### HIGH: Experience Count Mismatch
- **Actual**: 22 experiences
- **_stats.json**: 16
- **Fix**: Update `_stats.json.memory.experiences = 22`

### MEDIUM: Excessive Backups
- **Project**: `evolving-system`
- **Count**: 8 backups (max 3)
- **Action**: Delete oldest 5

### LOW: Progress Overflow
- **File**: `auswanderungs-ki.json`
- **Count**: 30 entries (max 10)
- **Action**: Archive entries older than 30 days

### LOW: Stale Backup
- **File**: `evolving-system.backup_20260101.json`
- **Age**: 6 days (max 7)
- **Action**: Will auto-delete tomorrow OR delete now

## Experience Memory Status

### Decay Analysis
| Experience | Relevance | Decay | Valid Until | Status |
|------------|-----------|-------|-------------|--------|
| exp-2026-001 | 85 | 0.95 | - | Active |
| exp-2026-005 | 28 | 0.45 | 2026-01-10 | ⚠️ Low |
| exp-2026-012 | 12 | 0.20 | 2025-12-30 | ❌ EXPIRED |

### Cleanup Candidates
1. `exp-2026-012` - Expired, delete
2. `exp-2026-005` - Low relevance, review
3. `exp-2026-008` - 2 months old, no access

## Backup Analysis

| Project | Backups | Oldest | Newest | Total Size |
|---------|---------|--------|--------|------------|
| evolving-system | 8 | 6 days | 1 day | 1.2 MB |
| auswanderungs-ki | 12 | 10 days | 1 day | 1.8 MB |
| thrive-vibes | 2 | 3 days | 1 day | 0.3 MB |

**Total Backup Size**: 3.3 MB (limit 5 MB)

### Cleanup Potential
- Delete 17 stale backups (> 7 days)
- Delete 7 excess backups (> 3 per project)
- **Space saved**: ~2.1 MB

## Auto-Sync Recommendations

### Current Problem
- Experience count not synced to _stats.json
- Backup retention not automated

### Recommended Solutions

```


#### Example



**Code:**
```bash

## Cleanup Roadmap

### Phase 1: Fix Critical (5 min)
1. Repair invalid JSON files

### Phase 2: Update Stats (2 min)
2. Update _stats.json.memory.experiences

### Phase 3: Clean Backups (5 min)
3. Delete 17 stale backups
4. Delete 7 excess backups

### Phase 4: Archive Progress (10 min)
5. Archive progress entries > 30 days
6. Trim progress arrays to max 10

### Phase 5: Clean Experiences (5 min)
7. Delete 3 expired experiences
8. Review 2 low-relevance experiences
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/memory-schema-validator-agent.md`</small>
