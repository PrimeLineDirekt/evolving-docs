---
title: cross-reference-checker-agent
type: agent
tags: []
lang: en
confidence: 100
---

# cross-reference-checker-agent


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

Validiert Konsistenz zwischen ALLEN Master-Docs, _stats.json und tatsächlicher Struktur


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Hook Output: "⚠️ SYNC CHECK: Agent → SYSTEM-MAP.md, README.md (count)"
Realität: Claude muss manuell updaten
```


#### Example



**Code:**
```bash
Für jede Komponenten-Kategorie:

COMMANDS:
- Tatsächliche Dateien: count(.claude/commands/*.md)
- _stats.json: components.commands
- COMMANDS.md: Header-Count
- README.md: Stats-Section
- detection-index.json: Array-Länge

AGENTS:
- Tatsächliche Dateien: count(.claude/agents/*.md)
- _stats.json: components.agents.total
- SYSTEM-MAP.md: Agent-Tabelle Rows
- README.md: Stats-Section

SKILLS:
- Tatsächliche Ordner: count(.claude/skills/*/)
- _stats.json: components.skills.total
- SYSTEM-MAP.md: Skills-Tabelle
- README.md: Stats-Section

... (analog für: hooks, rules, scenarios, blueprints, templates)
```


#### Example



**Code:**
```bash
_stats.json MUSS authoritative sein:

1. Prüfe: Stimmen alle Werte mit Realität überein?
2. Wenn NEIN: _stats.json ist veraltet
3. Recommendation: _stats.json zuerst updaten, dann andere Docs

Felder in _stats.json:
- components: agents, skills, commands, hooks, rules, scenarios, blueprints, templates
- knowledge: patterns, learnings, prompts, references, projects
- memory: ideas, experiences, ledgers
- graph: nodes, edges, routes
```


#### Example



**Code:**
```bash
Für jeden Command in .claude/commands/:
- Existiert Entry in detection-index.json?
- Hat Entry mindestens 3 Keywords?
- Confidence >= 50?

Für jeden Entry in detection-index.json:
- Existiert Command-Datei?
- Sind Keywords eindeutig (keine Duplikate mit anderen Commands)?
```


#### Example



**Code:**
```bash
Für jede Tabelle in SYSTEM-MAP.md:
- Agents-Tabelle: Alle .claude/agents/*.md gelistet?
- Skills-Tabelle: Alle .claude/skills/*/ gelistet?
- Commands-Tabelle: Alle .claude/commands/*.md gelistet?
- Hooks-Tabelle: Alle .claude/hooks/*.sh gelistet?
- Templates-Tabelle: Alle .claude/templates/**/*.md gelistet?
```


#### Example



**Code:**
```bash
In allen .md Dateien unter .claude/:
- "@agent-name" → Agent existiert?
- "/command-name" → Command existiert?
- "pattern-name.md" → Pattern existiert?
- "siehe: file.md" → Datei existiert?
```


#### Example



**Code:**
```bash
Prüfe ob Auto-Sync fehlt:
- Hook meldet "SYNC CHECK" aber Update wurde nicht gemacht
- Zeitstempel: Letzte Änderung an Agent > letzte Änderung an SYSTEM-MAP?
- Empfehlung für echten Auto-Sync-Mechanismus
```


#### Example



**Code:**
```python
def validate_cross_references():
    issues = []
    recommendations = []

    # 1. Load all sources
    stats = read_json("_stats.json")
    detection = read_json(".claude/detection-index.json")

    # Count actual files
    actual = {
        "commands": count_files(".claude/commands/*.md"),
        "agents": count_files(".claude/agents/*.md"),
        "skills": count_dirs(".claude/skills/*/"),
        "hooks": count_files(".claude/hooks/*.sh"),
        "rules": count_files(".claude/rules/*.md") + count_files("knowledge/rules/**/*.md"),
        "scenarios": count_files(".claude/scenarios/*.json"),
        "blueprints": count_files(".claude/blueprints/*.json"),
        "templates": count_files(".claude/templates/**/*.md"),
        "patterns": count_files("knowledge/patterns/*.md"),
        "learnings": count_files("knowledge/learnings/*.md"),
    }

    # 2. Compare with _stats.json
    for key, actual_count in actual.items():
        stats_count = get_nested(stats, key)
        if actual_count != stats_count:
            issues.append({
                "type": "stats_mismatch",
                "component": key,
                "actual": actual_count,
                "stats_json": stats_count,
                "severity": "HIGH"
            })

    # 3. Compare with README.md
    readme_counts = extract_counts_from_readme("README.md")
    for key, readme_count in readme_counts.items():
        if readme_count != actual[key]:
            issues.append({
                "type": "readme_outdated",
                "component": key,
                "actual": actual[key],
                "readme": readme_count,
                "severity": "MEDIUM"
            })

    # 4. Detection Index Coverage
    cmd_files = list_files(".claude/commands/*.md")
    detected_cmds = [e["command"] for e in detection]

    missing = set(cmd_files) - set(detected_cmds)
    orphan = set(detected_cmds) - set(cmd_files)

    for cmd in missing:
        issues.append({
            "type": "missing_detection",
            "command": cmd,
            "severity": "MEDIUM"
        })

    for cmd in orphan:
        issues.append({
            "type": "orphan_detection",
            "command": cmd,
            "severity": "MEDIUM"
        })

    # 5. Auto-Sync Recommendation
    recommendations.append({
        "type": "implement_auto_sync",
        "description": "Hook nur erinnert, führt keine Updates aus",
        "suggestion": "Implementiere _stats.json Auto-Regeneration Hook"
    })

    return issues, recommendations
