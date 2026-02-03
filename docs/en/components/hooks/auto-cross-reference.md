---
title: Auto Cross Reference
type: hook
tags: ["general", "bash"]
lang: en
confidence: 100
---

# Auto Cross Reference


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** |  Auto Cross-Reference Hook (v4.0) Auto-syncs Master Documents after structural changes  Trigger: PostToolUse (Write|Edit) Strategy: BLACKLIST - trigger on everything EXCEPT known "noise" paths  v4.0:  |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

 Auto Cross-Reference Hook (v4.0) Auto-syncs Master Documents after structural changes  Trigger: PostToolUse (Write|Edit) Strategy: BLACKLIST - trigger on everything EXCEPT known "noise" paths  v4.0: AUTO-SYNC - actually runs full-sync.sh for structural changes v3.0: Blacklist approach - future-proof, catches new paths automatically 

### Key Features

- Type: general
- Language: bash

## System Impact

Triggers after Write/Edit operations to detect structural changes. Automatically syncs master documentation (README.md, COMMANDS.md, SYSTEM-MAP.md) when components are added/modified. Uses blacklist strategy to filter noise and focus on structural changes.

**Auto-sync for:** Commands, Agents, Patterns, Learnings, Blueprints, Skills, Scenarios, Rules

## Architecture

**Hook Type:** PostToolUse (Write/Edit)
**Language:** Bash
**Strategy:** Blacklist filtering (ignores noise paths)
**Execution:** Background sync via `full-sync.sh`
**Lock:** `/tmp/evolving-sync.lock` prevents concurrent runs

## Usage

### Examples

#### Automatic trigger
Hook runs automatically after Write/Edit on structural paths:

```bash
# Claude creates new command
Write .claude/commands/new-cmd.md
→ Hook detects: "Command"
→ Auto-syncs: COMMANDS.md, SYSTEM-MAP.md, README.md, detection-index.json
```

#### Blacklisted paths (no sync)
- Session files: `knowledge/sessions/*`, `_handoffs/*`, `_ledgers/*`
- Memory: `_memory/experiences/exp-*`, `_memory/projects/*.json`
- Archive: `_archive/*`, `_sandbox/*`
- Build artifacts: `dashboard/.next/*`, `node_modules/*`

## Configuration

**Sync Lock:** `/tmp/evolving-sync.lock`
**Sync Log:** `/tmp/evolving-sync.log`
**Sync Script:** `.claude/scripts/full-sync.sh`

**Change Detection:**
- Commands → COMMANDS.md, SYSTEM-MAP.md, README.md, detection-index.json
- Agents → SYSTEM-MAP.md, README.md
- Patterns/Learnings → SYSTEM-MAP.md, README.md, knowledge/index.md
- Hooks → SYSTEM-MAP.md, settings.json

## Best Practices

**Do:**
- Let hook run automatically for structural changes
- Check sync log if changes not reflected
- Add new noise paths to blacklist as needed

**Don't:**
- Manually run sync while hook is active
- Modify master docs during sync (race conditions)
- Remove sync lock manually (breaks protection)




## Related


---

<small>Source: `.claude/hooks/auto-cross-reference.sh`</small>
