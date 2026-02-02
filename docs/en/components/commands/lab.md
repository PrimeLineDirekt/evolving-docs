---
title: lab
type: command
tags: []
lang: en
confidence: 100
---

# lab


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

Perplexity Labs Projekte (Reports, Dashboards, Spreadsheets, Code)


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Was soll ich in Perplexity Labs erstellen?

Bitte beschreibe:
1. **Thema/Ziel**: Was genau?
2. **Kontext**: Für welchen Zweck?

Beispiele:
- "Marktanalyse für Etsy Poster-Markt 2026"
- "Dashboard für Kryptowährungen Performance"
- "Spreadsheet: Vergleich von VPN-Anbietern"
```


#### Example



**Code:**
```bash
Welchen Lab-Typ soll ich erstellen?

[1] Report (Empfohlen)
    → Formatierter Bericht mit Analyse
    → Dauer: 5-10 Minuten

[2] Dashboard
    → Interaktive Visualisierung
    → Dauer: 10-15 Minuten

[3] Spreadsheet
    → Tabellarische Datenanalyse mit CSV
    → Dauer: 5-10 Minuten

[4] Code Prototype
    → Funktionierender Code/Mini-App
    → Dauer: 10-20 Minuten
```


#### Example



**Code:**
```bash
Soll ich Kontext aus unserer Knowledge Base in die Query einbauen?

Relevanter Kontext könnte sein:
- Projekt-spezifische Infos (z.B. aus knowledge/projects/)
- Vorherige Recherchen (z.B. aus knowledge/labs/)
- Learnings oder Patterns

[1] Ja - Suche relevanten Kontext
[2] Nein - Query ist selbsterklärend
```


#### Example



**Code:**
```bash
Erstelle ein [ARTEFAKT-TYP] fuer [THEMA]. Hintergrund: [KEY-FACTS-AUS-KB]. Features: (1) ...; (2) ...; (3) .... Datenquellen: [QUELLEN]. Output: [FORMAT].
```


#### Example



**Code:**
```bash
Erstelle einen UMFASSENDEN MARKTANALYSE-REPORT fuer Etsy Poster-Markt 2026. Hintergrund: Wir betreiben ThriveVibesArt, einen Shop fuer minimalistische Poster mit Fokus auf Affirmationen und Wellness, bisherige Bestseller ist die Breathe-Serie. Features: (1) Executive Summary mit Marktgroesse und Top-3 Trends; (2) Competitor-Analyse der Top-10 Seller in unserer Nische; (3) Preisstrategie-Empfehlung basierend auf unserem Sortiment. Datenquellen: Etsy Marketplace 2026, eRank. Output: Report mit Visualisierungen.
```


#### Example



**Code:**
```markdown
## Optimierte Query

**Original**: {user_input}
**Lab-Typ**: {selected_type}
**Optimiert**: {optimized_query}
```


#### Example



**Code:**
```python
# 1. Tab-Context holen
tabs_context_mcp(createIfEmpty=True)

# 2. Neuen Tab erstellen
tabs_create_mcp()

# 3. Zu Perplexity navigieren
navigate(url="https://www.perplexity.ai/", tabId=TAB_ID)

# 4. Warte kurz auf Laden
computer(action="wait", duration=2, tabId=TAB_ID)

# 5. Seite lesen um UI-Elemente zu finden
read_page(tabId=TAB_ID, filter="interactive")
```


#### Example



**Code:**
```python
# Finde den "Labs" Radio-Button
page = read_page(tabId=TAB_ID, filter="interactive")
# Suche nach: radio "Labs" [ref_XX]

# Klicke auf "Labs"
computer(action="left_click", ref="ref_XX", tabId=TAB_ID)
```


#### Example



**Code:**
```python
# 1. Textfeld klicken (NICHT form_input verwenden - ist oft DIV!)
computer(action="left_click", ref="ref_YY", tabId=TAB_ID)

# 2. Query eingeben - ALLES IN EINER ZEILE!
# Struktur durch Semikolons und nummerierte Listen, KEINE Newlines
computer(action="type", text="{optimized_query_single_line}", tabId=TAB_ID)

# 3. SCREENSHOT zur Verifizierung vor Absenden!
computer(action="screenshot", tabId=TAB_ID)
# → Prüfen ob VOLLE Query im Textfeld steht

