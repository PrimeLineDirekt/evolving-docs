---
title: compatibility-checker-agent
type: agent
tags: []
lang: en
confidence: 100
---

# compatibility-checker-agent


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

"Prüft externe Findings auf Kompatibilität mit dem Evolving System"


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
    "source_repo": "github.com/some/repo",
    "content": "... Agent-Definition ...",
    "extracted_tools": ["mcp__puppeteer__navigate", "Read", "Write"],
    "extracted_keywords": ["context", "manage", "session"]
  }
}
```


#### Example



**Code:**
```python
def check_tool_mutex(finding):
    # 1. Lade Mutex-Config
    mutex_config = Read(".claude/tools/tool-mutex.json")

    # 2. Extrahiere Tools aus Finding
    finding_tools = finding["extracted_tools"]

    # 3. Prüfe gegen Mutex-Gruppen
    conflicts = []
    for tool in finding_tools:
        for group_name, group in mutex_config["mutex_groups"].items():
            # Wildcard-Matching: mcp__puppeteer__* matched mcp__puppeteer__navigate
            if matches_pattern(tool, group["tools"]):
                # Prüfe ob konfliktierendes Tool bereits im System
                existing = get_system_tools()  # Aus SYSTEM-MAP.md
                for existing_tool in existing:
                    if matches_pattern(existing_tool, group["tools"]) and existing_tool != tool:
                        conflicts.append({
                            "finding_tool": tool,
                            "existing_tool": existing_tool,
                            "mutex_group": group_name,
                            "severity": group["conflict_type"],
                            "resolution_options": group["resolution_options"]
                        })

    return conflicts
```


#### Example



**Code:**
```markdown
❌ TOOL-MUTEX KONFLIKT

Finding nutzt: `mcp__puppeteer__navigate`
Konflikt mit: `mcp__claude-in-chrome__navigate` (bereits in System)
Mutex-Gruppe: browser_automation
Severity: NON-FIXABLE

Optionen:
1. Finding ablehnen
2. Bestehende Tools ersetzen (BREAKING!)
3. Als Template abstrahieren
```


#### Example



**Code:**
```python
def check_naming(finding):
    # 1. Lade alle existierenden Namen
    detection_index = Read(".claude/detection-index.json")
    graph_nodes = Read("_graph/nodes.json")

    all_names = extract_names(detection_index, graph_nodes)
    finding_name = normalize(finding["name"])

    # 2. Exakter Match?
    if finding_name in all_names:
        return {
            "severity": "NON-FIXABLE",
            "type": "EXACT_MATCH",
            "existing": finding_name,
            "resolution": "Rename oder Merge mit bestehendem"
        }

    # 3. Similarity Check (Levenshtein)
    similar = []
    for name in all_names:
        similarity = calculate_similarity(finding_name, name)
        if similarity >= 0.7:  # 70%+
            similar.append({"name": name, "similarity": similarity})

    if similar:
        suggested_name = generate_unique_name(finding_name, all_names)
        return {
            "severity": "FIXABLE",
            "type": "SIMILAR_NAMES",
            "similar": similar,
            "suggestion": f"Rename zu '{suggested_name}'"
        }

    return {"severity": "CLEAN"}
```


#### Example



**Code:**
```python
def calculate_similarity(a, b):
    # Levenshtein-basiert
    distance = levenshtein_distance(a, b)
    max_len = max(len(a), len(b))
    return 1 - (distance / max_len)
```


#### Example



**Code:**
```markdown
⚠️ NAMING-KONFLIKT (FIXABLE)

Finding: `context-manager`
Ähnlich zu:
- `context-manager-agent` (85% Similarity)
- `context-optimizer` (62% Similarity)

Empfehlung: Rename zu `ext-context-manager`

Auto-Fix anwenden? [y/N]
```


#### Example



**Code:**
```python
def check_pattern_overlap(finding):
    # 1. Lade Detection-Index
    detection_index = Read(".claude/detection-index.json")

    # 2. Finding-Keywords
    finding_kw = set(finding["extracted_keywords"])

    # 3. Vergleiche mit allen Commands
    overlaps = []
    for cmd, data in detection_index["commands"].items():
        cmd_kw = set(data.get("kw", []))

        intersection = finding_kw & cmd_kw
        if intersection:
            overlap_ratio = len(intersection) / len(finding_kw)

            if overlap_ratio >= 0.7:
                severity = "NON-FIXABLE"
            elif overlap_ratio >= 0.4:
                severity = "FIXABLE"
            else:
                continue

            overlaps.append({
                "command": cmd,
                "overlapping_keywords": list(intersection),
                "overlap_ratio": overlap_ratio,
                "severity": severity
            })

    return overlaps
```


#### Example



**Code:**
```markdown
❌ PATTERN-OVERLAP (NON-FIXABLE)

