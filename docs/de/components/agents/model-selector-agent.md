---
title: model-selector-agent
type: agent
tags: []
lang: en
confidence: 100
---

# model-selector-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Metacognitive Self-Assessment für optimale Model-Auswahl. Analysiert Tasks vor Ausführung und empfiehlt das passende Model (Haiku/Sonnet/Opus). |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents |</div>


## What It Does

Metacognitive Self-Assessment für optimale Model-Auswahl


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
"Weiß ich, was ich nicht weiß?"

Task → Self-Assessment → Model Recommendation → Confidence Check
```


#### Example



**Code:**
```yaml
haiku:
  speed: "fastest"
  cost: "lowest"
  reasoning: "basic"
  best_for:
    - Simple lookups
    - Formatting tasks
    - Classification
    - Quick answers
    - List generation
    - Status checks
  avoid_for:
    - Complex analysis
    - Multi-step reasoning
    - Research tasks
    - Creative strategy

sonnet:
  speed: "balanced"
  cost: "moderate"
  reasoning: "strong"
  best_for:
    - Code generation
    - Analysis tasks
    - Summarization
    - Document processing
    - General assistance
    - Moderate complexity
  avoid_for:
    - Simple tasks (use haiku)
    - Research-grade analysis (use opus)

opus:
  speed: "slowest"
  cost: "highest"
  reasoning: "maximum"
  best_for:
    - Complex reasoning
    - Multi-step planning
    - Research & strategy
    - Creative ideation
    - Risk assessment
    - Architecture decisions
  avoid_for:
    - Simple tasks (overkill)
    - Time-sensitive quick answers
```


#### Example



**Code:**
```json
{
  "task_description": "string",
  "context": {
    "domain": "string",
    "complexity_hints": [],
    "time_sensitivity": "low|medium|high",
    "quality_requirements": "draft|standard|production"
  }
}
```


#### Example



**Code:**
```xml
<self_assessment>
  <task_analysis>
    <complexity_indicators>
      - Multi-step required: [yes/no]
      - Domain expertise needed: [none/some/deep]
      - Reasoning depth: [shallow/moderate/deep]
      - Output complexity: [simple/structured/comprehensive]
      - Ambiguity level: [clear/moderate/high]
    </complexity_indicators>

    <capability_requirements>
      - Code generation: [yes/no]
      - Research synthesis: [yes/no]
      - Creative ideation: [yes/no]
      - Risk assessment: [yes/no]
      - Multi-perspective: [yes/no]
    </capability_requirements>
  </task_analysis>

  <complexity_score>
    <!-- 1-10 scale -->
    <!-- 1-3: Haiku territory -->
    <!-- 4-6: Sonnet territory -->
    <!-- 7-10: Opus territory -->
  </complexity_score>

  <confidence_in_assessment>
    <!-- How sure am I about this assessment? -->
    <!-- HIGH: Clear task, obvious model choice -->
    <!-- MEDIUM: Some ambiguity, but reasonable guess -->
    <!-- LOW: Unclear task, might need clarification -->
  </confidence_in_assessment>
</self_assessment>
```


#### Example



**Code:**
```json
{
  "recommended_model": "haiku|sonnet|opus",
  "complexity_score": 1-10,
  "confidence": "high|medium|low",
  "reasoning": "Why this model",
  "alternative": {
    "model": "alternative if confidence is medium",
    "when": "condition for alternative"
  },
  "warnings": ["potential issues"]
}
```


#### Example



**Code:**
```yaml
force_opus:
  - "strategy" in task
  - "architecture" in task
  - "research" in task AND depth == "deep"
  - quality_requirements == "production"
  - multi_agent_coordination == true

force_haiku:
  - time_sensitivity == "high"
  - task_type in ["list", "format", "lookup", "status"]
  - quality_requirements == "draft"

force_sonnet:
  - code_generation == true AND complexity < 7
  - analysis_required == true AND complexity < 7
```


#### Example



**Code:**
```python
# Before executing a command
assessment = model_selector.assess(task)

if assessment.confidence == "low":
    # Ask user for clarification
    return clarify_task(task)
else:
    # Execute with recommended model
    execute_with_model(task, assessment.recommended_model)
```


#### Example



**Code:**
```markdown
User: "Help me with SEO optimization"

Model Selector:
- Task: SEO optimization
- Indicators: Domain expertise (moderate), Analysis (yes)
- Complexity Score: 5/10
- Recommended: Sonnet
- Confidence: Medium (task could be simple tips OR deep strategy)
- Question: "Möchtest du schnelle SEO-Tipps (Haiku) oder eine umfassende Strategie (Opus)?"
```


#### Example



**Code:**
```xml
<agent_self_check>
  <question>Can I handle this task well?</question>
  <assessment>
    <my_capabilities>[list]</my_capabilities>
    <task_requirements>[list]</task_requirements>
    <gap_analysis>[missing capabilities]</gap_analysis>
  </assessment>
  <decision>
    IF gaps.length == 0 → Execute
    ELIF gaps are minor → Execute with caveats
    ELSE → Escalate to better model or human
  </decision>
</agent_self_check>
```


#### Example



**Code:**
```yaml
---
description: My command
model: auto  # Uses Model Selector
auto_model_hints:
  - complexity_weight: 0.7
  - quality_requirement: standard
---
```


#### Example



**Code:**
```yaml
---
description: Always use Opus for this
model: opus
skip_model_selection: true
---
```


#### Example



**Code:**
```json
{
  "prediction": {"model": "haiku", "complexity": 3},
  "actual_performance": "adequate|insufficient|overkill",
  "adjustment": "none|raise_threshold|lower_threshold"
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/model-selector-agent.md`</small>
