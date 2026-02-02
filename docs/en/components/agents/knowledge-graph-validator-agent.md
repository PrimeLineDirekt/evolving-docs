---
title: knowledge-graph-validator-agent
type: agent
tags: []
lang: en
confidence: 100
---

# knowledge-graph-validator-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents |</div>


## What It Does

Validiert Knowledge Graph Integrität - Nodes, Edges, Orphans, Legacy Status, _stats.json Sync


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
// _stats.json enthält:
"graph": {
  "nodes": 229,    // Muss = core-nodes + knowledge-nodes
  "edges": 245,    // Muss = edges.json count
  "routes": 32     // Muss = context-router routes
}
```


#### Example



**Code:**
```bash
Prüfe:
1. core-nodes.json: X nodes
2. knowledge-nodes.json: Y nodes
3. _stats.json.graph.nodes: Z
4. Erwartung: X + Y = Z

Legacy-Check:
5. nodes-legacy.json: L nodes
6. Frage: Sind alle L in (X+Y) migriert?
```


#### Example



**Code:**
```bash
Für jeden Edge in edges.json:
- source: Existiert in core-nodes ODER knowledge-nodes?
- target: Existiert in core-nodes ODER knowledge-nodes?
- relationship_type: Ist valide? (uses, implements, depends_on, etc.)

