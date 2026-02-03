---
title: Context Monitor
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Context Monitor


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Context Monitor v2 - StatusLine with Context Budget Awareness  Format: 145K 72% | Evolving | Opus | main *3 | ✓ Last → Current Colors: Green (<60%) | Yellow (60-79%) | Red (≥80%) Writes context % to / |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

Context Monitor v2 - StatusLine with Context Budget Awareness  Format: 145K 72% | Evolving | Opus | main *3 | ✓ Last → Current Colors: Green (<60%) | Yellow (60-79%) | Red (≥80%) Writes context % to /tmp for hooks

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
project_dir="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cwd=$(echo "$input" | jq -r '.workspace.current_dir // ""' 2>/dev/null)
[[ -z "$cwd" || "$cwd" == "null" ]] && cwd="$project_dir"
dir=$(basename "$cwd")
model=$(echo "$input" | jq -r '.model.display_name // "Claude"')
if [[ "$model" =~ Opus ]]; then
  m="Opus"
elif [[ "$model" =~ Sonnet ]]; then
  m="Sonnet"
elif [[ "$model" =~ Haiku ]]; then
  m="Haiku"
else
  m="${model%% *}"
fi
cache_read=$(echo "$input" | jq -r '.context_window.current_usage.cache_read_input_tokens // 0' 2>/dev/null)
cache_creation=$(echo "$input" | jq -r '.context_window.current_usage.cache_creation_input_tokens // 0' 2>/dev/null)
base_tokens=$((cache_read + cache_creation))
total_tokens=$((base_tokens * 120 / 100))
context_size=$(echo "$input" | jq -r '.context_window.context_window_size // 200000' 2>/dev/null)
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/context-monitor.sh`</small>
