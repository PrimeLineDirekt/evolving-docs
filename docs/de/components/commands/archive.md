---
title: archive
type: command
tags: []
lang: en
confidence: 100
---

# archive


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

"--execute, --force, --age=DAYS"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
/archive [TYPE] [FLAGS]
```


#### Example



**Code:**
```bash
# Dry-Run für alle Typen
/archive

# Nur Sessions archivieren (Dry-Run)
/archive sessions

# Sessions tatsächlich archivieren
/archive sessions --execute

# Handoffs älter als 7 Tage archivieren (statt 14)
/archive handoffs --age=7 --execute

# Frequency-Limit umgehen
/archive --force --execute
```


#### Example



**Code:**
```bash
python3 "$CLAUDE_PROJECT_DIR"/.claude/hooks/auto-archival.py \
  --type ${type:-all} \
  ${flags}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/archive.md`</small>
