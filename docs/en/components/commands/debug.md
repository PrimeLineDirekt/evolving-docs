---
title: debug
type: command
tags: []
lang: en
confidence: 100
---

# debug


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

Systematisches Debugging mit Hypothesen und Evidence Gathering


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Was debuggen wir heute?

Bitte beschreibe:
1. **Symptom**: Was passiert (nicht was du erwartest)?
2. **Kontext**: Wo/Wann tritt es auf?
3. **Reproduzierbar?**: Immer / Manchmal / Einmal
```


#### Example



**Code:**
```markdown
## Bug Report

**Symptom**: {was passiert}
**Expected**: {was sollte passieren}
**Kontext**: {wo/wann}
**Reproduzierbar**: {ja/nein/manchmal}
**Seit wann**: {wenn bekannt}
**Was hat sich geändert**: {wenn bekannt}
```


#### Example



**Code:**
```markdown
## Hypothesen (nach Wahrscheinlichkeit)

| # | Hypothese | Wahrscheinlichkeit | Test |
|---|-----------|-------------------|------|
| 1 | {hypothese} | Hoch | {wie testen} |
| 2 | {hypothese} | Mittel | {wie testen} |
| 3 | {hypothese} | Niedrig | {wie testen} |
```


#### Example



**Code:**
```python
# 1. Logs prüfen
logs = Bash("tail -100 {relevant_log}")
errors = Grep(pattern="error|exception|failed", path="{log_path}")

# 2. Code untersuchen
relevant_code = Read("{suspected_file}")
similar_patterns = Grep(pattern="{pattern}", path=".")

# 3. State prüfen
config = Read("{config_file}")
env = Bash("env | grep {relevant}")

# 4. Reproduzieren
test_result = Bash("{command_to_reproduce}")
```


#### Example



**Code:**
```markdown
## Evidence für Hypothese {N}

| Evidence | Gefunden | Unterstützt Hypothese? |
|----------|----------|----------------------|
| {was gesucht} | {ja/nein} | {ja/nein/neutral} |
| Logs zeigen X | Ja | Ja |
| Config ist Y | Ja | Nein |
```


#### Example



**Code:**
```markdown
## Root Cause gefunden

**Problem**: {konkrete Ursache}
**Warum**: {Erklärung}
**Beweise**: {Evidence die es bestätigt}

### Affected Components
- {Component 1}: {wie betroffen}
- {Component 2}: {wie betroffen}
```


#### Example



**Code:**
```markdown
## Erweiterte Analyse nötig

Bisherige Hypothesen ausgeschlossen:
- {Hypothese 1}: {warum ausgeschlossen}
- {Hypothese 2}: {warum ausgeschlossen}

Nächste Schritte:
1. Mehr Kontext sammeln
2. Isolation Testing
3. Bisection (wenn möglich)
```


#### Example



**Code:**
```markdown
## Lösungsoptionen

| Option | Aufwand | Risiko | Empfehlung |
|--------|---------|--------|------------|
| {Fix 1} | Niedrig | Niedrig | Empfohlen |
| {Fix 2} | Mittel | Niedrig | Alternative |
| {Workaround} | Minimal | - | Temporär |
```


#### Example



**Code:**
```bash
⚠️ Ich werde folgende Änderungen machen:

Datei: {path}
Änderung: {was}
Grund: {warum}

Fortfahren? (ja/nein)
```


#### Example



**Code:**
```markdown
## Bug Resolution: {TITLE}

**Datum**: {heute}
**Symptom**: {kurz}
**Root Cause**: {kurz}
**Fix**: {was geändert}
**Dateien**: {welche}

### Lessons Learned
- {Was können wir daraus lernen?}

### Prevention
- {Wie verhindern wir ähnliche Bugs?}
```


#### Example



**Code:**
```bash
# Bei "funktionierte mal"
git bisect start
git bisect bad HEAD
git bisect good {known_good_commit}
# Git führt durch die Commits
```


#### Example



**Code:**
```python
# Strategisch platzierte Logs
print(f"DEBUG: {variable=}")
print(f"DEBUG: Reached checkpoint {n}")
```


#### Example



**Code:**
```bash
# Was hat sich geändert?
git diff {last_working}..HEAD
git log --oneline {last_working}..HEAD
```


#### Example



**Code:**
```markdown
## Debug Summary

**Problem**: {1 Satz}
**Root Cause**: {1 Satz}
**Fix**: {was gemacht}
**Status**: {Gelöst / Workaround / Offen}

**Zeit investiert**: ~{minuten}
**Dateien geändert**: {liste}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/debug.md`</small>
