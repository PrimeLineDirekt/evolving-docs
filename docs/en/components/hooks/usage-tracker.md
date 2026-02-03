---
title: Usage Tracker
type: hook
tags: ["general", "python"]
lang: en
confidence: 100
---

# Usage Tracker


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | usage-tracker.py - Track all tool usage with detailed analytics Hook: PostToolUse (for ALL tools) Logs usage to: |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-python">python</span>
</div>

## What It Does

usage-tracker.py - Track all tool usage with detailed analytics Hook: PostToolUse (for ALL tools) Logs usage to:
- _memory/analytics/usage.json (aggregated counts)
- _memory/analytics/usage-history.jsonl (event log with tool details) Features:
- All tools tracked (Read, Edit, Bash, Skill, Task, etc.)
- Tool args preview (truncated to 200 chars)
- Success/error status
- Buffered writes (flush every 25 entries)
- Analyzer trigger (every 50 tool calls)

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
def get_session_id
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/usage-tracker.py`</small>
