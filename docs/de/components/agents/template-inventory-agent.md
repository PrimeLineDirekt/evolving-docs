---
title: template-inventory-agent
type: agent
tags: []
lang: en
confidence: 100
---

# template-inventory-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2026-01-04 |</div>


## What It Does

"Analyzes Evolving-Template repo and creates inventory comparison with source"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "source_path": "/path/to/Evolving",
  "target_path": "/path/to/Evolving-Template",
  "manifest": "template-sync-manifest.json contents"
}
```


#### Example



**Code:**
```bash
COMPONENTS = {
  "agents": ".claude/agents/*.md",
  "commands": ".claude/commands/*.md",
  "skills": ".claude/skills/*/",
  "blueprints": ".claude/blueprints/*.json",
  "rules_core": ".claude/rules/*.md",
  "rules_ondemand": "knowledge/rules/**/*.md",
  "patterns": "knowledge/patterns/**/*.md",
  "prompts": "knowledge/prompts/**/*.md",
  "references": "knowledge/references/**/*.md"
}
```


#### Example



**Code:**
```markdown
# Template Inventory Report

## Summary
| Component | Source | Target | New | Outdated |
|-----------|--------|--------|-----|----------|
| Agents | 23 | 19 | 4 | 2 |
| Commands | 39 | 34 | 5 | 3 |
| Skills | 5 | 4 | 1 | 0 |
| Patterns | 15 | 12 | 3 | 1 |
| Rules | 36 | 32 | 4 | 0 |

## New Components (to sync)
- `.claude/agents/new-agent.md`
- `.claude/commands/new-command.md`
- `knowledge/patterns/new-pattern.md`

## Outdated Components (to update)
- `.claude/CONTEXT.md` (Source: 2026-01-04, Target: 2026-01-02)
- `.claude/detection-index.json` (12 new entries)

## Template-Only (do not overwrite)
- `README.md`
- `START-SMALL.md`
- `BEGINNER-GUIDE.md`
- `_ONBOARDING.md`

## Recommendations
1. Sync 4 new agents
2. Update 2 outdated agents
3. Protect 4 template-only files
```


#### Example



**Code:**
```bash
# Count agents in source
ls -1 $SOURCE/.claude/agents/*.md | wc -l

# Get modification time
stat -f "%m" $FILE

# Find template-only files
comm -23 <(ls $TARGET) <(ls $SOURCE)
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/template-inventory-agent.md`</small>
