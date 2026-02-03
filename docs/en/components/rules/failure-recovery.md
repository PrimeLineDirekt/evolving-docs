---
title: failure-recovery
type: rule
tags: []
lang: en
confidence: 100
---

# failure-recovery


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────────────┐
│ VERSUCH 1-2: Selbst fixen                                   │
│ • Mit Evidence (Build, Test, Verify)                        │
│ • Root Cause identifizieren, nicht raten                    │
└──────────────────────┬──────────────────────────────────────┘
                       │ Failure?
                       ▼
┌─────────────────────────────────────────────────────────────┐
│ VERSUCH 3: SUB-AGENT ANALYSE (PFLICHT!)                     │
│                                                             │
│ STOP selbst fixen! Stattdessen:                             │
│                                                             │
│ 1. Explore Agent: "Was erwartet Component A wirklich?"      │
│ 2. Explore Agent: "Was sendet Component B wirklich?"        │
│ 3. Debugger Agent: "E2E Flow verifizieren"                  │
│                                                             │
│ Agents liefern FAKTEN, kein Raten mehr.                     │
└──────────────────────┬──────────────────────────────────────┘
                       │ Immer noch unklar?
                       ▼
┌─────────────────────────────────────────────────────────────┐
│ VERSUCH 4: USER MIT AGENT-FINDINGS                          │
│                                                             │
│ Präsentiere:                                                │
│ • Was Agents gefunden haben                                 │
│ • Wo der Widerspruch liegt                                  │
│ • Konkrete Optionen zur Lösung                              │
└──────────────────────┬──────────────────────────────────────┘
                       │ User kann nicht helfen?
                       ▼
┌─────────────────────────────────────────────────────────────┐
│ BLOCKED: Dokumentieren + Memory loggen                      │
└─────────────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```bash
Parallel starten:
1. Explore Agent → Backend: "Welche Felder erwartet Endpoint X?"
2. Explore Agent → Frontend: "Welche Felder sendet Component Y?"
3. Debugger Agent → "E2E Request/Response verifizieren"
```


#### Example



**Code:**
```bash
1. Debugger Agent → "Analysiere Error-Stack, finde Root Cause"
2. Explore Agent → "Prüfe Dependencies und Imports"
```


#### Example



**Code:**
```bash
1. Explore Agent → "Alle relevanten Config-Files analysieren"
2. Debugger Agent → "Environment und Runtime prüfen"
```


#### Example



**Code:**
```bash
Problem erkannt
     │
     ▼
┌─ Fix #1 ─┐
│ Versuch  │──── Erfolg? ──→ DONE
└────┬─────┘
     │ Fail
     ▼
┌─ Fix #2 ─┐
│ Versuch  │──── Erfolg? ──→ DONE
└────┬─────┘
     │ Fail
     ▼
╔═══════════════════════════════════╗
║ FIX #3 = SUB-AGENT PFLICHT!       ║
║                                   ║
║ NICHT selbst weiter probieren.    ║
║ Agents für systematische Analyse. ║
╚═══════════════════════════════════╝
```


#### Example



**Code:**
```bash
Sub-Agents parallel:
├─ Explore Agent: Backend auth.py → "form.get('email')"
├─ Explore Agent: Frontend page.tsx → "formData.append('email')"
└─ Debugger Agent: curl Test → Verifiziert

Ergebnis: Backend erwartet EMAIL (Handoff war falsch)
Keine weiteren Loops.
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/rules/failure-recovery.md`</small>
