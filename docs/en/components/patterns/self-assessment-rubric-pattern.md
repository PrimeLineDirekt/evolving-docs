---
title: self-assessment-rubric-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# self-assessment-rubric-pattern


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
Score berechnen (gewichteter Durchschnitt)
           │
           ▼
    ┌──────────────┐
    │ Score >= 4.0 │───Yes──▶ ACTION: NONE (nur loggen)
    └──────────────┘
           │ No
           ▼
    ┌──────────────┐
    │ Score >= 3.0 │───Yes──▶ ACTION: SUGGESTION (Human Review)
    └──────────────┘
           │ No
           ▼
    ┌──────────────┐
    │ Score >= 2.0 │───Yes──▶ ACTION: AUTO-UPDATE (automatisch verbessern)
    └──────────────┘
           │ No
           ▼
    ACTION: ESCALATE (Sofortige Aufmerksamkeit)
```


#### Example



**Code:**
```javascript
const OVERRIDE_CONDITIONS = {
  // Einzelnes Kriterium sehr niedrig
  anyCriterionBelow2: (scores) =>
    Object.values(scores).some(s => s < 2),

  // Konsistenter Abwärtstrend
  decliningTrend: (current, lastThree) =>
    lastThree.every(s => s > current),

  // Hohe Varianz in einem Kriterium
  inconsistentPerformance: (recent) =>
    standardDeviation(recent) > 1.0,

  // Wiederholte spezifische Schwäche
  repeatedWeakness: (reflections) =>
    reflections.filter(r =>
      r.weaknesses.includes('shallow responses')).length >= 3
};
```


#### Example



**Code:**
```json
{
  "overall_score": 4.2,
  "action_taken": "none",
  "scores": {
    "completeness": 4,
    "depth": 4,
    "tone": 5,
    "scope": 4,
    "missed_opportunities": 4
  },
  "strengths": [
    "Clear recommendation with reasoning",
    "Actionable steps provided"
  ],
  "weaknesses": [
    "Could mention middleware setup",
    "Security considerations not addressed"
  ],
  "patterns_noticed": [],
  "suggested_improvements": null
}
```


#### Example



**Code:**
```bash
Agent Output → Self-Assessment → Score < 4? → Refinement Loop
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

<small>Source: `knowledge/patterns/self-assessment-rubric-pattern.md`</small>
