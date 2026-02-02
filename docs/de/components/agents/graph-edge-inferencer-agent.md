---
title: graph-edge-inferencer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# graph-edge-inferencer-agent


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

"Infers Knowledge Graph edges from file content and relationships"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "new_nodes": ["agent-new-agent", "cmd-new-cmd"],
  "all_nodes": [...],
  "edges_json_path": "_graph/edges.json",
  "target_path": "/path/to/repo"
}
```


#### Example



**Code:**
```json
{
  "source": "cmd-new-cmd",
  "target": "agent-new-agent",
  "type": "uses"
}
```


#### Example



**Code:**
```markdown
# In command file:
Starte Task mit `xyz-agent`
# OR
Task mit xyz-agent-agent
# OR
agent: xyz-agent
```


#### Example



**Code:**
```yaml
# In agent frontmatter:
traits:
  - specialist
  - research
# OR in content:
basiert auf specialist-template
```


#### Example



**Code:**
```markdown
# In command file:
Skill tool mit "skill-name"
# OR
/skill-name aufrufen
```


#### Example



**Code:**
```markdown
# In skill reference.md:
Implementiert: pattern-name
# OR
Based on: xyz-pattern
```


#### Example



**Code:**
```bash
# In hook file:
claude -p "/command-name"
```


#### Example



**Code:**
```bash
FOR each new_node:
  1. Read source file content
  2. Scan for reference patterns:
     - Task with agent names
     - Template/trait references
     - Skill invocations
     - Pattern implementations
  3. For each detected reference:
     - Find target node by name/id
     - Determine relationship type
     - Create edge if target exists
  4. Deduplicate edges
```


#### Example



**Code:**
```json
{
  "inferred_edges": [
    {
      "source": "cmd-new-cmd",
      "target": "agent-new-agent",
      "type": "uses",
      "confidence": "high",
      "evidence": "Line 42: Task mit new-agent"
    }
  ],
  "summary": {
    "total_inferred": 3,
    "high_confidence": 2,
    "medium_confidence": 1
  }
}
```


#### Example



**Code:**
```bash
🔗 EDGE INFERENCE:
├── cmd-new-cmd → agent-new-agent (uses)
│   └── Evidence: "Task mit new-agent" [high]
├── agent-new-agent → tpl-specialist (based_on)
│   └── Evidence: "traits: specialist" [high]
└── Inferred: 3 edges (2 high, 1 medium confidence)
```


#### Example



**Code:**
```bash
# Find agent references in commands
grep -r "Task mit\|agent:" .claude/commands/

# Find template references
grep -r "traits:\|based_on:" .claude/agents/
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/graph-edge-inferencer-agent.md`</small>
