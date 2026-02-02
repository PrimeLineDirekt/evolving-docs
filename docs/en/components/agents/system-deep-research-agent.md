---
title: system-deep-research-agent
type: agent
tags: []
lang: en
confidence: 100
---

# system-deep-research-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2026-01-15 |</div>


## What It Does

"SETUP ONLY - Generates persistent storage-locations.json"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "version": "1.0",
  "generated": "2026-01-15T10:00:00Z",
  "categories": {
    "agents": {
      "path": ".claude/agents/*.md",
      "file_pattern": "*.md",
      "exclude": ["README.md"],
      "registrations": [
        "_stats.json:agents",
        "_graph/knowledge-nodes.json",
        "_graph/edges.json",
        ".claude/SYSTEM-MAP.md:Agents",
        "_graph/cache/context-router.json"
      ],
      "id_pattern": "agent-{filename}"
    },
    "commands": {
      "path": ".claude/commands/*.md",
      "file_pattern": "*.md",
      "exclude": ["README.md"],
      "registrations": [
        "_stats.json:commands",
        ".claude/detection-index.json",
        "_graph/knowledge-nodes.json",
        "_graph/edges.json",
        ".claude/SYSTEM-MAP.md:Commands",
        "_graph/cache/context-router.json"
      ],
      "id_pattern": "cmd-{filename}"
    }
  }
}
```


#### Example



**Code:**
```bash
# Count agents
ls -1 .claude/agents/*.md | wc -l

# List all categories
ls .claude/
ls knowledge/
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/system-deep-research-agent.md`</small>
