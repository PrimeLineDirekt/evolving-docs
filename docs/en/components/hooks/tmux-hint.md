---
title: Tmux Hint
type: hook
tags: ["general", "python"]
lang: en
confidence: 100
---

# Tmux Hint


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | tmux-hint.py - Suggest tmux for long-running dev servers Hook: PreToolUse (Bash) |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-python">python</span>
</div>

## What It Does

tmux-hint.py - Suggest tmux for long-running dev servers Hook: PreToolUse (Bash)
Trigger: When starting a dev server without tmux Purpose: Detects common dev server patterns (npm run dev, next dev, flask run, etc.) and suggests using tmux to ensure the server survives terminal close. Output: - continue: Always allows execution, but with helpful message - message: Suggests tmux command with example

### Key Features

- Type: general
- Language: python

## System Impact




## Architecture




## Usage


### Examples

#### Implementation



**Code:**
```python
def is_dev_server_command
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/tmux-hint.py`</small>
