---
title: knowledge-refresh
type: command
tags: []
lang: en
confidence: 100
---

# knowledge-refresh


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




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Lade alle Learnings aus knowledge/learnings/
Filter nach:
  - refresh_category (wenn --category)
  - last_validated > Intervall
  - valid_until nicht abgelaufen
```


#### Example



**Code:**
```bash
Für jedes Learning (max 5 pro Session):
  1. Prüfe Aktualität via WebSearch
  2. Vergleiche mit aktuellem Stand
  3. Klassifiziere: aktuell | geändert | deprecated
```


#### Example



**Code:**
```bash
aktuell:
  → last_validated = heute

geändert:
  → Inhalt aktualisieren
  → last_validated = heute
  → change_history erweitern

deprecated:
  → valid_until = heute
  → deprecation_reason setzen
  → Alternative dokumentieren
```


#### Example



**Code:**
```markdown
## Knowledge Refresh Report

**Geprüft**: 5 Learnings
**Aktuell**: 4
**Aktualisiert**: 1
**Deprecated**: 0

### Aktualisiert
- **claude-code-hooks**: Neue Hook-Typen hinzugefügt
  - Alt: 3 Hook-Typen
  - Neu: 5 Hook-Typen

### Nächste Refresh-Kandidaten
- react-server-components (in 5 Tagen fällig)
- typescript-5-features (in 12 Tagen fällig)
```


#### Example



**Code:**
```bash
/knowledge-refresh
→ Prüft stale Learnings (Standard: 5)

/knowledge-refresh --category=claude-code
→ Nur Claude Code Learnings

/knowledge-refresh --all --limit=10
→ Alle Kategorien, max 10 Learnings
```


#### Example



**Code:**
```yaml
---
title: Feature X Learnings
created: 2026-01-01
last_validated: 2026-01-03
valid_until: null
refresh_category: claude-code
confidence: 85
change_history:
  - "2026-01-03: Feature Y hinzugefügt"
---
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/knowledge-refresh.md`</small>
