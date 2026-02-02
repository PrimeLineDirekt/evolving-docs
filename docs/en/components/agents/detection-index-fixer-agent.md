---
title: detection-index-fixer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# detection-index-fixer-agent


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
      "id": "DIF-001",
      "severity": "MEDIUM",
      "type": "missing_command",
      "command": "evolving-audit",
      "file": ".claude/commands/evolving-audit.md",
      "details": "Command exists but not in detection-index.json"
    }
  ]
}
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Command-Datei lesen
2. Metadata extrahieren (description, argument-hint)
3. Detection-Entry generieren:
   - id: Filename ohne .md
   - keywords: Aus description + name extrahieren
   - confidence: 80 (default)
   - anti_keywords: Falls offensichtlich
4. Entry zu detection-index.json hinzufügen
5. Alphabetisch sortieren
```


#### Example



**Code:**
```python
def extract_keywords(name, description):
    keywords = [name.replace("-", " ")]
    # Split camelCase/kebab-case
    keywords += name.split("-")
    # Wichtige Wörter aus Description
    keywords += extract_nouns(description)
    return dedupe(keywords)
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Prüfen ob Command wirklich fehlt
2. Prüfen ob umbenannt (ähnlicher Name?)
3. Entry aus Index entfernen
4. _stats.json Count aktualisieren
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Duplikate identifizieren
2. Spezifischeren Command bestimmen
3. Option A: Keyword nur bei spezifischerem belassen
4. Option B: Keyword bei beiden, aber Confidence anpassen
5. Anti-Keywords für Disambiguation hinzufügen
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Keywords analysieren - sind sie spezifisch genug?
2. Bessere Keywords hinzufügen
3. Anti-Keywords für Abgrenzung
4. Confidence erhöhen wenn verbessert
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Ähnliche Commands identifizieren
2. Unterscheidende Anti-Keywords ableiten
3. Zu beiden Commands hinzufügen
```


#### Example



**Code:**
```markdown
Fix-Prozess:
1. Vergleiche detection-index mit context-router
2. Fehlende Routes in context-router ergänzen
3. Veraltete Routes entfernen
```


#### Example



**Code:**
```markdown
## Detection Index Fixes Applied

### Auto-Applied (2)
- [✓] DIF-001: Sorted detection-index.json alphabetically
- [✓] DIF-002: Updated _stats.json (detection_entries: 47→52)

### Batch 1: Missing Commands (Approved: 5 of 5)
- [✓] DIF-003: Added /evolving-audit
  - keywords: ["evolving", "audit", "system", "check", "integrity"]
  - confidence: 85
- [✓] DIF-004: Added /cross-reference-checker
  - keywords: ["cross", "reference", "sync", "docs", "verify"]
  - confidence: 80
- [✓] DIF-005: Added /graph-validator
- [✓] DIF-006: Added /memory-validator
- [✓] DIF-007: Added /hygiene-auditor

### Batch 2: Orphan Removal (Approved: 2 of 2)
- [✓] DIF-008: Removed /old-deprecated-command
- [✓] DIF-009: Removed /legacy-feature

### Individual Approval (1)
- [✓] DIF-010: Added anti_keywords to /idea-new vs /idea-work
  - /idea-new: anti_keywords: ["work", "session", "sparring"]
  - /idea-work: anti_keywords: ["new", "create", "add"]

### Summary
- Added: 5 new entries
- Removed: 2 orphans
- Updated: 1 disambiguation
```


#### Example



**Code:**
```bash
# Verify all commands indexed
for cmd in .claude/commands/*.md; do
  name=$(basename "$cmd" .md)
  grep -q "\"id\": \"$name\"" .claude/detection-index.json || echo "MISSING: $name"
done

# Verify no orphans
for id in $(jq -r '.commands[].id' .claude/detection-index.json); do
  [ -f ".claude/commands/$id.md" ] || echo "ORPHAN: $id"
done

# Verify unique keywords
jq -r '.commands[].keywords[]' .claude/detection-index.json | sort | uniq -d
```


#### Example



**Code:**
```json
{
  "id": "command-name",
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "anti_keywords": ["avoid1", "avoid2"],
  "confidence": 80,
  "context": "optional description",
  "category": "audit|workflow|utility|creation"
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/detection-index-fixer-agent.md`</small>
