---
title: Graph Update
type: hook
tags: ["synchronization", "bash"]
lang: en
confidence: 100
---

# Graph Update


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** |  Graph Update Hook (v1.0) Flags when knowledge graph needs updating after Write/Edit operations  Trigger: PostToolUse (Write|Edit) Strategy: Lightweight - just flag, don't rebuild  The graph captures  |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-synchronization">synchronization</span>
<span class="tag tag-bash">bash</span>
</div>

## What It Does

 Graph Update Hook (v1.0) Flags when knowledge graph needs updating after Write/Edit operations  Trigger: PostToolUse (Write|Edit) Strategy: Lightweight - just flag, don't rebuild  The graph captures relationships between system components. This hook identifies when changes might affect the graph structure. 

### Key Features

- Type: synchronization
- Language: bash

## System Impact

**Maintains knowledge graph freshness**

- Flags graph updates without rebuilding (lightweight approach)
- Prevents recursive triggers on graph file edits
- Tracks component type and timestamp for rebuild context
- Creates `.needs-update` flag file for batch processing

**Performance Optimization**

- Non-blocking: Only sets flag, doesn't rebuild
- Minimal overhead: Simple pattern matching on file paths
- Batch-friendly: Multiple changes accumulate in flag file

## Architecture

**Trigger Chain**

```
Write/Edit Tool → graph-update.sh (PostToolUse)
     │
     ├─ Parse file_path from tool_input
     ├─ Skip if _graph/* (anti-recursion)
     ├─ Match against component patterns
     │
     └─ If match: Append to .needs-update flag
```

**Component Detection Patterns**

| File Pattern | Component Type |
|--------------|----------------|
| `.claude/commands/*.md` | Command |
| `.claude/agents/*.md` | Agent |
| `.claude/skills/*/reference.md` | Skill |
| `knowledge/patterns/*.md` | Pattern |
| `knowledge/learnings/*.md` | Learning |
| `knowledge/references/*.md` | Reference |
| `.claude/rules/*.md`, `knowledge/rules/*.md` | Rule |
| `.claude/templates/*/*.md` | Template |
| `.claude/blueprints/*.json` | Blueprint |
| `knowledge/agents/*.json` | Agent Trait Definition |

**Flag File Format**

```
2026-02-03T14:30:00Z|Command|.claude/commands/new-cmd.md
2026-02-03T14:31:15Z|Pattern|knowledge/patterns/delegation.md
```

## Usage

**Automatic Operation**

Hook runs automatically after any Write/Edit tool use. No manual invocation needed.

**Graph Rebuild Process**

1. Hook flags updates throughout session
2. At convenient time (manual or scheduled), run graph rebuild
3. Rebuild script reads `.needs-update`, processes flagged components
4. Flag file cleared after successful rebuild

### Examples

#### Implementation

**Code:**
```bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
GRAPH_DIR="$PROJECT_ROOT/_graph"
GRAPH_FLAG="$GRAPH_DIR/.needs-update"
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')
[[ -z "$file_path" ]] && exit 0
case "$file_path" in
  *_graph/*)
    exit 0
    ;;
esac
needs_graph_update=false
component_type=""
case "$file_path" in
  *.claude/commands/*.md)
    needs_graph_update=true
    component_type="Command"
    ;;
```




## Configuration

**Environment Variables**

- `SCRIPT_DIR`: Auto-detected hook directory
- `PROJECT_ROOT`: Auto-detected project root (two levels up from hooks)
- `GRAPH_DIR`: `$PROJECT_ROOT/_graph`
- `GRAPH_FLAG`: `$GRAPH_DIR/.needs-update`

**Required Files**

- `.needs-update` flag file (created automatically in `_graph/`)
- No configuration file needed

## Best Practices

**Graph Maintenance**

- Run graph rebuild weekly or after major component additions
- Check `.needs-update` file size; rebuild if > 20 entries
- Clear flag file after successful rebuild to avoid duplicates

**Anti-Pattern Detection**

- Hook automatically skips `_graph/*` files (prevents recursion)
- Don't manually edit graph files; regenerate from source components

**Monitoring**

- Watch for `📊 GRAPH UPDATE` messages in Claude output
- Flag file grows linearly with component changes
- Large flag files indicate deferred rebuild needed

## Related


---

<small>Source: `.claude/hooks/graph-update.sh`</small>
