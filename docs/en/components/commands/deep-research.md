---
title: deep-research
type: command
tags: []
lang: en
confidence: 100
---

# deep-research


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

Deep Research für komplexe Themen (wahlweise WebSearch oder Perplexity)


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Was möchtest du recherchieren?

Bitte beschreibe:
1. **Thema**: Was genau?
2. **Tiefe**: Oberflächlich / Standard / Deep Dive?
3. **Fokus**: Fakten / Meinungen / Technisch / Markt?
```


#### Example



**Code:**
```bash
Wie soll ich recherchieren?

[1] Herkömmlich (WebSearch)
    → Mehrere Web-Suchen, Token-intensiv
    → Gut für: Schnelle Fakten, aktuelle News

[2] Perplexity Deep Research (Empfohlen)
    → Chrome-Automation, Token-sparend
    → Gut für: Komplexe Themen, tiefe Analysen
    → Dauert: 2-5 Minuten
```


#### Example



**Code:**
```markdown
## Research-Plan

**Thema**: {topic}
**Haupt-Frage**: {main_question}
**Sub-Fragen**:
1. {sub_question_1}
2. {sub_question_2}
3. {sub_question_3}

**Optimierte Query für Perplexity**:
"{optimized_query}"
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
# Finde den "Forschung" Radio-Button
page = read_page(tabId=TAB_ID, filter="interactive")
# Suche nach: radio "Forschung" [ref_XX]

# Klicke auf "Forschung"
computer(action="left_click", ref="ref_XX", tabId=TAB_ID)
```


#### Example



**Code:**
```python
# Finde das Textfeld
# Suche nach: textbox [ref_YY]

# Query eingeben
form_input(ref="ref_YY", value="{optimized_query}", tabId=TAB_ID)

# Enter drücken
computer(action="key", text="Return", tabId=TAB_ID)
```


#### Example



**Code:**
```python
# Polling-Loop
MAX_ITERATIONS = 60  # 60 * 10s = 10 Minuten
INTERVAL = 10  # Sekunden

for i in range(MAX_ITERATIONS):
    computer(action="wait", duration=INTERVAL, tabId=TAB_ID)

    text = get_page_text(tabId=TAB_ID)

    # Check ob Research fertig
    if "Sources" in text and "Searching" not in text:
        break

    # Progress-Update alle 30 Sekunden
    if i % 3 == 0:
        print(f"Research läuft... ({i * 10}s)")

# Timeout-Warnung
if i >= MAX_ITERATIONS - 1:
    print("TIMEOUT: Research dauert länger als erwartet")
```


#### Example



**Code:**
```python
# Finalen Text holen
result = get_page_text(tabId=TAB_ID)

# Optional: Screenshot für Dokumentation
computer(action="screenshot", tabId=TAB_ID)
```


#### Example



**Code:**
```markdown
## Deep Research Ergebnis

**Thema**: {topic}
**Methode**: {Herkömmlich | Perplexity}
**Dauer**: ~{duration}

### Kernerkenntnisse

1. **{finding_1}**
   {details}

2. **{finding_2}**
   {details}

3. **{finding_3}**
   {details}

### Quellen

{Bei Perplexity: Aus dem extrahierten Text}
{Bei WebSearch: Aus den Search-Ergebnissen}

### Offene Fragen

- {question_1}
- {question_2}

### Empfohlene nächste Schritte

1. {next_step_1}
2. {next_step_2}
```


#### Example



**Code:**
```bash
Chrome MCP nicht erreichbar.
→ Automatischer Fallback auf herkömmliche WebSearch.
```


#### Example



**Code:**
```bash
Perplexity zeigt Login-Screen.
→ Bitte einloggen und erneut versuchen.
```


#### Example



**Code:**
```bash
Research dauert länger als 10 Minuten.
→ Aktuellen Stand wird extrahiert.
→ Kann später fortgesetzt werden.
```


#### Example



**Code:**
```bash
/deep-research "Aktuelle Entwicklungen im Bereich KI-Agenten 2026"
```


#### Example



**Code:**
```bash
/deep-research "Vergleich von n8n vs Make vs Zapier für KI-Workflows"
```


#### Example



**Code:**
```bash
/deep-research "Best Practices für Claude Code Hooks und Memory-Systeme"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/deep-research.md`</small>
