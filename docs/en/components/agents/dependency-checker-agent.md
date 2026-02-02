---
title: dependency-checker-agent
type: agent
tags: []
lang: en
confidence: 100
---

# dependency-checker-agent


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

"Prüft Finding-Abhängigkeiten: Tool-Mutex, Naming, Overlap, Circular Dependencies"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "finding": {
    "name": "context-manager-agent",
    "type": "agent",
    "path": ".claude/agents/context-manager-agent.md",
    "source_repo": "github.com/some/repo",
    "content": "... Agent-Definition ...",
    "tools_used": ["mcp__puppeteer__navigate", "Read", "Write"],
    "keywords": ["context", "manage", "session"],
    "references": ["@other-agent", "@helper-agent"]
  }
}
```


#### Example



**Code:**
```python
def check_dependencies(finding):
    checks = {}

    # 1. Tool-Mutex Check
    checks["tool_mutex"] = check_tool_mutex(finding)

    # 2. Naming Check
    checks["naming"] = check_naming(finding)

    # 3. Pattern-Overlap Check
    checks["pattern_overlap"] = check_pattern_overlap(finding)

    # 4. Circular Dependency Check
    checks["circular"] = check_circular_dependencies(finding)

    # Aggregate Severity
    severities = [c["severity"] for c in checks.values()]

    if "BLOCKED" in severities:
        overall = "BLOCKED"
    elif "FIXABLE" in severities:
        overall = "FIXABLE"
    else:
        overall = "CLEAN"

    # Collect fixes
    fixes = []
    for check_name, result in checks.items():
        if result.get("fix"):
            fixes.append(result["fix"])

    return {
        "status": overall,
        "checks": checks,
        "fixes_available": fixes,
        "blocking_reason": get_blocking_reason(checks) if overall == "BLOCKED" else None
    }
```


#### Example



**Code:**
```python
def check_tool_mutex(finding):
    mutex_config = Read(".claude/tools/tool-mutex.json")
    finding_tools = finding.get("tools_used", [])

    if not finding_tools:
        return {"severity": "CLEAN", "conflicts": []}

    conflicts = []

    for tool in finding_tools:
        for group_name, group in mutex_config["mutex_groups"].items():
            # Wildcard-Matching
            if matches_any(tool, group["tools"]):
                # Prüfe ob konfliktierendes Tool im System aktiv
                for blocked_tool in group["tools"]:
                    if blocked_tool != tool and is_tool_in_use(blocked_tool):
                        conflicts.append({
                            "finding_tool": tool,
                            "blocked_by": blocked_tool,
                            "mutex_group": group_name,
                            "conflict_type": group.get("conflict_type", "NON-FIXABLE")
                        })

    if not conflicts:
        return {"severity": "CLEAN", "conflicts": []}

    # Severity basierend auf conflict_type
    has_non_fixable = any(c["conflict_type"] == "NON-FIXABLE" for c in conflicts)

    return {
        "severity": "BLOCKED" if has_non_fixable else "FIXABLE",
        "conflicts": conflicts,
        "fix": None if has_non_fixable else {
            "type": "tool_replacement",
            "description": "Replace conflicting tools with alternatives"
        }
    }

def matches_any(tool, patterns):
    """Wildcard matching: mcp__puppeteer__* matches mcp__puppeteer__navigate"""
    for pattern in patterns:
        if pattern.endswith("*"):
            prefix = pattern[:-1]
            if tool.startswith(prefix):
                return True
        elif tool == pattern:
            return True
    return False
```


#### Example



**Code:**
```python
def check_naming(finding):
    # Lade alle existierenden Namen
    detection_index = Read(".claude/detection-index.json")
    graph_nodes = Read("_graph/knowledge-nodes.json")

    existing_names = set()

    # Commands aus detection-index
    for cmd in json.loads(detection_index).get("commands", {}).keys():
        existing_names.add(normalize(cmd))

    # Nodes aus Graph
    for node in json.loads(graph_nodes).get("nodes", []):
        existing_names.add(normalize(node["name"]))
        existing_names.add(normalize(node["id"]))

    finding_name = normalize(finding["name"])

    # 1. Exakter Match
    if finding_name in existing_names:
        return {
            "severity": "BLOCKED",
            "type": "EXACT_MATCH",
            "existing": finding_name,
            "fix": None
        }

    # 2. Similarity Check
    similar = []
    for name in existing_names:
        sim = calculate_similarity(finding_name, name)
        if sim >= 0.8:
            similar.append({"name": name, "similarity": round(sim, 2)})

    if similar:
        suggested = generate_unique_name(finding_name, existing_names)
        return {
            "severity": "FIXABLE",
            "type": "SIMILAR_NAMES",
            "similar": sorted(similar, key=lambda x: -x["similarity"])[:3],
            "fix": {
                "type": "rename",
                "from": finding["name"],
                "to": suggested
            }
        }

    return {"severity": "CLEAN"}

def normalize(name):
    """Normalisiert Namen für Vergleich"""
    return name.lower().replace("-", "").replace("_", "").replace(" ", "")

def calculate_similarity(a, b):
    """Levenshtein-basierte Ähnlichkeit"""
    if len(a) == 0 or len(b) == 0:
        return 0
    distance = levenshtein_distance(a, b)
    max_len = max(len(a), len(b))
    return 1 - (distance / max_len)

