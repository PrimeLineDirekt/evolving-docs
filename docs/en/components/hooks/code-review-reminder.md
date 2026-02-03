---
title: Code Review Reminder
type: hook
tags: ["general", "python"]
lang: en
confidence: 100
---

# Code Review Reminder


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | PostToolUse Hook: Code Review Reminder |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-python">python</span>
</div>

## What It Does

PostToolUse Hook: Code Review Reminder
Triggers after Write/Edit on code files to remind about feature-dev agents. This hook addresses the problem that feature-dev agents are underutilized
because they only trigger on specific keywords. This hook triggers on ACTIONS.

### Key Features

- Type: general
- Language: python

## System Impact

Addresses underutilization of feature-dev agents by triggering on ACTIONS (Write/Edit) rather than keywords. Escalates reminder intensity based on session activity. Promotes proactive code quality checks during development.

**Triggers:** After code file modifications (10+ file extensions tracked)

## Architecture

**Hook Type:** PostToolUse (Write/Edit)
**Language:** Python 3
**Session Tracking:** `/tmp/code-edit-session.json`
**Escalation Levels:** 3 (gentle → moderate → urgent)

## Usage

### Examples

#### Level 1: Gentle (3+ edits or 2+ files)
```
💡 Code modified. `feature-dev:code-reviewer` available for quality check.
```

#### Level 2: Moderate (7+ edits or 4+ files)
```
🟡 Multiple code changes (7 edits, 4 files)

Consider running: `feature-dev:code-reviewer`
Use: Task tool with subagent_type="feature-dev:code-reviewer"
```

#### Level 3: Urgent (15+ edits or 8+ files)
```
🔴 SIGNIFICANT CODE CHANGES (15 edits, 8 files)

STRONGLY RECOMMENDED before continuing:
- `feature-dev:code-reviewer` - Check quality & bugs
- `pr-review-toolkit:silent-failure-hunter` - Check error handling
```

#### Config changes
```
💡 Config changes detected. Consider `feature-dev:code-architect` for structural review.
```

## Configuration

**Code Extensions:** `.ts`, `.tsx`, `.js`, `.jsx`, `.py`, `.go`, `.rs`, `.java`, `.rb`, `.php`, `.swift`, `.kt`, `.scala`, `.c`, `.cpp`, `.h`, `.cs`, `.vue`, `.svelte`

**Config Extensions:** `.json`, `.yaml`, `.yml`, `.toml`, `.env`, `.config`

**Thresholds:**
- Level 1: 3 edits OR 2 files
- Level 2: 7 edits OR 4 files
- Level 3: 15 edits OR 8 files

## Best Practices

**Do:**
- Run suggested review agents before committing
- Clear session file after major reviews
- Use appropriate agent for file type (reviewer vs architect)

**Don't:**
- Ignore urgent reminders (>15 edits)
- Disable hook (catches issues early)
- Skip reviews for "small" changes (accumulate quickly)




## Related


---

<small>Source: `.claude/hooks/code-review-reminder.py`</small>
