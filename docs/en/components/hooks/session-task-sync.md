---
title: Session Task Sync
type: hook
tags: ["synchronization", "bash"]
lang: en
confidence: 100
---

# Session Task Sync


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | session-task-sync.sh - Syncs completed tasks to Memory on session end Trigger: Stop Event Purpose: Bridge between session-scoped Tasks and project-scoped Memory |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-synchronization">synchronization</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

session-task-sync.sh - Syncs completed tasks to Memory on session end Trigger: Stop Event Purpose: Bridge between session-scoped Tasks and project-scoped Memory

### Key Features

- Type: synchronization
- Language: bash

## System Impact




## Architecture




## Usage


### Examples

#### Implementation



**Code:**
```bash
set -e
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
MEMORY_INDEX="$PROJECT_DIR/_memory/index.json"
if [[ ! -f "$MEMORY_INDEX" ]]; then
    exit 0
fi
ACTIVE_PROJECT=$(python3 -c "
import json
import sys
try:
    with open('$MEMORY_INDEX', 'r') as f:
        data = json.load(f)
    print(data.get('active_context', {}).get('project', ''))
except:
    print('')
" 2>/dev/null)
if [[ -z "$ACTIVE_PROJECT" ]]; then
    exit 0
fi
PROJECT_MEMORY="$PROJECT_DIR/_memory/projects/$ACTIVE_PROJECT.json"
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/session-task-sync.sh`</small>
