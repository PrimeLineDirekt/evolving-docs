---
title: multi-strategy-retrieval-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# multi-strategy-retrieval-pattern


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




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
                    ┌─────────────┐
                    │    Query    │
                    └──────┬──────┘
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  SEMANTIC   │    │   KEYWORD   │    │    GRAPH    │
│   (Vector)  │    │   (BM25)    │    │ (Traversal) │
│             │    │             │    │             │
│ Embeddings  │    │ Full-Text   │    │ Entity +    │
│ Cosine Sim  │    │ TF-IDF      │    │ Relation    │
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  TEMPORAL       │
                  │  (Time Filter)  │
                  │                 │
                  │ Recency Boost   │
                  │ Valid Window    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  SCORE FUSION   │
                  │                 │
                  │ Weighted Merge  │
                  │ Deduplication   │
                  │ Ranking         │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    Results      │
                  └─────────────────┘
```


#### Example



**Code:**
```python
# Pseudocode
query_embedding = embed(query)
results = vector_db.search(
    query_embedding,
    metric="cosine",
    top_k=20
)
```


#### Example



**Code:**
```python
# Pseudocode
results = search_index.query(
    query,
    algorithm="bm25",
    top_k=20
)
```


#### Example



**Code:**
```python
# Pseudocode
entities = extract_entities(query)
results = []
for entity in entities:
    node = graph.find_node(entity)
    related = graph.traverse(node, depth=2)
    results.extend(related)
```


#### Example



**Code:**
```python
# Pseudocode
results = base_results.filter(
    lambda r: r.valid_until is None or r.valid_until > now
).boost(
    lambda r: recency_score(r.created_at)
)
```


#### Example



**Code:**
```python
def rrf_score(rankings, k=60):
    """
    Combine multiple ranking lists.

    rankings: dict of {doc_id: rank} for each strategy
    k: constant (typically 60)
    """
    scores = {}
    for strategy, ranking in rankings.items():
        for doc_id, rank in ranking.items():
            if doc_id not in scores:
                scores[doc_id] = 0
            scores[doc_id] += 1 / (k + rank)
    return sorted(scores.items(), key=lambda x: -x[1])
```


#### Example



**Code:**
```python
def weighted_fusion(results, weights):
    """
    weights = {
        'semantic': 0.4,
        'keyword': 0.3,
        'graph': 0.2,
        'temporal': 0.1
    }
    """
    final_scores = {}
    for strategy, weight in weights.items():
        for doc, score in results[strategy]:
            if doc not in final_scores:
                final_scores[doc] = 0
            final_scores[doc] += score * weight
    return sorted(final_scores.items(), key=lambda x: -x[1])
```


#### Example



**Code:**
```python
# In _graph/cache/context-router.json
{
  "typescript-error": {
    "keywords": ["typescript", "ts", "type error", "tsc"],
    "fuzzy": true
  }
}
```


#### Example



**Code:**
```bash
Query: "API error"
→ Keyword Match: exp-2025-001 (API Error)
→ Graph Expansion: exp-2025-002 (HTTP Client), exp-2025-003 (Auth Error)
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/multi-strategy-retrieval-pattern.md`</small>
