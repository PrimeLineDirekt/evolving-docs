---
title: automation-setup-agent
type: agent
tags: []
lang: en
confidence: 100
---

# automation-setup-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Specialized automation agent that makes new findings automatically discoverable through routing, keywords, and graph connections. |
| **Complexity** | low |
| **Model** | haiku |
| **Category** | automation-setup |
| **Created** | 2026-01-08 |</div>


## What It Does

The Automation Setup Agent ensures that new findings (templates, patterns, learnings, commands) are automatically discoverable by the Context Scout system. It creates the necessary routing rules, detection keywords, and knowledge graph edges to make components findable.

**Core Principle:** Automatic discoverability - every finding should be reachable through Context Scout.

**Key Operations:**
1. **Context Router** - Creates/extends routes based on keyword overlap
2. **Detection Index** - Adds command keywords for plain-text triggers (commands only)
3. **Knowledge Graph Edges** - Creates relationships to related nodes based on tag overlap


## System Impact

- **Enables Context Scout discovery** - New components become findable by keywords
- **Powers plain-text command detection** - Commands trigger from natural language
- **Maintains knowledge graph connectivity** - Ensures no isolated nodes
- **Called by Integration Orchestrator** - Part of external finding integration workflow
- **Reduces manual configuration** - Automatic routing eliminates manual route creation


## Architecture

**Model:** Haiku (low complexity, deterministic operations)

**Capabilities:**
- `router-update` - Modify context router configuration
- `detection-index-update` - Add command keywords
- `edge-creation` - Create graph relationships

**Data Sources:**
- `_graph/cache/context-router.json` - Routing configuration (read/write)
- `.claude/detection-index.json` - Command detection keywords (read/write for commands)
- `_graph/edges.json` - Knowledge graph edges (read/write)
- `_graph/knowledge-nodes.json` - Node metadata for tag matching (read-only)

**Orchestration:**
- Invoked by `@integration-orchestrator-agent` after finding validation
- Receives finding metadata (name, type, path, tags, keywords)
- Returns automation setup results (routes created, edges added, etc.)

**Process Flow:**
1. Extract keywords from finding (tags + keywords)
2. Update Context Router (create/extend route based on keyword overlap ≥50%)
3. Update Detection Index (if finding type = command)
4. Create Graph Edges (to nodes with overlapping tags)
5. Return results summary


## Usage

**Input Format:**
```json
{
  "finding": {
    "name": "chunking-strategy",
    "type": "template",
    "path": ".claude/templates/chunking-strategy.md",
    "source_repo": "crawl4ai",
    "tags": ["llm", "chunking", "rag"],
    "keywords": ["chunk", "text splitting", "token limit"]
  }
}
```

**Invocation:**
```
@automation-setup-agent
{finding_json}
```

**Output:**
```json
{
  "status": "SUCCESS",
  "results": {
    "context_router": {
      "action": "extended",
      "route_name": "llm-processing",
      "keywords_added": ["chunking", "rag"],
      "node_added": "template-chunking-strategy"
    },
    "detection_index": {
      "skipped": true,
      "reason": "not a command"
    },
    "graph_edges": {
      "edges_created": 3,
      "total_count": 206
    }
  }
}
```


## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| **model** | haiku | Low complexity deterministic operations |
| **keyword_overlap_threshold** | 0.5 | Minimum 50% keyword overlap to extend existing route |
| **max_detection_keywords** | 10 | Maximum keywords per command in detection index |
| **edge_weight_calculation** | tag_overlap_count | Edge weight = number of shared tags |
| **default_command_confidence** | 80 | Default confidence score for new commands |

**Setup Matrix:**
| System | File | When | What |
|--------|------|------|------|
| Context Router | `context-router.json` | Always | Create/extend route |
| Detection Index | `detection-index.json` | Commands only | Add keywords |
| Graph Edges | `edges.json` | Always | Create relationships |

**Route Extension Logic:**
- If keyword overlap ≥ 50% with existing route → extend route
- If no match → create new route with finding's first tag as name


## Best Practices

**Do:**
- Provide comprehensive tags and keywords for better routing
- Use consistent tag naming across related findings
- Let the agent determine route placement (50% overlap threshold works well)
- Include source repository for external findings
- Validate finding metadata before invoking automation setup

**Don't:**
- Don't manually edit router/detection files after automation setup (breaks consistency)
- Don't provide empty tags/keywords arrays (agent will skip routing)
- Don't duplicate edges - agent already checks for existing edges
- Don't bypass this agent when integrating external findings (breaks discoverability)
- Don't use more than 10 keywords per command (detection index limit)




## Related


---

<small>Source: `.claude/agents/automation-setup-agent.md`</small>