Für _stats.json:
- edges.json.length == _stats.json.graph.edges?
```


#### Example



**Code:**
```bash
Für jeden Node mit file_path:
- Existiert die Datei?
- Ist der Typ korrekt? (agent → .claude/agents/*.md)
- Ist der Name konsistent? (node.id ≈ filename)
```


#### Example



**Code:**
```bash
Orphan Node:
- Keine eingehenden UND keine ausgehenden Edges
- Wird nirgends referenziert
- Kann sicher gelöscht werden?

Orphan Edge:
- source ODER target existiert nicht
- Muss entfernt werden
```


#### Example



**Code:**
```bash
Vergleiche nodes-legacy.json mit aktuellen Partitionen:

migrated = nodes in legacy AND in (core OR knowledge)
not_migrated = nodes in legacy BUT NOT in (core OR knowledge)
new_since_migration = nodes in (core OR knowledge) BUT NOT in legacy

Status:
- Migration complete? (not_migrated == 0)
- Safe to delete legacy? (all migrated)
```


#### Example



**Code:**
```bash
Für jeden Route in context-router.json:
- primary_nodes: Existieren alle in nodes?
- secondary_nodes: Existieren alle in nodes?
- context_files: Existieren alle Dateien?

_stats.json.graph.routes == context-router.routes.length?
```


#### Example



**Code:**
```bash
Prüfe domain_tags in allen Nodes:
- Tag in taxonomy.json definiert?
- Tag konsistent geschrieben (kebab-case)?
- Verwaiste Tags (definiert, nie genutzt)?
```


#### Example



**Code:**
```python
def validate_knowledge_graph():
    issues = []
    recommendations = []

    # Load all graph data
    core = read_json("_graph/core-nodes.json")
    knowledge = read_json("_graph/knowledge-nodes.json")
    edges = read_json("_graph/edges.json")
    legacy = read_json("_graph/nodes-legacy.json")
    stats = read_json("_stats.json")
    router = read_json("_graph/cache/context-router.json")

    all_nodes = {**core, **knowledge}
    node_ids = set(all_nodes.keys())

    # 1. Count Validation
    expected_nodes = len(core) + len(knowledge)
    stats_nodes = stats["graph"]["nodes"]

    if expected_nodes != stats_nodes:
        issues.append({
            "type": "node_count_mismatch",
            "actual": expected_nodes,
            "stats_json": stats_nodes,
            "severity": "HIGH"
        })

    # 2. Edge Count
    if len(edges) != stats["graph"]["edges"]:
        issues.append({
            "type": "edge_count_mismatch",
            "actual": len(edges),
            "stats_json": stats["graph"]["edges"],
            "severity": "HIGH"
        })

    # 3. Node-File Existence
    for node_id, node in all_nodes.items():
        if "file_path" in node:
            if not file_exists(node["file_path"]):
                issues.append({
                    "type": "missing_node_file",
                    "node_id": node_id,
                    "expected_path": node["file_path"],
                    "severity": "HIGH"
                })

    # 4. Edge Validity
    for edge in edges:
        if edge["source"] not in node_ids:
            issues.append({
                "type": "orphan_edge_source",
                "edge_id": edge.get("id", "unknown"),
                "source": edge["source"],
                "severity": "MEDIUM"
            })
        if edge["target"] not in node_ids:
            issues.append({
                "type": "orphan_edge_target",
                "edge_id": edge.get("id", "unknown"),
                "target": edge["target"],
                "severity": "MEDIUM"
            })

    # 5. Orphan Nodes
    nodes_with_edges = set()
    for edge in edges:
        nodes_with_edges.add(edge["source"])
        nodes_with_edges.add(edge["target"])

    orphan_nodes = node_ids - nodes_with_edges
    for orphan in orphan_nodes:
        issues.append({
            "type": "orphan_node",
            "node_id": orphan,
            "severity": "LOW"
        })

    # 6. Legacy Migration
    legacy_ids = set(legacy.keys()) if legacy else set()
    migrated = legacy_ids & node_ids
    not_migrated = legacy_ids - node_ids

    if not_migrated:
        issues.append({
            "type": "incomplete_migration",
            "count": len(not_migrated),
            "nodes": list(not_migrated)[:10],  # First 10
            "severity": "HIGH"
        })
    else:
        recommendations.append({
            "type": "safe_to_archive_legacy",
            "files": ["nodes-legacy.json", "edges-legacy.json"],
            "reason": "All nodes migrated to partitions"
        })

    # 7. Context Router Sync
    router_routes = len(router.get("routes", []))
    if router_routes != stats["graph"]["routes"]:
        issues.append({
            "type": "routes_count_mismatch",
            "actual": router_routes,
            "stats_json": stats["graph"]["routes"],
            "severity": "MEDIUM"
        })

    return issues, recommendations
```


#### Example



**Code:**
```markdown
# Knowledge Graph Validation Report

## Summary
- **Core Nodes**: {n}
- **Knowledge Nodes**: {n}
- **Total Nodes**: {n}
- **Edges**: {n}
- **Orphan Nodes**: {n}
- **Invalid Edges**: {n}
- **Graph Health Score**: {score}/100

## _stats.json Sync Status

| Metric | Actual | _stats.json | Status |
|--------|--------|-------------|--------|
| Nodes | 441 | 229 | ❌ OUTDATED |
| Edges | 322 | 245 | ❌ OUTDATED |
| Routes | 35 | 32 | ❌ OUTDATED |

## Partition Status

| Partition | Nodes | Edges | Status |
|-----------|-------|-------|--------|
| core-nodes.json | 164 | - | Active |
| knowledge-nodes.json | 277 | - | Active |
| edges.json | - | 322 | Active |
| nodes-legacy.json | 434 | - | **DEPRECATED** |
| edges-legacy.json | - | 200 | **DEPRECATED** |

## Legacy Migration Analysis

**Migration Status**: 98% complete

| Category | Migrated | Not Migrated |
|----------|----------|--------------|
| Agents | 59/59 | 0 |
| Commands | 63/63 | 0 |
| Patterns | 50/52 | 2 |
| Learnings | 28/31 | 3 |

### Not Migrated Nodes
1. `pattern-old-deprecated` - Review needed
2. `learning-outdated-2025` - Archive candidate
...

### Recommendation
✅ **Safe to archive legacy files** after migrating 5 remaining nodes

## Issues Found

### HIGH: Node Count Mismatch
- **Actual nodes**: 441 (164 core + 277 knowledge)
- **_stats.json**: 229
- **Fix**: Update `_stats.json.graph.nodes = 441`

### HIGH: Edge Count Mismatch
- **Actual edges**: 322
- **_stats.json**: 245
- **Fix**: Update `_stats.json.graph.edges = 322`

### MEDIUM: Orphan Edges (14 found)
```


#### Example



**Code:**
```bash
**Fix**: Remove these edges from edges.json

### LOW: Orphan Nodes (8 found)
```


#### Example



**Code:**
```bash
**Fix**: Add edges or remove nodes

## Context Router Analysis

| Metric | Value |
|--------|-------|
| Total Routes | 35 |
| Routes with valid nodes | 32 |
| Routes with invalid nodes | 3 |

### Invalid Route Targets
1. Route "debugging" → `agent-debug-helper` not found
2. Route "testing" → `pattern-test-old` not found

## Auto-Sync Recommendations

### Current Problem
- Graph changes don't update _stats.json
- Hook `graph-update.sh` is **PLACEHOLDER** (nicht implementiert!)

### Recommended Solution

```


#### Example



**Code:**
```bash

## Cleanup Roadmap

### Phase 1: Fix Stats (5 min)
1. Update _stats.json graph counts

### Phase 2: Clean Edges (15 min)
2. Remove 14 orphan edges
3. Verify edge integrity

### Phase 3: Archive Legacy (10 min)
4. Move nodes-legacy.json → _backup/
5. Move edges-legacy.json → _backup/
6. Update manifest.json

### Phase 4: Implement Auto-Sync (30 min)
7. Implement graph-update.sh hook
8. Test with new node creation
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/knowledge-graph-validator-agent.md`</small>
