---
title: Metacognitive Orchestrator
type: rule
tags: []
lang: en
confidence: 100
---

# Metacognitive Orchestrator


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Automatic pattern recognition and activation based on task type |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

The Metacognitive Orchestrator automatically recognizes task types from user input and activates appropriate thinking patterns. It uses a 3-layer progressive disclosure system to minimize token usage: JSON configs (500 tokens) for detection, pattern summaries (300 tokens) when matched, and full markdown (3000 tokens) only when needed. It also classifies request ambiguity and determines when to ask clarifying questions versus proceeding with reasonable defaults.


## System Impact

**When It Triggers:**
After every user request (after memory bootup, before task execution)

**Behavior Enforced:**
- Classify request type (trivial, explicit, exploratory, open-ended, domain work, ambiguous)
- Extract keywords and match against task-types.json
- Calculate confidence score (keywords +10, anti-keywords -15, boost)
- Check pattern mutex conflicts
- Load patterns based on confidence (≥80% auto, 50-79% ask, <50% skip)
- Respect context budget (>70% summary only, >90% no pattern)
- Challenge user when design seems flawed

**Integration Points:**
- _graph/cache/task-types.json (keyword → task type mapping)
- _graph/cache/pattern-mutex.json (conflict detection)
- _graph/cache/orchestration-config.json (thresholds)
- .claude/summaries/patterns/ (layer 2 summaries)
- knowledge/patterns/ (layer 3 full docs)


## Architecture

**Trigger:** Every user request (after memory bootup)

**Dependencies:**
- task-types.json (detection)
- pattern-mutex.json (conflicts)
- orchestration-config.json (thresholds)
- pattern summaries (quick reference)

**Detection Flow:**
1. **User Override Check**: Explicit pattern request?
2. **Keyword Extraction**: Parse user input
3. **Task-Type Matching**: Calculate confidence
4. **Mutex Check**: Pattern conflicts?
5. **Context Budget**: >70%? Adjust loading
6. **Confidence Decision**: Auto/Ask/Skip
7. **Delegation Check**: Should task be delegated?

**3-Layer Progressive Disclosure:**
- **Layer 1 (500T)**: JSON configs always loaded
- **Layer 2 (300T)**: Summaries loaded on match
- **Layer 3 (3000T)**: Full markdown only when needed


## Usage

**Request Type Classification:**

| Type | Signal | Action |
|------|--------|--------|
| Trivial | Single file, known location | Direct tools only |
| Explicit | Specific file/line, clear command | Execute directly |
| Exploratory | "How does X work?", "Find Y" | Explore agents parallel |
| Open-ended | "Improve", "Refactor", "Add feature" | Assess codebase first |
| Domain Work | Issue mentioned, "look into X" | Full cycle: investigate → implement → verify |
| Ambiguous | Unclear scope | Ask ONE clarifying question |

**Ambiguity Check:**
- Single interpretation → Proceed
- Multiple similar effort → Proceed with default, note assumption
- Multiple 2x+ effort difference → MUST ask
- Missing critical info → MUST ask
- Flawed design → MUST raise concern

**Confidence-Based Loading:**
- **≥80%**: Auto-load summary, apply pattern silently
- **50-79%**: Ask "Should I use [pattern]?"
- **<50%**: Skip pattern, respond normally

**User Overrides:**
- "use reflection" → Force reflection (100% confidence)
- "with react pattern" → Force react (100% confidence)
- "no pattern" → Skip detection entirely


## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| High Confidence | ≥80% | Auto-load pattern |
| Medium Confidence | 50-79% | Ask user first |
| Low Confidence | <50% | Skip pattern |
| Keyword Match | +10 | Confidence boost per keyword |
| Anti-Keyword | -15 | Confidence penalty |
| Context Threshold (Summary) | 70% | Only load summaries above this |
| Context Threshold (No Load) | 90% | Skip patterns above this |

**Pattern Mutex Groups:**
- A_iteration: reflection, react (mutually exclusive)
- B_multi_agent: blackboard, ensemble (mutually exclusive)
- C_decision: tree-of-thoughts (combinable with A/B)


## Best Practices

**Do:**
- Classify request type before responding
- Use progressive disclosure (JSON → summary → full doc)
- Respect context budget thresholds
- Ask ONE clarifying question for ambiguous requests
- Challenge user when design seems flawed
- Load patterns based on confidence automatically

**Don't:**
- Load full markdown unless needed (token waste)
- Activate conflicting patterns from same mutex group
- Load patterns when context >90%
- Skip ambiguity check (2x+ effort difference requires asking)
- Over-explain pattern activation (apply silently at high confidence)


## Related


---

<small>Source: `.claude/rules/metacognitive-orchestrator.md`</small>
