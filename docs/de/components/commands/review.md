---
title: review
type: command
tags: []
lang: en
confidence: 100
---

# review


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




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
/review              # Top 3 due items
/review all          # Alle due items (max 10)
/review experiences  # Nur Experiences
/review rules        # Nur Staged Rules
/review explorations # Nur Explorations
```


#### Example



**Code:**
```bash
User: /review

Claude:
📚 Review-Check (3 Items fällig):

1. [EXP] Supabase RLS Pattern (7d überfällig)
2. [RULE] Advanced Debugging (heute)
3. [EXPLORE] Hook-System (1d überfällig)

Aktionen: [C]onfirm all | [1-3] einzeln | [S]kip all | [D]etails

User: c1
Claude: ✓ Experience bestätigt. Nächster Review in 17 Tagen.

User: d2
Claude:
### RULE: Advanced Debugging
**Status**: trial (2/3 Sessions)
**Category**: debugging
**Pattern**: Observe → Hypothesize → Test → Verify
**Created**: 2026-01-28

[C]onfirm | [P]ractice | [S]kip

User: c
Claude: ✓ Rule bestätigt. Nächster Review in 7 Tagen.

User: s3
Claude: ✓ Exploration übersprungen. Nächster Review in 11 Tagen.

📊 Review complete: 2 confirmed, 1 skipped
```


#### Example



**Code:**
```bash
"📚 Review-Check (3 Items fällig). Jetzt reviewen? [Y/n/later]"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/review.md`</small>
