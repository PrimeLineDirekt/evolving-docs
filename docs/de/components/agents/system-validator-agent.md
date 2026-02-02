---
title: system-validator-agent
type: agent
tags: []
lang: en
confidence: 100
---

# system-validator-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2025-12-14 |</div>


## What It Does

"Validiert das generierte System auf Vollständigkeit und Korrektheit"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "generation_result": "object - Output from system-generator-agent",
  "architecture": "object - Original architecture from architect",
  "blueprint": "object - Blueprint configuration",
  "target_path": "string"
}
```


#### Example



**Code:**
```bash
Required directories:
- .claude/
- .claude/agents/
- .claude/commands/
- knowledge/ (if include_kb)
- _memory/ (if include_memory)

Result: PASS | FAIL with missing dirs
```


#### Example



**Code:**
```bash
Required files:
- CLAUDE.md
- README.md
- .claude/scenario.json

Result: PASS | FAIL with missing files
```


#### Example



**Code:**
```bash
For each agent in architecture.agents:
- File exists: .claude/agents/{agent.id}.md
- File has content (> 50 lines)
- Frontmatter is valid YAML
- No {PLACEHOLDERS} remain

Result: PASS | FAIL with details
```


#### Example



**Code:**
```bash
For each command in architecture.commands:
- File exists: .claude/commands/{command.id}.md
- File has content
- Frontmatter is valid
- Referenced agents exist

Result: PASS | FAIL with details
```


#### Example



**Code:**
```bash
Scan all .md and .json files for:
- Pattern: {[A-Z_]+}
- Exclude: Code blocks, examples

Result: PASS | WARN | FAIL with locations
```


#### Example



**Code:**
```bash
Check CLAUDE.md for:
- Has ## System Overview
- Has ## Agents section
- Has ## Commands section
- Minimum 50 lines
- No placeholders

Result: PASS | FAIL with details
```


#### Example



**Code:**
```bash
Check all internal references:
- @agent-name in commands → agent exists
- Pattern paths → files exist
- Links in README → targets exist

Result: PASS | WARN | FAIL
```


#### Example



**Code:**
```json
{
  "validation_result": {
    "overall": "PASS|WARN|FAIL",
    "score": "number 0-100",
    "timestamp": "ISO date"
  },
  "checks": [
    {
      "name": "string",
      "status": "PASS|WARN|FAIL",
      "details": "string",
      "items_checked": "number",
      "items_passed": "number"
    }
  ],
  "issues": [
    {
      "severity": "error|warning|info",
      "check": "string - which check failed",
      "file": "string - affected file",
      "line": "number - if applicable",
      "message": "string - description",
      "fix_suggestion": "string - how to fix"
    }
  ],
  "summary": {
    "total_checks": "number",
    "passed": "number",
    "warnings": "number",
    "failed": "number",
    "files_validated": "number",
    "issues_found": "number"
  },
  "recommendation": "string - overall assessment"
}
```


#### Example



**Code:**
```json
{
  "validation_result": {
    "overall": "PASS",
    "score": 95,
    "timestamp": "2025-12-14T15:30:00Z"
  },
  "checks": [
    {
      "name": "Directory Structure",
      "status": "PASS",
      "details": "All 5 required directories exist",
      "items_checked": 5,
      "items_passed": 5
    },
    {
      "name": "Required Files",
      "status": "PASS",
      "details": "All 3 required files exist",
      "items_checked": 3,
      "items_passed": 3
    },
    {
      "name": "Agent Files",
      "status": "PASS",
      "details": "5 agents validated",
      "items_checked": 5,
      "items_passed": 5
    },
    {
      "name": "Placeholder Scan",
      "status": "PASS",
      "details": "No unresolved placeholders found",
      "items_checked": 12,
      "items_passed": 12
    },
    {
      "name": "CLAUDE.md Quality",
      "status": "PASS",
      "details": "156 lines, all sections present",
      "items_checked": 5,
      "items_passed": 5
    },
    {
      "name": "Reference Integrity",
      "status": "WARN",
      "details": "1 optional reference not found",
      "items_checked": 8,
      "items_passed": 7
    }
  ],
  "issues": [
    {
      "severity": "warning",
      "check": "Reference Integrity",
      "file": ".claude/commands/steuer-beratung.md",
      "line": 45,
      "message": "Optional pattern reference 'reflection-pattern.md' not found in knowledge/patterns/",
      "fix_suggestion": "Add pattern file or remove reference"
    }
  ],
  "summary": {
    "total_checks": 6,
    "passed": 5,
    "warnings": 1,
    "failed": 0,
    "files_validated": 12,
    "issues_found": 1
  },
  "recommendation": "System ist bereit zur Nutzung. 1 optionale Warnung kann ignoriert oder behoben werden."
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/system-validator-agent.md`</small>
