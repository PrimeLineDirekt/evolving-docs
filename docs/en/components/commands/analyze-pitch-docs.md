---
title: analyze-pitch-docs
type: command
tags: []
lang: en
confidence: 100
---

# analyze-pitch-docs


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




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Gefundene Dateien:
1. {dateiname} ({typ}, {größe})
2. ...
```


#### Example



**Code:**
```bash
                        ┌─────────────────────┐
                        │   _inbox/ scannen   │
                        └──────────┬──────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │  pitch-document-analyzer    │
                    │  (für jede Datei)           │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┴────────────────────┐
              │                                         │
    ┌─────────▼─────────┐                    ┌─────────▼─────────┐
    │  pitch-content-   │                    │  pitch-style-     │
    │  categorizer      │                    │  extractor        │
    │  (immer)          │                    │  (nur bei PPTX)   │
    └─────────┬─────────┘                    └─────────┬─────────┘
              │                                         │
              └────────────────────┬────────────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │  Index & Glossar updaten    │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │  Zusammenfassung ausgeben   │
                    └─────────────────────────────┘
```


#### Example



**Code:**
```markdown
# Pitch-Dokument Analyse abgeschlossen

**Verarbeitet**: {Datum}
**Dateien**: {N}

---

## Verarbeitete Dokumente

### 1. {Dateiname}
- **Typ**: {dokumenttyp}
- **Hersteller**: {hersteller oder "Nicht spezifiziert"}
- **System**: {system oder "Allgemein"}
- **Kategorisiert als**: `{pfad}`
- **Neue Glossar-Einträge**: {N}
- **Stil-Profil**: {Ja/Nein}

### 2. {Dateiname}
...

---

## Neue KB-Einträge

| Datei | Kategorie | Pfad |
|-------|-----------|------|
| ... | ... | ... |

---

## Glossar-Updates

{N} neue Begriffe hinzugefügt:
- {Begriff 1} ({Kategorie})
- {Begriff 2} ({Kategorie})
...

---

## Nächste Schritte

- [ ] Original-Dateien aus `_inbox/` löschen?
- [ ] Querverweise zu existierenden Dokumenten prüfen
- [ ] Stil-Profile für neue Präsentationen nutzen
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/analyze-pitch-docs.md`</small>
