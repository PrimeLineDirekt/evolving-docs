---
title: Domain Memory Bootup Ritual
type: rule
tags: []
lang: en
confidence: 100
---

# Domain Memory Bootup Ritual


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | ## Konzept Domain Memory macht den Unterschied zwischen: - **Ohne**: "6yo dumb kid" / "Amnesiac with tool belt" - **Mit**: "Disciplined engineer" |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

## Konzept Domain Memory macht den Unterschied zwischen: - **Ohne**: "6yo dumb kid" / "Amnesiac with tool belt" - **Mit**: "Disciplined engineer"


## System Impact

**When It Triggers:**
- Every session start (automatically)
- Project switch
- After `/clear` command
- When resuming named sessions

**Effects on System:**
- Loads domain memory (index.json + active project)
- Activates knowledge graph context router
- Restores session state from handoffs
- Hydrates experience memory with decay filtering
- Ensures agent has full project context before any work

**Context Budget:**
- Session start: ~5K tokens for memory (Domain + Experience + Graph)
- Budget-aware: reduces to essentials at >60% context
- Critical threshold: skips optional loading at >90% context

## Architecture




## Usage




## Configuration



## Best Practices

**Do:**
- Always read memory at session start before any work
- Use "continue" command to resume from latest handoff automatically
- Keep progress entries compact (use abbreviated format)
- Filter experiences by effective_relevance > 30
- Load only primary graph nodes initially
- Sync completed tasks to memory at session end

**Don't:**
- Skip memory bootup even for "quick" tasks
- Load all experiences (use decay-filtered top-3)
- Exceed 5K token budget for memory at session start
- Update memory without completing actual work
- Forget to log failures for future learning
- Mix session-scoped tasks with persistent memory

**Context Optimization:**
- <60% context: full hydrate (all memory types)
- 60-90% context: reduce to top-1 experience, primary nodes only
- >90% context: skip optional graph context, emergency compression

## Related


---

<small>Source: `.claude/rules/domain-memory-bootup.md`</small>
