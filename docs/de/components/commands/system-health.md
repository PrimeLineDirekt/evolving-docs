---
title: system-health
type: command
tags: []
lang: en
confidence: 100
---

# system-health


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

System-Diagnostik für Knowledge Base


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
🔍 System Health Check - {MODE} Mode
Starting diagnostics...
```


#### Example



**Code:**
```bash
✓ Master Documents Sync: 25/25
  All stats synchronized across 4 documents
```


#### Example



**Code:**
```bash
⚠ Master Documents Sync: 15/25
  Issues found:
  - Ideas count: README (42) ≠ CONTEXT (41)
  - Projects count: START (12) ≠ index.md (11)
```


#### Example



**Code:**
```bash
.claude/
  commands/ (min 10 files erwartet)
  templates/ (7 Kategorien erwartet)
  skills/ (min 1 erwartet)
  CONTEXT.md
  settings.json
  workflow-patterns.md

knowledge/
  prompts/ (mit README.md)
  patterns/ (mit README.md)
  learnings/ (mit README.md)
  projects/ (mit README.md)
  index.md

ideas/
  index.json
```


#### Example



**Code:**
```bash
✓ File Structure Integrity: 25/25
  All expected directories and files present
```


#### Example



**Code:**
```bash
⚠ File Structure Integrity: 15/25
  Issues found:
  - Missing: knowledge/learnings/README.md
  - .claude/commands/ has 8 files (expected >= 10)
```


#### Example



**Code:**
```bash
✓ Frontmatter Validation: 25/25
  Sample: 5/5 files valid
```


#### Example



**Code:**
```bash
⚠ Frontmatter Validation: 15/25
  Sample: 3/5 files valid
  Issues:
  - knowledge/prompts/test.md: Missing 'created' field
  - knowledge/patterns/broken.md: Invalid YAML syntax
```


#### Example



**Code:**
```bash
✓ Cross-Reference Integrity: 25/25
  0 broken references found
```


#### Example



**Code:**
```bash
⚠ Cross-Reference Integrity: 15/25
  3 broken references:
  - ideas/index.json: idea-2024-005.related_ideas references non-existent 'idea-2024-099'
  - knowledge/prompts/test.md: Link to [[non-existent.md]]
  - knowledge/projects/foo.md: Link to /broken/path.md
```


#### Example



**Code:**
```bash
✓ Workflow Patterns: 10/10
  14/14 commands documented with patterns
```


#### Example



**Code:**
```bash
✓ Knowledge Coverage: 8/10
  Categories balanced, 15% stale content
```


#### Example



**Code:**
```bash
⚠ Git Health: 3/5
  4 uncommitted changes
```


#### Example



**Code:**
```bash
✓ Settings Validation: 5/5
  Valid JSON with hooks and permissions configured
```


#### Example



**Code:**
```markdown
# System Health Report

**Mode:** {quick|full}
**Timestamp:** {YYYY-MM-DD HH:MM:SS}
**Health Score:** {score}/{max_score}

## Status
{HEALTHY|WARNING|CRITICAL}

## Checks

### Quick Mode (4 Core Checks)

- [{✓|✗|⚠}] **Master Documents Sync:** {score}/25
  {Details oder "All synchronized"}

- [{✓|✗|⚠}] **File Structure Integrity:** {score}/25
  {Details oder "All present"}

- [{✓|✗|⚠}] **Frontmatter Validation:** {score}/25
  {Details oder "All valid"}

- [{✓|✗|⚠}] **Cross-Reference Integrity:** {score}/25
  {Details oder "0 broken references"}

{Wenn Full Mode:}
### Full Mode (4 Additional Checks)

- [{✓|✗|⚠}] **Workflow Patterns:** {score}/10
- [{✓|✗|⚠}] **Knowledge Coverage:** {score}/10
- [{✓|✗|⚠}] **Git Health:** {score}/5
- [{✓|✗|⚠}] **Settings Validation:** {score}/5

## Issues Found

{Wenn Issues vorhanden:}
1. **{Issue Title}**
   - Severity: {HIGH|MEDIUM|LOW}
   - Location: {file:line}
   - Fix: {Action to resolve}

{Wenn keine Issues:}
✅ No critical issues found.

## Recommendations

{Basierend auf Score und Issues:}
1. {Recommendation 1}
2. {Recommendation 2}

{Wenn Score < 90:}
## Auto-Fix Available

Ich kann folgende Probleme automatisch beheben:

- [ ] Sync Master Document Stats
- [ ] Create missing README files
- [ ] Remove broken cross-references
- [ ] Update stale content dates

Soll ich Auto-Fix ausführen? (ja/nein)
```


#### Example



**Code:**
```bash
✓ Auto-Fix completed:
  - Synced stats across 4 Master Documents
  - Removed 3 broken references
  - Created 1 missing README

Re-run /system-health to verify.
```


#### Example



**Code:**
```bash
✅ Health Check abgeschlossen.

**Score:** {score}/{max_score} ({percentage}%)
**Status:** {HEALTHY|WARNING|CRITICAL}
**Issues:** {count} gefunden

{Wenn WARNING oder CRITICAL:}
Führe `/system-health full` für detaillierte Analyse aus.

{Wenn Auto-Fix möglich:}
Nutze Auto-Fix um {count} Issues automatisch zu beheben.
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/system-health.md`</small>
