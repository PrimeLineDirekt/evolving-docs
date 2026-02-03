---
title: /archive
type: command
tags: []
lang: en
confidence: 100
---

# /archive


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Führt manuelle Archivierung durch. Standardmäßig Dry-Run (safe mode). |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Performs manual archival of sessions, experiences, handoffs, and backups:

1. **Scans target directories** for files exceeding age thresholds
2. **Dry-run by default** - shows what would be archived without taking action
3. **Archives when --execute flag** is provided - moves files to archive locations
4. **Supports selective archival** - choose specific types (sessions, experiences, handoffs, backups, all)
5. **Customizable age thresholds** via --age=DAYS flag
6. **Backup cleanup** - deletes (not archives) old backup files

Default thresholds: Sessions (30d), Experiences (90d + relevance <30), Handoffs (14d), Backups (7d)


## System Impact

- Enables manual cleanup of memory system accumulation
- Integrates with auto-archival hook (runs at session stop with 24h frequency limit)
- Critical for maintaining performance and preventing context bloat
- Preserves historical data in dated archive directories


## Architecture

**Dependencies:**
- Hook: `.claude/hooks/auto-archival.py`
- Archive destinations: `knowledge/sessions/archive/`, `_memory/archives/`, `_handoffs/archive/`

**Data Flow:**
1. Hook scans source directories (sessions, experiences, handoffs, backups)
2. Filters by age threshold and additional criteria (e.g., relevance score)
3. Dry-run: Reports findings
4. Execute mode: Moves files to `YYYY/MM/` structured archives (backups deleted)
5. Updates last_run timestamp for frequency limiting

**Triggers:** Manual via `/archive` or automatic at session stop events (dry-run only)


## Usage

**Syntax:**
```bash
/archive [TYPE] [FLAGS]
```

**Types:**
- `sessions` - Session files (30d threshold)
- `experiences` - Low-relevance experiences (90d + relevance <30)
- `handoffs` - Handoff files (14d threshold)
- `backups` - Backup files (7d threshold, deleted not archived)
- `all` - All types (default)

**Flags:**
- `--execute` - Actually archive (default is dry-run)
- `--force` - Bypass 24h frequency limit
- `--age=DAYS` - Override default age threshold

### Examples

#### Basic Usage

Dry-run for all types:

**Code:**
```bash
/archive
```

**Output:**
```
Scanned: 45 files
Would archive: 12 sessions, 3 handoffs
Would delete: 5 backups
```

#### Selective Archival

Archive only sessions older than 30 days:

**Code:**
```bash
/archive sessions --execute
```

#### Custom Age Threshold

Archive handoffs older than 7 days (instead of 14):

**Code:**
```bash
/archive handoffs --age=7 --execute
```

#### Force Execution

Bypass 24h frequency limit:

**Code:**
```bash
/archive --force --execute
```


## Configuration

| Type | Default Age | Archive Location | Notes |
|------|-------------|------------------|-------|
| sessions | 30 days | `knowledge/sessions/archive/YYYY/MM/` | Session summary files |
| experiences | 90 days | `_memory/archives/experiences/YYYY/` | Only if relevance <30 |
| handoffs | 14 days | `_handoffs/archive/YYYY/` | Handoff markdown files |
| backups | 7 days | (deleted) | No archive, permanent deletion |

**Frequency Limit:**
- Auto-archival: Max 1x per 24h (configurable)
- Manual: Bypass with `--force`

**Safety:**
- Default mode: Dry-run (reports only)
- Execute mode: Requires explicit `--execute` flag


## Best Practices

**Do:**
- Run dry-run first to preview what would be archived
- Use `--execute` only after reviewing dry-run output
- Archive sessions regularly (monthly) to keep working directory clean
- Use custom `--age` for specific cleanup needs
- Check archive directories before deleting originals

**Don't:**
- Use `--execute` without previewing with dry-run
- Archive too aggressively (short age thresholds lose recent context)
- Skip reviewing backup deletion reports (backups are permanently deleted)
- Ignore frequency limits (they prevent accidental duplicate runs)
- Archive experiences with high relevance scores (they're still useful)




## Related


---

<small>Source: `.claude/commands/archive.md`</small>
