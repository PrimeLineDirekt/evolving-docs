---
title: Auto Cross Reference
type: Hook
tags: ["hook", "general"]
lang: en
confidence: 100
---

# Auto Cross Reference


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** |  Auto Cross-Reference Hook (v4.0) Auto-syncs Master Documents after structural changes  Trigger: PostToolUse (Write|Edit) Strategy: BLACKLIST - trigger on everything EXCEPT known "noise" paths  v4.0:  |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-hook">hook</span>
<span class="tag tag-general">general</span>
</div>

## What It Does

 Auto Cross-Reference Hook (v4.0) Auto-syncs Master Documents after structural changes  Trigger: PostToolUse (Write|Edit) Strategy: BLACKLIST - trigger on everything EXCEPT known "noise" paths  v4.0: AUTO-SYNC - actually runs full-sync.sh for structural changes v3.0: Blacklist approach - future-proof, catches new paths automatically 


## System Impact




## Architecture




## Usage


### Examples

#### Code



**Code:**
```python
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SYNC_SCRIPT="$SCRIPT_DIR/../scripts/full-sync.sh"
SYNC_LOCK="/tmp/evolving-sync.lock"
SYNC_QUEUE="/tmp/evolving-sync-queue.txt"
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')
[[ -z "$file_path" ]] && exit 0
case "$file_path" in
  # Session files - transient, no sync needed
  *knowledge/sessions/*|*_handoffs/*|*_ledgers/*)
    exit 0
    ;;
```




## Configuration



## Best Practices




## Related


---

<small>Source: `/Users/neoforce/Buisiness/Evolving/.claude/hooks/auto-cross-reference.sh`</small>
