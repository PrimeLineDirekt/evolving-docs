---
title: pitch-style-extractor-agent
type: agent
tags: []
lang: en
confidence: 100
---

# pitch-style-extractor-agent


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

Stil-Extraktion aus PPTX Präsentationen für Windenergie Pitch-Systeme


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
1. {slide-typ} - {Zweck}
2. {slide-typ} - {Zweck}
...
```


#### Example



**Code:**
```bash
--- Slide 1 ---
[Titel]
{Inhalt}

--- Slide 2 ---
[Titel]
{Inhalt}
...
```


#### Example



**Code:**
```json
{
  "profile_name": "{Quelldatei}-style",
  "version": "1.0.0",
  "extracted_from": "{Quelldatei}",
  "extraction_date": "{YYYY-MM-DD}",

  "metadata": {
    "total_slides": {N},
    "language": "{DE|EN|mixed}",
    "target_audience": "{techniker|ingenieur|management|allgemein}",
    "manufacturer": "{hersteller oder null}",
    "system": "{system oder null}"
  },

  "structure": {
    "typical_sections": [
      {
        "name": "{Abschnittsname}",
        "slide_types": ["{typ1}", "{typ2}"],
        "typical_slide_count": {N}
      }
    ],
    "patterns": [
      {
        "name": "{Pattern-Name}",
        "sequence": ["{typ1}", "{typ2}", "{typ3}"],
        "use_case": "{Wann verwenden}"
      }
    ]
  },

  "slide_templates": {
    "title": {
      "elements": ["logo", "haupttitel", "untertitel", "datum"],
      "example_titles": ["{Beispiel1}", "{Beispiel2}"]
    },
    "content": {
      "title_style": "{kurz|beschreibend|nummeriert}",
      "bullet_style": "{vollsaetze|stichpunkte}",
      "hierarchy_depth": {1-3},
      "example_bullets": ["{Beispiel1}", "{Beispiel2}"]
    },
    "diagram": {
      "types": ["{blockschaltbild|schaltplan|ablauf}"],
      "typical_elements": ["{element1}", "{element2}"]
    },
    "warning": {
      "elements": ["symbol", "titel", "text"],
      "severity_levels": ["info", "warnung", "gefahr"],
      "example_text": "{Beispiel-Warnung}"
    },
    "procedure": {
      "numbering_style": "{1.|Schritt 1:|a)}",
      "action_verbs": ["{verb1}", "{verb2}"],
      "example_step": "{Beispiel-Schritt}"
    }
  },

  "language_patterns": {
    "headings": {
      "style": "{substantiv|verb|frage}",
      "max_words": {N},
      "examples": ["{Beispiel1}", "{Beispiel2}"]
    },
    "body_text": {
      "sentence_style": "{vollstaendig|verkuerzt}",
      "typical_starters": ["{Bei}", "{Wenn}", "{ACHTUNG:}"],
      "technical_terms_handling": "{erklaert|vorausgesetzt}"
    },
    "units_format": {
      "examples": ["{kW}", "{Nm}", "{°C}"],
      "spacing": "{mit_leerzeichen|ohne}"
    },
    "norm_references": {
      "format": "{ISO 13849-1|ISO13849-1}",
      "examples": ["{Beispiel1}"]
    }
  },

  "visual_conventions": {
    "header_content": ["{element1}", "{element2}"],
    "footer_content": ["{element1}", "{element2}"],
    "logo_position": "{links_oben|rechts_oben}",
    "emphasis": {
      "strong": "{fett|farbe}",
      "caution": "{gelb|orange}",
      "danger": "{rot}"
    }
  },

  "quality_markers": {
    "consistency_score": "{hoch|mittel|niedrig}",
    "completeness": "{vollstaendig|teilweise}",
    "reusability": "{hoch|mittel|niedrig}",
    "notes": "{Anmerkungen zur Qualität}"
  }
}
```


#### Example



**Code:**
```markdown
# Stil-Profil: {Quelldatei}

**Extrahiert**: {Datum}
**Zielgruppe**: {Zielgruppe}
**Sprache**: {Sprache}

---

## Zusammenfassung

{2-3 Sätze zum Gesamtstil}

---

## Struktur-Template

1. **Einleitung** ({N} Slides)
   - Titelfolie
   - Agenda

2. **Hauptteil** ({N} Slides)
   - {Typische Abschnitte}

3. **Abschluss** ({N} Slides)
   - Zusammenfassung
   - Q&A

---

## Formulierungsmuster

### Überschriften
- Stil: {Beschreibung}
- Beispiele: "{Beispiel1}", "{Beispiel2}"

### Bullet Points
- Stil: {Beschreibung}
- Typische Starter: {Liste}

### Fachsprache
- Abkürzungen: {Handling}
- Normverweise: {Format}

---

## Wiederverwendbarkeit

**Empfohlen für**: {Use Cases}
**Nicht geeignet für**: {Ausschlüsse}

---

## Speicherort

`knowledge/external-projects/schulung-pitch/style/{profile-name}.json`
```


#### Example



**Code:**
```json
{
  "profile_name": "keba-pitchone-service-style",
  "metadata": {
    "total_slides": 45,
    "language": "DE",
    "target_audience": "techniker",
    "manufacturer": "KEBA",
    "system": "PitchOne"
  },
  "structure": {
    "typical_sections": [
      {"name": "Systemübersicht", "slide_types": ["section", "diagram", "content"], "typical_slide_count": 8},
      {"name": "Komponenten", "slide_types": ["section", "diagram", "table"], "typical_slide_count": 12},
      {"name": "Wartung", "slide_types": ["section", "procedure", "warning"], "typical_slide_count": 10}
    ]
  },
  "language_patterns": {
    "headings": {
      "style": "substantiv",
      "max_words": 4,
      "examples": ["Systemarchitektur", "Motor-Spezifikationen", "Wartungsintervalle"]
    },
    "body_text": {
      "typical_starters": ["Bei", "Vor", "Nach", "ACHTUNG:", "HINWEIS:"]
    }
  }
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/pitch-style-extractor-agent.md`</small>
