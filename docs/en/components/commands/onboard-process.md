---
title: onboard-process
type: command
tags: []
lang: en
confidence: 100
---

# onboard-process


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

Verarbeite ausgefüllten Onboarding-Fragebogen


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
❌ _ONBOARDING.md nicht gefunden

Soll ich das Onboarding-Dokument erstellen?
Falls du es schon ausgefüllt hast, prüfe den Dateinamen.
```


#### Example



**Code:**
```bash
📋 _ONBOARDING.md gefunden aber scheint noch leer zu sein

Möchtest du:
[1] Trotzdem verarbeiten (falls minimal ausgefüllt)
[2] Abbrechen und erst ausfüllen
```


#### Example



**Code:**
```bash
═══════════════════════════════════
📋 Onboarding-Fragebogen Analyse
═══════════════════════════════════

Gefundene Informationen:

✓ Persönliche Infos: Ja
✓ Skills: {anzahl} Technical, {anzahl} Business, {anzahl} Soft
✓ Projekte: {anzahl} gefunden
✓ Ideen: {anzahl} gefunden
✓ Prompts: {anzahl} gefunden
✓ Learnings: {anzahl} gefunden
✓ Ziele & Vision: Ja
✓ Interessen: {anzahl} Themen

Details:
────────────────────────────────────

Projekte:
1. {Projekt-Name} - {Status}
2. {Projekt-Name} - {Status}

Ideen:
1. {Ideen-Titel}
2. {Ideen-Titel}

Prompts:
1. {Prompt-Name}
2. {Prompt-Name}

────────────────────────────────────

Ich werde jetzt:
→ Persönliche Infos in about-me.md einpflegen
→ Skills in skills.md einpflegen
→ {anzahl} Projekte mit /project-add verarbeiten
→ {anzahl} Ideen mit /idea-new erfassen
→ {anzahl} Prompts mit /knowledge-add speichern
→ {anzahl} Learnings mit /knowledge-add speichern

Soll ich fortfahren?
[Ja / Nein / Zeig mir mehr Details]
```


#### Example



**Code:**
```markdown
# About Me

## Persönliche Informationen
**Name**: {aus Fragebogen}
**Hintergrund**: {aus Fragebogen}
**Standort**: {aus Fragebogen}
**Status**: {aus Fragebogen}

## Working Style
{aus Fragebogen: Arbeitsweise}

## Motivation & Antrieb
{aus Fragebogen: Was treibt dich an}

## Ziele

### Kurzfristig (3 Monate)
{aus Abschnitt F}

### Mittelfristig (1 Jahr)
{aus Abschnitt F}

### Langfristig (3-5 Jahre)
{aus Abschnitt F}

## Interessen & Themen
{aus Abschnitt G}
- {Thema 1}
- {Thema 2}

## Communities & Netzwerke
{aus Abschnitt G}

{Behalte bestehenden Content, füge neues hinzu}
```


#### Example



**Code:**
```markdown
# Skills

## Technical Skills

### Programmierung
{aus Fragebogen - merge mit bestehendem}

### Tools & Plattformen
{aus Fragebogen - merge}

### AI & Automation
{aus Fragebogen - merge}

## Business Skills

### Marketing & Sales
{aus Fragebogen - merge}

### E-Commerce
{aus Fragebogen - merge}

## Soft Skills

### Kreativität & Innovation
{aus Fragebogen}

### Analytisches Denken
{aus Fragebogen}

## Skills zu entwickeln
{aus Abschnitt B: "Skills die ich lernen möchte"}
```


#### Example



**Code:**
```bash
   Status: ✅ Verarbeitet
   Gespeichert: knowledge/projects/{name}/
```


#### Example



**Code:**
```bash
   Status: ✅ Erfasst
   ID: idea-2024-001
   Potential: {score}/10
```


#### Example



**Code:**
```bash
   Status: ✅ Gespeichert
   Pfad: knowledge/prompts/{category}/{name}.md
```


#### Example



**Code:**
```bash
═══════════════════════════════════
✅ Onboarding abgeschlossen!
═══════════════════════════════════

Erfolgreich verarbeitet:

📋 Persönliche Informationen
   → knowledge/personal/about-me.md (updated)

🎯 Skills
   → knowledge/personal/skills.md (updated)
   → {anzahl} neue Skills hinzugefügt
   → {anzahl} bestehende Skills erweitert

📦 Projekte: {anzahl}
   ✓ {Projekt 1} → knowledge/projects/{name}/
   ✓ {Projekt 2} → knowledge/projects/{name}/
   Skills extrahiert: {skills}

💡 Ideen: {anzahl}
   ✓ {Idee 1} - idea-2024-001 (Potential: {score}/10)
   ✓ {Idee 2} - idea-2024-002 (Potential: {score}/10)

📝 Prompts: {anzahl}
   ✓ {Prompt 1} → knowledge/prompts/...
   ✓ {Prompt 2} → knowledge/prompts/...

🎓 Learnings: {anzahl}
   ✓ {Learning 1} → knowledge/learnings/...
   ✓ {Learning 2} → knowledge/learnings/...

════════════════════════════════════

Dein System kennt dich jetzt!

Nächste Schritte:
• /idea-list - Schau dir deine Ideen an
• /idea-connect - Finde Synergien
• /knowledge-search - Durchsuche dein Wissen
```


#### Example



**Code:**
```bash
📄 _ONBOARDING.md wurde vollständig verarbeitet

Soll ich die Original-Datei jetzt löschen?

[1] Ja, löschen (empfohlen)
[2] Nein, behalten
[3] In Archiv verschieben (_ONBOARDING_backup.md)
```


#### Example



**Code:**
```bash
✓ _ONBOARDING.md gelöscht
```


#### Example



**Code:**
```bash
✓ Datei behalten - du findest sie weiterhin im Root
```


#### Example



**Code:**
```bash
✓ Umbenannt zu: _ONBOARDING_backup.md
```


#### Example



**Code:**
```bash
💡 Empfohlene nächste Schritte:

Basierend auf deinen Informationen:

1. **Synergien finden**
   → /idea-connect
   Deine {anzahl} Ideen könnten Synergien haben!

2. **Skill-Gap Analyse**
   → /idea-list gaps
   Zeigt welche Skills für Ideen fehlen

3. **Erste Idee ausarbeiten**
   → /idea-work {top-potential-idee}
   Starte mit deiner Top-Idee (Potential: {score}/10)

4. **Wissen durchsuchen**
   → /knowledge-search {relevantes-thema}
   Entdecke Verbindungen in deinem Wissen

Was möchtest du tun?
```


#### Example



**Code:**
```bash
⚠️ Warnung: Abschnitt {name} konnte nicht vollständig geparst werden

Gefunden: {was ich verstanden habe}
Unklar: {was fehlt}

Soll ich:
[1] Mit dem was ich habe fortfahren
[2] Dich fragen wie ich es interpretieren soll
[3] Diesen Abschnitt überspringen
```


#### Example



**Code:**
```bash
❌ Fehler beim Verarbeiten von {item}
   Workflow: {workflow}
   Fehler: {error-message}

Ich fahre mit den anderen Items fort.
Dieses Item kannst du später manuell hinzufügen.
```


#### Example



**Code:**
```bash
⚠️ Projekt "{name}" existiert bereits in knowledge/projects/

Soll ich:
[1] Überschreiben mit neuen Infos
[2] Merge (bestehend + neu kombinieren)
[3] Überspringen
[4] Als neues Projekt "{name}-2" speichern
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/onboard-process.md`</small>
