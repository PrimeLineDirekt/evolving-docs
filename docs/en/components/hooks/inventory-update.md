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

**Component Count Synchronization**

- Auto-updates `component-counts.json` after changes to `.claude/` or `knowledge/rules/`
- Section-specific debouncing (2-minute cooldown per section)
- Non-blocking background execution
- Maintains ANALYSIS.md accuracy

**Performance Characteristics**

- Debounced: Max 1 update per section per 2 minutes
- Background execution: No session blocking
- Lock file prevents concurrent updates

## Architecture

**Trigger Logic**

```
Write/Edit → inventory-update.sh (PostToolUse)
     │
     ├─ Parse file_path
     ├─ Determine section (commands, agents, skills, hooks, rules)
     │
     ├─ Check debounce lock (/tmp/inventory-update-{section})
     │   └─ Skip if < 2 minutes since last update
     │
     └─ Background: Execute scripts/sync-counts.sh
```

**Section Detection**

| File Pattern | Section |
|--------------|---------|
| `.claude/commands/` | commands |
| `.claude/agents/` | agents |
| `.claude/skills/` | skills |
| `.claude/hooks/` | hooks |
| `.claude/rules/`, `knowledge/rules/` | rules |
| Any `.claude/` | general |

**Lock File Mechanism**

```
/tmp/inventory-update-{section} contains timestamp
Last update time compared to current time
Skip if diff < 120 seconds
```

## Usage

**Automatic Operation**

Runs after any Write/Edit in relevant directories. No manual trigger needed.

**Manual Sync**

```bash
scripts/sync-counts.sh
```

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

**Environment Variables**

- `CLAUDE_PROJECT_DIR`: Project directory (defaults to pwd)

**Dependencies**

- `jq`: JSON parsing
- `scripts/sync-counts.sh`: Count synchronization script

**Lock Files**

- Location: `/tmp/inventory-update-{section}`
- Content: Unix timestamp of last update
- Cleanup: Auto-removed after 2 minutes on next trigger

## Best Practices

**Debounce Tuning**

- 2-minute window prevents excessive updates during bulk edits
- Section-specific: Editing commands doesn't affect agents debounce
- Increase window if frequent false updates occur

**Background Execution**

- Hook spawns background process, returns immediately
- No session blocking or performance impact
- stderr/stdout redirected to `/dev/null`

**Lock File Hygiene**

- Lock files in `/tmp/` auto-cleaned on reboot
- Manual cleanup rarely needed
- Check `/tmp/inventory-update-*` if issues persist

**Monitoring**

- Check `component-counts.json` timestamp after changes
- Verify counts match actual file counts via manual script run
- Review `ANALYSIS.md` sections for accuracy

## Related


---

<small>Source: `.claude/hooks/inventory-update.sh`</small>
