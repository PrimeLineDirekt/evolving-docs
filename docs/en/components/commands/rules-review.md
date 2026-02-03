---
title: /rules-review
type: command
tags: []
lang: en
confidence: 100
---

# /rules-review


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Manual review and management of rules in the staging system. Shows validation metrics, status, and enables promotion, archival, or editing |
| **Complexity** | high |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Reviews staged rules with metrics (applied count, success rate, age). Supports promotion, archival, and editing. Flags: --force, --all, --status=CANDIDATE|TRIAL|STABLE


## System Impact

Reads staging index, displays metrics, updates rule status based on user decisions.

## Architecture




## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/rules-review
```




## Configuration



## Best Practices

- Review candidate rules regularly
- Promote rules with proven success rate (3+ applications)
- Archive rules that conflict or are outdated
- Monitor trial rules for effectiveness

## Related


---

<small>Source: `.claude/commands/rules-review.md`</small>
