---
title: Session Summary
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Session Summary


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** |  Session Summary Hook (Smart Version v2) Creates session summary ONLY when NEW meaningful work was done  Trigger: Stop Purpose: Feed into Session-Evaluation system (Self-Improving)  ONLY creates summa |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

 Session Summary Hook (Smart Version v2) Creates session summary ONLY when NEW meaningful work was done  Trigger: Stop Purpose: Feed into Session-Evaluation system (Self-Improving)  ONLY creates summary when: - NEW commits since last summary, OR - NEW handoff since last summary  Anti-Spam: Max 1 summary per 30 minutes 

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
if command -v jq &> /dev/null; then
    session_id=$(echo "$input" | jq -r '.session_id // "unknown"')
    stop_reason=$(echo "$input" | jq -r '.stop_hook_active // "user_initiated"')
else
    session_id="unknown"
    stop_reason="unknown"
fi
EVOLVING_HOME="/Users/neoforce/Buisiness/Evolving"
cwd="$EVOLVING_HOME"
timestamp=$(date +%Y-%m-%d-%H%M%S)
date_readable=$(date +"%Y-%m-%d %H:%M:%S")
date_short=$(date +%Y-%m-%d)
sessions_dir="$cwd/knowledge/sessions"
mkdir -p "$sessions_dir"
last_summary=$(ls -1t "$sessions_dir"/session-*.md 2>/dev/null | head -1) || true
if [ -n "$last_summary" ]; then
    # Get last summary timestamp (file modification time)
    last_summary_time=$(stat -f %m "$last_summary" 2>/dev/null || stat -c %Y "$last_summary" 2>/dev/null) || last_summary_time=0
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/session-summary.sh`</small>
