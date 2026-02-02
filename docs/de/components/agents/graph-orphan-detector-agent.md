---
title: graph-orphan-detector-agent
type: agent
tags: []
lang: en
confidence: 100
---

# graph-orphan-detector-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2026-01-06 |</div>


## What It Does

"Detects files without corresponding Knowledge Graph nodes"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "synced_files": ["path/to/file1.md", "path/to/file2.md"],
  "nodes_json_path": "_graph/nodes.json",
  "target_path": "/path/to/repo"
}
```


#### Example



**Code:**
```bash
FOR each file in synced_files:
  1. Match against path patterns → determine type
  2. Generate expected node ID:
     - Extract filename without extension
     - Convert to kebab-case
     - Prepend type prefix
  3. Search nodes.json for matching:
     - ID match OR
     - Path match
  4. If no match → ORPHAN
```


#### Example



**Code:**
```json
{
  "summary": {
    "total_checked": 95,
    "in_graph": 89,
    "orphans": 6
  },
  "orphans": [
    {
      "path": ".claude/agents/new-agent.md",
      "expected_type": "agent",
      "expected_id": "agent-new-agent",
      "reason": "no_node_found"
    }
  ]
}
```


#### Example



**Code:**
```bash
🔍 ORPHAN DETECTION:
├── Geprüft: 95 Dateien
├── Im Graph: 89
└── Orphans: 6
    ├── .claude/agents/new-agent.md (agent)
    ├── .claude/commands/new-cmd.md (command)
    └── knowledge/patterns/new-pattern.md (pattern)
```


#### Example



**Code:**
```bash
# List all agent files
ls -1 .claude/agents/*.md

# Check if path exists in nodes.json
grep -c "path/to/file.md" _graph/nodes.json
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/graph-orphan-detector-agent.md`</small>
