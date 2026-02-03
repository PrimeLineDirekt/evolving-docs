---
title: Ledger Auto Save
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Ledger Auto Save


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** |  Ledger Auto-Save Hook (v2 - Dynamic Snapshot) Generates fresh CURRENT.md from memory sources at session end Ready for next session - no manual maintenance needed  Trigger: Stop Sources: _memory/index |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

 Ledger Auto-Save Hook (v2 - Dynamic Snapshot) Generates fresh CURRENT.md from memory sources at session end Ready for next session - no manual maintenance needed  Trigger: Stop Sources: _memory/index.json, _memory/projects/*.json, _handoffs/, knowledge/sessions/ 

### Key Features

- Type: general
- Language: bash

## System Impact




## Architecture




## Usage


### Examples

#### Implementation



**Code:**
```bash
set -euo pipefail
input=$(cat)
EVOLVING_HOME="/Users/neoforce/Buisiness/Evolving"
cwd="$EVOLVING_HOME"
ledger_dir="$cwd/_ledgers"
current_ledger="$ledger_dir/CURRENT.md"
memory_index="$cwd/_memory/index.json"
handoffs_dir="$cwd/_handoffs"
sessions_dir="$cwd/knowledge/sessions"
if [ ! -d "$ledger_dir" ]; then
    exit 0
fi
today=$(date +%Y-%m-%d)
active_project="unknown"
if [ -f "$memory_index" ] && command -v jq &> /dev/null; then
    active_project=$(jq -r '.active_context.project // "unknown"' "$memory_index" 2>/dev/null) || true
fi
project_file="$cwd/_memory/projects/${active_project}.json"
current_phase=""
last_progress=""
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/ledger-auto-save.sh`</small>
