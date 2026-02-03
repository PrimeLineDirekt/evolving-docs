---
title: Auto Rule Generation
type: rule
tags: []
lang: en
confidence: 100
---

# Auto Rule Generation


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Automatically generates new rules from user corrections |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

The Auto Rule Generation system creates new behavioral rules from user corrections. When you correct Claude's behavior, the correction-detector hook identifies patterns and suggests creating a rule. After explicit user confirmation, it generates a structured rule document and stores it in the staging area for validation.

---


## System Impact

**When It Triggers:**
- User explicitly corrects Claude's behavior
- Correction-detector hook identifies a generalizable pattern
- User confirms rule creation with "Yes, create rule"

**Behavior Enforced:**
- Conservative rule generation (requires explicit confirmation)
- Categorizes corrections into 6 types (assumption, scope, over_engineering, misunderstanding, preference, automation)
- Creates standardized rule documents with pattern/anti-pattern examples
- Implements spam prevention (category cooldown, session limits)

**Integration Points:**
- `correction-detector.py` hook for pattern detection
- `knowledge/rules/staging/` directory for new rules
- `/rules-review` command for manual activation
- Domain memory bootup for reviewing candidate rules


## Architecture

**Trigger:** User confirms rule creation after hook suggestion

**Dependencies:**
- correction-detector.py hook (detection)
- knowledge/rules/staging/_template.md (rule structure)
- knowledge/rules/staging/_index.json (tracking)

**Flow:**
1. Hook detects correction → categorizes → suggests rule
2. User confirms → spam check (24h cooldown, session limit)
3. Extract context from last 3-5 conversation turns
4. Generate rule from template with category-specific fields
5. Save to staging with status "candidate" (confidence: 30)
6. Update index with metadata


## Usage

**Automatic Detection:**
When you correct Claude, the correction-detector hook analyzes the pattern and suggests:
```
💡 This could be a rule!
Category: {assumption|scope|over_engineering|...}
Should I create a rule?
```

**Manual Review & Activation:**
```bash
# List candidate rules
/rules-review list --status=CANDIDATE

# Promote to trial status
/rules-review promote {rule_id}
```

**Rule Lifecycle:**
candidate → trial (manual) → stable (after 3+ successful applications)


## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| Category Cooldown | 24h | Prevents duplicate rules in same category |
| Session Limit | 3 | Max rules generated per session |
| Initial Confidence | 30 | Starting confidence for new rules |
| Trial Interval | 3-14 days | Category-specific validation period |


## Best Practices

**Do:**
- Wait for explicit user confirmation before generating
- Extract concrete examples from conversation context
- Use category-appropriate trial intervals (assumption: 3d, preference: 14d)
- Check for similar existing rules to avoid duplication

**Don't:**
- Auto-generate without user approval
- Create rules for one-off corrections ("only this time")
- Generate when existing rule already covers the pattern
- Skip spam checks (respect cooldowns and limits)




## Related


---

<small>Source: `.claude/rules/auto-rule-generation.md`</small>
