---
title: run-prompt
type: command
tags: []
lang: en
confidence: 100
---

# run-prompt


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

Führe gespeicherte Prompts in frischem Sub-Agent Kontext aus


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
/run-prompt              → Letzten/neuesten Prompt
/run-prompt 004          → Prompt Nummer 004
/run-prompt seo          → Prompt mit "seo" im Namen
/run-prompt 004 005 006  → Mehrere Prompts
/run-prompt 004 005 --parallel   → Parallel ausführen
/run-prompt 004 005 --sequential → Sequentiell ausführen
```


#### Example



**Code:**
```python
args = parse($ARGUMENTS)

if args.empty:
    mode = "latest"
    prompts = [get_latest_prompt()]

elif args.is_single_number:
    mode = "single"
    prompts = [resolve_by_number(args[0])]

elif args.is_single_text:
    mode = "single"
    prompts = [resolve_by_name(args[0])]

elif args.is_multiple:
    mode = "parallel" if "--parallel" in args else "sequential"
    prompts = [resolve(x) for x in args if not x.startswith("--")]
```


#### Example



**Code:**
```python
all_prompts = Glob("prompts/*.md")

# Sortiert nach Nummer
# prompts/001-xxx.md
# prompts/002-xxx.md
# ...
```


#### Example



**Code:**
```python
def resolve_by_number(num):
    pattern = f"prompts/{num.zfill(3)}-*.md"
    matches = Glob(pattern)
    if len(matches) == 1:
        return matches[0]
    elif len(matches) == 0:
        error(f"Kein Prompt mit Nummer {num} gefunden")
    else:
        error(f"Mehrere Matches - bitte spezifischer")
```


#### Example



**Code:**
```python
def resolve_by_name(name):
    matches = [p for p in all_prompts if name.lower() in p.lower()]
    if len(matches) == 1:
        return matches[0]
    elif len(matches) == 0:
        error(f"Kein Prompt mit '{name}' gefunden")
    else:
        show_options(matches)
        ask("Welchen meinst du?")
```


#### Example



**Code:**
```bash
Mehrere Prompts gefunden für "analysis":

1. prompts/002-competitor-analysis.md
2. prompts/005-market-analysis.md
3. prompts/008-data-analysis.md

Welchen möchtest du ausführen? (Nummer oder genauerer Name)
```


#### Example



**Code:**
```python
prompt_content = Read(prompt_path)
```


#### Example



**Code:**
```yaml
---
created: 2025-12-01
type: research
level: 3
model: opus
status: ready
---
```


#### Example



**Code:**
```python
if metadata.status != "ready":
    warn(f"Prompt Status: {metadata.status}")
    ask("Trotzdem ausführen?")

if metadata.model != current_model:
    info(f"Empfohlenes Model: {metadata.model}")
    ask("Mit empfohlenem Model ausführen?")
```


#### Example



**Code:**
```python
def execute_single(prompt_path):
    prompt = Read(prompt_path)

    # Nutze Task Tool für Sub-Agent Kontext
    result = Task(
        prompt=prompt,
        subagent_type="general-purpose",
        model=metadata.model or "sonnet"
    )

    return result
```


#### Example



**Code:**
```python
def execute_parallel(prompts):
    # ALLE Task-Calls in EINER Message
    # Das ist kritisch für echte Parallelität

    results = []
    for prompt in prompts:
        # Diese werden parallel gestartet
        Task(prompt=Read(prompt), subagent_type="general-purpose")

    # Warte auf alle
    return aggregate_results(results)
```


#### Example



**Code:**
```bash
Starte parallele Ausführung:

🔄 prompts/004-market-research.md
🔄 prompts/005-competitor-analysis.md
🔄 prompts/006-trend-research.md