Finding-Keywords: ["repo", "analyze", "deep dive"]
Konflikt mit: `/analyze-repo`
Überlappung: ["repo", "analyze"] (66%)

Problem: Finding würde `/analyze-repo` triggern!

Optionen:
1. Keywords ändern zu ["external-repo", "source-audit"]
2. Nur programmatisch nutzbar (kein Trigger)
3. Finding ablehnen
```


#### Example



**Code:**
```python
def check_subagent_usage(finding):
    content = finding["content"]

    # 1. Tasks identifizieren (heuristisch)
    tasks = extract_tasks_from_workflow(content)

    # 2. Komplexität bewerten (1-10)
    scored_tasks = []
    for task in tasks:
        complexity = estimate_complexity(task)
        has_delegation = "Task(" in task or "@" in task

        scored_tasks.append({
            "description": task[:50],
            "complexity": complexity,
            "delegated": has_delegation,
            "recommended_model": get_model(complexity)
        })

    # 3. Delegation-Score berechnen
    delegatable = [t for t in scored_tasks if t["complexity"] <= 6]
    actually_delegated = [t for t in delegatable if t["delegated"]]

    if len(delegatable) == 0:
        score = 10
    else:
        score = (len(actually_delegated) / len(delegatable)) * 10

    # 4. Token-Ersparnis schätzen
    savings = sum(
        estimate_token_savings(t["complexity"])
        for t in delegatable if not t["delegated"]
    )

    return {
        "severity": "FIXABLE" if score < 7 else "CLEAN",
        "score": round(score, 1),
        "delegatable_tasks": len(delegatable),
        "actually_delegated": len(actually_delegated),
        "missing_delegation": [t for t in delegatable if not t["delegated"]],
        "potential_savings": f"~{savings}K Tokens"
    }

def get_model(complexity):
    if complexity <= 3:
        return "haiku"
    elif complexity <= 6:
        return "sonnet"
    else:
        return "opus"

def estimate_token_savings(complexity):
    # Grobe Schätzung
    if complexity <= 3:
        return 5  # 5K Tokens
    elif complexity <= 6:
        return 3  # 3K Tokens
    return 0
```


#### Example



**Code:**
```markdown
⚠️ SUB-AGENT NUTZUNG (FIXABLE)

Delegation-Score: 4/10

Nicht-delegierte Tasks:
1. "List Python files" (Kompl. 2) → Haiku (~5K gespart)
2. "Extract signatures" (Kompl. 3) → Haiku (~5K gespart)
3. "Generate graph" (Kompl. 5) → Sonnet (~3K gespart)

Potenzielle Ersparnis: ~13K Tokens/Run

Optimierung vorschlagen? [y/N]
```


#### Example



**Code:**
```python
def run_compatibility_check(finding):
    results = {
        "finding": finding["name"],
        "source": finding["source_repo"],
        "checks": {}
    }

    # 1. Alle Checks ausführen
    results["checks"]["tool_mutex"] = check_tool_mutex(finding)
    results["checks"]["naming"] = check_naming(finding)
    results["checks"]["pattern_overlap"] = check_pattern_overlap(finding)
    results["checks"]["subagent"] = check_subagent_usage(finding)

    # 2. Severity aggregieren
    severities = [
        get_severity(results["checks"]["tool_mutex"]),
        get_severity(results["checks"]["naming"]),
        get_severity(results["checks"]["pattern_overlap"]),
        results["checks"]["subagent"]["severity"]
    ]

    if "NON-FIXABLE" in severities:
        results["overall_severity"] = "NON-FIXABLE"
        results["action"] = "BLOCK_AND_ASK"
    elif "FIXABLE" in severities:
        results["overall_severity"] = "FIXABLE"
        results["action"] = "WARN_AND_OFFER_FIX"
    else:
        results["overall_severity"] = "CLEAN"
        results["action"] = "PROCEED"

    # 3. Report generieren
    report = generate_report(results)

    return results, report
```


#### Example



**Code:**
```json
{
  "finding": "context-manager-agent",
  "source": "github.com/some/repo",
  "overall_severity": "FIXABLE",
  "action": "WARN_AND_OFFER_FIX",
  "checks": {
    "tool_mutex": {"severity": "CLEAN", "conflicts": []},
    "naming": {"severity": "FIXABLE", "similar": [...]},
    "pattern_overlap": {"severity": "CLEAN", "overlaps": []},
    "subagent": {"severity": "FIXABLE", "score": 4.0}
  },
  "fixes_available": [
    {"type": "rename", "from": "context-manager", "to": "ext-context-manager"},
    {"type": "add_delegation", "tasks": [...]}
  ]
}
```


#### Example



**Code:**
```bash
@compatibility-checker-agent
{
  "finding": {
    "name": "...",
    "type": "agent",
    "source_repo": "...",
    "content": "...",
    "extracted_tools": [...],
    "extracted_keywords": [...]
  }
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/compatibility-checker-agent.md`</small>
