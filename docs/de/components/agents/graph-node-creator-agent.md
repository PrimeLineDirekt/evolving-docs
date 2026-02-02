---
title: graph-node-creator-agent
type: agent
tags: []
lang: en
confidence: 100
---

# graph-node-creator-agent


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

"Creates Knowledge Graph nodes from file metadata"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "orphan_files": [
    {
      "path": ".claude/agents/new-agent.md",
      "expected_type": "agent",
      "expected_id": "agent-new-agent"
    }
  ],
  "target_path": "/path/to/repo"
}
```


#### Example



**Code:**
```json
{
  "id": "agent-new-agent",
  "type": "agent",
  "name": "New Agent",
  "path": ".claude/agents/new-agent.md",
  "domain": ["automation", "workflow"],
  "description": "Brief description of purpose"
}
```


#### Example



**Code:**
```json
{
  "created_nodes": [
    {
      "id": "agent-new-agent",
      "type": "agent",
      "name": "New Agent",
      "path": ".claude/agents/new-agent.md",
      "domain": ["automation", "workflow"],
      "description": "Automates workflow tasks"
    }
  ],
  "summary": {
    "total": 6,
    "created": 6,
    "failed": 0
  }
}
```


#### Example



**Code:**
```bash
🔨 NODE CREATION:
├── agent-new-agent
│   ├── type: agent
│   ├── domain: [automation, workflow]
│   └── description: "Automates workflow tasks"
├── cmd-new-cmd
│   ├── type: command
│   └── domain: [utility]
└── Created: 6 nodes
```


#### Example



**Code:**
```bash
# Extract frontmatter
sed -n '/^---$/,/^---$/p' file.md

# Get first heading
grep -m1 "^# " file.md
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/graph-node-creator-agent.md`</small>