```


#### Example



**Code:**
```markdown
# Cross-Reference Audit Report

## Summary
- **Master-Docs geprüft**: 7
- **Komponenten-Kategorien**: 10
- **Total Checks**: {n}
- **Passed**: {n}
- **Failed**: {n}
- **Integrity Score**: {score}/100

## _stats.json Validation (Single Source of Truth)

| Komponente | Tatsächlich | _stats.json | Status |
|------------|-------------|-------------|--------|
| Commands | 63 | 58 | ❌ OUTDATED |
| Agents | 60 | 36 | ❌ OUTDATED |
| Skills | 6 | 12 | ❌ WRONG |
| Hooks | 12 | 12 | ✅ OK |

**_stats.json ist VERALTET** - Muss zuerst aktualisiert werden!

## Master-Doc Sync Status

| Dokument | Letzte Änderung | Sync Status |
|----------|-----------------|-------------|
| COMMANDS.md | 2026-01-05 | ⚠️ Behind |
| SYSTEM-MAP.md | 2026-01-04 | ⚠️ Behind |
| README.md | 2026-01-03 | ❌ Outdated |
| detection-index.json | 2026-01-06 | ✅ Current |

## Detection Index Coverage

| Metric | Value |
|--------|-------|
| Commands total | 63 |
| In detection-index | 58 |
| Coverage | 92% |
| Missing entries | 5 |
| Orphan entries | 2 |

### Missing Detection Entries
1. `/evolving-audit` - Keine Keywords definiert
2. `/new-command` - Keine Keywords definiert
...

### Orphan Entries (Command existiert nicht)
1. `/old-deprecated` - Datei gelöscht
2. `/renamed-cmd` - Wurde umbenannt

## Count Discrepancies

### Commands
| Source | Count | Status |
|--------|-------|--------|
| Actual files | 63 | Reference |
| _stats.json | 58 | ❌ -5 |
| COMMANDS.md | 61 | ❌ -2 |
| README.md | 58 | ❌ -5 |
| detection-index | 60 | ❌ -3 |

### Agents
| Source | Count | Status |
|--------|-------|--------|
| Actual files | 60 | Reference |
| _stats.json | 36 | ❌ -24 |
| SYSTEM-MAP.md | 57 | ❌ -3 |
| README.md | 36 | ❌ -24 |

## Auto-Sync Gap Analysis

### Aktueller Status
- `auto-cross-reference.sh` Hook: **NUR REMINDER**
- Tatsächliche Updates: **MANUELL durch Claude**
- Vergessene Updates: **~15 seit letztem Sync**

### Empfohlene Auto-Sync Lösung

```


#### Example



**Code:**
```bash

## Broken References Found

| File | Reference | Status |
|------|-----------|--------|
| orchestrator-agent.md | @helper-agent | ❌ Not found |
| audit-cmd.md | /old-audit | ❌ Renamed |

## Recommendations

### Immediate (heute)
1. **_stats.json regenerieren** - Single Source of Truth fixen
2. **5 fehlende Detection-Entries** hinzufügen
3. **2 Orphan-Entries** aus detection-index entfernen

### This Week
4. **README.md Counts** aktualisieren
5. **SYSTEM-MAP.md Tabellen** vervollständigen
6. **COMMANDS.md Count** im Header fixen

### Langfristig
7. **Auto-Stats-Hook implementieren** (regeneriert _stats.json)
8. **Master-Doc-Generator** erstellen (generiert aus _stats.json)
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/cross-reference-checker-agent.md`</small>
