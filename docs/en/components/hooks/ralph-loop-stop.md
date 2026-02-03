---
title: Ralph Loop Stop
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Ralph Loop Stop


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** |  Ralph Loop Stop Hook Prevents session exit when a ralph-loop is active Feeds the SAME prompt back to continue the loop  Trigger: Stop State: .claude/ralph-loop.local.md Based on: anthropics/claude-pl |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

 Ralph Loop Stop Hook Prevents session exit when a ralph-loop is active Feeds the SAME prompt back to continue the loop  Trigger: Stop State: .claude/ralph-loop.local.md Based on: anthropics/claude-plugins-official/ralph-loop 

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
HOOK_INPUT=$(cat)
EVOLVING_HOME="/Users/neoforce/Buisiness/Evolving"
RALPH_STATE_FILE="$EVOLVING_HOME/.claude/ralph-loop.local.md"
if [[ ! -f "$RALPH_STATE_FILE" ]]; then
  # No active loop - allow normal exit
  exit 0
fi
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$RALPH_STATE_FILE")
ITERATION=$(echo "$FRONTMATTER" | grep '^iteration:' | sed 's/iteration: *//')
MAX_ITERATIONS=$(echo "$FRONTMATTER" | grep '^max_iterations:' | sed 's/max_iterations: *//')
COMPLETION_PROMISE=$(echo "$FRONTMATTER" | grep '^completion_promise:' | sed 's/completion_promise: *//' | sed 's/^"\(.*\)"$/\1/')
VERIFY_CMD=$(echo "$FRONTMATTER" | grep '^verify:' | sed 's/verify: *//' | sed 's/^"\(.*\)"$/\1/')
if [[ ! "$ITERATION" =~ ^[0-9]+$ ]]; then
  echo "⚠️  Ralph loop: State file corrupted (invalid iteration)" >&2
  rm "$RALPH_STATE_FILE"
  exit 0
fi
if [[ ! "$MAX_ITERATIONS" =~ ^[0-9]+$ ]]; then
  echo "⚠️  Ralph loop: State file corrupted (invalid max_iterations)" >&2
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/ralph-loop-stop.sh`</small>
