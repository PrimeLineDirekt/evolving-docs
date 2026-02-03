---
title: Post-Todo Review
type: rule
tags: []
lang: en
confidence: 100
---

# Post-Todo Review


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Automatic code review after todo completion using specialized agents |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

After completing a todo list that involved code changes, this rule automatically triggers a review by specialized agents. It analyzes what was changed (types, structures, error handling, tests, comments) and selects appropriate review agents to run in parallel. The rule includes context awareness (handoff to next session if >85%) and outputs a structured findings report with critical issues, warnings, and suggestions.


## System Impact

**When It Triggers:**
After todo completion when: (1) ≥3 items, (2) all completed, (3) code files changed, (4) not just docs/config

**Behavior Enforced:**
- Detect code changes (not just docs/config)
- Analyze change types (types, structures, error handling, tests, comments)
- Select agents: base (code-reviewer) + specialized based on changes
- Run agents in parallel using Task Tool
- Synthesize findings (critical/warnings/suggestions)
- Create handoff entry if context >85%

**Integration Points:**
- TodoWrite/TodoUpdate (completion detection)
- feature-dev plugin agents
- pr-review-toolkit plugin agents  
- delegation-enforcer.py hook
- Handoff system (context >85%)


## Architecture

**Trigger:** Todo list completion + code changes

**Dependencies:**
- feature-dev:code-reviewer (base, always)
- pr-review-toolkit agents (specialized)
- Task Tool (parallel execution)
- Context monitoring

**Agent Selection Matrix:**

| Change Type | Agent | Priority |
|-------------|-------|----------|
| Code changes | feature-dev:code-reviewer | ALWAYS |
| New types/interfaces | type-design-analyzer | HIGH |
| New structures | code-architect | MEDIUM |
| Error handling | silent-failure-hunter | MEDIUM |
| Tests | pr-test-analyzer | MEDIUM |
| Comments/docs | comment-analyzer | LOW |


## Usage

**Automatic Trigger:**
```
Todo list: All items completed ✅
  ↓
Code files changed? (.ts, .py, .js, etc.)
  ↓ YES
Analyze changes:
  - Types? → + type-design-analyzer
  - Structures? → + code-architect
  - Error handling? → + silent-failure-hunter
  - Tests? → + pr-test-analyzer
  - Comments? → + comment-analyzer
  ↓
Run agents in PARALLEL
  ↓
Present findings:
  Critical (0)
  Warnings (2)
  Suggestions (1)
```

**Context Awareness:**
- <60%: All relevant agents
- 60-75%: Max 3 agents
- 75-85%: Only code-reviewer
- >85%: HANDOFF with pending review note


## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| Min Todos | 3 | Minimum items to trigger review |
| Base Agent | feature-dev:code-reviewer | Always included |
| Context Threshold (Limit Agents) | 60% | Start reducing agents |
| Context Threshold (Handoff) | 85% | Defer to next session |
| Parallel Execution | Yes | All agents run simultaneously |
| Confidence Filter | >70% | Only report high-confidence findings |


## Best Practices

**Do:**
- Always run base code-reviewer
- Add specialized agents based on actual changes
- Run agents in parallel (one Task Tool message)
- Filter findings by confidence >70%
- Create handoff entry if context >85%
- Skip review for docs-only or config-only changes

**Don't:**
- Review when no code changed
- Run review at >85% context (handoff instead)
- Skip base code-reviewer
- Report low-confidence findings
- Review trivial changes (typos, formatting)


## Related


---

<small>Source: `.claude/rules/post-todo-review.md`</small>
