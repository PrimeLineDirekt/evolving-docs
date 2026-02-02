---
title: idea-connector-agent
type: agent
tags: []
lang: en
confidence: 100
---

# idea-connector-agent


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

"Cross-idea synergy discovery and connection pattern identification"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "idea_data": "object",
  "all_ideas": "array",
  "connection_types": "array",
  "context_refs": "array"
}
```


#### Example



**Code:**
```json
{
  "agent_id": "idea-connection-specialist",
  "execution_id": "uuid",
  "priority_level": "MEDIUM",
  "time_allocation": "60 seconds",
  "success_criteria": "High-value connections with actionable synergy opportunities"
}
```


#### Example



**Code:**
```bash
ASSESSMENT_MATRIX = {
  "synergy_potential": {
    "evaluation": "Value created through idea combinations",
    "scoring": "1-10 scale (10 = high synergy value)",
    "weight": "critical"
  },
  "connection_strength": {
    "evaluation": "Strength and relevance of discovered connections",
    "scoring": "1-10 scale (10 = strong natural connections)",
    "weight": "critical"
  },
  "resource_optimization": {
    "evaluation": "Efficiency gains through resource sharing",
    "scoring": "1-10 scale (10 = significant optimization)",
    "weight": "high"
  },
  "integration_feasibility": {
    "evaluation": "Ease of integrating connected ideas",
    "scoring": "1-10 scale (10 = straightforward integration)",
    "weight": "high"
  },
  "collaboration_value": {
    "evaluation": "Value created through collaboration patterns",
    "scoring": "1-10 scale (10 = high collaboration value)",
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

    # False Synergy Risks
    if weak_connection_signals:
        risks["significant"].append("False Synergy - Connections may be superficial")

    # Integration Complexity
    if complex_integration_requirements:
        risks["significant"].append("Complexity - High integration effort required")

    # Resource Conflicts
    if competing_resource_needs:
        risks["minor"].append("Resources - Potential conflicts in shared resources")

    return prioritized_risks(risks)
```


#### Example



**Code:**
```bash
RECOMMENDATION = {
  "priority": "high",
  "action": "Integrate user authentication across ideas A and B",
  "rationale": "Shared authentication reduces development time by 40% and improves UX consistency",
  "timeline": "immediate",
  "impact": "Saves 20 hours development, enables cross-product features",
  "effort": "low",
  "dependencies": ["Shared auth service", "Data schema alignment"]
}
```


#### Example



**Code:**
```markdown
# Idea Connection Specialist Report

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
- **Synergy Potential**: {SCORE}/10 - {ASSESSMENT}
- **Connection Strength**: {SCORE}/10 - {ASSESSMENT}
- **Resource Optimization**: {SCORE}/10 - {ASSESSMENT}
- **Integration Feasibility**: {SCORE}/10 - {ASSESSMENT}
- **Collaboration Value**: {SCORE}/10 - {ASSESSMENT}

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

<small>Source: `.claude/agents/idea-connector-agent.md`</small>
