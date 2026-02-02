---
title: visa-kb-add
type: command
tags: []
lang: en
confidence: 100
---

# visa-kb-add


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

Pfad zur Perplexity Export-Datei (optional - wird abgefragt)


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
User: /visa-kb-add ~/Downloads/visa-export.md
                    │
         ┌──────────┴──────────┐
         │ MAIN: Input Check   │  (~500 Tokens)
         │ - Datei existiert?  │
         │ - Pfad expandieren  │
         └──────────┬──────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────┐
│ PHASE 1: File Analyzer (Haiku)                    │
│                                                   │
│ Analysiert Perplexity-Export, extrahiert:         │
│ - Country, Region, Confidence                     │
│ - Section-by-Section Confidence                   │
│ Output: JSON mit Scores + Gap-Liste               │
└───────────────────────────────────────────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │ Confidence >= 90%?   │
         └──────────┬───────────┘
                    │
         ┌──────────┴──────────┐
         │                     │
        YES                   NO
         │                     │
         ▼                     ▼
┌─────────────────┐  ┌──────────────────────────────┐
│ Skip Gap-Fill   │  │ PHASE 1.5: Gap-Filling       │
│ → Phase 2       │  │                              │
└─────────────────┘  │ Für jede Section < 90%:      │
                     │ 1. WebSearch gezielte Query  │
                     │ 2. Infos extrahieren         │
                     │ 3. In Content einfügen       │
                     │ 4. Confidence neu berechnen  │
                     └──────────────┬───────────────┘
                                    │
                    ┌───────────────┘
                    ▼
┌───────────────────────────────────────────────────┐
│ PHASE 2: File Writer (Haiku)                      │
│                                                   │
│ Speichert finalen Content mit >= 90% Confidence   │
│ Output: Pfad zur gespeicherten Datei              │
└───────────────────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────┐
│ PHASE 3: System Updater (Haiku)                   │
│                                                   │
│ Aktualisiert _index.md + README.md                │
│ Output: Liste aktualisierter Dateien              │
└───────────────────────────────────────────────────┘
                    │
                    ▼
         ┌──────────┴──────────┐
         │ MAIN: Summary       │  (~200 Tokens)
         │ - Ergebnis ausgeben │
         │ - Gap-Fill Report   │
         └─────────────────────┘
```


#### Example



**Code:**
```bash
Bitte gib den Pfad zur Perplexity Export-Datei:
(z.B. ~/Downloads/Visa Knowledge Base Portugal.md)
```


#### Example



**Code:**
```bash
Task Tool mit:
- subagent_type: "general-purpose"
- model: "haiku"
- prompt: [siehe unten]
```


#### Example



**Code:**
```markdown
## TASK
Analysiere die Perplexity Visa Export-Datei und extrahiere Section-by-Section Confidence.

## FILE
{file_path}

## EXPECTED OUTCOME
JSON mit Confidence pro Section:
{
  "country": "Portugal",
  "region": "europe",
  "overall_confidence": 78,
  "sections": {
    "visa_overview": {"confidence": 95, "gaps": []},
    "digital_nomad": {"confidence": 85, "gaps": ["Bearbeitungszeit unklar"]},
    "retirement": {"confidence": 70, "gaps": ["Finanzanforderung fehlt", "PR-Weg unklar"]},
    "golden_visa": {"confidence": 90, "gaps": []},
    "pr_pathways": {"confidence": 65, "gaps": ["Sprachanforderung", "Integration", "Citizenship-Zeit"]},
    "tourist": {"confidence": 92, "gaps": []},
    "practical": {"confidence": 88, "gaps": ["Botschaft Website"]}
  },
  "gaps_to_fill": [
    {"section": "retirement", "query": "[COUNTRY] retirement visa requirements 2025 2026", "priority": "high"},
    {"section": "pr_pathways", "query": "[COUNTRY] permanent residence requirements language 2025", "priority": "high"}
  ],
  "content_start": 1,
  "content_end": 350
}

## REQUIRED TOOLS
- Read (mit offset/limit für große Dateien)
- Grep (für Pattern-Suche)

## MUST DO
1. YAML Frontmatter lesen → confidence_score extrahieren
2. Section 9 (Datenqualität) finden → Section-Confidences extrahieren
3. Für jede Section < 90%: Gap identifizieren
4. Search-Queries formulieren für Gap-Filling
5. Priorität: high wenn < 80%, medium wenn 80-89%

## MUST NOT DO
- Keine Dateien schreiben oder editieren
- Nicht die ganze Datei auf einmal lesen bei > 500 Zeilen
- Keine Annahmen ohne Beweis aus der Datei
```


#### Example



**Code:**
```bash
FÜR JEDE Section in gaps_to_fill (sortiert nach Priorität):
    │
    ├─ 1. WebSearch mit formulierter Query
    │     z.B. "Portugal D7 visa retirement requirements 2025 2026"
    │
    ├─ 2. Top 3 Ergebnisse analysieren
    │     - Tier 1 Quellen bevorzugen (gov, diplo)
    │     - Konkrete Zahlen/Fakten extrahieren
    │
    ├─ 3. Content-Snippet vorbereiten
    │     - Im KB-Format (Tabelle oder Bullet Points)
    │     - Mit Quellenangabe
    │
    └─ 4. Merge-Anweisung für Phase 2 erstellen
          {"section": "retirement", "insert_after": "### Optionen", "content": "..."}
