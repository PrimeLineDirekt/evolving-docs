---
title: loop-until-done
type: command
tags: []
lang: en
confidence: 100
---

# loop-until-done


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

Task mit klarem Completion-Kriterium iterativ ausführen bis fertig


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
# TypeScript Errors fixen bis Build grün
/loop-until-done "Fix alle TypeScript errors" --verify "npx tsc --noEmit" --max 15

# Tests grün machen
/loop-until-done "Alle Tests müssen passen" --verify "npm test" --max 10

# Custom Completion-Signal
/loop-until-done "Implementiere Feature X" --completion "DONE" --max 25
```


#### Example



**Code:**
```markdown
---
iteration: 1
max_iterations: {MAX}
completion_promise: "{COMPLETION}"
verify: "{VERIFY_CMD}"
started: {ISO_TIMESTAMP}
---

{TASK_TEXT}
```


#### Example



**Code:**
```markdown
---
iteration: 1
max_iterations: 15
completion_promise: "DONE"
verify: "npx tsc --noEmit"
started: 2026-01-07T12:00:00
---

Fix alle TypeScript errors in diesem Projekt.
Prüfe jeden Error, verstehe die Ursache, und behebe ihn.
```


#### Example



**Code:**
```bash
🔄 Ralph Loop gestartet!

Task: {TASK}
Max Iterationen: {MAX}
Verify: {VERIFY oder "nicht gesetzt"}
Completion: <promise>{COMPLETION}</promise>

Loop läuft bis:
- Verify-Command erfolgreich ODER
- Completion-Promise ausgegeben ODER
- Max Iterationen erreicht

Abbrechen: /cancel-ralph
```


#### Example



**Code:**
```bash
1. Du rufst /loop-until-done auf
   ↓
2. State-Datei wird erstellt
   ↓
3. Du arbeitest am Task
   ↓
4. Du versuchst zu stoppen (oder Task ist "fertig")
   ↓
5. Stop-Hook prüft:
   │
   ├─ Verify-Command passed? → EXIT ✅
   ├─ <promise>X</promise> gefunden? → EXIT ✅
   ├─ Max Iterationen erreicht? → EXIT ✅
   │
   └─ Sonst: BLOCK EXIT, gleicher Prompt zurück 🔄
```


#### Example



**Code:**
```bash
<promise>DONE</promise>
```


#### Example



**Code:**
```bash
/cancel-ralph
```


#### Example



**Code:**
```bash
# GUT: Klares Verify-Command
/loop-until-done "Fix types" --verify "npx tsc --noEmit"

# SCHLECHT: Kein Verify
/loop-until-done "Verbessere den Code"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/loop-until-done.md`</small>
