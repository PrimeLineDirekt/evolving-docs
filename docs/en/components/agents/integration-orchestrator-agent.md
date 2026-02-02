---
title: integration-orchestrator-agent
type: agent
tags: []
lang: en
confidence: 100
---

# integration-orchestrator-agent


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

"Koordiniert die vollautomatische Integration von Findings mit 4 spezialisierten Sub-Agents"


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
    "keywords": ["chunk", "text splitting"],
    "description": "Chunking-Strategien für RAG Pipelines",
    "content": "... Full content ...",
    "tools_used": [],
    "references": [],
    "frontmatter": {}
  }
}
```


#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────────────────┐
│                    INTEGRATION ORCHESTRATOR                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Phase 1: DEPENDENCY CHECK (Sequential - Must Pass First)       │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  @dependency-checker-agent                               │    │
│  │  → Tool-Mutex, Naming, Overlap, Circular                 │    │
│  │  → Returns: CLEAN | FIXABLE | BLOCKED                    │    │
│  └─────────────────────────────────────────────────────────┘    │
│           │                                                      │
│           ├── BLOCKED ──────► STOP + Return blocking_reason     │
│           │                                                      │
│           ├── FIXABLE ──────► Apply fixes, continue             │
│           │                                                      │
│           └── CLEAN ────────► Continue to Phase 2               │
│                                                                  │
│  Phase 2: PARALLEL CHECKS                                        │
│  ┌──────────────────────┐  ┌──────────────────────┐             │
│  │  @doc-sync-agent     │  │  @harmony-checker    │             │
│  │  → README, SYSTEM-MAP│  │  → Naming, Tags      │             │
│  │  → Graph Nodes       │  │  → Schema, Relations │             │
│  └──────────────────────┘  └──────────────────────┘             │
│           │                         │                            │
│           └─────────┬───────────────┘                            │
│                     │                                            │
│                     ▼                                            │
│  Phase 3: AUTOMATION SETUP (After Parallel Completes)           │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  @automation-setup-agent                                 │    │
│  │  → Context Router, Detection Index, Graph Edges          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                     │                                            │
│                     ▼                                            │
│  Phase 4: AGGREGATION & COMMIT                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │  Collect all changes, create single commit               │    │
│  │  "integrate: {name} from {source_repo}"                  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```python
def orchestrate_integration(finding):
    results = {
        "finding": finding["name"],
        "source": finding["source_repo"],
        "phases": {}
    }

    # ═══════════════════════════════════════════════════════════
    # PHASE 1: Dependency Check (Sequential - MUST pass first)
    # ═══════════════════════════════════════════════════════════

    dependency_result = invoke_agent(
        "@dependency-checker-agent",
        {"finding": finding}
    )

    results["phases"]["dependency"] = dependency_result

    if dependency_result["status"] == "BLOCKED":
        return {
            "status": "BLOCKED",
            "phase": "dependency",
            "reason": dependency_result["blocking_reason"],
            "results": results
        }

    # Apply fixes if FIXABLE
    applied_fixes = []
    if dependency_result["status"] == "FIXABLE":
        for fix in dependency_result["fixes_available"]:
            apply_result = apply_fix(fix, finding)
            applied_fixes.append(apply_result)
            # Update finding with fixes
            finding = apply_result["updated_finding"]

    results["phases"]["dependency"]["applied_fixes"] = applied_fixes

    # ═══════════════════════════════════════════════════════════
    # PHASE 2: Parallel Checks (Doc-Sync + Harmony)
    # ═══════════════════════════════════════════════════════════

    # Run in parallel using Task tool
    doc_sync_result, harmony_result = parallel_invoke([
        ("@doc-sync-agent", {"finding": finding}),
        ("@harmony-checker-agent", {"finding": finding})
    ])

    results["phases"]["doc_sync"] = doc_sync_result
    results["phases"]["harmony"] = harmony_result

    # Apply harmony fixes if auto_fixable
    if harmony_result.get("auto_fixable"):
        for suggestion in harmony_result.get("suggestions", []):
            if suggestion.get("auto_fix"):
                apply_harmony_fix(suggestion, finding)
                applied_fixes.append(suggestion)

    # ═══════════════════════════════════════════════════════════
    # PHASE 3: Automation Setup (After parallel completes)
    # ═══════════════════════════════════════════════════════════

    automation_result = invoke_agent(
        "@automation-setup-agent",
        {"finding": finding}
    )

    results["phases"]["automation"] = automation_result

    # ═══════════════════════════════════════════════════════════
    # PHASE 4: Aggregation & Commit
    # ═══════════════════════════════════════════════════════════

    all_changed_files = collect_changed_files(results)

    commit_result = create_commit(
        files=all_changed_files,
        message=f"integrate: {finding['name']} from {finding['source_repo']}"
    )

    results["phases"]["commit"] = commit_result

    return {
        "status": "INTEGRATED",
        "results": results,
        "summary": generate_summary(results)
    }
