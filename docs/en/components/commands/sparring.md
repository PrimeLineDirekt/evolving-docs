---
title: sparring
type: command
tags: []
lang: en
confidence: 100
---

# sparring


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

Freies Brainstorming & Sparring (nicht Ideen-spezifisch)


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Sparring Session - Wähle einen Modus:

[1] 💭 Freies Brainstorming - Neue Ideen entwickeln
[2] 🎯 Problem-Solving - Spezifisches Problem lösen
[3] 🔍 Strategie-Entwicklung - Business/Projekt-Strategie
[4] 🌱 Opportunitäts-Scan - Neue Möglichkeiten finden
[5] 🤔 Devil's Advocate - Kritisch hinterfragen
[6] 📚 Wissens-Synthese - Verbinde bestehendes Wissen neu
[7] 🚀 Vision-Building - Große Zukunftspläne entwickeln

Oder beschreibe einfach woran du denken möchtest:
```


#### Example



**Code:**
```markdown
---
type: sparring
mode: {modus}
date: {datum}
topic: {thema}
duration: {optional}
tags: [{automatisch generiert}]
related_ideas: [{falls relevant}]
related_projects: [{falls relevant}]
---

# Sparring Session: {Thema}

## Modus
{Welcher Modus wurde verwendet}

## Thema/Frage
{Ursprüngliche Frage oder Thema}

## Diskussion

### Key Points
- {Punkt 1}
- {Punkt 2}
- {Punkt 3}

### Insights
- {Insight 1}
- {Insight 2}

### Entscheidungen/Conclusions
- {Entscheidung 1}
- {Entscheidung 2}

## Nächste Schritte
- [ ] {Action 1}
- [ ] {Action 2}
- [ ] {Action 3}

## Neue Ideen
{Falls neue Ideen entstanden sind}

## Zu vertiefen
{Themen die weiter erforscht werden sollten}

## Links
{Verbindungen zu Ideen/Projekten/Wissen}
```


#### Example



**Code:**
```bash
✓ Sparring Session beendet

Zusammenfassung:
{2-3 Sätze über die Session}

Key Insights:
• {Insight 1}
• {Insight 2}
• {Insight 3}

Nächste Schritte:
{Action items}

Session gespeichert: knowledge/sessions/sparring-{datum}.md

Weitere Aktionen:
/idea-new - Neue Idee aus dieser Session
/sparring - Neue Session starten
/knowledge-search - Verwandtes Wissen finden
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/sparring.md`</small>
