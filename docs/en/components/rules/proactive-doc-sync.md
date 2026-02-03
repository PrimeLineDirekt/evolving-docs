---
title: proactive-doc-sync
type: rule
tags: []
lang: en
confidence: 100
---

# proactive-doc-sync


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Hook meldet: "SYNC CHECK: {type}"
                │
                ▼
┌─────────────────────────────────────┐
│ Ist die Änderung dokumentationswürdig? │
│                                      │
│ JA wenn:                             │
│ - Neue Komponente (Command, Agent,   │
│   Template, Skill, Pattern, etc.)    │
│ - Geänderte Counts/Stats             │
│ - Strukturelle Reorganisation        │
│                                      │
│ NEIN wenn:                           │
│ - Nur interner Bugfix                │
│ - Keine öffentliche API-Änderung     │
│ - Rein kosmetische Änderungen        │
└──────────────────┬──────────────────┘
                   │
                   ▼ JA
┌─────────────────────────────────────┐
│ Automatisch aktualisieren:           │
│                                      │
│ 1. Betroffene Master Docs lesen      │
│ 2. Counts/Stats prüfen               │
│ 3. Neue Einträge hinzufügen          │
│ 4. In EINEM Commit zusammenfassen    │
│ 5. User informieren was getan wurde  │
└─────────────────────────────────────┘
```


#### Example



**Code:**
```bash
[Ich erstelle .claude/commands/new-command.md]

Hook: "⚠️ SYNC CHECK: Command - new-command.md"

Ich (ohne User-Nachfrage):
1. Lese COMMANDS.md → Count ist 50
2. Füge /new-command Entry hinzu
3. Update Count auf 51
4. Update SYSTEM-MAP.md Commands-Tabelle
5. Update README.md Count
6. Update detection-index.json
7. Commit: "docs: Add /new-command to master documents"
8. Sage: "Master Docs aktualisiert für /new-command"
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/rules/proactive-doc-sync.md`</small>
