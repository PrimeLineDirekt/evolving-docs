---
title: Delegation Enforcer
type: hook
tags: ["enforcement", "python"]
lang: en
confidence: 100
---

# Delegation Enforcer


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Delegation Enforcer Hook (Multi-Event) Supports multiple hook events: |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-enforcement">enforcement</span>
<span class="tag tag-python">python</span>
</div>

## What It Does

Delegation Enforcer Hook (Multi-Event) Supports multiple hook events:
- UserPromptSubmit: Enforces delegation rules on user prompts
- Stop: Session-end summary of delegation gaps Bei Score >= DELEGATION_THRESHOLD wird eine Warnung ausgegeben,
die Claude daran erinnert, zu delegieren statt selbst zu machen. Requires: Python 3.8+

### Key Features

- Type: enforcement
- Language: python

## System Impact

Multi-event hook enforcing delegation patterns. On UserPromptSubmit: analyzes prompts and reminds to delegate when score ≥3. On Stop: shows session summary of delegation gaps from plan execution. Supports inline hints for explicit delegation.

**Key:** Shifts work to specialized agents instead of main agent doing everything.

## Architecture

**Hook Type:** Multi-event (UserPromptSubmit + Stop)
**Language:** Python 3.8+
**Config:** `_graph/cache/delegation-config.json`
**Gap Tracking:** `_memory/analytics/delegation-gaps.jsonl`

## Usage

### Examples

#### Inline hints
```
User: "[review] Check the auth code"
→ Detects: code_review_feature_dev
→ Agent: feature-dev:code-reviewer
→ Model: sonnet
```

```
User: "[explore] Find all API endpoints"
→ Detects: exploration
→ Agent: Explore
→ Model: haiku
```

#### Keyword-based delegation
```
User: "Find all references to User model"
→ Keywords: find, references
→ Score: 5 (≥3 threshold)
→ Enforces: Explore agent delegation
```

#### Session-end summary
```
📊 Delegation Summary: 2/5 [DELEGATE] hints not followed

  - [DELEGATE] Implement auth service...
  - [DELEGATE:code-reviewer] Phase 2 Review...

💡 Tip: Use Task tool with subagent_type for [DELEGATE] tasks
```

## Configuration

**Delegation Threshold:** Score ≥3
**Priority:** Built-in agents > Plugin agents > Trait-based

**Inline Hints Available:**
- `[explore]`, `[debug]`, `[plan]` - Built-in agents
- `[review]`, `[architect]`, `[deep]` - feature-dev plugin
- `[types]`, `[errors]`, `[test]`, `[comments]` - pr-review-toolkit
- `[sec]`, `[fix]`, `[research]`, `[doc]` - Trait-based

**Score Factors:**
- Always delegate keywords (find, search, debug, review): +3 to +5
- Scope indicators (all, every, multiple): +2
- Critical keywords (production, deploy, password): -10

## Best Practices

**Do:**
- Use inline hints for explicit control
- Follow delegation suggestions (designed for efficiency)
- Check session summary for patterns
- Delegate exploration/research tasks

**Don't:**
- Do everything in main agent (token waste)
- Ignore high-score suggestions
- Delete gaps file (loses tracking)
- Force delegation for critical security tasks




## Related


---

<small>Source: `.claude/hooks/delegation-enforcer.py`</small>
