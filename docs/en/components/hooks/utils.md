---
title: Utils
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Utils


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Shared utilities for Evolving hooks Source this file: source "$(dirname "$0")/utils.sh" ============================================ DEBOUNCING ============================================ Check if ac |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

Shared utilities for Evolving hooks Source this file: source "$(dirname "$0")/utils.sh" ============================================ DEBOUNCING ============================================ Check if action should be debounced Usage: check_debounce "name" seconds || exit 0 Returns 0 if OK to proceed, 1 if should skip

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
check_debounce() {
    local name=$1
    local seconds=${2:-120}
    local debounce_file="/tmp/evolving-debounce-${name}.txt"

    if [[ -f "$debounce_file" ]]; then
        local last_run=$(cat "$debounce_file")
        local now=$(date +%s)
        if (( now - last_run < seconds )); then
            return 1  # Too soon, should skip
        fi
    fi

    echo "$(date +%s)" > "$debounce_file"
    return 0  # OK to proceed
}
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/utils.sh`</small>
