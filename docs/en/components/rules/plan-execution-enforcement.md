---
title: Plan Execution Enforcement
type: rule
tags: []
lang: en
confidence: 100
---

# Plan Execution Enforcement


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Enforce hint-based delegation during plan execution |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

Plan Execution Enforcement ensures that plans act as coordinators, not executors. Each task in a plan contains hints ([EXPLORE], [DELEGATE], [DELEGATE:agent-name], [DIRECT]) that dictate how it should be executed. The rule enforces automatic delegation based on these hints, with a score-based fallback for plans without hints. It also mandates phase-end review tasks and tracks delegation gaps through the delegation-enforcer.py hook.

**Core Principle:** "Plans coordinate specialists, they don't do specialist work."


## System Impact

**When It Triggers:**
During plan execution (after interview/approval)

**Behavior Enforced:**
- Extract hint from task title using regex
- Follow hint mapping: [EXPLORE]→Explore agent, [DELEGATE]→trait-based, [DELEGATE:X]→specific agent, [DIRECT]→self-execute
- Score-based fallback when no hint (keywords +3 for explore, +2 for multi-file, etc.)
- Mandate review tasks at end of each phase
- Never delegate critical operations (deploy, secrets, destructive)
- Track delegation gaps via hook

**Integration Points:**
- delegation-enforcer.py hook (gap tracking)
- _graph/cache/delegation-config.json (agent mappings)
- Task Tool (execution)
- Plan interview (hint validation)


## Architecture

**Trigger:** Plan execution start

**Dependencies:**
- Plan hints in task titles
- delegation-config.json (mappings)
- delegation-enforcer.py (tracking)

**Execution Flow:**
1. **Extract Hint**: Parse task title for `[TYPE:agent]` pattern
2. **Agent Selection**: Follow hint or calculate score
3. **Model Selection**: Haiku/Sonnet based on complexity
4. **Task Tool**: Execute with structured prompt
5. **Verify**: Check results, track gaps

**Review Enforcement:**
- Early phases: Quick-check (code-reviewer)
- Final phase: Full analysis (all relevant agents parallel)


## Usage

**Hint Mapping:**

| Hint | Agent | Model | Use Case |
|------|-------|-------|----------|
| [EXPLORE] | Explore | haiku | Codebase analysis, search |
| [DELEGATE] | general-purpose + traits | sonnet | Implementation tasks |
| [DELEGATE:code-reviewer] | feature-dev:code-reviewer | sonnet | Code review |
| [DELEGATE:code-architect] | feature-dev:code-architect | sonnet | Architecture design |
| [DIRECT] | Self-execute | - | Simple edits, git operations |

**Score Fallback (no hint):**
```
Keywords "find/search/explore": +3
Multi-file scope (>2 files): +2
"investigate/analyze": +2
Bulk operation: +2

Single-file <100 lines: -1
Git commit/push: -2
Critical keywords: -10

Score ≥3 → Delegate
Score <3 → Direct execute
```

**Review Tasks:**
Each phase must end with review. Final phase gets full parallel analysis.


## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| Hint Regex | `\[(\w+)(?::[\w-]+)?\]` | Extract hint from task title |
| Delegation Threshold | Score ≥3 | Auto-delegate at this score |
| Review Frequency | Per phase | Every phase ends with review |
| Final Phase Review | All agents parallel | Comprehensive analysis |
| Gap Tracking | delegation-gaps.jsonl | Logs non-delegated [DELEGATE] tasks |
| Context Threshold (Handoff) | >85% | Prompt user for handoff or clear |


## Best Practices

**Do:**
- Use explicit hints in all plan tasks
- Follow hint instructions (don't override without reason)
- Add review tasks at phase boundaries
- Use [DIRECT] + user confirmation for critical operations
- Let delegation-enforcer hook track gaps

**Don't:**
- Delegate critical operations (deploy, secrets, destructive)
- Skip phase-end reviews
- Ignore hints and execute directly
- Use [DELEGATE] for trivial tasks
- Execute without verifying hint compliance


## Related


---

<small>Source: `.claude/rules/plan-execution-enforcement.md`</small>
