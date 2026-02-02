---
title: system-audit
type: command
tags: []
lang: en
confidence: 100
---

# system-audit


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

System-Integritäts-Audit mit 4 spezialisierten Validatoren


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Task(
  subagent_type="general-purpose",
  model="haiku",
  prompt="""
## Task: Detection Index Audit

Validiere `.claude/detection-index.json`:

1. Alle Commands im Index existieren als Files in `.claude/commands/`
2. Keine Orphan-Entries (außer bekannte Plugin-Commands)
3. Keywords sind angemessen, keine Duplikate
4. Confidence-Levels korrekt (high/medium/low)
5. Patterns vorhanden für alle Commands

## Output Format (EXAKT einhalten!)
```


#### Example



**Code:**
```bash
"""
)
```


#### Example



**Code:**
```bash
Task(
  subagent_type="general-purpose",
  model="haiku",
  prompt="""
## Task: Knowledge Graph Audit

Validiere `_graph/`:

1. Alle Nodes haben `partition` field (core-nodes.json → "core", knowledge-nodes.json → "knowledge")
2. Keine Orphan-Edges (Edges die auf nicht-existente Nodes zeigen)
3. Keine Duplicate-Edges
4. Edge-Types sind normalisiert (lowercase, keine Sonderzeichen)

Files: _graph/core-nodes.json, _graph/knowledge-nodes.json, _graph/edges.json

## Output Format (EXAKT einhalten!)
```


#### Example



**Code:**
```bash
"""
)
```


#### Example



**Code:**
```bash
Task(
  subagent_type="general-purpose",
  model="haiku",
  prompt="""
## Task: Memory Schema Audit

Validiere `_memory/`:

1. index.json hat validen active_context
2. Project-Files haben required fields (goals, features, state, progress, failures)
3. Keine Test-Pollution in progress/failures Arrays (z.B. "test action", "test result")
4. Datenqualität angemessen

Files: _memory/index.json, _memory/projects/*.json (keine Backups!)

## Output Format (EXAKT einhalten!)
```


#### Example



**Code:**
```bash
"""
)
```


#### Example



**Code:**
```bash
Task(
  subagent_type="general-purpose",
  model="haiku",
  prompt="""
## Task: Cross-Reference Audit

Validiere Konsistenz zwischen `_stats.json` und tatsächlichen File-Counts.

## Counts zu prüfen (bash ausführen):
- commands: find .claude/commands -name "*.md" | wc -l
- agents: find .claude/agents -name "*.md" | wc -l
- hooks: find .claude/hooks -type f \( -name "*.sh" -o -name "*.py" \) | wc -l
- rules: find .claude/rules -name "*.md" | wc -l
- graph.nodes: jq '.nodes | length' _graph/core-nodes.json + jq '.nodes | length' _graph/knowledge-nodes.json

Vergleiche mit _stats.json Werten.

## Output Format (EXAKT einhalten!)
```


#### Example



**Code:**
```bash
"""
)
```


#### Example



**Code:**
```bash
╔═══════════════════════════════════════════════════════════════╗
║                    SYSTEM INTEGRITY AUDIT                     ║
║                      {YYYY-MM-DD HH:MM}                       ║
╠═══════════════════════════════════════════════════════════════╣
║ VALIDATOR SCORES                                              ║
║                                                               ║
║   Detection Index    [{bar}] {score}/100  {icon}              ║
║   Knowledge Graph    [{bar}] {score}/100  {icon}              ║
║   Memory Schema      [{bar}] {score}/100  {icon}              ║
║   Cross-Reference    [{bar}] {score}/100  {icon}              ║
║                                                               ║
║   ─────────────────────────────────────────────────           ║
║   OVERALL SCORE      [{bar}] {avg}/100    {icon}              ║
╠═══════════════════════════════════════════════════════════════╣
║ ISSUES BY PRIORITY                                            ║
║                                                               ║
║   🔴 CRITICAL: {count}                                        ║
║   🟡 HIGH:     {count}                                        ║
║   🟠 MEDIUM:   {count}                                        ║
║   🔵 LOW:      {count}                                        ║
╠═══════════════════════════════════════════════════════════════╣
║ TOP ISSUES                                                    ║
║                                                               ║
║   {list top 5 issues with severity}                           ║
╚═══════════════════════════════════════════════════════════════╝
```


#### Example



**Code:**
```bash
╔═══════════════════════════════════════════════════════════════╗
║                    SYSTEM INTEGRITY AUDIT                     ║
║                      2026-01-13 17:30                         ║
╠═══════════════════════════════════════════════════════════════╣
║ VALIDATOR SCORES                                              ║
║                                                               ║
║   Detection Index    [████████░░] 82/100   ⚠️                 ║
║   Knowledge Graph    [██████████] 100/100  ✅                 ║
║   Memory Schema      [███████░░░] 78/100   ⚠️                 ║
║   Cross-Reference    [██████░░░░] 65/100   ❌                 ║
║                                                               ║
║   ─────────────────────────────────────────────────           ║
║   OVERALL SCORE      [████████░░] 81/100   ⚠️                 ║
╠═══════════════════════════════════════════════════════════════╣
║ ISSUES BY PRIORITY                                            ║
║                                                               ║
║   🔴 CRITICAL: 1                                              ║
║   🟡 HIGH:     2                                              ║
║   🟠 MEDIUM:   3                                              ║
║   🔵 LOW:      1                                              ║
╠═══════════════════════════════════════════════════════════════╣
║ TOP ISSUES                                                    ║
║                                                               ║
║   🔴 Test pollution in didit-medical-care.json                ║
║   🟡 3 commands missing detection patterns                    ║
║   🟡 _stats.json counts outdated                              ║
║   🟠 Sparse progress data in thrive-vibes-art                 ║
║   🔵 Last detection-index update 3 days ago                   ║
╚═══════════════════════════════════════════════════════════════╝
```


#### Example



**Code:**
```bash
╔═══════════════════════════════════════════════════════════════╗
║ AUTO-FIX VERFÜGBAR                                            ║
║                                                               ║
║ Folgende Issues können automatisch behoben werden:            ║
║   • {fixable issue 1}                                         ║
║   • {fixable issue 2}                                         ║
║   ...                                                         ║
║                                                               ║
║ Soll ich die Fixes durchführen? [Ja/Nein]                     ║
╚═══════════════════════════════════════════════════════════════╝
```


#### Example



**Code:**
```bash
Für jedes Issue:
- Missing patterns → Patterns generieren und hinzufügen
- Orphan entries → Entry entfernen (außer Plugin-Commands)
- Timestamp veraltet → updated Feld aktualisieren
```


#### Example



**Code:**
```bash
Für jedes Issue:
- Missing partition → partition field zu allen Nodes hinzufügen (jq)
- Orphan edges → Edge entfernen
- Duplicate edges → Duplikat entfernen
- Non-standard edge types → Type normalisieren
```


#### Example



**Code:**
```bash
Für jedes Issue:
- Test pollution → Test-Entries aus progress/failures entfernen
- Missing fields → Leere Felder mit Default-Werten füllen
- Schema inconsistency → Schema normalisieren
```


#### Example



**Code:**
```bash
Für jedes Issue:
- Count mismatch → _stats.json mit korrekten Counts updaten
- Run actual counts via bash und update _stats.json
```


#### Example



**Code:**
```bash
╔═══════════════════════════════════════════════════════════════╗
║ FIX RESULTS                                                   ║
║                                                               ║
║   Fixed:    {count} issues                                    ║
║   Skipped:  {count} (manual intervention required)            ║
║   Failed:   {count}                                           ║
║                                                               ║
║   NEW SCORE: {old} → {new}/100  {improvement_icon}            ║
╠═══════════════════════════════════════════════════════════════╣
║ REMAINING ISSUES (manual fix required)                        ║
║                                                               ║
║   {list remaining issues if any}                              ║
╚═══════════════════════════════════════════════════════════════╝
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/system-audit.md`</small>
