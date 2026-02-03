---
title: Template Reminder
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Template Reminder


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Template Sync Reminder Hook Triggers when new generic content is created that might be relevant for template sync Read input from stdin |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

Template Sync Reminder Hook Triggers when new generic content is created that might be relevant for template sync Read input from stdin

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
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // .tool_input.path // empty')
if [ -z "$file_path" ]; then
    exit 0
fi
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
MANIFEST="$PROJECT_ROOT/config/template-sync-manifest.json"
if [ -n "${EVOLVING_TEMPLATE:-}" ]; then
    TARGET="$EVOLVING_TEMPLATE"
elif [ -f "$MANIFEST" ]; then
    TARGET=$(jq -r '.paths.target // empty' "$MANIFEST")
    if [ -z "$TARGET" ] || [ "$TARGET" = "null" ]; then
        TARGET="$(dirname "$(dirname "$PROJECT_ROOT")")/Evolving-Template"
    fi
else
    TARGET="$(dirname "$(dirname "$PROJECT_ROOT")")/Evolving-Template"
fi
INCLUDE_PATTERNS=(
    ".claude/agents/"
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/template-reminder.sh`</small>
