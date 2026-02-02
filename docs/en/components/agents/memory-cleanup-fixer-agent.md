---
title: memory-cleanup-fixer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# memory-cleanup-fixer-agent


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
      "id": "MCF-001",
      "severity": "LOW",
      "type": "stale_backup",
      "file": "_memory/projects/evolving-system.json.backup_20260101",
      "age_days": 15,
      "details": "Backup older than 7 days"
    }
  ]
}
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Alle Backup-Dateien älter als 7 Tage identifizieren
2. Retention Policy anwenden:
   - Behalte max 3 Backups pro Original-File
   - Lösche alle > 7 Tage
3. Löschung ausführen
```


#### Example



**Code:**
```bash
# Auto-Cleanup Command
find _memory -name "*.backup_*" -mtime +7 -delete
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Progress-Array lesen
2. Letzte 10 Entries behalten
3. Ältere in separates Archiv verschieben:
   - _memory/archives/progress-{project}-{date}.json
4. Project-File mit gekürztem Array speichern
```


#### Example



**Code:**
```markdown
Fix-Prozess für häufige Violations:

a) Missing required field:
   - date: Aktuelles Datum einfügen
   - action: "Unknown action" als Placeholder
   - result: "No result documented"

b) Invalid JSON:
   - Backup erstellen
   - JSON-Syntax-Fehler korrigieren
   - Validieren

c) Wrong type:
   - progress: [] wenn nicht Array
   - failures: [] wenn nicht Array
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Experiences mit valid_until < heute identifizieren
2. Decay-Factor auf 0 setzen (statt löschen)
3. In Archiv verschieben nach 30 Tagen Ablauf
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Referenz auf nicht-existente Experience identifizieren
2. Referenz aus Index/Project entfernen
3. Index neu generieren
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Duplikate identifizieren (gleiche date + action)
2. Neuere/vollständigere Version behalten
3. Duplikat entfernen
```


#### Example



**Code:**
```markdown
## Memory Cleanup Fixes Applied

### Stale Backups Deleted (53)
- [✓] evolving-system.json.backup_20260101 (15 days old)
- [✓] evolving-system.json.backup_20260102 (14 days old)
- ... (51 more)

### Progress Trimmed (2 projects)
- [✓] evolving-system.json: 47 → 10 entries
  - Archived to: _memory/archives/progress-evolving-2026-01-01.json
- [✓] auswanderungs-ki.json: 23 → 10 entries
  - Archived to: _memory/archives/progress-auswanderungs-2026-01-01.json

### Expired Experiences Archived (3)
- [✓] exp-2025-047 → _memory/archives/expired/
- [✓] exp-2025-089 → _memory/archives/expired/
- [✓] exp-2025-102 → _memory/archives/expired/

### Schema Fixes (1)
- [✓] MCF-015: Added missing 'date' field to progress entry

### Summary
- Deleted: 53 backup files (freed 2.3 MB)
- Trimmed: 60 progress entries archived
- Archived: 3 expired experiences
- Schema fixes: 1
```


#### Example



**Code:**
```bash
# Verify no stale backups
stale=$(find _memory -name "*.backup_*" -mtime +7 | wc -l)
[ "$stale" -eq 0 ] || echo "STALE BACKUPS: $stale"

# Verify progress length
for f in _memory/projects/*.json; do
  len=$(jq '.progress | length' "$f")
  [ "$len" -le 10 ] || echo "OVERFLOW: $f ($len entries)"
done

# Verify JSON validity
for f in _memory/**/*.json; do
  jq . "$f" > /dev/null 2>&1 || echo "INVALID JSON: $f"
done
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/memory-cleanup-fixer-agent.md`</small>
