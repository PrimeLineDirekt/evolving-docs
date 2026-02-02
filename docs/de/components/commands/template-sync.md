---
title: template-sync
type: command
tags: []
lang: en
confidence: 100
---

# template-sync


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

Synchronizes generic content from Evolving to Evolving-Template with privacy protection


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
1. Parse --profile Argument (default: "template")
2. Lade passendes Manifest:
   - template → .claude/config/template-sync-manifest.json
   - benji → .claude/config/benji-sync-manifest.json
3. Prüfe Pfade:
   - Source: $EVOLVING_SOURCE oder $PWD
   - Target: manifest.paths.target
4. Falls Target nicht konfiguriert:
   → Frage User nach Pfad
   → Speichere in Manifest
5. Prüfe ob Target existiert und git repo ist
6. Zeige: "Sync Profile: {profile} → {target_path}"
```


#### Example



**Code:**
```bash
Analysiere beide Repos und erstelle Inventar:
- Zähle Komponenten (Agents, Commands, Skills, etc.)
- Identifiziere NEW, UPDATED, TEMPLATE-ONLY
- Zeige Summary
```


#### Example



**Code:**
```bash
📦 TEMPLATE INVENTORY:
├── Agents: 19 (Source: 23 → 4 neu)
├── Commands: 34 (Source: 39 → 5 neu)
├── Patterns: 12 (Source: 15 → 3 neu)
└── Template-Only: 8 (geschützt)
```


#### Example



**Code:**
```bash
Kategorisiere alle Dateien:
- NEW: Nur in Source
- UPDATED: Source neuer
- DIVERGED: Beide geändert
- TEMPLATE-ONLY: Geschützt
- IDENTICAL: Keine Änderung
```


#### Example



**Code:**
```bash
📊 DIFF ANALYSE:
├── NEW: 12 Dateien
├── UPDATED: 8 Dateien
├── DIVERGED: 1 Datei (Review nötig)
├── TEMPLATE-ONLY: 8 Dateien (skip)
└── IDENTICAL: 45 Dateien
```


#### Example



**Code:**
```bash
Scanne alle zu synchronisierenden Dateien:
- CRITICAL: API Keys, Secrets → BLOCK
- HIGH: Persönliche Namen, Projekte → ANONYMIZE
- MEDIUM: Pfade, Locations → ANONYMIZE
```


#### Example



**Code:**
```bash
🔒 PRIVACY SCAN:
├── CRITICAL: 0 (keine API Keys)
├── HIGH: 3 Dateien mit persönlichen Referenzen
└── MEDIUM: 5 Dateien mit lokalen Pfaden
```


#### Example



**Code:**
```bash
Starte Task mit `content-anonymizer-agent`:
- Ersetze persönliche Referenzen mit Placeholdern
- Zeige Vorher/Nachher Preview
- Frage bei unklaren Fällen
```


#### Example



**Code:**
```bash
🔄 ANONYMISIERUNG:
├── .claude/agents/xyz-agent.md
│   └── "Robin" → "{USER}"
├── knowledge/patterns/example.md
│   └── "Auswanderungs-KI" → "{PROJECT}"
└── .claude/CONTEXT.md
    └── "/Users/neoforce" → "{HOME}"
```


#### Example



**Code:**
```bash
DIVERGED: .claude/agents/example.md

Source: 2026-01-04 10:30
Target: 2026-01-03 14:15

Optionen:
  [S] Source übernehmen
  [T] Target behalten
  [M] Manuell mergen
  [D] Diff anzeigen
```


#### Example



**Code:**
```bash
═══════════════════════════════════════
SYNC PREVIEW
═══════════════════════════════════════
NEW (12):        ████████████ sync
UPDATED (8):     ████████ sync
ANONYMIZED (3):  ███ transform + sync
DIVERGED (1):    █ [User-Entscheidung]
SKIP (8):        ████████ template-only
═══════════════════════════════════════

Proceed with sync? [Y/n/details]
```


#### Example



**Code:**
```bash
1. Erstelle Backup-Commit im Template:
   git commit -m "backup: Pre-sync state"

2. Kopiere NEW Dateien:
   cp -r $SOURCE/$FILE $TARGET/$FILE

3. Update UPDATED Dateien:
   cp $SOURCE/$FILE $TARGET/$FILE

