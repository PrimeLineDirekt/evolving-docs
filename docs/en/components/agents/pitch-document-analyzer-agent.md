---
title: pitch-document-analyzer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# pitch-document-analyzer-agent


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

Analyse technischer Dokumentation für Windenergie Pitch-Systeme


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
- Hauptthema 1
  - Unterthema 1.1
  - Unterthema 1.2
- Hauptthema 2
  - ...
```


#### Example



**Code:**
```markdown
# Dokument-Analyse: {Titel aus Dokument}

**Analysiert**: {Datum}
**Quelle**: {Dateiname}
**Seiten**: {Anzahl}

---

## 1. Metadaten

| Feld | Wert | Quelle |
|------|------|--------|
| Dokumenttyp | {typ} | {Begründung} |
| Dokumentnummer | {Nr. oder "Nicht angegeben"} | |
| Revision | {Rev. oder "Nicht angegeben"} | |
| Hersteller | {Wert oder "Nicht genannt"} | S. {x} |
| System/Produkt | {Wert oder "Nicht spezifiziert"} | S. {x} |
| Sprache | {Sprache} | - |
| Erstellungsdatum | {Datum oder "Nicht angegeben"} | |

---

## 2. Inhaltsstruktur

### Themen-Hierarchie
{Exakte Struktur aus dem Dokument}

### Abbildungen & Diagramme
| Nr. | Titel | Typ | Seite |
|-----|-------|-----|-------|
| {Nr.} | {Titel} | {Typ} | S. {x} |

---

## 3. Fachbegriffe & Abkürzungen

### Fachbegriffe
| Begriff | Sprache | Definition | Kontext | Seite |
|---------|---------|------------|---------|-------|
| {Begriff} | {DE/EN} | {Definition} | {Kontext} | S. {x} |

### Abkürzungen
| Abkürzung | Bedeutung | Im Dokument erklärt |
|-----------|-----------|---------------------|
| {ABK} | {Ausgeschrieben} | {Ja/Nein, S. x} |

**Neu entdeckte Begriffe**: {Liste}

---

## 4. Elektrische Spezifikationen

| Parameter | Wert | Einheit | Bedingung | Quelle |
|-----------|------|---------|-----------|--------|
| {Parameter} | {Wert} | {Einheit} | {Bedingung} | S. {x} |

*(Abschnitt weglassen wenn keine elektrischen Daten im Dokument)*

---

## 5. Mechanische Spezifikationen

| Parameter | Wert | Einheit | Quelle |
|-----------|------|---------|--------|
| {Parameter} | {Wert} | {Einheit} | S. {x} |

*(Abschnitt weglassen wenn keine mechanischen Daten im Dokument)*

---

## 6. Umgebungsbedingungen

| Parameter | Min | Max | Einheit | Quelle |
|-----------|-----|-----|---------|--------|
| {Parameter} | {Min} | {Max} | {Einheit} | S. {x} |

*(Abschnitt weglassen wenn keine Umgebungsdaten im Dokument)*

---

## 7. Sicherheit & Normen

### Sicherheitshinweise
| Typ | Text (exakt) | Seite |
|-----|--------------|-------|
| {GEFAHR/WARNUNG/...} | "{Wortlaut}" | S. {x} |

### Normen & Zertifizierungen
| Norm | Beschreibung | Kontext |
|------|--------------|---------|
| {Norm} | {Beschreibung} | S. {x} |

### Safety-Level
- Performance Level: {PL oder "Nicht genannt"}
- SIL: {SIL oder "Nicht genannt"}
- Kategorie: {Kat oder "Nicht genannt"}

---

## 8. Artikel & Bestellnummern

| Artikelnummer | Bezeichnung | Beschreibung | Quelle |
|---------------|-------------|--------------|--------|
| {Nummer} | {Name} | {Beschreibung} | S. {x} |

*(Abschnitt weglassen wenn keine Artikelnummern im Dokument)*

---

## 9. Schnittstellen & Kommunikation

### Anschlüsse
| Bezeichnung | Typ | Pinbelegung | Funktion |
|-------------|-----|-------------|----------|
| {X1} | {Typ} | {Pins} | {Funktion} |

### Protokolle
| Protokoll | Version | Parameter |
|-----------|---------|-----------|
| {Protokoll} | {Version} | {Parameter} |

*(Abschnitt weglassen wenn keine Interface-Daten im Dokument)*

---

## 10. Software & Parameter

### Firmware/Software
| Element | Version | Beschreibung |
|---------|---------|--------------|
| {Element} | {Version} | {Beschreibung} |

### Konfigurationsparameter
| Parameter | Bereich | Default | Beschreibung | Quelle |
|-----------|---------|---------|--------------|--------|
| {Param} | {Bereich} | {Default} | {Beschreibung} | S. {x} |

*(Abschnitt weglassen wenn keine Software-Daten im Dokument)*

---

## 11. Fehlerdiagnose

### Fehlercodes
| Code | Bezeichnung | Ursache | Abhilfe | Quelle |
|------|-------------|---------|---------|--------|
| {Code} | {Name} | {Ursache} | {Abhilfe} | S. {x} |

### Statusanzeigen
| Anzeige | Zustand | Bedeutung |
|---------|---------|-----------|
| {LED/Display} | {Zustand} | {Bedeutung} |

*(Abschnitt weglassen wenn keine Diagnose-Daten im Dokument)*

---

## 12. Verfahren & Anleitungen

### Prozeduren
| Verfahren | Schritte | Werkzeuge | Seite |
|-----------|----------|-----------|-------|
| {Name} | {Anzahl} | {Tools} | S. {x} |

### Wartungsintervalle
| Komponente | Intervall | Maßnahme | Quelle |
|------------|-----------|----------|--------|
| {Teil} | {Intervall} | {Aktion} | S. {x} |

*(Abschnitt weglassen wenn keine Verfahren im Dokument)*

---

## 13. Referenzen

### Hersteller/Lieferanten
| Name | Produkt | Kontext |
|------|---------|---------|
| {Hersteller} | {Produkt} | {Kontext} |

### Referenzierte Dokumente
| Dokument | Nummer | Beschreibung |
|----------|--------|--------------|
| {Titel} | {Nr.} | {Wofür} |

---

## 14. Analyse-Zusammenfassung

### Vollständigkeit
| Kategorie | Vorhanden | Umfang |
|-----------|-----------|--------|
| Elektrische Specs | Ja/Nein | {Anzahl Einträge} |
| Mechanische Specs | Ja/Nein | {Anzahl Einträge} |
| Sicherheitshinweise | Ja/Nein | {Anzahl Einträge} |
| Fehlercodes | Ja/Nein | {Anzahl Einträge} |
| Verfahren | Ja/Nein | {Anzahl Einträge} |

### Unklarheiten
{Liste von Stellen die nicht eindeutig interpretiert werden konnten}

### Empfohlene Kategorisierung
- **Primäre Kategorie**: {Kategorie}
- **Unterkategorie**: {Unterkategorie}
- **Tags**: {tag1}, {tag2}, ...
- **Begründung**: {Warum diese Kategorisierung}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/pitch-document-analyzer-agent.md`</small>
