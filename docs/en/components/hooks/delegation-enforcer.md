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




## Architecture




## Usage


### Examples

#### Implementation



**Code:**
```python
def track_delegation_gap
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/delegation-enforcer.py`</small>