4. Schreibe anonymisierte Versionen:
   (transformierte Inhalte aus Phase 4)

5. Überspringe TEMPLATE-ONLY Dateien
```


#### Example



**Code:**
```bash
Vollständiger Audit des GESAMTEN Templates:
- Scanne alle Dateien
- Prüfe auf Leaks
- Validiere Ergebnis
```


#### Example



**Code:**
```bash
[8/8] Post-Sync Validation...

✓ Git-Status: clean
✓ Keine CRITICAL Privacy-Findings
✓ Template-Protected Dateien: unverändert
✓ JSON-Dateien: valid
⚠ 1 MEDIUM Warning (akzeptabel)

Validation: PASSED
```


#### Example



**Code:**
```bash
1. Erstelle Commit im Template:
   git commit -m "sync: Add X new, update Y (DATE)"

2. Update Manifest:
   - last_sync: { date, backup_commit, sync_commit, stats }
   - sync_history: append entry
```


#### Example



**Code:**
```bash
Input:
- Liste der sync'd Dateien (NEW + UPDATED)
- _graph/nodes.json

Prüft diese Pfad-Patterns:
- .claude/agents/*.md → type: agent
- .claude/commands/*.md → type: command
- .claude/skills/*/reference.md → type: skill
- knowledge/patterns/**/*.md → type: pattern
- knowledge/rules/**/*.md → type: rule

Output: Liste von Dateien ohne Graph-Node
```


#### Example



**Code:**
```bash
🔍 ORPHAN DETECTION:
├── Geprüft: 95 Dateien
├── Im Graph: 89
└── Orphans: 6
    ├── .claude/agents/new-agent.md
    ├── .claude/commands/new-cmd.md
    └── knowledge/patterns/new-pattern.md
```


#### Example



**Code:**
```bash
Input: Orphan files list

Für jede Datei:
1. Lese YAML frontmatter (description, domain, capabilities)
2. Leite ab:
   - id: {type}-{kebab-case-name}
   - type: aus Pfad-Pattern
   - name: aus Titel oder Dateiname
   - path: relativer Pfad
   - domain: aus frontmatter oder description
   - description: aus frontmatter

Output: Neue Node-Einträge (JSON Array)
```


#### Example



**Code:**
```bash
🔨 NODE CREATION:
├── agent-new-agent
│   ├── type: agent
│   ├── domain: [automation, workflow]
│   └── description: "..."
└── cmd-new-cmd
    ├── type: command
    └── domain: [utility]
```


#### Example



**Code:**
```bash
Input: Alle Nodes (inkl. neue), edges.json

Inference Rules:
1. command → agent: Wenn Command "Task mit X-agent" enthält
2. agent → template: Wenn Agent auf Template basiert (traits)
3. skill → pattern: Wenn Skill Pattern implementiert
4. command → skill: Wenn Command Skill aufruft

Methoden:
- Datei-Inhalt scannen nach Referenzen
- YAML frontmatter "uses", "based_on"
- Naming-Conventions

Output: Neue Edge-Einträge (JSON Array)
```


#### Example



**Code:**
```bash
🔗 EDGE INFERENCE:
├── cmd-new-cmd → agent-new-agent (uses)
├── agent-new-agent → tpl-specialist (based_on)
└── Neue Edges: 3
```


#### Example



**Code:**
```bash
1. Merge neue Nodes in _graph/nodes.json
   - Sortiere alphabetisch nach ID
   - Update count und generated timestamp

2. Merge neue Edges in _graph/edges.json
   - Dedupliziere (keine Duplikate)
   - Update count

3. Regeneriere Indexes:
   - _graph/index/by-type.json (Nodes nach Type)
   - _graph/index/by-domain.json (Nodes nach Domain-Tags)

4. Update Stats in:
   - README.md: "Knowledge Graph: X nodes, Y edges"
   - SYSTEM-MAP.md: Graph Statistics Sektion
```


#### Example



**Code:**
```bash
📊 GRAPH UPDATE:
├── Nodes: 222 → 228 (+6)
├── Edges: 293 → 296 (+3)
├── by-type.json: regeneriert (14 types)
├── by-domain.json: regeneriert (168 domains)
├── README.md: stats aktualisiert
└── SYSTEM-MAP.md: stats aktualisiert
```


#### Example



**Code:**
```bash
[10/10] Graph Integration...