[Alle laufen gleichzeitig...]
```


#### Example



**Code:**
```python
def execute_sequential(prompts):
    results = []

    for i, prompt in enumerate(prompts):
        info(f"Schritt {i+1}/{len(prompts)}: {prompt}")

        # Vorherige Ergebnisse als Kontext
        context = results[-1] if results else None

        result = Task(
            prompt=Read(prompt),
            context=context,
            subagent_type="general-purpose"
        )

        results.append(result)

    return results
```


#### Example



**Code:**
```bash
Starte sequentielle Ausführung:

✅ 1/3: prompts/004-research.md (fertig)
🔄 2/3: prompts/005-analysis.md (läuft...)
⏳ 3/3: prompts/006-strategy.md (wartet)
```


#### Example



**Code:**
```bash
## Ergebnis: {PROMPT_NAME}

{RESULT_CONTENT}

---

**Prompt**: prompts/{NNN}-{name}.md
**Model**: {model}
**Dauer**: ~{sekunden}s
```


#### Example



**Code:**
```bash
## Ergebnisse

### 1. {PROMPT_1_NAME}
{RESULT_1}

### 2. {PROMPT_2_NAME}
{RESULT_2}

---

**Ausführung**: {parallel|sequential}
**Prompts**: {anzahl}
**Gesamt-Dauer**: ~{sekunden}s
```


#### Example



**Code:**
```bash
Prompt erfolgreich ausgeführt!

Optionen:
1. **Archive** → Nach prompts/archive/ verschieben
2. **Keep** → Für spätere Wiederverwendung behalten
3. **Delete** → Prompt löschen
```


#### Example



**Code:**
```bash
prompts/
├── 001-active-prompt.md
├── 002-another-prompt.md
└── archive/
    ├── 2025-12-01/
    │   ├── 001-old-prompt.md
    │   └── 002-another-old.md
    └── 2025-12-02/
        └── ...
```


#### Example



**Code:**
```bash
Änderungen durch Prompt-Ausführung:

Modified:
- src/components/Header.tsx
- src/styles/main.css

Created:
- src/components/NewFeature.tsx

Git commit erstellen?
```


#### Example



**Code:**
```bash
[prompt]: {kurze beschreibung}

Executed: prompts/{NNN}-{name}.md
Type: {research|creative|strategy|technical}
```


#### Example



**Code:**
```bash
❌ Prompt nicht gefunden

Gesucht: {input}
Verfügbare Prompts:
- 001-etsy-seo.md
- 002-competitor-analysis.md
- 003-pricing-strategy.md

Tipp: Nutze Nummer oder Teil des Namens
```


#### Example



**Code:**
```bash
❌ Fehler bei Ausführung

Prompt: prompts/{NNN}-{name}.md
Error: {error_message}

Optionen:
1. **Retry** - Nochmal versuchen
2. **Edit** - Prompt anpassen
3. **Abort** - Abbrechen
```


#### Example



**Code:**
```bash
⚠️ Teilweise erfolgreich

✅ prompts/004-research.md - OK
❌ prompts/005-analysis.md - Error: {reason}
✅ prompts/006-strategy.md - OK

Fehlgeschlagenen Prompt erneut versuchen?
```


#### Example



**Code:**
```bash
/run-prompt 004

→ Lädt prompts/004-etsy-competitor-analysis.md
→ Führt in Sub-Agent aus
→ Zeigt Ergebnis
```


#### Example



**Code:**
```bash
/run-prompt seo

→ Findet prompts/001-etsy-seo-optimization.md
→ Führt aus
→ Zeigt Ergebnis
```


#### Example



**Code:**
```bash
/run-prompt 004 005 006 --parallel

→ Startet alle drei gleichzeitig
→ Wartet auf alle
→ Zeigt aggregierte Ergebnisse
```


#### Example



**Code:**
```bash
/run-prompt 004 005 006 --sequential

→ Führt 004 aus
→ Nutzt Ergebnis als Kontext für 005
→ Nutzt Ergebnis als Kontext für 006
→ Zeigt finale Ergebnisse
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/run-prompt.md`</small>
