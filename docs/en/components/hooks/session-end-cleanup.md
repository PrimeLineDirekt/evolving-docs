---
title: Session End Cleanup
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Session End Cleanup


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** |  Session End Cleanup Hook Archives session-specific security approvals when session ends  Usage: Called by Claude Code on Stop event Location: .claude/hooks/session-end-cleanup.sh  This hook: 1. Archi |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

 Session End Cleanup Hook Archives session-specific security approvals when session ends  Usage: Called by Claude Code on Stop event Location: .claude/hooks/session-end-cleanup.sh  This hook: 1. Archives session-approvals.json to dated backup 2. Clears the active session approvals 3. Logs the cleanup action

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
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SECURITY_DIR="$PROJECT_ROOT/_memory/security"
APPROVALS_FILE="$SECURITY_DIR/session-approvals.json"
ARCHIVE_DIR="$SECURITY_DIR/archive"
mkdir -p "$ARCHIVE_DIR"
ARCHIVED_COUNT=0
ARCHIVE_PATH=""
DELETED_COUNT=0
if [[ -f "$APPROVALS_FILE" ]]; then
    # Check if file has actual approvals (not just empty structure)
    APPROVAL_COUNT=$(jq -r '.approvals | length' "$APPROVALS_FILE" 2>/dev/null || echo "0")
    if [[ "$APPROVAL_COUNT" -gt 0 ]]; then
        # Generate archive filename with timestamp
        TIMESTAMP=$(date +%Y%m%d-%H%M%S)
        ARCHIVE_FILE="$ARCHIVE_DIR/session-approvals-$TIMESTAMP.json"
        # Archive the file
        cp "$APPROVALS_FILE" "$ARCHIVE_FILE"
        # Track for metadata
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/session-end-cleanup.sh`</small>
