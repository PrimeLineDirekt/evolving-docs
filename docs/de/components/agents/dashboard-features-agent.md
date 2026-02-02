---
title: dashboard-features-agent
type: agent
tags: []
lang: en
confidence: 100
---

# dashboard-features-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents |</div>


## What It Does

"Dashboard feature generation and prioritization"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "current_features": "array - List of existing dashboard features",
  "user_pain_points": "string - User feedback, issues, or requests",
  "technical_constraints": "string - Known limitations or requirements",
  "priority_focus": "string - Area to focus on (UX, Performance, Features, etc.)"
}
```


#### Example



**Code:**
```json
{
  "agent_id": "dashboard-features-specialist",
  "execution_id": "uuid",
  "priority_level": "MEDIUM",
  "time_allocation": "60 seconds",
  "success_criteria": "Generate 3-5 actionable feature ideas with clear prioritization"
}
```


#### Example



**Code:**
```bash
ASSESSMENT_MATRIX = {
  "user_value": {
    "evaluation": "How much does this feature benefit users?",
    "scoring": "1-10 scale",
    "weight": "40%"
  },
  "technical_complexity": {
    "evaluation": "How difficult is implementation?",
    "scoring": "1-10 scale (10=easy)",
    "weight": "25%"
  },
  "strategic_alignment": {
    "evaluation": "How well does it fit system goals?",
    "scoring": "1-10 scale",
    "weight": "20%"
  },
  "uniqueness": {
    "evaluation": "How innovative/differentiated?",
    "scoring": "1-10 scale",
    "weight": "15%"
  }
}
```


#### Example



**Code:**
```python
def assess_feature_risks(feature_idea):
    risks = {
        "critical": [],
        "significant": [],
        "minor": []
    }

    # Check for breaking changes
    if affects_existing_functionality(feature_idea):
        risks["significant"].append("May affect existing workflows")

    # Check performance impact
    if high_computation_required(feature_idea):
        risks["significant"].append("Performance considerations needed")

    # Check complexity
    if requires_new_dependencies(feature_idea):
        risks["minor"].append("New dependencies required")

    return prioritized_risks(risks)
```


#### Example



**Code:**
```bash
FEATURE_IDEA = {
  "name": "Feature name",
  "description": "What it does",
  "user_benefit": "Why users want this",
  "priority": "high|medium|low",
  "effort": "small|medium|large",
  "dependencies": ["Prerequisites"],
  "success_metrics": ["How to measure success"]
}
```


#### Example



**Code:**
```markdown
# Dashboard Feature Ideas Report

## Executive Summary
**Ideas Generated**: X
**Top Priority Feature**: [FEATURE_NAME]
**Estimated Total Effort**: [TIMEFRAME]
**Focus Area**: [PRIORITY_FOCUS]

### Quick Wins (High Impact, Low Effort):
1. [FEATURE_1]
2. [FEATURE_2]

## Feature Ideas

### 1. [FEATURE_NAME] (Priority: HIGH)

**Description**: [What it does]

**User Benefit**: [Why users want this]

**Implementation**:
- Effort: [Small|Medium|Large]
- Components: [What needs to be built]
- Dependencies: [Prerequisites]

**Success Metrics**:
- [Metric 1]
- [Metric 2]

**Risks**:
- [Risk and mitigation]

---

### 2. [FEATURE_NAME] (Priority: MEDIUM)
[Same structure...]

## Implementation Roadmap

### Phase 1 (Quick Wins):
- [ ] [Feature]
- [ ] [Feature]

### Phase 2 (Core Features):
- [ ] [Feature]

### Phase 3 (Nice-to-Haves):
- [ ] [Feature]

## Technical Considerations

- [Architecture consideration]
- [Performance consideration]
- [UX consideration]

---

**Confidence Score**: [0-100]%
**Follow-up Required**: [YES|NO] - [Description]
```


#### Example



**Code:**
```bash
IF missing_critical_data:
  Review existing dashboard codebase for context
  Provide analysis based on available data
  Request user feedback for targeted ideation
```


#### Example



**Code:**
```bash
IF requirements_unclear:
  List assumptions made
  Provide multiple feature directions
  Request clarification on priority focus
```


#### Example



**Code:**
```bash
IF complexity_exceeds_scope:
  Break down into smaller features
  Recommend phased implementation
  Flag areas requiring architectural decisions
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/dashboard-features-agent.md`</small>
