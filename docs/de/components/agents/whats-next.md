---
title: whats-next
type: agent
tags: []
lang: en
confidence: 100
---

# whats-next


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
```bash
EVOLVING_ROOT = /Users/neoforce/Buisiness/Evolving
```


#### Example



**Code:**
```bash
1. Memory lesen (_memory/index.json)
2. Projekt-Memory lesen (_memory/projects/{active}.json)
3. Plan prüfen (falls active_plan gesetzt)
4. Git-Status für geänderte Files
5. Handoff-File schreiben (_handoffs/YYYY-MM-DD-{topic}.md)
6. Memory updaten (index.json + projects/{x}.json)
7. FERTIG - Nur Pfad zurückgeben
```


#### Example



**Code:**
```bash
# Lese aktives Projekt
cat {EVOLVING_ROOT}/_memory/index.json
```


#### Example



**Code:**
```bash
cat {EVOLVING_ROOT}/_memory/projects/{active_project}.json
```


#### Example



**Code:**
```bash
# Geänderte Files in dieser Session
git status --short
git diff --name-only HEAD~5 2>/dev/null || git diff --name-only
```


#### Example



**Code:**
```markdown
# Session Handoff: {TOPIC}

**Erstellt**: {DATUM} {UHRZEIT}
**Session-Dauer**: ~{geschätzt}
**Kontext-Nutzung**: {hoch/mittel/niedrig}

---

## 🎯 PROJECT CONTEXT

| Feld | Wert |
|------|------|
| **Projekt** | {projekt-id} - {kurzer Name} |
| **Modul/Bereich** | {src/ordner/ oder Thema} |
| **Branch** | {branch-name} |
| **Ziel/OKR** | {Konkretes Ziel dieser Arbeit} |
| **Blockers** | {Keine / Liste} |

### Warum diese Arbeit?
{1-2 Sätze: Business-Kontext}

---

## 📋 AKTIVER PLAN (falls vorhanden)

| Feld | Wert |
|------|------|
| **Plan-Datei** | `{pfad/zum/plan.md}` |
| **Plan-Titel** | {Titel aus Plan} |
| **Complete** | {Y} Phasen |
| **In Progress** | {Z} Phasen |

### Phasen-Übersicht
```


#### Example



**Code:**
```bash

---

## Was wurde erreicht

### Abgeschlossen
- [x] {Task 1}
- [x] {Task 2}

### Erstellt/Geändert
| Datei | Aktion | Beschreibung |
|-------|--------|--------------|
| {path} | Created/Modified | {was} |

### Entscheidungen
| Entscheidung | Alternativen | Begründung |
|--------------|--------------|------------|
| {Was gewählt} | {Optionen} | {Warum} |

---

## Offene Punkte

### Noch zu tun
| Task | Priorität | Effort |
|------|-----------|--------|
| {Task} | HIGH/MED/LOW | ~{zeit} |

### Offene Fragen
- [ ] {Frage}? → Optionen: A, B, C

### Bekannte Risiken
- {Issue}: {Impact + Workaround}

---

## 🔍 EMPFOHLENE REVIEWS (falls Code-Arbeit)

| Agent | Priorität | Grund |
|-------|-----------|-------|
| `feature-dev:code-reviewer` | PFLICHT | {X} Files geändert |
| {weitere} | EMPFOHLEN | {Grund} |

---

## 🚀 Nächste Session

### CONTEXT LOADING ORDER

**0. PLAN ZUERST (falls vorhanden):**
- `{plan-pfad}` - Gesamtplan verstehen

**1. DANN dieses Handoff:**
- `{kritische-datei}` - {warum}

### Empfohlener Einstieg
```


#### Example



**Code:**
```bash

### Sofort-Aktionen
1. {Erste Aktion} - {Ergebnis}
2. {Zweite Aktion} - {Ergebnis}

### Stop-Kriterien
- [ ] {Wann ist DONE?}

---

## Quick Summary

```


#### Example



**Code:**
```python
# _memory/projects/{active_project}.json
# Update phases-Objekt:
{
  "active_plan": "{plan-pfad}",  # Falls Plan existiert
  "phases": {
    "X.1": "complete",      # Bestehendes beibehalten
    "X.2": "in_progress"    # Diese Session
  }
}
```


#### Example



**Code:**
```python
# _memory/index.json
{
  "last_updated": "JETZT",
  "active_context": {
    "project": "{projekt}",
    "focus": "{aktueller Stand}",
    "active_plan": "{plan-pfad}" oder null
  },
  "recent_sessions": [
    {
      "date": "HEUTE",
      "project": "{projekt}",
      "summary": "{kurz}",
      "handoff": "_handoffs/{filename}.md"
    }
    // ... vorherige (max 20)
  ]
}
```


#### Example



**Code:**
```bash
HANDOFF_CREATED: _handoffs/YYYY-MM-DD-{topic}.md
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/whats-next.md`</small>
