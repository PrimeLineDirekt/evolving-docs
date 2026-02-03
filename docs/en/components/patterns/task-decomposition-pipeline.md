---
title: task-decomposition-pipeline
type: pattern
tags: ["[multi-agent", " autonomous", " research", " planning", " execution]"]
lang: en
confidence: 100
---

# task-decomposition-pipeline


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns || **Created** | 2024-12-09 |</div>

<div class="component-tags">
<span class="tag tag-[multi-agent">[multi-agent</span>
<span class="tag tag--autonomous"> autonomous</span>
<span class="tag tag--research"> research</span>
<span class="tag tag--planning"> planning</span>
<span class="tag tag--execution]"> execution]</span>
</div>

## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────────────────┐
│                         User Query                              │
│     "Vergleiche Steuern in Portugal vs Zypern für Freelancer"   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 1: PLANNER                            │
│                                                                 │
│  Input: User Query                                              │
│  Output: Liste von High-Level Tasks                             │
│                                                                 │
│  Beispiel-Output:                                               │
│  ├── Task 1: Portugal Steuersystem für Freelancer recherchieren │
│  ├── Task 2: Zypern Steuersystem für Freelancer recherchieren   │
│  ├── Task 3: Konkrete Steuerberechnung für beide Länder         │
│  └── Task 4: Vergleich erstellen mit Empfehlung                 │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 2: EXECUTOR                            │
│                                                                 │
│  Für jeden Task:                                                │
│  1. Subtasks identifizieren (welche Tools/Quellen?)             │
│  2. Tools aufrufen und Daten sammeln                            │
│  3. Ergebnisse speichern (Context Management)                   │
│  4. Validieren ob vollständig                                   │
│                                                                 │
│  Task 1 → Subtasks:                                             │
│  ├── Knowledge Base: "Portugal NHR Regime"                      │
│  ├── Tool: get_tax_info("Portugal", "freelancer")               │
│  └── Tool: calculate_tax("Portugal", income=80000)              │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PHASE 3: SYNTHESIZER                          │
│                                                                 │
│  Input: Alle gesammelten Daten aus Phase 2                      │
│  Output: Strukturierte, fundierte Antwort                       │
│                                                                 │
│  - Fasst alle Recherche-Ergebnisse zusammen                     │
│  - Erstellt Vergleichstabellen                                  │
│  - Gibt konkrete Empfehlung mit Begründung                      │
│  - Nennt nächste Schritte                                       │
└─────────────────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```bash
Input: "Vergleiche Steuern Portugal vs Zypern für 80k Freelancer"

Planner Output:
{
  "tasks": [
    {"id": 1, "description": "Portugal Steuerregime für Freelancer analysieren"},
    {"id": 2, "description": "Zypern Steuerregime für Freelancer analysieren"},
    {"id": 3, "description": "Steuerberechnung für 80.000€ in beiden Ländern"},
    {"id": 4, "description": "Vergleichsmatrix erstellen mit Empfehlung"}
  ]
}
```


#### Example



**Code:**
```bash
Task 1: "Portugal Steuerregime für Freelancer analysieren"

Executor identifiziert Subtasks:
├── Subtask 1.1: Knowledge Base durchsuchen → "NHR Regime Details"
├── Subtask 1.2: Aktuelle Steuersätze holen → 20% flat rate
├── Subtask 1.3: Besonderheiten für Freelancer → keine Sozialabgaben-Pflicht
└── Subtask 1.4: Aufenthaltsbedingungen → 183 Tage Regel

Ergebnisse werden gespeichert:
.context/query_abc123/
├── task1_subtask1_kb_result.json
├── task1_subtask2_tax_rates.json
├── task1_subtask3_freelancer_rules.json
└── task1_subtask4_residency.json
```


#### Example



**Code:**
```bash
Synthesizer lädt alle relevanten Contexts und erstellt:

## Steuervergleich: Portugal vs Zypern (Freelancer, 80.000€)

### Portugal (NHR Regime)
- Steuersatz: 20% flat
- Steuer bei 80k: 16.000€
- Besonderheiten: 10 Jahre gültig, keine Sozialabgaben-Pflicht
- Aufenthalt: min. 183 Tage/Jahr

### Zypern
- Steuersatz: 12.5% Corporate
- Steuer bei 80k: 10.000€ (als Ltd)
- Besonderheiten: Non-Dom Status, 60 Tage Regel möglich
- Aufenthalt: Flexibler

### Empfehlung
Zypern bietet 6.000€/Jahr Ersparnis, aber erfordert Ltd-Gründung...

### Nächste Schritte
1. ...
2. ...
```


