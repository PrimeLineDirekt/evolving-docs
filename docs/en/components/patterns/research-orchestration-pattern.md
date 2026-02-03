---
title: research-orchestration-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# research-orchestration-pattern


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does




## System Impact

**Capabilities Provided:**
- Structured approach to component creation
- Automated validation and best practices
- Standardized output format
- Integration with system architecture

**When to Use:**
- Creating new system components
- Standardizing component structure
- Ensuring consistency across codebase
- Automating repetitive creation tasks



## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Research the semiconductor supply chain crisis and its current status.
Use web_search and web_fetch tools.

Begin by examining:
- Quarterly reports from TSMC, Samsung, Intel (investor relations)
- Industry reports from SEMI, Gartner, IDC

Investigate government responses:
- US CHIPS Act progress at commerce.gov
- EU Chips Act at ec.europa.eu

Prioritize original sources over news aggregators.

Focus on:
- Current bottlenecks
- Projected capacity increases
- Geopolitical factors
- Expert predictions

Output: Dense fact report covering current situation, solutions,
future outlook with specific timelines and quantitative data.
```


#### Example



**Code:**
```bash
ALWAYS parallel for 2+ independent subagents:

[Planning Phase] → Sequential (you do this)
       ↓
[Subagent Creation] → PARALLEL (3 subagents simultaneously)
       ↓
[Results Collection] → Wait for all
       ↓
[Synthesis] → Sequential (you do this)
```




## Configuration



## Best Practices

**Do:**
- Use for multi-expert coordination requiring diverse perspectives
- Apply when problem benefits from iterative refinement
- Combine with proper state management and validation
- Monitor blackboard size to prevent context overflow

**Don't:**
- Use for simple single-agent tasks
- Apply to strictly sequential workflows
- Ignore controller bottleneck risks
- Forget to handle write conflicts in concurrent scenarios




## Related


---

<small>Source: `knowledge/patterns/research-orchestration-pattern.md`</small>