```


#### Example



**Code:**
```json
{
  "filled_gaps": [
    {
      "section": "retirement",
      "original_confidence": 70,
      "new_confidence": 92,
      "additions": [
        "Finanzanforderung: €760/Monat (Quelle: SEF.pt)",
        "PR-Weg: Nach 5 Jahren mit A2 Portugiesisch"
      ],
      "sources_added": ["sef.pt", "diplomatico.de"]
    }
  ],
  "new_overall_confidence": 91,
  "merge_instructions": [...]
}
```


#### Example



**Code:**
```bash
Task Tool mit:
- subagent_type: "general-purpose"
- model: "haiku"
- prompt: [siehe unten]
```


#### Example



**Code:**
```markdown
## TASK
Erstelle die finale Visa KB Datei mit Gap-Fill Merges.

## INPUT
Source: {file_path}
Analysis: {agent1_output_json}
Gap-Fills: {gap_fill_output_json}  # Kann leer sein wenn >= 90%

## EXPECTED OUTCOME
Gespeicherte Datei mit Bestätigung:
{
  "saved": true,
  "path": "/Users/neoforce/Buisiness/Auswanderungs-KI-v2/knowledge-base/visa/europe/portugal.md",
  "lines": 420,
  "final_confidence": 92,
  "gaps_filled": 3,
  "yaml_valid": true,
  "sections_found": 9
}

## REQUIRED TOOLS
- Read (Source-Datei)
- Write (Ziel-Datei)

## MUST DO
1. Source-Datei lesen (content_start:content_end)
2. YAML Frontmatter aktualisieren:
   - confidence_score: {new_overall_confidence}
   - status: "complete" (wenn >= 90%)
   - last_updated: "2026-01-10"
3. Gap-Fill Merges einfügen (wenn vorhanden):
   - An insert_after Position
   - Mit "*(Ergänzt via CC Research)*" Marker
4. Section 9 Confidence-Werte aktualisieren
5. Neue Quellen in Section 8 hinzufügen
6. Speichern in: /Users/neoforce/Buisiness/Auswanderungs-KI-v2/knowledge-base/visa/{region}/{country_lowercase}.md

## MUST NOT DO
- Keine System-Dateien editieren (_index.md, README.md)
- Bestehenden validen Content nicht überschreiben
- Keine Duplikate einfügen

## TARGET PATH
/Users/neoforce/Buisiness/Auswanderungs-KI-v2/knowledge-base/visa/{region}/{country_lowercase}.md

Country → Filename Mapping:
- "Thailand" → thailand.md
- "UAE (Dubai)" → uae.md
- "Costa Rica" → costa-rica.md
- "Hong Kong" → hong-kong.md
- "Vietnam" → vietnam.md
```


#### Example



**Code:**
```bash
Task Tool mit:
- subagent_type: "general-purpose"
- model: "haiku"
- prompt: [siehe unten]
```


#### Example



**Code:**
```markdown
## TASK
Aktualisiere die System-Dateien nach erfolgreicher Visa KB Integration.

## INPUT
Country: {country}
Region: {region}
Confidence: {final_confidence}
Saved Path: {saved_path}
Gaps Filled: {gaps_filled_count}

## EXPECTED OUTCOME
{
  "updated": ["_index.md", "README.md"],
  "index_progress": "3/30",
  "readme_updated": true
}

## REQUIRED TOOLS
- Read
- Edit

## MUST DO

### 1. _index.md aktualisieren
Datei: `/Users/neoforce/Buisiness/Auswanderungs-KI-v2/knowledge-base/visa/_index.md`

Finde: `- [ ] {Country}`
Ersetze: `- [x] {Country} ({confidence}% confidence, 2026-01-10)`

### 2. README.md aktualisieren
Datei: `/Users/neoforce/Buisiness/Auswanderungs-KI-v2/knowledge-base/README.md`

In der "Visa Knowledge Base" Tabelle:
- Region-Zeile finden (z.B. `| Asia |`)
- Count erhöhen (z.B. `1/6` → `2/6`)
- GESAMT erhöhen

In "Fertige Länder:" Liste:
- Neues Land hinzufügen mit Features

## MUST NOT DO
- Keine Visa-Content-Dateien editieren
- Keine Struktur-Änderungen an den Dateien
- Nur die spezifischen Sections aktualisieren
```


#### Example



**Code:**
```bash
✅ Visa KB Integration: {country}

📄 Gespeichert: knowledge-base/visa/{region}/{country}.md
📊 Confidence: {final_confidence}% (Ziel: ≥90% ✓)
🔍 Gap-Fills: {gaps_filled_count} Sections ergänzt
📝 Updates: _index.md, README.md
⚡ ChromaDB: Auto-indexed bei nächstem Run

Gap-Fill Details:
- {section1}: {old}% → {new}% (+{sources} Quellen)
- {section2}: {old}% → {new}% (+{sources} Quellen)
```


#### Example



**Code:**
```markdown
| Visa-Typ | Min. Alter | Finanzanforderung | Gültigkeit |
|----------|------------|-------------------|------------|
| D7 Visa | 18+ | €760/Monat *(CC)* | 2 Jahre |
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/visa-kb-add.md`</small>
