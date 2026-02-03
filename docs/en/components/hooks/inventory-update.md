---
title: Inventory Update
type: hook
tags: ["synchronization", "bash"]
lang: en
confidence: 100
---

# Inventory Update


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | Inventory Update Hook Trigger: Nach Write/Edit in .claude/ oder knowledge/rules/ Aktion: component-counts.json + ANALYSIS.md aktualisieren (debounced, sektions-spezifisch) |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-synchronization">synchronization</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

Inventory Update Hook Trigger: Nach Write/Edit in .claude/ oder knowledge/rules/ Aktion: component-counts.json + ANALYSIS.md aktualisieren (debounced, sektions-spezifisch)

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
input=$(cat)
project_dir="${CLAUDE_PROJECT_DIR:-$(pwd)}"
file_path=$(echo "$input" | jq -r '.tool_input.file_path // ""' 2>/dev/null)
section=""
if [[ "$file_path" == *".claude/commands/"* ]]; then
    section="commands"
elif [[ "$file_path" == *".claude/agents/"* ]]; then
    section="agents"
elif [[ "$file_path" == *".claude/skills/"* ]]; then
    section="skills"
elif [[ "$file_path" == *".claude/hooks/"* ]]; then
    section="hooks"
elif [[ "$file_path" == *".claude/rules/"* ]] || [[ "$file_path" == *"knowledge/rules/"* ]]; then
    section="rules"
fi
if [[ -n "$section" ]] || [[ "$file_path" == *".claude/"* ]]; then
    # Debounce: Nur alle 2 Minuten updaten (pro Sektion)
    lock_file="/tmp/inventory-update-${section:-general}"
    if [[ -f "$lock_file" ]]; then
        last_update=$(cat "$lock_file")
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/inventory-update.sh`</small>
