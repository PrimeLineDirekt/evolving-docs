---
title: Security Tier Check
type: hook
tags: ["validation", "python"]
lang: en
confidence: 100
---

# Security Tier Check


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Security Tier Check Hook for Claude Code |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-validation">validation</span>
<span class="tag tag-python">python</span>
</div>

## What It Does

Security Tier Check Hook for Claude Code
PreToolUse hook that checks Bash commands against security tiers. Exit Codes: 0 = Allow (with optional warning) 1 = Warn and require confirmation (WARN_CONFIRM) 2 = Block immediately (BLOCK) Usage in settings.json: { "hooks": { "PreToolUse": [{ "matcher": "Bash", "hooks": [{ "type": "command", "command": "python3 .claude/hooks/security-tier-check.py" }] }] } }

### Key Features

- Type: validation
- Language: python

## System Impact




## Architecture




## Usage


### Examples

#### Implementation



**Code:**
```python
def load_tiers
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/security-tier-check.py`</small>
