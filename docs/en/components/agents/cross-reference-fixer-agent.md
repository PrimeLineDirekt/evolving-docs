---
title: cross-reference-fixer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# cross-reference-fixer-agent


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
      "id": "CRF-001",
      "severity": "HIGH",
      "type": "count_mismatch",
      "source": "COMMANDS.md",
      "expected": 63,
      "actual": 58,
      "details": "Command count in header doesn't match actual commands"
    }
  ]
}
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Tatsächliche Counts ermitteln:
   - Commands: ls .claude/commands/*.md | wc -l
   - Agents: ls .claude/agents/*.md | wc -l
   - Skills: ls .claude/skills/*.md | wc -l
   - Patterns: ls knowledge/patterns/*.md | wc -l

2. _stats.json als Single Source of Truth aktualisieren

3. Alle Master-Docs mit korrekten Counts updaten:
   - COMMANDS.md Header
   - README.md Stats-Tabelle
   - SYSTEM-MAP.md Inventar
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Fehlende Command-Datei lesen
2. Metadata extrahieren (description, argument-hint)
3. Entry in korrektem Format erstellen
4. An passende Stelle einfügen (alphabetisch oder nach Kategorie)
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Prüfen ob Entry wirklich orphan (File existiert nicht)
2. Entry aus Dokument entfernen
3. Count aktualisieren
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Referenziertes Target identifizieren
2. Alternativen suchen (renamed? moved?)
3. Option A: Referenz updaten auf neues Target
4. Option B: Referenz entfernen mit Kommentar
```


#### Example



**Code:**
```markdown
## Cross-Reference Fixes Applied

### Auto-Applied (5)
- [✓] CRF-001: _stats.json commands 58→63
- [✓] CRF-002: COMMANDS.md header count fixed
- [✓] CRF-003: README.md stats table updated
- [✓] CRF-004: SYSTEM-MAP.md inventar count fixed
- [✓] CRF-005: Alphabetic sort in COMMANDS.md

### Batch 1 (Approved: 4 of 5)
- [✓] CRF-006: Added /evolving-audit to COMMANDS.md
- [✓] CRF-007: Added /evolving-audit to detection-index.json
- [✓] CRF-008: Added /audit-fix to detection-index.json
- [✓] CRF-009: Removed orphan /old-command
- [⊘] CRF-010: Skipped by user

### Individual Approval (2)
- [✓] CRF-011: Fixed reference Agent-A → Agent-B (renamed)
- [✗] CRF-012: Could not fix broken ref (target unknown)

### Summary
- Applied: 10
- Skipped: 1
- Failed: 1
```


#### Example



**Code:**
```bash
# Verify counts match
actual_commands=$(ls .claude/commands/*.md | wc -l)
stats_commands=$(jq '.commands' _stats.json)
[ "$actual_commands" -eq "$stats_commands" ] || echo "MISMATCH!"

# Verify no orphans
for cmd in $(jq -r '.commands[].id' .claude/detection-index.json); do
  [ -f ".claude/commands/$cmd.md" ] || echo "ORPHAN: $cmd"
done
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/cross-reference-fixer-agent.md`</small>
