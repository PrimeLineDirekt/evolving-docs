---
title: create-skill
type: command
tags: []
lang: en
confidence: 100
---

# create-skill


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

Erstellt neuen Skill aus Template


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Simple:
  - Kann in <500 Zeilen erklärt werden
  - Straightforward use case
  - Wenig Sub-Topics
  - Hauptsächlich Guidelines/Rules

Progressive:
  - Komplexer Domain (>500 Zeilen nötig)
  - Multiple Sub-Topics
  - Needs detailed reference
  - Benefits from examples
```


#### Example



**Code:**
```bash
.claude/templates/skills/simple-skill/SKILL.md
```


#### Example



**Code:**
```bash
.claude/templates/skills/progressive-skill/SKILL.md
.claude/templates/skills/progressive-skill/reference.md
.claude/templates/skills/progressive-skill/examples.md
```


#### Example



**Code:**
```yaml
---
name: {skill-name}  # lowercase-with-hyphens
description: "{DESCRIPTION mit Trigger-Hints}"
allowed-tools: {TOOL_1}, {TOOL_2}, {TOOL_3}
---
```


#### Example



**Code:**
```bash
"PDF Processing Skill. Aktiviert bei 'analyze pdf', 'extract from pdf'.
Supports text extraction, table analysis, metadata extraction."
```


#### Example



**Code:**
```yaml
description: "{Description MIT Trigger-Keywords}"
```


#### Example



**Code:**
```markdown
### Skills: {SKILL_NAME}

**Trigger-Keywords**:
- {KEYWORD_1}
- {KEYWORD_2}

**Auto-Activation**: {WHEN_TO_ACTIVATE}
```


#### Example



**Code:**
```bash
✓ {SKILL_NAME} Skill erfolgreich erstellt!

{Simple}
Datei: .claude/skills/{name}/SKILL.md

{Progressive}
Dateien:
  .claude/skills/{name}/SKILL.md
  .claude/skills/{name}/reference.md
  .claude/skills/{name}/examples.md

Typ: {Simple|Progressive} Skill
Complexity: {Low|Medium|High}
Tools: {LIST_OF_TOOLS}

Auto-Activation Triggers:
→ {TRIGGER_1}
→ {TRIGGER_2}

Nächste Schritte:
→ Skill aktiviert sich automatisch bei {TRIGGER_CONTEXT}
→ Teste mit: {EXAMPLE_PROMPT}
→ {SIMPLE: "Erweitere mit mehr Patterns/Examples"}
→ {PROGRESSIVE: "Review reference.md für Details, examples.md für Walkthroughs"}

{Falls Progressive}
Progressive Disclosure:
→ SKILL.md: Entry point (<500 Zeilen)
→ reference.md: Detailed documentation
→ examples.md: Practical examples

Related Skills: {RELATED_SKILLS}
```


#### Example



**Code:**
```bash
✓ API Rate Limiting Skill erfolgreich erstellt!

Datei: .claude/skills/api-rate-limiting/SKILL.md

Typ: Simple Skill
Complexity: Low
Tools: Read, Write, WebFetch

Auto-Activation Triggers:
→ "api integration"
→ "rate limit"
→ "api quota"

Nächste Schritte:
→ Skill aktiviert sich automatisch bei API-bezogenen Tasks
→ Teste mit: "Implement rate limiting for Twitter API"
→ Erweitere mit mehr Patterns/Examples für spezifische APIs

Related Skills: web-scraping, api-design
```


#### Example



**Code:**
```bash
✓ PDF Processing Skill erfolgreich erstellt!

Dateien:
  .claude/skills/pdf-processing/SKILL.md
  .claude/skills/pdf-processing/reference.md
  .claude/skills/pdf-processing/examples.md

Typ: Progressive Skill
Complexity: Medium-High
Tools: Read, Write, mcp__pdf-tools

Auto-Activation Triggers:
→ "analyze pdf"
→ "extract from pdf"
→ "pdf summary"

Nächste Schritte:
→ Skill aktiviert sich automatisch bei PDF-bezogenen Tasks
→ Teste mit: "Extract text from /path/to/document.pdf"
→ Review reference.md für Technical Details
→ Review examples.md für Step-by-Step Walkthroughs

Progressive Disclosure:
→ SKILL.md: Entry point (<500 Zeilen)
→ reference.md: Processing methods, APIs, configurations
→ examples.md: Text extraction, table analysis, summary generation

Related Skills: document-analysis, ocr-processing
```


#### Example



**Code:**
```bash
1. Read template file
2. Replace all placeholders
3. Validate
4. Bash: mkdir -p .claude/skills/{name}
5. Write SKILL.md
6. Confirm to user
```


#### Example



**Code:**
```bash
1. Read 3 template files
2. Replace placeholders in all 3
3. Validate
4. Bash: mkdir -p .claude/skills/{name}
5. Write SKILL.md
6. Write reference.md
7. Write examples.md
8. Confirm to user
```


#### Example



**Code:**
```bash
IF template_not_found:
  Liste verfügbare Skill-Templates
  Frage User welcher Template
  Retry
```


#### Example



**Code:**
```bash
IF skill_exists:
  Frage: "Skill existiert bereits. Überschreiben? (Y/N)"
  IF no: Frage nach alternativem Namen
  IF yes: Backup erstellen (optional), dann überschreiben
```


#### Example



**Code:**
```bash
IF mkdir_fails:
  Prüfe Permissions
  Versuche Parent-Directory zu erstellen
  Falls persistent fehlschlägt: Error an User mit Anleitung
```


#### Example



**Code:**
```bash
IF one_file_fails:
  Rollback bereits geschriebene Files
  Oder: Frage User ob partial creation ok ist
  Log welche Files erfolgreich erstellt wurden
```


#### Example



**Code:**
```bash
User: /create-skill api-rate-limiting

Komplexität: Simple
Purpose: "Apply rate limiting patterns to API integrations"
Use Cases: External APIs, Quota prevention, Graceful degradation
Principles: Respect limits, Exponential backoff, Cache aggressively
Categories: Rate Limit Detection, Retry Strategies

→ Erstellt: .claude/skills/api-rate-limiting/SKILL.md
→ Triggers: "api integration", "rate limit"
```


#### Example



**Code:**
```bash
User: /create-skill pdf-processing

Komplexität: Progressive
Purpose: "Extract, analyze, and summarize PDF documents"
Triggers: "analyze pdf", "extract from pdf", "pdf summary"
Tools: Read, Write, mcp__pdf-tools

SKILL.md: Entry point, Quick Start
reference.md: PDF structure, Extraction methods, OCR, Table detection
examples.md: Research paper extraction, Financial report tables, Summary generation

→ Erstellt: 3 Files in .claude/skills/pdf-processing/
→ Progressive Disclosure optimiert
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/create-skill.md`</small>