#### Example



**Code:**
```bash
User: "Wo zahle ich als Freelancer mit 100k€ am wenigsten Steuern in Europa?"

KI: "Es gibt mehrere Optionen wie Portugal, Zypern, Malta..."
→ Oberflächlich, keine konkreten Zahlen, keine Empfehlung
```


#### Example



**Code:**
```bash
User: "Wo zahle ich als Freelancer mit 100k€ am wenigsten Steuern in Europa?"

PLANNER:
├── Task 1: Top 5 steuerfreundliche EU-Länder für Freelancer identifizieren
├── Task 2: Für jedes Land konkrete Steuerberechnung
├── Task 3: Aufenthaltsbedingungen und Komplexität bewerten
└── Task 4: Ranking erstellen mit personalisierter Empfehlung

EXECUTOR:
├── Recherchiert jedes Land systematisch
├── Berechnet konkrete Steuerlast
├── Prüft Aufenthaltsbedingungen
└── Speichert alle Daten

SYNTHESIZER:
├── Erstellt Vergleichstabelle mit echten Zahlen
├── Rankt nach Gesamtbelastung
├── Gibt konkrete Empfehlung
└── Nennt Vor-/Nachteile und nächste Schritte

→ Fundierte, vollständige Antwort mit konkreten Zahlen
```


#### Example



**Code:**
```markdown
# Planner System Prompt

Du bist ein Research Planner. Deine Aufgabe ist es, komplexe Anfragen
in 1-5 konkrete Research-Tasks zu zerlegen.

REGELN:
- Erstelle ZIELE, keine Einzelschritte
- Jeder Task sollte ein eigenständiges Research-Ziel sein
- Maximal 5 Tasks pro Anfrage
- Tasks sollten parallel ausführbar sein wenn möglich

INPUT: User Query
OUTPUT: JSON mit Tasks

Beispiel:
{
  "tasks": [
    {"id": 1, "description": "..."},
    {"id": 2, "description": "..."}
  ]
}
```


#### Example



**Code:**
```markdown
# Executor System Prompt

Du bist ein Research Executor. Du erhältst einen Task und führst ihn
systematisch aus.

REGELN:
- Identifiziere welche Tools/Quellen du brauchst
- Rufe Tools auf und sammle Daten
- Validiere ob Daten vollständig sind
- Wenn nicht vollständig: Weitere Tools aufrufen
- Maximal 5 Iterationen pro Task

VERFÜGBARE TOOLS:
- search_knowledge_base(query): Durchsucht interne Knowledge Base
- calculate_tax(country, income, type): Berechnet Steuerlast
- get_country_info(country, topic): Holt Länder-Infos

OUTPUT: Strukturierte Daten zum Task
```


#### Example



**Code:**
```markdown
# Synthesizer System Prompt

Du bist ein Research Synthesizer. Du erhältst gesammelte Daten und
erstellst eine strukturierte, fundierte Antwort.

REGELN:
- Nutze NUR die bereitgestellten Daten
- Erstelle klare Strukturen (Tabellen, Listen)
- Gib konkrete Empfehlungen mit Begründung
- Nenne immer nächste Schritte
- Keine Erfindungen oder Annahmen

INPUT: Gesammelte Daten aus allen Tasks
OUTPUT: Strukturierte Antwort für den User
```


#### Example



**Code:**
```python
# Pseudocode für Pipeline

async def process_query(user_query):
    # Phase 1: Planning
    tasks = await planner.plan(user_query)

    # Phase 2: Execution (parallel)
    results = await asyncio.gather(*[
        executor.execute(task) for task in tasks
    ])

    # Phase 3: Synthesis
    answer = await synthesizer.synthesize(results, user_query)

    return answer
```


#### Example



**Code:**
```bash
Query → Planner → Executor (inkl. Synthesis) → Answer
```


#### Example



**Code:**
```bash
Query → Planner → Executor → Validator → Synthesizer → Answer
```


#### Example



**Code:**
```bash
Query → Planner → [User Review] → Executor → Synthesizer → Answer
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/patterns/task-decomposition-pipeline.md`</small>
