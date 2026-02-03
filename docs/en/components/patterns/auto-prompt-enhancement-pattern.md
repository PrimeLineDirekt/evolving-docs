---
title: auto-prompt-enhancement-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# auto-prompt-enhancement-pattern


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
User Input (Simple)
       │
       ▼
┌──────────────────────────────────────────────────────────┐
│              AUTO-ENHANCEMENT PIPELINE                    │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │  ANALYZER   │→ │  EXTRACTOR  │→ │  ENHANCER   │      │
│  │ (Complexity)│  │  (Context)  │  │ (Technique) │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│         │                │                │              │
│         ▼                ▼                ▼              │
│    Level 1-5        Relevant         Enhanced            │
│    Assessment       Context          Prompt              │
└──────────────────────────────────────────────────────────┘
       │
       ▼
Enhanced Prompt (Complex)
```


#### Example



**Code:**
```python
def classify_complexity(prompt):
    # Level 1 Indicators
    if is_factual_question(prompt):
        return 1

    # Level 2 Indicators
    if needs_explanation(prompt) or needs_examples(prompt):
        return 2

    # Level 3 Indicators
    if is_multi_step(prompt) or is_creation_task(prompt):
        return 3

    # Level 4 Indicators
    if is_research(prompt) or is_strategic(prompt):
        return 4

    # Level 5 Indicators
    if needs_strict_format(prompt) or is_edge_case(prompt):
        return 5

    return 2  # Default: moderate enhancement
```


#### Example



**Code:**
```python
def extract_context(prompt, session):
    context = {}

    # 1. Session Context
    context['recent'] = get_relevant_messages(session, limit=5)
    context['decisions'] = get_session_decisions(session)

    # 2. Domain Memory
    active_project = read_memory_index()
    if active_project:
        context['project'] = read_project_memory(active_project)

    # 3. Knowledge Base (keyword-matched)
    keywords = extract_keywords(prompt)
    context['knowledge'] = search_knowledge_base(keywords)

    # 4. Experience Memory
    context['experiences'] = search_experiences(keywords)

    return context
```


#### Example



**Code:**
```xml
<!-- Level 2 Enhancement -->
<context>
  {EXTRACTED_CONTEXT}
</context>

<role>
  Du bist ein Experte für {DOMAIN}.
</role>

<task>
  {ORIGINAL_PROMPT}
</task>

<output_format>
  {STRUCTURE_HINT}
</output_format>
```


#### Example



**Code:**
```xml
<!-- Level 3+ Enhancement -->
<objective>
  {GOAL_FROM_PROMPT}
</objective>

<context>
  {EXTRACTED_CONTEXT}
</context>

<phase_1>
  <name>Analyse</name>
  <task>{DECOMPOSED_STEP_1}</task>
</phase_1>

<phase_2>
  <name>Synthese</name>
  <task>{DECOMPOSED_STEP_2}</task>
</phase_2>

<success_criteria>
  {INFERRED_CRITERIA}
</success_criteria>
```


#### Example



**Code:**
```bash
User: "Hilf mir mit meiner Etsy SEO"

System (intern):
  1. Complexity: Level 3 (multi-step task)
  2. Context: Active project = ThriveVibesArt,
              Known: Etsy SEO Patterns, Pinterest Integration
  3. Enhance: Add structure, inject knowledge

Enhanced Prompt (intern):
  <context>
    Projekt: ThriveVibesArt (Etsy Shop)
    Bekannte Patterns: Keyword Research, Title Structure
    Ziel: Listing-Optimierung
  </context>

  <task>
    Unterstütze bei Etsy SEO Optimierung
  </task>

  <phases>
    1. Keyword-Analyse
    2. Title-Optimierung
    3. Tag-Strategie
  </phases>

User sieht: Strukturierte, fundierte Antwort
```


#### Example



**Code:**
```bash
/run-prompt 004 --enhance

oder

/create-prompt --auto "Analysiere meinen Markt"
```


#### Example



**Code:**
```python
ENHANCEMENT_THRESHOLD = 2  # Nur Level 2+ enhancen

if complexity >= ENHANCEMENT_THRESHOLD:
    enhance(prompt)
else:
    execute_directly(prompt)
```


#### Example



**Code:**
```markdown
/enhance [prompt]

→ Analysiert Komplexität
→ Extrahiert Kontext
→ Zeigt enhanced Prompt
→ Fragt: "Ausführen?"
```


#### Example



**Code:**
```markdown
/create-prompt --auto [task]

→ Alles automatisch
→ Optimales Level wählen
→ Kontext injizieren
→ Als Datei speichern
→ Optional direkt ausführen
```


#### Example



**Code:**
```python
Task(
    prompt=prompt,
    auto_enhance=True,  # NEU
    subagent_type="general-purpose"
)
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/patterns/auto-prompt-enhancement-pattern.md`</small>
