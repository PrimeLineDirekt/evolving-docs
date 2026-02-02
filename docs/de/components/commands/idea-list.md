---
title: idea-list
type: command
tags: []
lang: en
confidence: 100
---

# idea-list


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

Zeige alle Ideen mit Filtern & Übersicht


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
=== Deine Ideen ({anzahl}) ===

🟢 ACTIVE ({anzahl})
─────────────────────
[1] {Titel} (⭐ 9/10)
    business/e-commerce · Updated: {datum}
    Next: {erste TODO}

[2] {Titel} (⭐ 8/10)
    tech/automation · Updated: {datum}
    Next: {erste TODO}

📝 DRAFT ({anzahl})
─────────────────────
[3] {Titel} (⭐ 6/10)
    content/creator · Created: {datum}

⏸️  PAUSED ({anzahl})
─────────────────────
[4] {Titel} (⭐ 7/10)
    business/saas · Paused since: {datum}

✓ COMPLETED ({anzahl})
─────────────────────
[5] {Titel} (⭐ 8/10)
    tech/automation · Completed: {datum}
```


#### Example



**Code:**
```bash
=== {Titel} ===
ID: {id}
Kategorie: {kategorie}
Status: {status}
Potential: {score}/10

{Erste 100 Zeichen der Beschreibung}...

Skills: {skills}
Related: {verwandte Ideen}

Progress:
{Anzahl Sessions} sessions · {Anzahl TODOs} open todos
Last: {letzte Session Zusammenfassung}

Next: /idea-work {id}
────────────────────────────────────
```


#### Example



**Code:**
```bash
=== Ideen-Statistiken ===

Total: {anzahl}
├─ Active: {anzahl}
├─ Draft: {anzahl}
├─ Paused: {anzahl}
└─ Completed: {anzahl}

By Category:
├─ business/*: {anzahl}
│  ├─ e-commerce: {anzahl}
│  └─ saas: {anzahl}
├─ tech/*: {anzahl}
└─ content/*: {anzahl}

By Potential:
├─ High (8-10): {anzahl}
├─ Medium (5-7): {anzahl}
└─ Low (1-4): {anzahl}

Top Ideas by Potential:
1. {titel} (⭐ 9/10) - {kategorie}
2. {titel} (⭐ 9/10) - {kategorie}
3. {titel} (⭐ 8/10) - {kategorie}

Most Recently Updated:
1. {titel} - {datum}
2. {titel} - {datum}
3. {titel} - {datum}

Insights:
- {AI-generierte Insights basierend auf Patterns}
```


#### Example



**Code:**
```bash
=== Ideen-Matrix (Potential vs. Effort) ===

High Potential
│
│  High Effort          │  Low Effort
│  ───────────────────  │  ─────────────────
│  • {Titel}            │  • {Titel} ⭐
│  • {Titel}            │  • {Titel} ⭐
│                       │
│  ────────────────────────────────────────
│
│  High Effort          │  Low Effort
│  • {Titel}            │  • {Titel}
│
Low Potential

⭐ = Quick Wins (High Potential, Low Effort) - Start hier!
```


#### Example



**Code:**
```bash
Aktionen:
[1] An Idee arbeiten - Gib Nummer/ID an
[2] Filter ändern
[3] View-Mode wechseln
[4] Verbindungen analysieren
[5] Neue Idee erfassen

Was möchtest du tun?
```


#### Example



**Code:**
```bash
Quick Commands:
/idea-work {nummer} - An Idee arbeiten
/idea-connect - Synergien finden
/idea-new - Neue Idee
```


#### Example



**Code:**
```bash
=== Skill-Gap Analyse ===

Häufig benötigte Skills die du noch entwickeln solltest:

1. React/Frontend (benötigt für 3 Ideen)
   • {Idee 1}
   • {Idee 2}
   • {Idee 3}

2. API Development (benötigt für 2 Ideen)
   • {Idee 1}
   • {Idee 2}

Empfehlung: Fokussiere auf {Skill} um {anzahl} Ideen umsetzen zu können.
```


#### Example



**Code:**
```bash
=== Verwaiste Ideen ===

Nicht bearbeitet seit 30+ Tagen:

• {Titel} - {Tage} Tage - Status: {status}
• {Titel} - {Tage} Tage - Status: {status}

Empfehlung:
- Archivieren oder reaktivieren?
- /idea-work {id} um weiterzumachen
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/idea-list.md`</small>
