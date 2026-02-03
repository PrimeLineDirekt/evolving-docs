---
title: Correction Detector
type: hook
tags: ["detection", "python"]
lang: en
confidence: 100
---

# Correction Detector


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Correction Detector Hook - Self-Evolving System Detects user corrections in prompts and offers to generate rules from them. |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-detection">detection</span>
<span class="tag tag-python">python</span>
</div>

## What It Does

Correction Detector Hook - Self-Evolving System Detects user corrections in prompts and offers to generate rules from them.
Part of the closed-loop learning system. Event: UserPromptSubmit
Timeout: 5s

### Key Features

- Type: detection
- Language: python

## System Impact

Self-evolving system that learns from user corrections. Detects 7 correction patterns in user prompts and offers to generate rules. Part of closed-loop learning system enabling automatic rule creation from real usage patterns.

**Triggers:** When user corrects Claude's behavior with confidence ≥60%

## Architecture

**Hook Type:** UserPromptSubmit
**Language:** Python 3
**Timeout:** 5 seconds
**Confidence Scoring:** Pattern-based with weights 0.65-0.9

## Usage

### Examples

#### Pattern detection
**Explicit negation** (weight 0.9):
```
User: "No, that's not right. I meant X"
→ Category: misunderstanding
→ Confidence: 90%
```

**Wrong assumption** (weight 0.85):
```
User: "I never said that. Where did you get that from?"
→ Category: assumption
→ Confidence: 85%
```

**Too much** (weight 0.75):
```
User: "That's overkill. I just need X"
→ Category: over_engineering
→ Confidence: 75%
```

#### Hook suggestion
```
🔍 Correction detected (Confidence: 85%)

Category: false assumption
Patterns: wrong_assumption, explicit_negation

Generate a Rule from this?
- Rule goes to staging initially
- After 3 successful applications → permanent

Reply "Yes, create rule" or ignore.
```

## Configuration

**Categories:**
- `assumption` - False assumptions
- `scope` - Scope too broad/narrow
- `over_engineering` - Too complex
- `misunderstanding` - Wrong goal
- `preference` - User preference ignored
- `automation` - Too proactive

**Confidence Threshold:** 60% minimum
**Bonus Factors:**
- Last turn was Claude: +20
- Similar correction exists: +15
- Long detailed correction: +10

## Best Practices

**Do:**
- Confirm rule creation when suggested
- Review generated rules in staging
- Let high-confidence corrections auto-suggest

**Don't:**
- Ignore repeated correction patterns
- Reject all suggestions (prevents learning)
- Manually lower confidence threshold (noise risk)




## Related


---

<small>Source: `.claude/hooks/correction-detector.py`</small>