```


#### Example



**Code:**
```python
dependency_result = Task(
    subagent_type="general-purpose",
    model="sonnet",
    prompt="""
    @dependency-checker-agent
    {
      "finding": ${JSON.stringify(finding)}
    }

    Return JSON with: status, checks, fixes_available, blocking_reason
    """
)
```


#### Example



**Code:**
```python
def apply_fix(fix, finding):
    if fix["type"] == "rename":
        finding["name"] = fix["to"]
        # Also rename file if exists
        if finding.get("path"):
            old_path = finding["path"]
            new_path = old_path.replace(fix["from"], fix["to"])
            Bash(f"mv {old_path} {new_path}")
            finding["path"] = new_path

    elif fix["type"] == "keyword_change":
        finding["keywords"] = fix["keep"]

    elif fix["type"] == "tool_replacement":
        # Complex: requires manual intervention usually
        pass

    return {"fix": fix, "updated_finding": finding}
```


#### Example



**Code:**
```python
# Use Task tool with multiple calls in single message
doc_sync_task = Task(
    subagent_type="general-purpose",
    model="haiku",
    prompt="@doc-sync-agent {...}",
    run_in_background=True
)

harmony_task = Task(
    subagent_type="general-purpose",
    model="sonnet",
    prompt="@harmony-checker-agent {...}",
    run_in_background=True
)

# Wait for both
doc_sync_result = TaskOutput(doc_sync_task.id)
harmony_result = TaskOutput(harmony_task.id)
```


#### Example



**Code:**
```python
def apply_harmony_fix(suggestion, finding):
    if suggestion["type"] == "naming":
        finding["name"] = suggestion["suggested"]

    elif suggestion["type"] == "tag":
        old_tags = finding.get("tags", [])
        new_tags = [
            suggestion["suggested"] if t == suggestion["current"] else t
            for t in old_tags
        ]
        finding["tags"] = new_tags

    elif suggestion["type"] == "description":
        finding["description"] = suggestion["suggested"]
```


#### Example



**Code:**
```python
automation_result = Task(
    subagent_type="general-purpose",
    model="haiku",
    prompt="""
    @automation-setup-agent
    {
      "finding": ${JSON.stringify(finding)}
    }

    Return JSON with: context_router, detection_index, graph_edges
    """
)
```


#### Example



**Code:**
```python
def collect_changed_files(results):
    files = set()

    # From doc-sync
    if results["phases"].get("doc_sync"):
        files.update(results["phases"]["doc_sync"].get("updated_files", []))

    # From automation
    if results["phases"].get("automation"):
        auto = results["phases"]["automation"]["results"]
        if auto.get("context_router"):
            files.add("_graph/cache/context-router.json")
        if auto.get("detection_index") and not auto["detection_index"].get("skipped"):
            files.add(".claude/detection-index.json")
        if auto.get("graph_edges"):
            files.add("_graph/edges.json")

    # The finding file itself
    files.add(results["finding"]["path"])

    return list(files)
```


#### Example



**Code:**
```python
def create_commit(files, message):
    # Stage files
    for f in files:
        Bash(f"git add {f}")

    # Commit
    Bash(f'''git commit -m "$(cat <<'EOF'
{message}

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)"''')

    return {"files": files, "message": message}
```


#### Example



**Code:**
```json
{
  "status": "INTEGRATED",
  "results": {
    "finding": "chunking-strategy",
    "source": "crawl4ai",
    "phases": {
      "dependency": {
        "status": "CLEAN",
        "checks": {...}
      },
      "doc_sync": {
        "updated_files": ["README.md", "SYSTEM-MAP.md", "_graph/knowledge-nodes.json"],
        "changes": {...}
      },
      "harmony": {
        "harmony_score": 8.5,
        "suggestions": [...],
        "auto_fixable": true
      },
      "automation": {
        "context_router": {"action": "extended", "route": "llm-processing"},
        "graph_edges": {"edges_created": 2}
      },
      "commit": {
        "files": [...],
        "message": "integrate: chunking-strategy from crawl4ai"
      }
    }
  },
  "summary": {
    "docs_updated": 3,
    "edges_created": 2,
    "fixes_applied": 0,
    "harmony_score": 8.5
  }
}
```


#### Example



**Code:**
```json
{
  "status": "BLOCKED",
  "phase": "dependency",
  "reason": "Tool-Mutex conflict: mcp__puppeteer conflicts with mcp__claude-in-chrome",
  "results": {
    "phases": {
      "dependency": {
        "status": "BLOCKED",
        "checks": {...},
        "blocking_reason": "..."
      }
    }
  }
}
```


#### Example



**Code:**
```python
def safe_invoke(agent, input):
    try:
        return invoke_agent(agent, input)
    except Exception as e:
        return {
            "status": "ERROR",
            "error": str(e),
            "agent": agent
        }
```


#### Example



**Code:**
```bash
@integration-orchestrator-agent
{
  "finding": {
    "name": "chunking-strategy",
    "type": "template",
    "path": ".claude/templates/chunking-strategy.md",
    "source_repo": "crawl4ai",
    "tags": ["llm", "chunking", "rag"],
    "keywords": ["chunk", "text splitting"],
    "description": "Chunking-Strategien für RAG Pipelines",
    "content": "...",
    "tools_used": [],
    "references": [],
    "frontmatter": {}
  }
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/integration-orchestrator-agent.md`</small>
