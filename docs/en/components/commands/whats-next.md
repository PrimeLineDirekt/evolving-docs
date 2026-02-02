---
title: whats-next
type: command
tags: []
lang: en
confidence: 100
---

# whats-next


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

Session-Handoff erstellen für Kontextwechsel oder Pause


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
1. Agent starten (whats-next Agent)
2. Agent macht ALLES autonom:
   - Memory lesen
   - Plan analysieren
   - Handoff schreiben
   - Memory updaten
3. Ergebnis dem User mitteilen
```


#### Example



**Code:**
```bash
Task Tool aufrufen:
- subagent_type: "general-purpose"
- model: "sonnet"
- prompt: "Du bist der whats-next Agent. Lies ~/.claude/agents/whats-next.md und führe den kompletten Workflow aus. Gib am Ende NUR den Handoff-Pfad zurück im Format: HANDOFF_CREATED: {pfad}"
```


#### Example



**Code:**
```bash
Task Tool aufrufen:
- subagent_type: "general-purpose"
- model: "sonnet"
- run_in_background: true
- prompt: (gleicher Prompt)
```


#### Example



**Code:**
```bash
✅ Handoff erstellt!

📋 **Für nächste Session kopieren:**
@_handoffs/{filename}.md

💡 Session benennen? `/rename {name}` für einfaches Fortsetzen
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/whats-next.md`</small>
