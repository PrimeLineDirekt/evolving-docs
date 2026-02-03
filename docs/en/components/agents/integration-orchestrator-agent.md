---
title: integration-orchestrator-agent
type: agent
tags: [orchestration, integration, automation]
lang: en
confidence: 100
---

# integration-orchestrator-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Orchestrator agent that coordinates the fully automatic integration of external findings through 4 specialized sub-agents. |
| **Complexity** | high |
| **Model** | opus |
| **Category** | integration-coordination |
| **Created** | 2026-01-08 |</div>


## What It Does

The Integration Orchestrator Agent coordinates the complete, fully automated integration of external findings (templates, patterns, learnings from other repos) by managing 4 specialized sub-agents in a choreographed workflow.

**Core Principle:** Orchestrated automation - break complex integration into controlled steps.

**Sub-Agents Managed:**
- `dependency-checker-agent` - Checks for conflicts (FIRST, sequential)
- `doc-sync-agent` - Updates documentation (PARALLEL)
- `harmony-checker-agent` - Validates style consistency (PARALLEL)
- `automation-setup-agent` - Sets up routing (LAST, sequential)


## System Impact

- **Enables external knowledge ingestion** - Safely integrates findings from other repos
- **Ensures system consistency** - All checks pass before integration
- **Maintains documentation sync** - README, SYSTEM-MAP, graph updated automatically
- **Powers /analyze-repo command** - Called in Phase 5 of repo analysis
- **Reduces manual integration work** - What took 30 minutes now takes 2 minutes


## Architecture

**Model:** Opus (high complexity orchestration)

**Capabilities:**
- Dependency orchestration
- Parallel execution
- Fix aggregation
- Commit preparation

**4-Phase Workflow:**

```
Phase 1: DEPENDENCY CHECK (Sequential - Must Pass First)
  └─ @dependency-checker-agent
     → Tool-Mutex, Naming, Overlap, Circular
     → Returns: CLEAN | FIXABLE | BLOCKED

Phase 2: PARALLEL CHECKS
  ├─ @doc-sync-agent → README, SYSTEM-MAP, Graph Nodes
  └─ @harmony-checker → Naming, Tags, Schema, Relations

Phase 3: AUTOMATION SETUP (After Parallel Completes)
  └─ @automation-setup-agent
     → Context Router, Detection Index, Graph Edges

Phase 4: AGGREGATION & COMMIT
  └─ Collect all changes, create single commit
     "integrate: {name} from {source_repo}"
```

### Phase 1: Dependency Check (BLOCKING)

**Checks:**
- Tool mutex conflicts (e.g., puppeteer vs claude-in-chrome)
- Naming collisions (command/agent name already exists)
- Keyword overlap (too similar to existing component)
- Circular dependencies

**Decision Logic:**
- `CLEAN` → Continue to Phase 2
- `FIXABLE` → Apply auto-fixes, continue
- `BLOCKED` → Stop immediately, return blocking reason

### Phase 2: Parallel Checks

**Doc-Sync Agent (Haiku):**
- Updates README.md (component counts)
- Updates SYSTEM-MAP.md (component table + changelog)
- Creates knowledge graph node
- Updates related documentation

**Harmony Checker Agent (Sonnet):**
- Validates naming conventions (kebab-case)
- Checks tag consistency (existing taxonomy)
- Validates description format
- Suggests style improvements

### Phase 3: Automation Setup

**Automation-Setup Agent (Haiku):**
- Creates Context Router route (keyword → component mapping)
- Adds Detection Index entry (for commands only)
- Creates knowledge graph edges (tag-based relationships)

### Phase 4: Commit

**Orchestrator:**
- Collects all changed files from sub-agents
- Stages all files with `git add`
- Creates single commit: `integrate: {name} from {source_repo}`
- Returns comprehensive results summary


## Usage

### Input Format

```json
{
  "finding": {
    "name": "chunking-strategy",
    "type": "template",
    "path": ".claude/templates/chunking-strategy.md",
    "source_repo": "crawl4ai",
    "tags": ["llm", "chunking", "rag"],
    "keywords": ["chunk", "text splitting"],
    "description": "Chunking strategies for RAG pipelines",
    "content": "... Full content ..."
  }
}
```

### Output Format (Success)

```json
{
  "status": "INTEGRATED",
  "results": {
    "finding": "chunking-strategy",
    "source": "crawl4ai",
    "phases": {
      "dependency": {"status": "CLEAN", "checks": {...}},
      "doc_sync": {"updated_files": ["README.md", "SYSTEM-MAP.md"], "changes": {...}},
      "harmony": {"harmony_score": 8.5, "suggestions": [], "auto_fixable": true},
      "automation": {"context_router": {...}, "graph_edges": {...}},
      "commit": {"files": [...], "message": "integrate: chunking-strategy from crawl4ai"}
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

### Output Format (Blocked)

```json
{
  "status": "BLOCKED",
  "phase": "dependency",
  "reason": "Tool-Mutex conflict: mcp__puppeteer conflicts with mcp__claude-in-chrome"
}
```


## Configuration

### Performance Characteristics

**Typical Execution Time:**
- Phase 1 (Dependency): 15-20s
- Phase 2 (Parallel): 20-30s (both agents concurrently)
- Phase 3 (Automation): 10-15s
- Phase 4 (Commit): 5s
- **Total: ~60-70 seconds**

**Token Usage:**
- Orchestrator (Opus): ~5K tokens
- Sub-agents combined: ~15K tokens
- **Total: ~20K tokens per integration**

### Error Handling

**Graceful Degradation:**
- Sub-agent fails → Log error, continue with other agents
- File not found → Skip that update, continue
- Git commit fails → Return results without commit
- Timeout → Return partial results


## Best Practices

- **Always run dependency check first** - Prevents integration conflicts
- **Use parallel execution for Phase 2** - Faster than sequential
- **Apply fixable issues automatically** - Don't block on auto-fixable problems
- **Create single commit** - All integration changes in one atomic commit
- **Validate output before returning** - Ensure all phases completed successfully


## Related

- [/analyze-repo](../commands/analyze-repo.md) - Calls this orchestrator in Phase 5
- [dependency-checker-agent](dependency-checker-agent.md) - Conflict detection
- [doc-sync-agent](doc-sync-agent.md) - Documentation updates
- [harmony-checker-agent](harmony-checker-agent.md) - Style consistency
- [automation-setup-agent](automation-setup-agent.md) - Routing setup

---

<small>Source: `.claude/agents/integration-orchestrator-agent.md`</small>
