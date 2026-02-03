---
title: lock-methodology-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# lock-methodology-pattern


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Learn → Observe → Check → Keep
  ↓        ↓        ↓       ↓
Context  Hypothese  Test   Record
```


#### Example



**Code:**
```markdown
## Learn
- **Trigger**: {Was hat die Untersuchung gestartet?}
- **Context**: {Relevanter Hintergrund}
- **Known**: {Was wissen wir schon?}
- **Resources**: {Verfügbare Quellen/Tools}
```


#### Example



**Code:**
```markdown
## Observe
- **Hypothesis**: {Testbare Annahme}
- **Observable Indicators**: {Was würden wir sehen wenn wahr?}
- **Expected Pattern**: {Konkretes Muster}
```


#### Example



**Code:**
```markdown
## Check
- **Method**: {Wie wird getestet?}
- **Query/Search**: {Konkrete Abfrage}
- **Constraints**: {Zeit-Limit, Result-Cap}
- **Results**: {Ergebnisse}
```


#### Example



**Code:**
```markdown
## Keep
- **Finding**: {Was wurde entdeckt/gelernt}
- **Outcome**: {Confirmed | Refuted | Inconclusive}
- **Worked**: {Was funktionierte}
- **Didn't Work**: {Was nicht funktionierte}
- **Next Steps**: {Folge-Aktionen}
- **Lessons**: {Lessons Learned}
```


#### Example



**Code:**
```markdown
# Investigation: {Title}

**ID**: INV-{YYYY-NNN}
**Status**: draft | in_progress | completed
**Created**: YYYY-MM-DD
**Related**: [Verknüpfte Investigations]

---

## Learn

**Trigger**: Was hat diese Untersuchung ausgelöst?

**Context**:
- Relevanter Hintergrund
- Bekannte Informationen

**Resources**:
- Verfügbare Datenquellen
- Tools und Zugriffe

---

## Observe

**Hypothesis**:
> Testbare Annahme in einem Satz

**Observable Indicators**:
- Was wir sehen sollten wenn die Hypothese stimmt
- Konkrete Patterns/Verhalten

---

## Check

**Method**: Beschreibung des Test-Ansatzes

**Query/Search**:
```


#### Example



**Code:**
```bash

**Constraints**:
- Zeitfenster: {z.B. letzte 7 Tage}
- Result-Cap: {z.B. max 100 Ergebnisse}

**Results**:
{Ergebnisse der Untersuchung}

---

## Keep

**Outcome**: ✓ Confirmed | ✗ Refuted | ○ Inconclusive

**Finding**:
{Was wurde entdeckt oder gelernt}

**What Worked**:
- {Erfolgreicher Ansatz 1}
- {Erfolgreicher Ansatz 2}

**What Didn't Work**:
- {Fehlgeschlagener Ansatz 1}

**Lessons Learned**:
- {Erkenntnis für zukünftige Untersuchungen}

**Next Steps**:
- [ ] {Folge-Aktion 1}
- [ ] {Folge-Aktion 2}
```


#### Example



**Code:**
```bash
Tier 1: CLI-basierte Suche (wenn verfügbar)
        athf hunt search "keyword"
        athf hunt list --category X

Tier 2: Grep-basierte Suche (Fallback)
        grep -r "pattern" investigations/

Tier 3: YAML Frontmatter Parsing
        Strukturierte Metadaten für Filter
```


#### Example



**Code:**
```bash
investigations/
├── INV-2025-001.md         # Hypothese + Ergebnisse
├── INV-2025-001_queries/   # Queries/Code
└── INV-2025-001_runs/      # Datierte Ausführungen
    ├── 2025-12-14.md
    └── 2025-12-16.md
```


#### Example



**Code:**
```markdown
# investigations/ Ordner

Ähnlich wie hunts/ in ATHF:
- YAML Frontmatter für Metadaten
- LOCK-Struktur für Inhalt
- Datierte Iterationen für Refinement
- Verknüpfung mit ideas/ und knowledge/
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/patterns/lock-methodology-pattern.md`</small>
