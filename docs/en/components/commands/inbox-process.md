---
title: inbox-process
type: command
tags: []
lang: en
confidence: 100
---

# inbox-process


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

Verarbeite Dateien aus der Inbox automatisch


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
📭 Inbox ist leer

Lege Dateien in _inbox/ ab und sage mir Bescheid!
```


#### Example



**Code:**
```bash
📬 {anzahl} Datei(en) in der Inbox gefunden

Starte Verarbeitung...
```


#### Example



**Code:**
```bash
Beschreibt es ein bestehendes Projekt?
├─ Ja → Projekt-README
└─ Nein
   └─ Ist es eine Anweisung/Prompt?
      ├─ Ja → Prompt
      └─ Nein
         └─ Beschreibt es eine neue Idee?
            ├─ Ja → Idee
            └─ Nein → Learning/Note
```


#### Example



**Code:**
```bash
📄 Datei: {filename}

Meine Analyse:
Typ: {typ} (Confidence: {score}/10)
{Kurze Begründung}

Stimmt das?
[1] Ja, korrekt
[2] Nein, es ist: {alternative Optionen}
```


#### Example



**Code:**
```bash
→ Führe /project-add aus

Nutze den Datei-Content als Input.
Importiere als README.
```


#### Example



**Code:**
```bash
→ Führe /knowledge-add aus

Type: prompt
Content: {Datei-Inhalt}
Auto-kategorisiere basierend auf Zweck
```


#### Example



**Code:**
```bash
→ Führe /idea-new aus

Beschreibung: {Datei-Inhalt}
Lass KI-Analyse wie gewohnt laufen
```


#### Example



**Code:**
```bash
→ Führe /knowledge-add aus

Type: learning oder note (je nachdem)
Content: {Datei-Inhalt}
```


#### Example



**Code:**
```bash
📄 Verarbeite: {filename}
   Typ: {typ}
   Workflow: {workflow}
   Status: ⏳ In Arbeit...
```


#### Example



**Code:**
```bash
   Status: ✅ Verarbeitet
   Gespeichert: {pfad zum neuen Dokument}
```


#### Example



**Code:**
```bash
✅ {filename} wurde verarbeitet als: {typ}
   Neuer Speicherort: {pfad}

Original-Datei in _inbox/ löschen?
[1] Ja, löschen
[2] Nein, behalten
[3] In Archiv verschieben
```


#### Example



**Code:**
```bash
═══════════════════════════════════
📬 Inbox-Verarbeitung abgeschlossen
═══════════════════════════════════

Verarbeitet: {anzahl} Datei(en)

Breakdown:
├─ Projekte: {anzahl}
├─ Prompts: {anzahl}
├─ Ideen: {anzahl}
└─ Knowledge: {anzahl}

Details:
────────────────────────────────────
✓ {filename} → {typ} → {speicherort}
✓ {filename} → {typ} → {speicherort}
...

Nächste Schritte:
• /idea-list - Neue Ideen anschauen
• /knowledge-search - Neues Wissen durchsuchen
• Weitere Dateien in _inbox/ ablegen
```


#### Example



**Code:**
```bash
❌ Fehler bei {filename}
   Grund: {error}
   Aktion: Übersprungen

→ Bitte prüfe die Datei
```


#### Example



**Code:**
```bash
❓ {filename} konnte nicht eindeutig kategorisiert werden

Inhalt scheint: {mögliche Typen}

Bitte gib an:
[1] Projekt
[2] Prompt
[3] Idee
[4] Learning/Note
[5] Überspringen
```


#### Example



**Code:**
```bash
❌ Fehler beim Verarbeiten von {filename}
   Workflow: {workflow}
   Fehler: {error}

Datei bleibt in _inbox/ für manuelle Verarbeitung.
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/inbox-process.md`</small>
