---
title: /analyze-pitch-docs
type: command
tags: []
lang: en
confidence: 100
---

# /analyze-pitch-docs


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Process wind energy pitch system documents from inbox with specialized agents. |
| **Complexity** | high |
| **Model** | claude-sonnet-4-5 |
| **Category** | workflow |</div>


## What It Does

Orchestrates analysis of wind energy pitch system documents using three specialized agents:

1. **pitch-document-analyzer-agent**: Technical analysis - document type, metadata, topic hierarchy, technical specs
2. **pitch-content-categorizer-agent**: Categorization - primary category, tags, glossary extraction, reusable snippets
3. **pitch-style-extractor-agent**: (PPTX only) Slide types, structure patterns, phrasing patterns, style profile

Processes documents from `_inbox/` and distributes analyzed content to appropriate knowledge base locations.


## System Impact

- Enables automated knowledge extraction from pitch training materials
- Integrates with external projects KB at `knowledge/external-projects/schulung-pitch/`
- Critical for building domain glossary and style profiles
- Maintains separation between raw analysis and categorized content


## Architecture

**Dependencies:**
- Three specialized agents: document-analyzer, content-categorizer, style-extractor
- Inbox directory: `_inbox/` for unprocessed files (PDF, DOCX, PPTX, MD, TXT)
- Knowledge base structure at `knowledge/external-projects/schulung-pitch/`

**Data Flow:**
1. Scan `_inbox/` → identify unprocessed files
2. For each file: document-analyzer → raw analysis
3. content-categorizer → categorized KB entry
4. If PPTX: style-extractor → style profile
5. Update index.json and glossary/terms.json
6. Archive processed files

**Agent Orchestration:**
```
_inbox/ scan
    │
    ▼
document-analyzer (all files)
    │
    ├──► content-categorizer (always)
    │
    └──► style-extractor (PPTX only)
         │
         ▼
    Index & Glossary update
```


## Usage

**Basic syntax:**
```bash
/analyze-pitch-docs
```

Automatically scans inbox and processes all new files.

### Examples

#### Basic Usage

Process all pending pitch documents:

**Code:**
```bash
/analyze-pitch-docs
```

**Output:**
```markdown
# Pitch-Dokument Analyse abgeschlossen

**Verarbeitet**: 2026-02-03
**Dateien**: 3

---

## Verarbeitete Dokumente

### 1. Senvion-Technical-Specs.pdf
- **Typ**: Technical Documentation
- **Hersteller**: Senvion
- **System**: MM82
- **Kategorisiert als**: `systems/senvion/technical/mm82-specs.md`
- **Neue Glossar-Einträge**: 12
- **Stil-Profil**: Nein

### 2. Pitch-Training-Slides.pptx
- **Typ**: Training Material
- **Hersteller**: Nicht spezifiziert
- **System**: Allgemein
- **Kategorisiert als**: `training/general/pitch-basics.md`
- **Neue Glossar-Einträge**: 5
- **Stil-Profil**: Ja

---

## Nächste Schritte

- [ ] Original-Dateien aus `_inbox/` löschen?
- [ ] Querverweise zu existierenden Dokumenten prüfen
- [ ] Stil-Profile für neue Präsentationen nutzen
```


## Configuration

**Document Types:**
- PDF, DOCX, PPTX, MD, TXT

**Archive Locations:**
| Content Type | Path |
|--------------|------|
| Raw Analysis | `knowledge/external-projects/schulung-pitch/raw/{filename}-analysis.md` |
| Categorized | `knowledge/external-projects/schulung-pitch/{category}/{subcategory}/{filename}.md` |
| Style Profiles | `knowledge/external-projects/schulung-pitch/style/{filename}-style.json` |
| Index | `knowledge/external-projects/schulung-pitch/index.json` |
| Glossary | `knowledge/external-projects/schulung-pitch/glossary/terms.json` |

**Thresholds:**
- Age threshold: Process files regardless of age
- Skip already processed files (check existence in raw/)


## Best Practices

**Do:**
- Process all document types (PDF, DOCX, PPTX, MD, TXT)
- Extract technical terms ONLY from documents (no assumptions)
- Document conflicting terminology with sources
- Update both index and glossary after processing
- Apply style extraction only for PPTX files

**Don't:**
- Make technical assumptions without document evidence
- Skip glossary updates for new terminology
- Ignore categorization uncertainties (use "needs-review" tag)
- Process files already in `raw/` directory
- Apply style extraction to non-PPTX formats




## Related


---

<small>Source: `.claude/commands/analyze-pitch-docs.md`</small>
