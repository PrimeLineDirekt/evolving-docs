---
title: README
type: prompt
tags: ["[prompts", " patterns", " best-practices", " inspiration", " reusable]"]
lang: en
confidence: 100
---

# README


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Prompt |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | prompts || **Created** | 2024-11-22 |</div>

<div class="component-tags">
<span class="tag tag-[prompts">[prompts</span>
<span class="tag tag--patterns"> patterns</span>
<span class="tag tag--best-practices"> best-practices</span>
<span class="tag tag--inspiration"> inspiration</span>
<span class="tag tag--reusable]"> reusable]</span>
</div>

## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Beispiel aus profil-analyse.md:

STRUKTUR-PATTERN:
- Identity Establishment ("Du bist...")
- Core Capabilities (Bulletpoints)
- Input Specification (Was bekommst du)
- Output Format (Strukturierte Sections)
- Quality Criteria (Self-Validation)

→ Übertrage auf deine Domain!
```


#### Example



**Code:**
```markdown
GOOD: "Du bist ein Senior Tax Advisor mit 20+ Jahren Erfahrung in internationaler Steuerplanung..."
BAD:  "Du bist ein Berater."
```


#### Example



**Code:**
```markdown
GOOD:
AUSGABE-FORMAT:
1. EXECUTIVE SUMMARY (200 Wörter)
2. DETAILLIERTE ANALYSE
3. ACTION ITEMS (Priorisiert)

BAD: "Erstelle eine Analyse."
```


#### Example



**Code:**
```markdown
GOOD: "Analysiere §6 AStG Wegzugsbesteuerung, DBA-Implikationen..."
BAD:  "Schau dir Steuergesetze an."
```


#### Example



**Code:**
```markdown
GOOD:
QUALITÄTS-CHECKS:
✓ Alle kritischen Punkte adressiert
✓ Keine Widersprüche
✓ Mindestens 3 konkrete Action Items

BAD: (keine Quality Gates)
```


#### Example



**Code:**
```markdown
GOOD:
INPUT: 126-Felder User-Profil mit [spezifische Felder]
DEPENDENCIES: Nutze Output von [other_agent]

BAD: (implizite Annahmen)
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/prompts/README.md`</small>
