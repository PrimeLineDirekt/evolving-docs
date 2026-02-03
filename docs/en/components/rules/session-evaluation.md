---
title: session-evaluation
type: rule
tags: []
lang: en
confidence: 100
---

# session-evaluation


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
"Ich sehe X unbewertete Session(s). Kurze Evaluation? (30 Sek pro Session)"
```


#### Example



**Code:**
```bash
1. Session-File lesen
2. Git Commits + Handoff analysieren
3. 5 Kriterien bewerten (1-5)
4. Gewichteten Score berechnen
5. Experience speichern (MCP: experience_create)
6. Session-File LÖSCHEN (Cleanup)
7. Bei Score < 3.5: Learning-Extraktion anbieten
```


#### Example



**Code:**
```json
{
  "type": "session_eval",
  "summary": "Session 2026-01-08: Score 4.1/5 - Gute Arbeit, fokussiert",
  "tags": ["session", "evaluation", "2026-01"],
  "projects": ["evolving-system"]
}
```


#### Example



**Code:**
```bash
rm knowledge/sessions/session-YYYY-MM-DD-HHMMSS.md
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/rules/session-evaluation.md`</small>
