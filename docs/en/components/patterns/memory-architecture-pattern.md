---
title: memory-architecture-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# memory-architecture-pattern


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does




## System Impact

**Capabilities Provided:**
- Structured approach to component creation
- Automated validation and best practices
- Standardized output format
- Integration with system architecture

**When to Use:**
- Creating new system components
- Standardizing component structure
- Ensuring consistency across codebase
- Automating repetitive creation tasks



## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
          Latency    Capacity    Persistence
             ↓          ↓           ↓
┌─────────────────────────────────────────────┐
│  WORKING MEMORY (Context Window)            │
│  - Zero latency, volatile                   │
│  - Scratchpad, current task state           │
└─────────────────────────────────────────────┘
             ↓
┌─────────────────────────────────────────────┐
│  SHORT-TERM MEMORY (Session-Scoped)         │
│  - Session-persistent, searchable           │
│  - Intermediate results, caches             │
└─────────────────────────────────────────────┘
             ↓
┌─────────────────────────────────────────────┐
│  LONG-TERM MEMORY (Cross-Session)           │
│  - Persistent, structured                   │
│  - User preferences, project state          │
└─────────────────────────────────────────────┘
             ↓
┌─────────────────────────────────────────────┐
│  ENTITY MEMORY (Knowledge Graph)            │
│  - Entity identity across conversations     │
│  - Relationship tracking                    │
└─────────────────────────────────────────────┘
             ↓
┌─────────────────────────────────────────────┐
│  TEMPORAL KNOWLEDGE GRAPH                   │
│  - Validity periods (valid_from/valid_until)│
│  - Time-travel queries                      │
│  - Context clash prevention                 │
└─────────────────────────────────────────────┘
```


#### Example



**Code:**
```bash
_memory/
├── index.json              # Aktiver Context
├── projects/
│   └── {name}.json         # Projekt-State
├── experiences/
│   └── exp-YYYY-NNN.json   # Experience Memory
└── sessions/
    └── context.json        # Session-spezifisch
```


#### Example



**Code:**
```python
def add_with_metadata(text, entity, valid_from, valid_until=None):
    embedding = embed(text)
    metadata = {
        "entity": entity,
        "valid_from": valid_from.isoformat(),
        "valid_until": valid_until.isoformat() if valid_until else None
    }
    vector_store.add(embedding, metadata)
```


#### Example



**Code:**
```json
{
  "nodes": [...],
  "edges": [
    {
      "source": "project-evolving",
      "target": "pattern-multi-agent",
      "type": "implements",
      "valid_from": "2025-12-01T00:00:00Z",
      "valid_until": null
    }
  ]
}
```


#### Example



**Code:**
```python
def query_at_time(graph, query_time):
    """Query graph state at specific point in time."""
    valid_edges = []
    for edge in graph.edges:
        valid_from = parse_date(edge.get("valid_from", "1970-01-01"))
        valid_until = edge.get("valid_until")

        if valid_from <= query_time:
            if valid_until is None or parse_date(valid_until) > query_time:
                valid_edges.append(edge)

    return valid_edges
```


#### Example



**Code:**
```python
def consolidate(memory_system):
    # 1. Find duplicates (same subject + predicate)
    duplicates = find_duplicate_groups()

    # 2. Merge related facts
    for group in duplicates:
        keeper = max(group, key=lambda e: e.confidence)
        merge_properties(keeper, *group)
        delete_others(group, except_=keeper)

    # 3. Update validity periods
    update_validity_periods()

    # 4. Rebuild indexes
    rebuild_indexes()
```


#### Example



**Code:**
```python
# Hybrid: KG für Relationships, ChromaDB für Semantic Search
def hybrid_query(query, query_time=None):
    # 1. Semantic search in ChromaDB
    semantic_results = chromadb.query(query, n=10)

    # 2. Entity extraction from results
    entities = extract_entities(semantic_results)

    # 3. Graph traversal for relationships
    related = graph.find_related(entities, query_time)

    # 4. Merge and rank
    return merge_and_rank(semantic_results, related)
```




## Configuration



## Best Practices

**Do:**
- Use for multi-expert coordination requiring diverse perspectives
- Apply when problem benefits from iterative refinement
- Combine with proper state management and validation
- Monitor blackboard size to prevent context overflow

**Don't:**
- Use for simple single-agent tasks
- Apply to strictly sequential workflows
- Ignore controller bottleneck risks
- Forget to handle write conflicts in concurrent scenarios




## Related


---

<small>Source: `knowledge/patterns/memory-architecture-pattern.md`</small>
