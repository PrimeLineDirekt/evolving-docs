---
title: Auto Archival
type: hook
tags: ["general", "python"]
lang: en
confidence: 100
---

# Auto Archival


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Auto-Archival Hook Central orchestrator for automated data cleanup and archival. |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-python">python</span>
</div>

## What It Does

Auto-Archival Hook Central orchestrator for automated data cleanup and archival.
Runs at Stop events with 24h frequency limit. Usage: # Dry-run (default, safe mode) python3 auto-archival.py # Execute archival python3 auto-archival.py --execute # Specific type only python3 auto-archival.py --type sessions --execute # Override age threshold python3 auto-archival.py --type handoffs --age 7 --execute # Bypass 24h limiter python3 auto-archival.py --force --execute # Hook mode (called by Stop event) python3 auto-archival.py --hook Supported types: - sessions: Archive session files > 30 days - experiences: Archive low-relevance experiences > 90 days - handoffs: Archive handoffs > 14 days - backups: Delete backup files > 7 days - rules: Archive unused staged rules > 30 days - all: Process all types (default) Requires: Python 3.8+

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
def run_archival
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/auto-archival.py`</small>
