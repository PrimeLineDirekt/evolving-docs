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
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2026-01-08 |</div>


## What It Does

"Richtet automatische Findbarkeit ein: Context Router, Detection Index, Graph Edges"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
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


#### Example



**Code:**
```python
def setup_automation(finding):
    results = {}

    # 1. Context Router
    router_result = update_context_router(finding)
    results["context_router"] = router_result

    # 2. Detection Index (nur Commands)
    if finding["type"] == "command":
        detection_result = update_detection_index(finding)
        results["detection_index"] = detection_result
    else:
        results["detection_index"] = {"skipped": True, "reason": "not a command"}

    # 3. Graph Edges
    edges_result = create_graph_edges(finding)
    results["graph_edges"] = edges_result

    return {
        "status": "SUCCESS",
        "results": results
    }
```


#### Example



**Code:**
```python
def update_context_router(finding):
    router = Read("_graph/cache/context-router.json")
    routes = json.loads(router)

    # 1. Finding-Keywords sammeln
    finding_keywords = set(finding.get("tags", []) + finding.get("keywords", []))

    # 2. Beste existierende Route finden
    best_match = None
    best_overlap = 0

    for route_name, route_data in routes["routes"].items():
        route_keywords = set(route_data.get("keywords", []))
        overlap = len(finding_keywords & route_keywords) / len(finding_keywords)

        if overlap >= 0.5 and overlap > best_overlap:
            best_match = route_name
            best_overlap = overlap

    # 3. Route erweitern oder neu erstellen
    node_id = f"{finding['type']}-{finding['name']}"

    if best_match:
        # Zu existierender Route hinzufügen
        routes["routes"][best_match]["primary"].append(node_id)

        # Neue Keywords hinzufügen
        for kw in finding_keywords:
            if kw not in routes["routes"][best_match]["keywords"]:
                routes["routes"][best_match]["keywords"].append(kw)

        action = "extended"
        route_name = best_match
    else:
        # Neue Route erstellen
        route_name = finding["tags"][0] if finding.get("tags") else finding["name"]

        routes["routes"][route_name] = {
            "keywords": list(finding_keywords),
            "primary": [node_id],
            "secondary": [],
            "context_files": [finding["path"]]
        }

        # Route Count erhöhen
        routes["count"] = len(routes["routes"])

        action = "created"

    # 4. Schreiben
    Write("_graph/cache/context-router.json", json.dumps(routes, indent=2))

    return {
        "action": action,
        "route_name": route_name,
        "keywords_added": list(finding_keywords),
        "node_added": node_id
    }
```


#### Example



**Code:**
```json
{
  "routes": {
    "llm-processing": {
      "keywords": ["llm", "chunking", "rag", "embedding"],
      "primary": ["template-chunking-strategy", "pattern-context-window"],
      "secondary": ["learning-token-limits"],
      "context_files": [".claude/templates/chunking-strategy.md"]
    }
  },
  "count": 45
}
```


#### Example



**Code:**
```python
def update_detection_index(finding):
    if finding["type"] != "command":
        return {"skipped": True, "reason": "not a command"}

    detection = Read(".claude/detection-index.json")
    index = json.loads(detection)

    command_name = finding["name"]

    # Prüfe ob Command bereits existiert
    if command_name in index["commands"]:
        return {"skipped": True, "reason": "command exists"}

    # Keywords aus Finding
    keywords = finding.get("keywords", []) + finding.get("tags", [])

    # Neuen Command-Eintrag erstellen
    index["commands"][command_name] = {
        "kw": keywords[:10],  # Max 10 Keywords
        "cf": 80,  # Default Confidence
        "cat": determine_category(finding.get("tags", []))
    }

    # Count erhöhen
    index["count"] = len(index["commands"])

    # Schreiben
    Write(".claude/detection-index.json", json.dumps(index, indent=2))

    return {
        "command": command_name,
        "keywords": keywords[:10],
        "count": index["count"]
    }

def determine_category(tags):
    """Kategorie aus Tags ableiten"""
    category_map = {
        "research": "research",
        "audit": "audit",
        "idea": "ideas",
        "memory": "memory",
        "sync": "sync",
        "model": "model"
    }

    for tag in tags:
        for key, cat in category_map.items():
            if key in tag.lower():
                return cat

    return "utility"  # Default
```


#### Example



**Code:**
```json
{
  "commands": {
    "analyze-repo": {
      "kw": ["repo", "analyze", "external", "github"],
      "cf": 85,
      "cat": "research"
    }
  },
  "count": 47
}
```


#### Example



**Code:**
```python
def create_graph_edges(finding):
    edges_file = Read("_graph/edges.json")
    edges = json.loads(edges_file)

    nodes_file = Read("_graph/knowledge-nodes.json")
    nodes = json.loads(nodes_file)

    finding_id = f"{finding['type']}-{finding['name']}"
    finding_tags = set(finding.get("tags", []))

    new_edges = []

    # Finde Nodes mit überlappenden Tags
    for node in nodes["nodes"]:
        if node["id"] == finding_id:
            continue  # Skip self

        node_tags = set(node.get("tags", []))
        overlap = finding_tags & node_tags

        if len(overlap) >= 1:
            # Relation-Type bestimmen
            if finding["type"] == node["type"]:
                relation = "sibling"
            elif finding["type"] in ["pattern", "learning"]:
                relation = "related_to"
            else:
                relation = "connected_to"

            edge = {
                "source": finding_id,
                "target": node["id"],
                "relation": relation,
                "weight": len(overlap),  # Mehr Overlap = stärkere Verbindung
                "created": get_date()
            }

            # Prüfe ob Edge bereits existiert
            exists = any(
                e["source"] == edge["source"] and e["target"] == edge["target"]
                for e in edges["edges"]
            )

            if not exists:
                edges["edges"].append(edge)
                new_edges.append(edge)

    # Count aktualisieren
    edges["count"] = len(edges["edges"])

    # Schreiben
    Write("_graph/edges.json", json.dumps(edges, indent=2))

    return {
        "edges_created": len(new_edges),
        "edges": new_edges,
        "total_count": edges["count"]
    }
```


#### Example



**Code:**
```json
{
  "edges": [
    {
      "source": "template-chunking-strategy",
      "target": "pattern-context-window-ownership",
      "relation": "related_to",
      "weight": 2,
      "created": "2026-01-08"
    }
  ],
  "count": 203
}
```


#### Example



**Code:**
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
      "edges": [...],
      "total_count": 206
    }
  }
}
```


#### Example



**Code:**
```bash
@automation-setup-agent
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




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/automation-setup-agent.md`</small>
