---
title: create-prompt
type: command
tags: []
lang: en
confidence: 100
---

# create-prompt


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

Erstelle optimierten Prompt und speichere für spätere Ausführung


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "questions": [{
    "question": "Welche Art von Task soll der Prompt lösen?",
    "header": "Task Type",
    "options": [
      {"label": "Research", "description": "Recherche, Analyse, Informationen sammeln"},
      {"label": "Creative", "description": "Texte, Ideen, Content erstellen"},
      {"label": "Strategy", "description": "Planung, Entscheidungen, Roadmaps"},
      {"label": "Technical", "description": "Code, Debugging, Implementation"}
    ],
    "multiSelect": false
  }]
}
```


#### Example



**Code:**
```bash
Ich erstelle einen Prompt für:

**Task**: {zusammenfassung}
**Typ**: {research|creative|strategy|technical}
**Ziel**: {was soll erreicht werden}
**Output**: {gewünschtes Ergebnis}

Proceed / Ask more / Add context?
```


#### Example



**Code:**
```xml
<analysis>
  <complexity>[simple|moderate|complex|research-grade]</complexity>
  <domain>[single|interdisciplinary|emergent]</domain>
  <type>[factual|analytical|creative|procedural|strategic]</type>
  <output_requirements>[brief|detailed|structured|iterative]</output_requirements>
  <ambiguity>[clear|moderate|high]</ambiguity>
</analysis>
```


#### Example



**Code:**
```xml
<context_extraction>
  <explicit_requirements>Was wurde direkt gefordert?</explicit_requirements>
  <implicit_needs>Was wird wahrscheinlich benötigt?</implicit_needs>
  <constraints>Zeit, Format, Ressourcen</constraints>
  <success_criteria>Woran wird Erfolg gemessen?</success_criteria>
</context_extraction>
```


#### Example



**Code:**
```bash
Faktenfragen     → Level 1 (Clear & Direct)
Analyse          → Level 2 (Structured CoT)
Kreativ          → Level 2 (Role + Context)
Multi-Step       → Level 3 (Chaining)
Research         → Level 4 (Extended Thinking)
Entscheidung     → Level 4 (Tree of Thought)
Strict Format    → Level 5 (Prefilling)
```


#### Example



**Code:**
```xml
<context>
  [Vollständige Hintergrundinformationen]
  [Wer, Was, Warum, Constraints]
</context>

<task>
  [Klare, spezifische Aufgabenbeschreibung]
  [Erfolgskriterien]
</task>

<examples>
  [2-3 Input/Output Paare wenn hilfreich]
</examples>

<output_format>
  [Exakte Formatvorgaben]
  [Struktur-Requirements]
</output_format>

<success_criteria>
  [Woran erkennt man dass die Aufgabe erfüllt ist]
</success_criteria>
```


#### Example



**Code:**
```xml
<objective>
  [Übergeordnetes Ziel]
</objective>

<phase_1>
  <name>[Phase Name]</name>
  <task>[Was in dieser Phase]</task>
  <output>[Erwartetes Zwischenergebnis]</output>
</phase_1>

<phase_2>
  <input>{{phase_1.output}}</input>
  <task>[Aufbauend auf Phase 1]</task>
  <output>[Erwartetes Ergebnis]</output>
</phase_2>

<synthesis>
  <inputs>{{all_phases}}</inputs>
  <final_deliverable>[Finales Ergebnis]</final_deliverable>
</synthesis>

<success_criteria>
  [Qualitätskriterien für das Endergebnis]
</success_criteria>
```


#### Example



**Code:**
```xml
<evolving_context>
  Nutze folgende Ressourcen wenn hilfreich:
  - Knowledge Base: knowledge/
  - Patterns: knowledge/patterns/
  - Prompts: knowledge/prompts/
  - Projects: knowledge/projects/
</evolving_context>
```


#### Example



**Code:**
```bash
□ Colleague Test: Würde Fachfremder verstehen was zu tun ist?
□ Context Complete: Ist ALLES nötige Wissen im Prompt?
□ Success Defined: Ist klar wann die Aufgabe erfüllt ist?
□ Output Specified: Ist das Format eindeutig?
□ Right Level: Nicht über- oder unter-engineered?
```


#### Example



**Code:**
```xml
<performance>
  <technique_level>[1-5]</technique_level>
  <estimated_tokens>[Input + Output]</estimated_tokens>
  <expected_latency>[schnell|moderat|länger]</expected_latency>
  <recommended_model>[haiku|sonnet|opus]</recommended_model>
</performance>
```


#### Example



**Code:**
```markdown
---
created: {YYYY-MM-DD}
type: {research|creative|strategy|technical}
level: {1-5}
model: {haiku|sonnet|opus}
status: ready
---

# {PROMPT_TITLE}

{DER GENERIERTE PROMPT}

---

## Metadata

**Erstellt von**: /create-prompt
**Ausführen mit**: /run-prompt {NNN}
```


#### Example



**Code:**
```bash
mkdir -p prompts
```


#### Example



**Code:**
```bash
Prompt erstellt und gespeichert!

**Datei**: prompts/{NNN}-{name}.md
**Level**: {1-5} ({technique})
**Model**: {empfohlen}

Was möchtest du tun?

1. **Run now** → /run-prompt {NNN}
2. **Review first** → Ich zeige den Prompt
3. **Save for later** → Fertig
4. **Edit** → Anpassungen machen
```


#### Example



**Code:**
```bash
User: /create-prompt Analysiere meine Etsy Konkurrenz

Claude: Ich erstelle einen Prompt für Konkurrenzanalyse.

        **Task**: Etsy Konkurrenzanalyse
        **Typ**: Research
        **Ziel**: Wettbewerber verstehen, Insights gewinnen

        Proceed / Ask more / Add context?

User: Proceed

Claude: [Analysiert → Level 2 Structured CoT]
        [Generiert Prompt mit XML-Struktur]
        [Speichert als prompts/004-etsy-competitor-analysis.md]

        Prompt erstellt!

        **Datei**: prompts/004-etsy-competitor-analysis.md
        **Level**: 2 (Structured CoT + Role)
        **Model**: sonnet

        1. Run now
        2. Review first
        3. Save for later

User: Run now

Claude: → /run-prompt 004
```


#### Example



**Code:**
```bash
Ich erkenne, dass dieser Task mehrere Prompts benötigt:

1. **Research Phase** → prompts/005-market-research.md
2. **Analysis Phase** → prompts/006-data-analysis.md
3. **Strategy Phase** → prompts/007-strategy-development.md

Execution:
- **Parallel**: 005 + 006 können gleichzeitig
- **Sequential**: 007 braucht Output von 005 + 006

Alle erstellen?
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/create-prompt.md`</small>