✓ 6 Orphans erkannt
✓ 6 Nodes erstellt
✓ 3 Edges abgeleitet
✓ Indexes regeneriert
✓ Stats aktualisiert

Graph Integration: COMPLETE
```


#### Example



**Code:**
```bash
Letzter Sync: 2026-01-04 10:45
Backup-Commit: abc1234
Sync-Commit: def5678

Rollback durchführen?
→ git reset --hard abc1234 im Template

[Y/n]
```


#### Example



**Code:**
```bash
SYNC HISTORY (letzte 5):

2026-01-04 10:45  +12 ~8 ✓3  abc1234 → def5678
2026-01-03 14:20  +2 ~3 ✓1   xyz789 → uvw012
2026-01-01 09:00  +15 ~0 ✓0  (initial sync)
```


#### Example



**Code:**
```bash
Template-Pfad nicht konfiguriert.

Wo liegt dein Evolving-Template Repository?
> [User gibt Pfad ein]

Pfad gespeichert.
```


#### Example



**Code:**
```bash
🚨 CRITICAL: API Key gefunden!

Datei: .claude/agents/xyz.md
Zeile 42: sk-xxxxxxx

Sync wird BLOCKIERT.
Bitte entferne den Key aus der Source-Datei.
```


#### Example



**Code:**
```bash
⚠ Uncommitted changes im Template!

Optionen:
  [C] Commit current state first
  [S] Stash and continue
  [A] Abort
```


#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────────┐
│                    /template-sync                        │
└─────────────────────┬───────────────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
┌───────────────────┐    ┌───────────────────┐
│ Template Inventory │    │   Template Diff    │
│      Agent         │    │      Agent         │
└────────┬──────────┘    └────────┬──────────┘
         │                        │
         └──────────┬─────────────┘
                    ▼
         ┌───────────────────┐
         │  Privacy Scanner  │
         │   (pre-sync)      │
         └────────┬──────────┘
                  │
                  ▼ (wenn Findings)
         ┌───────────────────┐
         │ Content Anonymizer│
         └────────┬──────────┘
                  │
                  ▼
         ┌───────────────────┐
         │   Sync Execution  │
         └────────┬──────────┘
                  │
                  ▼
         ┌───────────────────┐
         │  Privacy Scanner  │
         │   (post-sync)     │
         └────────┬──────────┘
                  │
                  ▼
         ┌───────────────────┐
         │ Commit & Manifest │
         └────────┬──────────┘
                  │
                  ▼
         ┌───────────────────┐
         │ Graph Integration │
         │  (Phase 10)       │
         └────────┬──────────┘
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐
   │ Orphan  │ │  Node   │ │  Edge   │
   │ Detect  │ │ Creator │ │ Infer   │
   └────┬────┘ └────┬────┘ └────┬────┘
        └─────────┬─────────────┘
                  ▼
         ┌───────────────────┐
         │ Index & Stats     │
         │ Regeneration      │
         └───────────────────┘
```


#### Example



**Code:**
```bash
User: /template-sync

Claude:
  Lade Manifest...
  Source: /Users/neoforce/Buisiness/Evolving
  Target: /Users/neoforce/Buisiness/Evolving-Template

  [1/8] Template Inventory Agent...
  📦 Agents: 19→23 (+4) | Commands: 34→39 (+5)

  [2/8] Template Diff Agent...
  📊 NEW: 12 | UPDATED: 8 | DIVERGED: 1

  [3/8] Privacy Scanner (pre-sync)...
  🔒 CRITICAL: 0 | HIGH: 3 | MEDIUM: 5

  [4/8] Content Anonymizer...
  🔄 3 Dateien anonymisiert

  [5/8] DIVERGED Review...
  → example.md: [S]ource gewählt

  [6/8] Sync Preview...
  Proceed? [Y]

  [7/8] Syncing...
  ✓ 20 Dateien synchronisiert
  ✓ 3 Dateien anonymisiert

  [8/8] Post-Sync Validation...
  ✓ Template Audit: PASSED

  Commit erstellen? [Y]
  ✓ Commit: sync: Add 12 new, update 8

  ✅ Sync erfolgreich abgeschlossen!
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/template-sync.md`</small>
