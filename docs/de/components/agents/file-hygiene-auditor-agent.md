---
title: file-hygiene-auditor-agent
type: agent
tags: []
lang: en
confidence: 100
---

# file-hygiene-auditor-agent


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

Prüft Duplikate, übergroße Dateien, Legacy-Files, Backup-Retention


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Prüfe auf identische/sehr ähnliche Inhalte:
- Dateien mit gleichem Hash
- Dateien mit >90% Textüberlappung
- Ausnahme: Bewusste Kopien (templates/)
```


#### Example



**Code:**
```bash
Schwellwerte:
- .md Dateien > 500 Zeilen → "Overload"
- .json Dateien > 1000 Zeilen → "Large"
- .md Dateien > 1000 Zeilen → "Split recommended"

Ausnahmen:
- knowledge/sessions/ (Logs, dürfen groß sein)
- knowledge/projects/ (Projektdocs)
```


#### Example



**Code:**
```bash
Legacy-Indikatoren:
- Dateiname enthält "legacy", "old", "deprecated"
- Datei unverändert > 30 Tage + nicht referenziert
- Parallel existierende neue Version (v2, -new)
```


#### Example



**Code:**
```bash
Prüfe Backup-Verzeichnisse:
- _backup/
- _memory/**/*.backup_*
- Alter > 7 Tage ohne explizites Keep
```


#### Example



**Code:**
```bash
Dateien die nirgends importiert/referenziert werden:
- Keine Edges im Graph
- Nicht in COMMANDS.md, SYSTEM-MAP.md
- Keine Imports in anderen Dateien
```


#### Example



**Code:**
```python
def audit_file_hygiene():
    issues = []

    # Scope: Core system files (nicht knowledge/sessions)
    scan_paths = [
        ".claude/",
        "_graph/",
        "_memory/",
        "knowledge/patterns/",
        "knowledge/rules/"
    ]

    # 1. Size Analysis
    for path in scan_paths:
        for file in glob(f"{path}/**/*"):
            lines = count_lines(file)

            if file.endswith(".md") and lines > 500:
                issues.append({
                    "type": "overload_file",
                    "file": file,
                    "lines": lines,
                    "recommendation": "Consider splitting",
                    "severity": "MEDIUM"
                })

            if file.endswith(".json") and lines > 2000:
                issues.append({
                    "type": "large_json",
                    "file": file,
                    "lines": lines,
                    "severity": "LOW"
                })

    # 2. Legacy Detection
    legacy_patterns = ["legacy", "old", "deprecated", "-v1"]
    for file in all_files:
        if any(p in file.lower() for p in legacy_patterns):
            issues.append({
                "type": "legacy_file",
                "file": file,
                "indicator": "naming",
                "severity": "MEDIUM"
            })

    # 3. Backup Retention
    backup_files = glob("_backup/**/*") + glob("_memory/**/*.backup_*")
    for backup in backup_files:
        age = get_file_age_days(backup)
        if age > 7:
            issues.append({
                "type": "stale_backup",
                "file": backup,
                "age_days": age,
                "severity": "LOW"
            })

    # 4. Duplicate Detection
    hashes = {}
    for file in all_files:
        h = file_hash(file)
        if h in hashes:
            issues.append({
                "type": "duplicate",
                "files": [hashes[h], file],
                "severity": "MEDIUM"
            })
        else:
            hashes[h] = file

    return issues
```


#### Example



**Code:**
```markdown
# File Hygiene Audit Report

## Summary
- **Files Scanned**: {n}
- **Total Size**: {mb} MB
- **Duplicates Found**: {n}
- **Overload Files**: {n}
- **Legacy Files**: {n}
- **Stale Backups**: {n}
- **Hygiene Score**: {score}/100

## Size Distribution

| Category | Files | Avg Lines | Largest |
|----------|-------|-----------|---------|
| .claude/commands/ | 63 | 85 | 250 |
| .claude/agents/ | 59 | 120 | 380 |
| _graph/ | 8 | 1500 | 5034 |

## Issues Found

### MEDIUM: Overload File
- **File**: `.claude/COMMANDS.md`
- **Lines**: 1,202
- **Recommendation**: Split into categories or use summary-layer

### MEDIUM: Legacy File
- **File**: `_graph/nodes-legacy.json`
- **Lines**: 5,034
- **Status**: Parallel version exists (core-nodes + knowledge-nodes)
- **Recommendation**: Archive to _backup/ after validation

### MEDIUM: Duplicate Content
- **File 1**: `knowledge/prompts/a/profil-analyse.md`
- **File 2**: `knowledge/projects/b/profil-analyse.md`
- **Similarity**: 98%
- **Recommendation**: Keep one, symlink other

### LOW: Stale Backup
- **File**: `_memory/projects/evolving-system.backup_20260101.json`
- **Age**: 6 days
- **Recommendation**: Delete (newer backups exist)

## Cleanup Potential

| Action | Files | Space Saved |
|--------|-------|-------------|
| Delete stale backups | 53 | 2.1 MB |
| Archive legacy | 2 | 187 KB |
| Remove duplicates | 18 | 800 KB |
| **Total** | **73** | **~3 MB** |

## Overload Files (Top 10)

| File | Lines | Status |
|------|-------|--------|
| _graph/nodes-legacy.json | 5,034 | LEGACY |
| _graph/knowledge-nodes.json | 3,086 | Active |
| _graph/edges.json | 2,907 | Active |
| .claude/COMMANDS.md | 1,202 | OVERLOAD |
| .claude/CONTEXT.md | 890 | Borderline |

## Recommendations

1. **Immediate**: Delete 53 stale backups (6+ days old)
2. **This Week**: Archive 2 legacy graph files
3. **Consider**: Split COMMANDS.md into category files
4. **Resolve**: 18 duplicate files (keep canonical version)
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/file-hygiene-auditor-agent.md`</small>
