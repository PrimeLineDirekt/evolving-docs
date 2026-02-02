---
title: update-check
type: command
tags: []
lang: en
confidence: 100
---

# update-check


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
Lies _memory/system-updates.json
→ known_features
→ last_check
→ update_history
```


#### Example



**Code:**
```bash
Queries (max 3):
1. "Claude Code changelog 2026 new features"
2. "MCP protocol updates 2026"
3. "Anthropic Claude model updates 2026"
```


#### Example



**Code:**
```bash
Für jeden Fund:
  - Ist das Feature bereits in known_features?
  - Ist es neu?
  - Ist es relevant für unser System?
```


#### Example



**Code:**
```bash
Bei neuen relevanten Features:
  1. Learning erstellen in knowledge/learnings/
  2. known_features aktualisieren
  3. update_history erweitern
```


#### Example



**Code:**
```markdown
## Update Check Report

**Letzte Prüfung**: 2026-01-03
**Neue Features gefunden**: 2
**Integriert**: 1
**Übersprungen**: 1 (nicht relevant)

### Neu integriert
- **Claude Code Hooks v2**: Neue Hook-Typen für ...
  → Learning erstellt: claude-code-hooks-v2.md

### Übersprungen
- **Feature X**: Nicht relevant für unser Use Case
```


#### Example



**Code:**
```bash
/update-check
→ Standard-Check, nur wenn > 7 Tage

/update-check --force
→ Sofortiger Check

/update-check --category=claude-code
→ Nur Claude Code Updates
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/update-check.md`</small>
