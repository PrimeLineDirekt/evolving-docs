---
title: Context Warning
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Context Warning


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Context Warning Hook - PreToolUse (v4 - Progressive Escalation) Warnt bei hohem Context % mit progressiver Eskalation  ESKALATIONSSTUFEN: - 70%: Warnung (continue: true) - 85%: Auto-Trigger Agent im B |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

Context Warning Hook - PreToolUse (v4 - Progressive Escalation) Warnt bei hohem Context % mit progressiver Eskalation  ESKALATIONSSTUFEN: - 70%: Warnung (continue: true) - 85%: Auto-Trigger Agent im Background (continue: true) - 88%: FORCE Handoff - muss erst reagieren (continue: false) - 90%: BLOCK - nur Handoff-Tools erlaubt  FEATURES: - Debouncing: warnt nur alle 120 Sekunden (außer ≥85%) - Einmaliger Trigger pro Session (handoff_triggered_file)

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
session_id="${CLAUDE_SESSION_ID:-$PPID}"
pct_file="/tmp/claude-context-pct-${session_id}.txt"
last_warn_file="/tmp/claude-context-warn-${session_id}.txt"
handoff_triggered_file="/tmp/claude-handoff-triggered-${session_id}.txt"
DEBOUNCE_SECONDS=120
now=$(date +%s)
last_warn=0
if [[ -f "$last_warn_file" ]]; then
  last_warn=$(cat "$last_warn_file" 2>/dev/null || echo 0)
fi
time_since=$((now - last_warn))
input=$(cat)
tool_name=$(echo "$input" | jq -r '.tool_name // ""' 2>/dev/null)
pct=0
if [[ -f "$pct_file" ]]; then
  pct=$(cat "$pct_file" 2>/dev/null || echo 0)
fi
if [[ "$pct" -lt 85 ]] && [[ "$time_since" -lt "$DEBOUNCE_SECONDS" ]]; then
  echo '{}'
  exit 0
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/context-warning.sh`</small>
