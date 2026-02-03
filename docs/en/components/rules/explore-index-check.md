---
title: Explore Index Check
type: rule
tags: []
lang: en
confidence: 100
---

# Explore Index Check


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Check exploration index before launching Explore agent to avoid duplicate work |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

Before starting any Explore agent task, this rule mandates checking the exploration index (`knowledge/explorations/_index.json`) for existing findings on the same topic. If matching keywords are found, the user is asked whether to load existing findings or conduct a fresh exploration. This prevents redundant exploration work and leverages previously gathered insights.


## System Impact

**When It Triggers:**
BEFORE every Explore agent task (Task Tool with subagent_type=Explore)

**Behavior Enforced:**
1. Load exploration index from knowledge/explorations/_index.json
2. Extract keywords from user query
3. Match against entry.keywords in index
4. If match found: Ask user "Load existing findings from [date] or explore fresh?"
5. If no match: Proceed with new exploration normally

**Integration Points:**
- Task Tool (Explore agent invocation)
- knowledge/explorations/_index.json (findings registry)
- SubagentStop hook (creates index entries after exploration)


## Architecture

**Trigger:** Before Task(subagent_type="Explore", ...)

**Dependencies:**
- knowledge/explorations/_index.json (exploration registry)
- SubagentStop hook (populates index)

**Check Flow:**
1. **Load Index**: Read _index.json
2. **Extract Keywords**: Parse user query for relevant terms
3. **Match**: Check if keywords overlap with any index entry
4. **Decide**: Match → Ask user | No match → Explore
5. **Execute**: Load findings OR start fresh exploration

**Exceptions:**
- Skip check if user says "fresh exploration"
- Skip if index file doesn't exist
- Skip if last match is >30 days old


## Usage

**Before starting Explore agent:**
```python
# WRONG (old way):
Task(subagent_type="Explore", prompt="How does hook system work?")

# RIGHT (with index check):
# 1. Read index
findings_index = Read("knowledge/explorations/_index.json")

# 2. Extract keywords from user query
user_keywords = ["hooks", "system", "routing"]

# 3. Match check
for entry in findings_index["entries"]:
    if any(kw in entry["keywords"] for kw in user_keywords):
        # Match found!
        ask_user(f"Found findings from {entry['date']}. Load or explore fresh?")
        break
else:
    # No match, proceed with exploration
    Task(subagent_type="Explore", ...)
```

**Example Dialog:**
```
User: "How does the hook system work?"

Claude: "I have findings from 2026-01-09 about hooks.
         Should I load those or conduct fresh exploration?"

User: "Load existing" → Read findings document
User: "Fresh" → Start new Explore agent
```


## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| Index Location | knowledge/explorations/_index.json | Central exploration registry |
| Match Threshold | Any keyword overlap | Triggers user prompt |
| Staleness Threshold | 30 days | Skip check if match >30d old |
| Exceptions | "fresh", "new exploration" | User can force new exploration |


## Best Practices

**Do:**
- Always check index before starting Explore agent
- Extract meaningful keywords from user query (3-5 terms)
- Present match date to user for informed decision
- Skip check only when explicitly requested
- Respect 30-day staleness threshold

**Don't:**
- Skip index check by default
- Start exploration without checking for existing work
- Use vague keyword matching (be specific)
- Ignore user preference (always ask when match found)
- Check index when user explicitly wants fresh exploration




## Related


---

<small>Source: `.claude/rules/explore-index-check.md`</small>
