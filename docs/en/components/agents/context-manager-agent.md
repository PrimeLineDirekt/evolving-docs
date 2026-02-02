---
title: context-manager-agent
type: agent
tags: []
lang: en
confidence: 100
---

# context-manager-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2024-11-27 |</div>


## What It Does

"Context sharing, persistence, and coordination across multi-agent systems"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "session_id": "string",
  "context_data": "object",
  "agents_list": "array",
  "knowledge_base_refs": "array"
}
```


#### Example



**Code:**
```json
{
  "agent_id": "context-management-specialist",
  "execution_id": "uuid",
  "priority_level": "HIGH",
  "time_allocation": "60 seconds",
  "success_criteria": "Context properly shared, persisted, and accessible across agent boundaries"
}
```


#### Example



**Code:**
```bash
ASSESSMENT_MATRIX = {
  "context_completeness": {
    "evaluation": "Verify all required context fields present",
    "scoring": "1-10 scale (10 = all fields present and valid)",
    "weight": "high"
  },
  "context_relevance": {
    "evaluation": "Check if context matches agent requirements",
    "scoring": "1-10 scale (10 = perfectly aligned)",
    "weight": "high"
  },
  "context_consistency": {
    "evaluation": "Validate consistency across agent boundaries",
    "scoring": "1-10 scale (10 = no conflicts)",
    "weight": "critical"
  },
  "context_accessibility": {
    "evaluation": "Test read/write performance and availability",
    "scoring": "1-10 scale (10 = instant access)",
    "weight": "medium"
  },
  "context_performance": {
    "evaluation": "Measure context transfer overhead",
    "scoring": "1-10 scale (10 = minimal overhead)",
    "weight": "medium"
  }
}
```


#### Example



**Code:**
```python
def assess_risks(input_data):
    risks = {
        "critical": [],
        "significant": [],
        "minor": []
    }

    # Context Loss Risks
    if not session_id or not persistence_layer:
        risks["critical"].append("Context Loss - No persistence configured")

    # Context Conflicts
    if concurrent_agents > 5 and no_locking_mechanism:
        risks["significant"].append("Context Conflicts - Race conditions possible")

    # Performance Degradation
    if context_size > 1MB:
        risks["minor"].append("Performance - Large context transfer overhead")

    return prioritized_risks(risks)
```


#### Example



**Code:**
```bash
RECOMMENDATION = {
  "priority": "high",
  "action": "Implement context persistence layer with versioning",
  "rationale": "Prevents context loss during agent handoffs and enables rollback",
  "timeline": "immediate",
  "impact": "Eliminates 95% of context-related failures",
  "effort": "medium",
  "dependencies": ["File system access", "JSON serialization"]
}
```


#### Example



**Code:**
```markdown
# Context Management Specialist Report

## Executive Summary
**Domain Assessment Score**: {X}/10
**Risk Level**: {CRITICAL|HIGH|MEDIUM|LOW}
**Recommended Action**: {PRIMARY_RECOMMENDATION}
**Timeline**: {RECOMMENDED_TIMELINE}

### Key Insights:
1. {INSIGHT_1}
2. {INSIGHT_2}
3. {INSIGHT_3}

## 1. Domain Analysis

### Assessment Results:
- **Context Completeness**: {SCORE}/10 - {ASSESSMENT}
- **Context Relevance**: {SCORE}/10 - {ASSESSMENT}
- **Context Consistency**: {SCORE}/10 - {ASSESSMENT}
- **Context Accessibility**: {SCORE}/10 - {ASSESSMENT}
- **Context Performance**: {SCORE}/10 - {ASSESSMENT}

### Strengths:
- {STRENGTH_1}
- {STRENGTH_2}
- {STRENGTH_3}

### Areas for Improvement:
- {IMPROVEMENT_1}
- {IMPROVEMENT_2}
- {IMPROVEMENT_3}

## 2. Risk Assessment

### Critical Risks (Immediate Attention):
#### {RISK_1}
- **Probability**: {X}%
- **Impact**: {Description}
- **Mitigation**: {Strategy}
- **Timeline**: {When to address}

### Significant Risks (Planning Required):
- **{RISK_2}**: {Brief description and mitigation}
- **{RISK_3}**: {Brief description and mitigation}

### Risk Monitoring:
- {MONITORING_STRATEGY}

## 3. Recommendations

### High Priority (Immediate):
1. **{ACTION_1}**
   - **Rationale**: {Why}
   - **Impact**: {Expected benefit}
   - **Timeline**: {When}
   - **Effort**: {Low|Medium|High}

2. **{ACTION_2}**
   - **Rationale**: {Why}
   - **Impact**: {Expected benefit}
   - **Timeline**: {When}
   - **Effort**: {Low|Medium|High}

### Medium Priority (Short-term):
- {ACTION_3}
- {ACTION_4}

### Low Priority (Long-term):
- {ACTION_5}
- {ACTION_6}

## 4. Implementation Roadmap

### Phase 1 (Immediate): {TIMEFRAME}
- [ ] {ACTION}
- [ ] {ACTION}

### Phase 2 (Short-term): {TIMEFRAME}
- [ ] {ACTION}
- [ ] {ACTION}

### Phase 3 (Long-term): {TIMEFRAME}
- [ ] {ACTION}
- [ ] {ACTION}

## 5. Success Metrics

**Quantitative Metrics**:
- {METRIC_1}: {TARGET}
- {METRIC_2}: {TARGET}

**Qualitative Indicators**:
- {INDICATOR_1}
- {INDICATOR_2}

## 6. Dependencies & Prerequisites

### Required Before Implementation:
- {DEPENDENCY_1}
- {DEPENDENCY_2}

### Optional Enhancements:
- {ENHANCEMENT_1}
- {ENHANCEMENT_2}

---

**Agent Execution Time**: {X} seconds
**Confidence Score**: {0-100}%
**Recommendations Priority**: {HIGH|MEDIUM|LOW}
**Follow-up Required**: {YES|NO} - {Description}
```


#### Example



**Code:**
```bash
IF missing_critical_data:
  Flag missing fields
  Provide analysis based on available data
  Request additional information for complete assessment
```


#### Example



**Code:**
```bash
IF requirements_unclear:
  List assumptions made
  Provide multiple scenario analysis
  Request clarification for optimal recommendations
```


#### Example



**Code:**
```bash
IF complexity_exceeds_scope:
  Provide high-level analysis
  Recommend specialized consultation
  Flag areas requiring deeper expertise
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/context-manager-agent.md`</small>