def generate_unique_name(base, existing):
    """Generiert eindeutigen Namen mit ext- Prefix"""
    candidate = f"ext-{base}"
    if normalize(candidate) not in existing:
        return candidate

    # Mit Nummer
    for i in range(2, 10):
        candidate = f"ext-{base}-{i}"
        if normalize(candidate) not in existing:
            return candidate

    return f"ext-{base}-{hash(base)[:4]}"
```


#### Example



**Code:**
```python
def check_pattern_overlap(finding):
    detection_index = Read(".claude/detection-index.json")
    index = json.loads(detection_index)

    finding_keywords = set(finding.get("keywords", []))

    if not finding_keywords:
        return {"severity": "CLEAN", "overlaps": []}

    overlaps = []

    for cmd, data in index.get("commands", {}).items():
        cmd_keywords = set(data.get("kw", []))

        intersection = finding_keywords & cmd_keywords
        if intersection:
            overlap_ratio = len(intersection) / len(finding_keywords)

            if overlap_ratio >= 0.6:
                overlaps.append({
                    "command": cmd,
                    "keywords": list(intersection),
                    "ratio": round(overlap_ratio, 2)
                })

    if not overlaps:
        return {"severity": "CLEAN", "overlaps": []}

    # High overlap = potential trigger conflict
    max_ratio = max(o["ratio"] for o in overlaps)

    if max_ratio >= 0.8:
        return {
            "severity": "BLOCKED",
            "overlaps": overlaps,
            "reason": "Keywords would trigger existing command",
            "fix": None
        }
    else:
        # Unique keywords vorschlagen
        conflicting = set()
        for o in overlaps:
            conflicting.update(o["keywords"])

        unique_keywords = finding_keywords - conflicting

        return {
            "severity": "FIXABLE",
            "overlaps": overlaps,
            "fix": {
                "type": "keyword_change",
                "remove": list(conflicting),
                "keep": list(unique_keywords),
                "suggestion": f"Use only: {list(unique_keywords)}"
            }
        }
```


#### Example



**Code:**
```python
def check_circular_dependencies(finding):
    # Nur relevant für Agents
    if finding["type"] != "agent":
        return {"severity": "CLEAN", "skipped": True}

    references = finding.get("references", [])
    if not references:
        return {"severity": "CLEAN", "references": []}

    # Lade existierende Agent-Referenzen
    agent_graph = build_agent_graph()

    # Füge Finding temporär hinzu
    finding_id = f"agent-{finding['name']}"
    agent_graph[finding_id] = references

    # DFS für Zyklus-Erkennung
    cycles = find_cycles(agent_graph, finding_id)

    if cycles:
        return {
            "severity": "BLOCKED",
            "cycles": cycles,
            "reason": f"Circular dependency detected: {' → '.join(cycles[0])}",
            "fix": None
        }

    return {"severity": "CLEAN", "references": references}

def build_agent_graph():
    """Baut Graph aus allen Agent-Referenzen"""
    agents_dir = ".claude/agents/"
    graph = {}

    for agent_file in Glob(f"{agents_dir}*.md"):
        content = Read(agent_file)
        agent_name = extract_agent_name(agent_file)
        references = extract_references(content)  # Findet @agent-name Patterns
        graph[f"agent-{agent_name}"] = references

    return graph

def find_cycles(graph, start):
    """DFS Zyklus-Erkennung"""
    visited = set()
    path = []
    cycles = []

    def dfs(node):
        if node in path:
            cycle_start = path.index(node)
            cycles.append(path[cycle_start:] + [node])
            return

        if node in visited:
            return

        visited.add(node)
        path.append(node)

        for ref in graph.get(node, []):
            dfs(ref)

        path.pop()

    dfs(start)
    return cycles

def extract_references(content):
    """Extrahiert @agent-name Referenzen aus Content"""
    import re
    pattern = r'@([a-z0-9-]+)-agent'
    matches = re.findall(pattern, content.lower())
    return [f"agent-{m}" for m in matches]
```


#### Example



**Code:**
```json
{
  "status": "FIXABLE",
  "checks": {
    "tool_mutex": {
      "severity": "CLEAN",
      "conflicts": []
    },
    "naming": {
      "severity": "FIXABLE",
      "type": "SIMILAR_NAMES",
      "similar": [{"name": "context-agent", "similarity": 0.85}],
      "fix": {"type": "rename", "from": "context-manager", "to": "ext-context-manager"}
    },
    "pattern_overlap": {
      "severity": "CLEAN",
      "overlaps": []
    },
    "circular": {
      "severity": "CLEAN",
      "references": ["@helper-agent"]
    }
  },
  "fixes_available": [
    {"type": "rename", "from": "context-manager", "to": "ext-context-manager"}
  ],
  "blocking_reason": null
}
```


#### Example



**Code:**
```bash
@dependency-checker-agent
{
  "finding": {
    "name": "context-manager-agent",
    "type": "agent",
    "path": ".claude/agents/context-manager-agent.md",
    "source_repo": "github.com/some/repo",
    "content": "...",
    "tools_used": ["Read", "Write"],
    "keywords": ["context", "session"],
    "references": ["@helper-agent"]
  }
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/dependency-checker-agent.md`</small>
