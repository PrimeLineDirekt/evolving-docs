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

Triggers at Stop events with 24-hour frequency limit. Orchestrates automated cleanup across 5 data types:
- Sessions (>30 days old)
- Low-relevance experiences (>90 days)
- Handoffs (>14 days)
- Backup files (>7 days)
- Unused staged rules (>30 days)

## Architecture

**Hook Type:** PostToolUse (Stop event)
**Language:** Python 3.8+
**Mode:** Batch processing with frequency limiting
**Safety:** Dry-run default, requires `--execute` flag

## Usage

### Examples

#### Dry-run (safe default)
```bash
python3 auto-archival.py
```

#### Execute archival
```bash
python3 auto-archival.py --execute
```

#### Specific type only
```bash
python3 auto-archival.py --type sessions --execute
```

#### Override age threshold
```bash
python3 auto-archival.py --type handoffs --age 7 --execute
```

#### Force bypass 24h limiter
```bash
python3 auto-archival.py --force --execute
```

## Configuration

**Retention Defaults:**
- Sessions: 30 days
- Experiences: 90 days (with relevance filter)
- Handoffs: 14 days
- Backups: 7 days
- Rules: 30 days (unused only)

**Frequency Limit:** 24 hours between runs (bypass with `--force`)

## Best Practices

**Do:**
- Use dry-run first to preview changes
- Run manually with `--execute` for important cleanups
- Check archive directories before deletion
- Use `--type` to target specific cleanup

**Don't:**
- Force frequent runs (defeats frequency protection)
- Delete archives manually (breaks tracking)
- Modify age thresholds without understanding impact




## Related


---

<small>Source: `.claude/hooks/auto-archival.py`</small>
