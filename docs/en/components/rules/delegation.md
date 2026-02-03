---
title: Delegation
type: rule
tags: []
lang: en
confidence: 100
---

# Delegation


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Automatic task delegation to specialized agents based on scoring |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

The Delegation rule automatically determines when tasks should be delegated to specialized sub-agents rather than handled directly. It uses a scoring system to evaluate task characteristics (scope, complexity, type) and selects appropriate agents with optimal model assignments. When delegation score ≥ 3, the task is automatically delegated without asking the user.

Key features:
- Score-based delegation (automatic at score ≥ 3)
- Built-in agents for common patterns (Explore, debugger, Plan)
- Trait-based agent profiles for custom scenarios
- Model selection by complexity (Haiku 1-3, Sonnet 4-6, Opus 7+)
- Structured 7-section delegation prompts
- Delegation-request pattern for sub-agent coordination


## System Impact

**When It Triggers:**
Automatically evaluated for EVERY task (CRITICAL priority)

**Behavior Enforced:**
- Calculate delegation score from task characteristics
- Auto-delegate when score ≥ 3 (no user confirmation)
- Select agent: Built-in → Plugin → Trait-based
- Choose model by complexity threshold
- Format structured prompts (TASK, OUTCOME, TOOLS, MUST DO/NOT, CONTEXT)
- Verify results after delegation (mandatory)

**Integration Points:**
- delegation-enforcer.py hook (enforcement)
- _graph/cache/delegation-config.json (task-type mappings)
- Task Tool (execution)
- knowledge/rules/delegation/trait-system.md (480 trait combinations)


## Architecture

**Trigger:** Every task evaluation (automatic)

**Dependencies:**
- delegation-config.json (task-type → agent mappings)
- trait-system.md (trait combinations)
- delegation-enforcer.py hook (tracking)

**Decision Flow:**
1. **Score Calculation**: Sum positive factors, subtract penalties
2. **Agent Selection**: Built-in > Plugin > Traits
3. **Model Selection**: Complexity-based (Haiku/Sonnet/Opus)
4. **Execution**: Task Tool with structured prompt
5. **Verification**: Check MUST DO/NOT requirements

**Layer 2 Workaround (Delegation-Request Pattern):**
Sub-agents can't spawn tasks, so they return JSON delegation requests that Layer 1 executes.


## Usage

**Score Factors (+):**
- Scope > 2 files: +2
- Bulk operation: +2
- Research/Learn: +2
- Code review: +2
- Exploration/Search: +3
- Independent task: +2

**Score Penalties (-):**
- Critical keywords (production, deploy, password): -10
- User wants to see ("show me", "explain"): -5
- Complexity > 6: -3

**Always Delegate (no score):**
- Exploration/Search → Explore (haiku)
- Codebase questions → Explore (haiku)
- Debugging → debugger (sonnet)
- Planning → Plan (sonnet)

**Never Delegate:**
- Critical operations (deploy, secrets)
- Destructive operations (delete all, drop database)
- User explicitly wants visibility
- Complexity 7+ (too complex for sub-agent)


## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| Delegation Threshold | Score ≥ 3 | Auto-delegate at this score |
| Haiku Complexity | 1-3 | Fast, cheap tasks |
| Sonnet Complexity | 4-6 | Balanced tasks |
| Opus Complexity | 7+ | Don't delegate (handle directly) |
| Prompt Sections | 7 | Required structure (TASK, OUTCOME, TOOLS, MUST DO, MUST NOT, CONTEXT) |
| Verification | Mandatory | Check requirements after delegation |


## Best Practices

**Do:**
- Calculate score for every task automatically
- Delegate silently when score ≥ 3 (no announcement)
- Use built-in agents when available (Explore, debugger, Plan)
- Structure prompts with all 7 sections
- Verify results against MUST DO/NOT requirements
- Use delegation-request pattern for sub-agent coordination

**Don't:**
- Ask user permission when score ≥ 3 (just delegate)
- Delegate critical operations (deploy, secrets)
- Skip verification after delegation
- Use Opus for simple tasks (inefficient)
- Delegate when user wants visibility ("show me")




## Related


---

<small>Source: `.claude/rules/delegation.md`</small>
