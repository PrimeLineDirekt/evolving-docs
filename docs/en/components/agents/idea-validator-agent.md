---
title: idea-validator-agent
type: agent
tags: []
lang: en
confidence: 100
---

# idea-validator-agent


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

"Comprehensive idea validation with feasibility, market, and technical assessment"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "idea_data": "object",
  "validation_depth": "string",
  "validation_criteria": "array",
  "context_refs": "array"
}
```


#### Example



**Code:**
```json
{
  "agent_id": "idea-validation-specialist",
  "execution_id": "uuid",
  "priority_level": "HIGH",
  "time_allocation": "60 seconds",
  "success_criteria": "Comprehensive validation with actionable recommendations"
}
```


#### Example



**Code:**
```bash
ASSESSMENT_MATRIX = {
  "feasibility": {
    "evaluation": "Technical and resource feasibility assessment",
    "scoring": "1-10 scale (10 = highly feasible)",
    "weight": "critical"
  },
  "market_potential": {
    "evaluation": "Market size, demand, and opportunity assessment",
    "scoring": "1-10 scale (10 = large proven market)",
    "weight": "critical"
  },
  "technical_viability": {
    "evaluation": "Technical implementation complexity and challenges",
    "scoring": "1-10 scale (10 = straightforward implementation)",
    "weight": "high"
  },
  "resource_requirements": {
    "evaluation": "Time, budget, and skill requirements",
    "scoring": "1-10 scale (10 = minimal resources)",
    "weight": "high"
  },
  "competitive_advantage": {
    "evaluation": "Unique value proposition and differentiation",
    "scoring": "1-10 scale (10 = strong differentiation)",
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

    # Market Risks
    if unproven_market or saturated_market:
        risks["critical"].append("Market Risk - Uncertain demand or high competition")

    # Technical Risks
    if complex_technical_requirements:
        risks["significant"].append("Technical Risk - Implementation complexity")

    # Resource Risks
    if insufficient_resources or skill_gaps:
        risks["significant"].append("Resource Risk - Capability or capacity gaps")

    # Timeline Risks
    if aggressive_timeline:
        risks["minor"].append("Timeline Risk - Compressed development schedule")

    return prioritized_risks(risks)
```


#### Example



**Code:**
```bash
RECOMMENDATION = {
  "priority": "high",
  "action": "Conduct market validation with target user interviews",
  "rationale": "Validates demand assumptions before significant investment",
  "timeline": "immediate",
  "impact": "Reduces market risk by 60%, informs product direction",
  "effort": "low",
  "dependencies": ["Target user access", "Interview framework"]
}
```


#### Example



**Code:**
```markdown
# Idea Validation Specialist Report

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
- **Feasibility**: {SCORE}/10 - {ASSESSMENT}
- **Market Potential**: {SCORE}/10 - {ASSESSMENT}
- **Technical Viability**: {SCORE}/10 - {ASSESSMENT}
- **Resource Requirements**: {SCORE}/10 - {ASSESSMENT}
- **Competitive Advantage**: {SCORE}/10 - {ASSESSMENT}

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

<small>Source: `.claude/agents/idea-validator-agent.md`</small>