# 4. Erst dann absenden (Klick auf Send-Button, NICHT Enter)
computer(action="left_click", coordinate=[SEND_BUTTON_X, SEND_BUTTON_Y], tabId=TAB_ID)
```


#### Example



**Code:**
```bash
Erstelle ein [ARTEFAKT-TYP] fuer [THEMA]. Features: (1) [Feature-A] mit [Details]; (2) [Feature-B] fuer [Zweck]; (3) [Feature-C] zeigt [Was]. Datenquellen: [Quelle-1], [Quelle-2]. Output: [Format].
```


#### Example



**Code:**
```python
# Polling-Loop
MAX_ITERATIONS = 120  # 120 * 10s = 20 Minuten
INTERVAL = 10  # Sekunden

for i in range(MAX_ITERATIONS):
    computer(action="wait", duration=INTERVAL, tabId=TAB_ID)

    text = get_page_text(tabId=TAB_ID)

    # Check ob Lab fertig
    # Labs zeigt "Assets" Tab wenn fertig
    if "Assets" in text and "Generating" not in text:
        break

    # Progress-Update alle 30 Sekunden
    if i % 3 == 0:
        print(f"Lab läuft... ({i * 10}s)")

# Timeout-Warnung
if i >= MAX_ITERATIONS - 1:
    print("TIMEOUT: Lab dauert länger als erwartet")
```


#### Example



**Code:**
```python
# 1. Haupt-Ergebnis holen
result = get_page_text(tabId=TAB_ID)

# 2. Screenshot für Dokumentation
computer(action="screenshot", tabId=TAB_ID)

# 3. Assets-Tab klicken (falls vorhanden)
# read_page → Assets Tab ref finden → klicken
# Assets auflisten (CSV, Charts, Code-Files)
```


#### Example



**Code:**
```bash
knowledge/labs/{YYYY-MM-DD}-{topic-slug}/
├── README.md          # Projekt-Übersicht
├── result.md          # Extrahierter Lab-Output
├── assets/            # Heruntergeladene Assets (falls möglich)
│   ├── data.csv
│   └── chart-1.png
└── screenshot.png     # Browser-Screenshot
```


#### Example



**Code:**
```markdown
# Lab: {topic}

**Erstellt**: {date}
**Typ**: {lab_type}
**Dauer**: ~{duration}

## Query
{optimized_query}

## Ergebnis-Zusammenfassung
{brief_summary}

## Assets
- [data.csv](./assets/data.csv)
- [Chart 1](./assets/chart-1.png)

## Perplexity Link
{direct_link_if_available}

## Nächste Schritte
- {next_step_1}
- {next_step_2}
```


#### Example



**Code:**
```bash
✓ Lab erstellt: {topic}
  Typ: {lab_type}
  Dauer: ~{duration}

  Assets:
  - {asset_1}
  - {asset_2}

  Gespeichert in: knowledge/labs/{folder}/

Nächste Schritte:
- Assets manuell herunterladen (falls nicht automatisch)
- /knowledge-search {topic} - In KB suchen
```


#### Example



**Code:**
```bash
Chrome MCP nicht erreichbar.
→ Bitte Chrome mit Claude Extension öffnen.
→ Dann erneut versuchen.
```


#### Example



**Code:**
```bash
Perplexity zeigt Login-Screen.
→ Bitte einloggen (Pro-Account für Labs erforderlich!)
→ Dann erneut versuchen.
```


#### Example



**Code:**
```bash
Labs-Option nicht gefunden.
→ Pro-Subscription erforderlich
→ Oder: Perplexity UI hat sich geändert - read_page für neue refs
```


#### Example



**Code:**
```bash
Lab dauert länger als 20 Minuten.
→ Aktueller Stand wird extrahiert.
→ Perplexity-Tab bleibt offen für manuellen Check.
```


#### Example



**Code:**
```bash
/lab "Detaillierte Marktanalyse: AI-generierte Kunst auf Etsy 2026"
```


#### Example



**Code:**
```bash
/lab "Interaktives Dashboard für Bitcoin, Ethereum, Solana Performance"
```


#### Example



**Code:**
```bash
/lab "Vergleichstabelle: Top 10 VPN-Anbieter mit Preisen und Features"
```


#### Example



**Code:**
```bash
/lab "Baue eine einfache Pomodoro-Timer Web-App"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/lab.md`</small>
