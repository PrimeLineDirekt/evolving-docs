---
title: pitch-content-categorizer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# pitch-content-categorizer-agent


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

KB-Kategorisierung für Windenergie Pitch-System Dokumentation


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
knowledge/external-projects/schulung-pitch/
├── systems/              # Systemspezifische Dokumentation
│   ├── {hersteller}/    # KEBA, Moog, SSB, Bosch Rexroth, Beckhoff
│   └── general/         # Herstellerübergreifend
│
├── safety/              # Sicherheitskonzepte
│   ├── iso-normen/      # ISO13849, IEC61508, etc.
│   └── konzepte/        # PLd/PLe, Notfahrten, SIL
│
├── components/          # Komponenten
│   ├── motoren/         # Pitch-Motoren, Getriebe
│   ├── regler/          # PitchOne, PitchMaster, etc.
│   └── backup-power/    # Energiespeicher, Supercaps, Batterien
│
├── procedures/          # Verfahren
│   ├── wartung/         # Wartungsanleitungen
│   ├── inbetriebnahme/  # Commissioning Guides
│   └── troubleshooting/ # Fehlersuche
│
├── glossary/            # Fachbegriffe
│   └── terms.json       # DE/EN Terminologie
│
├── style/               # Stil-Profile
│   └── {source}.json    # Analysierte Präsentationsstile
│
└── raw/                 # Original-Analysen
    └── {filename}-analysis.md
```


#### Example



**Code:**
```json
{
  "term_de": "Deutscher Begriff",
  "term_en": "English Term",
  "definition": "Präzise technische Definition",
  "category": "systems|safety|components|procedures",
  "source": "Quelldokument",
  "related": ["verwandte", "begriffe"]
}
```


#### Example



**Code:**
```markdown
# Dokument-Analyse: {Titel}

## Metadaten
| Feld | Wert |
|------|------|
| Dokumenttyp | {typ} |
| Hersteller | {hersteller} |
| System/Produkt | {system} |
| Sprache | {sprache} |

## Themen-Hierarchie
{hierarchische Liste}

## Fachbegriffe
{Tabelle}

## Technische Spezifikationen
{Liste oder Tabelle}

## Sicherheitsrelevante Informationen
{Zusammenfassung}

## Hersteller/System-Referenzen
{Liste}
```


#### Example



**Code:**
```markdown
# Kategorisierung: {Titel}

**Quelle**: {Original-Analyse}
**Kategorisiert**: {Datum}

---

## Einordnung

| Feld | Wert |
|------|------|
| Primäre Kategorie | {systems\|safety\|components\|procedures} |
| Unterkategorie | {spezifisch} |
| Ziel-Pfad | `knowledge/external-projects/schulung-pitch/{pfad}/` |
| Dateiname | `{name}.md` |

---

## Tags

```


#### Example



**Code:**
```bash

---

## Glossar-Einträge (Neu)

```


#### Example



**Code:**
```bash

---

## Wiederverwendbare Snippets

### Snippet 1: {Titel}
**Typ**: {definition|specification|procedure|warning}
**Wiederverwendbar für**: {use-cases}

```


#### Example



**Code:**
```bash

### Snippet 2: {Titel}
...

---

## Querverweise

Verbindungen zu existierenden KB-Einträgen:
- [ ] `{pfad/zu/verwandtem/dokument.md}` - {Grund}
- [ ] `glossary/terms.json` - {N} neue Begriffe

---

## Aktionen

- [ ] Datei erstellen in `{ziel-pfad}`
- [ ] Glossar aktualisieren mit {N} Begriffen
- [ ] Index aktualisieren (`index.json`)
- [ ] Querverweise prüfen
```


#### Example



**Code:**
```bash
Dokumenttyp: schulung
Hersteller: KEBA
System: PitchOne
Hauptthemen: Systemarchitektur, Sicherheitskonzept, Inbetriebnahme
```


#### Example



**Code:**
```markdown
## Einordnung

| Feld | Wert |
|------|------|
| Primäre Kategorie | systems |
| Unterkategorie | keba |
| Ziel-Pfad | `knowledge/external-projects/schulung-pitch/systems/keba/` |
| Dateiname | `pitchone-schulung.md` |

## Tags
{
  "primary": ["schulung", "pitch-system"],
  "manufacturer": "keba",
  "system": "pitchone",
  "topics": ["architektur", "sicherheit", "inbetriebnahme"],
  "components": ["regler"],
  "safety": ["pld", "iso13849"]
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/pitch-content-categorizer-agent.md`</small>
