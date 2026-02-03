---
title: explore-index-check
type: rule
tags: []
lang: en
confidence: 100
---

# explore-index-check


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
User fragt etwas Exploratives
         │
         ▼
┌─────────────────────────────────┐
│ 1. INDEX LADEN                  │
│    knowledge/explorations/      │
│    _index.json                  │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 2. KEYWORD MATCH                │
│    User-Keywords gegen          │
│    entry.keywords prüfen        │
└──────────────┬──────────────────┘
               │
         Match gefunden?
         /           \
       JA            NEIN
        │              │
        ▼              ▼
┌─────────────┐  ┌─────────────┐
│ USER FRAGEN │  │ EXPLORE     │
│             │  │ STARTEN     │
│ "Dazu gibt  │  │             │
│ es Findings │  │ (normal)    │
│ vom [date]" │  │             │
└──────┬──────┘  └─────────────┘
       │
       ▼
   User will...
   /         \
 Laden     Neu erkunden
   │           │
   ▼           ▼
 READ       EXPLORE
 Finding    (neu)
```


#### Example



**Code:**
```python
Task(subagent_type="Explore", prompt="...")
```


#### Example



**Code:**
```python
# 1. Index lesen
Read("knowledge/explorations/_index.json")

# 2. Keywords extrahieren aus User-Anfrage
keywords = ["hooks", "subagent", "routing"]  # Beispiel

# 3. Match suchen
for entry in index["entries"]:
    if any(kw in entry["keywords"] for kw in keywords):
        # Match! User fragen
        pass

# 4. Bei Match: "Ich habe Findings vom [date] zu diesem Thema. Laden oder neu erkunden?"
```


#### Example



**Code:**
```bash
User: "Wie funktioniert das Hook-System?"

Claude (VORHER - falsch):
  → Startet sofort Explore-Agent

Claude (JETZT - richtig):
  → Liest _index.json
  → Findet: {"date": "2026-01-09", "keywords": ["hook", "system", "subagent"], ...}
  → "Ich habe Findings vom 2026-01-09 zu Hooks. Soll ich die laden oder neu erkunden?"
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/rules/explore-index-check.md`</small>
