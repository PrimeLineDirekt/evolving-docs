---
title: recursive-research-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# recursive-research-pattern


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
Komplexe Frage
      ↓
  Orchestrator
      ↓
┌─────┼─────┐
│     │     │
R1    R2    R3   (Researchers parallel)
│           │
├──┐     ┌──┤
S1 S2   S3 S4   (Sub-agents rekursiv)
│     │
└──┬──┘
   ↓
SYNTHESIS
```


#### Example



**Code:**
```markdown
Bevor du antwortest, IMMER fragen:
"Gibt es mehrere Perspektiven die Exploration verdienen?"

WENN JA:
  → Spawne Sub-Agents für jede Perspektive
  → Sammle alle Findings
  → Synthetisiere zu kohärentem Ergebnis

WENN NEIN:
  → Antworte direkt mit Bias zu gründlicher Untersuchung
```


#### Example



**Code:**
```bash
WICHTIG: Haiku-Researchers spawnen KEINE Sub-Researchers.
→ Für tiefe Rekursion: Mindestens Sonnet als Researcher
```


#### Example



**Code:**
```bash
Atomic (direkt beantworten):
- "Was ist die Definition von X?"
- "Wann wurde Y erfunden?"
- Faktenfragen mit klarer Antwort

Decomposable (Sub-Agents spawnen):
- "Warum treffen intelligente Menschen schlechte Entscheidungen?"
- "Was macht gute Software-Architektur aus?"
- Fragen mit mehreren Dimensionen
```


#### Example



**Code:**
```typescript
function shouldDecompose(question: string): boolean {
  const signals = [
    question.includes('warum'),
    question.includes('wie'),
    question.includes('was macht'),
    question.split(' ').length > 10,
    hasMultipleDimensions(question)
  ];

  return signals.filter(Boolean).length >= 2;
}
```


#### Example



**Code:**
```markdown
# Research Report: {Question}

## Methodology
- Orchestrator: {model}
- Researchers: {model}
- Sub-agent Depth: {max_depth}
- Total Agents: {count}

## Findings by Dimension

### 1. Technical & Structural
{findings}

### 2. Human & Social
{findings}

### 3. Business & Economic
{findings}

### 4. Context-Dependence
| Factor | Startup | Enterprise |
|--------|---------|------------|
| {x}    | {y}     | {z}        |

### 5. Evolution Over Time
- Phase 1: {description}
- Phase 2: {description}
- Phase 3: {description}

### 6. Decision Framework
{criteria}

## Synthesis
{integrative_conclusion}

## Meta-Principle
{one_sentence_truth}

## Practical Application
1. {question_1}
2. {question_2}
...
```


#### Example



**Code:**
```bash
#!/bin/bash

MODEL="${1:-opus}"
RESEARCHER="${2:-sonnet}"
QUESTION="$3"
WEB_FLAG="${4:-}"

# Agent DNA - wird vererbt
PROMPT="Du bist ein Research Agent.

CORE INSTRUCTION:
Bevor du antwortest, frage: 'Gibt es mehrere Perspektiven?'
- JA → Spawne Sub-Agents, synthetisiere
- NEIN → Antworte direkt

TO SPAWN SUB-AGENT:
claude -p '[sub-question]' --model $RESEARCHER --allowedTools 'Bash(claude:*)'

QUESTION: $QUESTION"

# Ausführen
claude -p "$PROMPT" \
  --model "$MODEL" \
  --allowedTools "Bash(claude:*)" \
  $WEB_FLAG
```


#### Example



**Code:**
```bash
# Agent erkennt: "Diese Frage hat 3 Perspektiven"
# Agent generiert:

claude -p "Perspektive 1: Technische Sicht auf X" --model sonnet &
claude -p "Perspektive 2: Business-Sicht auf X" --model sonnet &
claude -p "Perspektive 3: User-Sicht auf X" --model sonnet &

wait  # Alle parallel, dann sammeln
```


#### Example



**Code:**
```bash
#!/bin/bash

# Aktive Agents zählen
active=$(ps aux | grep "claude -p" | grep -v grep | wc -l)
echo "Active agents: $active"

# Agent Details
ps aux | grep "claude -p" | grep -v grep | while read line; do
  question=$(echo "$line" | sed 's/.*-p ["\x27]*\([^"\x27]*\).*/\1/' | cut -c1-80)
  model=$(echo "$line" | grep -o '\-\-model [a-z]*' | cut -d' ' -f2)
  echo "  [$model] $question..."
done

# Report Status
echo "Reports:"
ls -d reports/2025* 2>/dev/null | while read dir; do
  if [ -f "$dir/SYNTHESIS.md" ]; then
    lines=$(wc -l < "$dir/SYNTHESIS.md")
    echo "  ✓ $dir ($lines lines)"
  else
    echo "  ◌ $dir (in progress)"
  fi
done
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/patterns/recursive-research-pattern.md`</small>
