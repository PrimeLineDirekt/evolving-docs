---
title: file-hygiene-fixer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# file-hygiene-fixer-agent


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




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "findings": [
    {
      "id": "FHF-001",
      "severity": "LOW",
      "type": "duplicate",
      "files": [
        ".claude/rules/old/some-rule.md",
        "knowledge/rules/some-rule.md"
      ],
      "similarity": 95,
      "details": "Nearly identical content at two locations"
    }
  ]
}
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Beide Dateien analysieren
2. Canonical Location bestimmen:
   - Rules → knowledge/rules/
   - Patterns → knowledge/patterns/
   - Commands → .claude/commands/
3. Nicht-canonical entfernen oder → _backup/
4. Symlink oder Redirect erstellen wenn nötig
5. Referenzen updaten
```


#### Example



**Code:**
```bash
| Location A | Location B | Keep |
|------------|------------|------|
| .claude/rules/old/ | knowledge/rules/ | B |
| .claude/backup/ | anywhere | Other |
| _backup/ | anywhere | Other |
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Datei analysieren - kann sie gesplittet werden?
2. Logische Abschnitte identifizieren
3. Option A: In mehrere Dateien splitten
4. Option B: Auslagern in Sub-Ordner
5. Option C: Akzeptieren (manche Files sind groß by design)
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Legacy-Status verifizieren
   - Hat "legacy" im Namen/Pfad?
   - Keine Referenzen mehr?
   - Ersetzt durch neuere Version?
2. In _backup/ verschieben mit Timestamp
3. README in _backup/ updaten
4. Referenzen entfernen/updaten
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Backup-Alter prüfen
2. Retention Policy anwenden:
   - _backup/: 30 Tage, max 5 Versionen
   - _memory/: 7 Tage, max 3 Versionen
   - Andere: 14 Tage, max 3 Versionen
3. Überschüssige löschen
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Prüfen ob Verzeichnis leer ist
2. Prüfen ob es .gitkeep enthält (intentionally empty)
3. Falls wirklich leer und ungenutzt → löschen
4. Falls leer aber gebraucht → .gitkeep hinzufügen
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Naming-Convention prüfen:
   - Agents: {name}-agent.md
   - Commands: {name}.md
   - Skills: {name}.md
2. Umbenennen wenn inkonsistent
3. Referenzen updaten
4. Git rename für History
```


#### Example



**Code:**
```markdown
## File Hygiene Fixes Applied

### Auto-Applied (2)
- [✓] FHF-001: Added .gitkeep to empty _backup/temp/
- [✓] FHF-002: Deleted .claude/commands/.DS_Store

### Individual Approval Required

#### Duplicates (4 pairs)
| # | File A | File B | Action |
|---|--------|--------|--------|
| 1 | .claude/rules/old/ultrathink.md | knowledge/rules/creation/ultrathink.md | Keep B, delete A? [y/n] |
| 2 | knowledge/patterns/react.md | knowledge/patterns/react-pattern.md | Keep pattern.md, delete other? [y/n] |

**User Response**: Approved 1, 2. Skipped 3, 4.
- [✓] FHF-003: Deleted .claude/rules/old/ultrathink.md
- [✓] FHF-004: Deleted knowledge/patterns/react.md (kept react-pattern.md)
- [⊘] FHF-005: Skipped by user
- [⊘] FHF-006: Skipped by user

#### Legacy Archival (3)
| # | File | Reason | Action |
|---|------|--------|--------|
| 1 | _graph/nodes-legacy.json | Superseded by partitioned nodes | Archive? [y/n] |
| 2 | _graph/edges-legacy.json | Superseded by partitioned edges | Archive? [y/n] |
| 3 | .claude/rules/old/deprecated.md | Marked deprecated | Archive? [y/n] |

**User Response**: Approved all 3.
- [✓] FHF-007: Archived nodes-legacy.json → _backup/legacy/
- [✓] FHF-008: Archived edges-legacy.json → _backup/legacy/
- [✓] FHF-009: Archived deprecated.md → _backup/rules/

### Summary
- Auto-fixed: 2
- Duplicates resolved: 2 (2 skipped)
- Legacy archived: 3
- Total freed: 145 KB
```


#### Example



**Code:**
```bash
# Verify no empty dirs (except with .gitkeep)
find . -type d -empty ! -name .git -exec test ! -f {}/.gitkeep \; -print

# Verify no obvious duplicates
find . -name "*.md" -exec md5sum {} \; | sort | uniq -d -w32

# Verify naming conventions
for f in .claude/agents/*.md; do
  [[ $(basename "$f") == *-agent.md ]] || echo "NAMING: $f"
done
```


#### Example



**Code:**
```bash
NEVER touch:
- CLAUDE.md (any location)
- README.md (root)
- .gitignore
- _memory/index.json
- _stats.json
- Any file with "DO NOT DELETE" comment
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/file-hygiene-fixer-agent.md`</small>
