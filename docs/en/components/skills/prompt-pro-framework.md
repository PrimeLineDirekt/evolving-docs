---
title: Prompt Pro Framework
type: skill
tags: [framework, prompt-engineering, optimization]
lang: en
confidence: 95
---

# Prompt Pro Framework

![Prompt Pro Framework Skill](../../shared/assets/infographics/skills/prompt-pro-framework.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Transform any input into optimal Claude-optimized prompts |
| **Complexity** | High |
| **Model** | sonnet |
| **Category** | frameworks |
</div>

## What It Does

The Prompt Pro Framework is a highly adaptive prompt engineering system that transforms any input into optimal, Claude-optimized prompts using a 5-level technique hierarchy. It morphs into the world's leading expert in the exact domain for each request, ensuring prompts are clear, complete, and performance-optimized.

## Core Principles

### 1. Adaptive Expert Transformation
- Transform into world-leading expert of the EXACT domain
- For interdisciplinary topics: Multiple expert perspectives
- Never solve the problem - ONLY create the perfect prompt

### 2. Clarity-First Architecture
- "Colleague Test": Non-expert colleague could follow instructions
- Context is King: Everything relevant must be explicit
- XML tags as standard structure

### 3. Performance-Driven Design
- Start simple, escalate smart
- Make latency vs. quality trade-offs transparent
- Define measurable success metrics

## The 5-Level Technique Hierarchy

### LEVEL 1 - FOUNDATION (70% of cases)
```xml
<foundation_techniques>
  <clear_direct>
    - Explicit instructions
    - Complete context (Who, What, Why, How, When)
    - Defined success criteria
  </clear_direct>

  <xml_structure>
    - <context> for background information
    - <task> for specific assignment
    - <constraints> for limitations
    - <output_format> for desired format
  </xml_structure>
</foundation_techniques>
```

### LEVEL 2 - ENHANCED
```xml
<enhanced_techniques>
  <multishot_examples>2-3 high-quality Input → Output pairs</multishot_examples>
  <structured_cot><thinking> → <analysis> → <answer></structured_cot>
  <role_assignment>Specific expertise, perspective, standards</role_assignment>
</enhanced_techniques>
```

### LEVEL 3 - COMPLEX
```xml
<complex_techniques>
  <prompt_chaining>Subtasks → Output-Input Pipeline → Parallel where possible</prompt_chaining>
  <verification_loops>Generate → Review → Refine → Validate</verification_loops>
  <conditional_branching>IF/THEN, Fallbacks, Error handling</conditional_branching>
  <reflection_loop>Generator → Critic → Refiner → Repeat until quality threshold</reflection_loop>
</complex_techniques>
```

### LEVEL 4 - ADVANCED
```xml
<advanced_techniques>
  <extended_thinking>1k-32k tokens depending on complexity</extended_thinking>
  <least_to_most>Simplest subproblems first → Cumulative</least_to_most>
  <tree_of_thought>Multiple solution paths parallel → Best path</tree_of_thought>
  <knowledge_synthesis>Generated knowledge → Application</knowledge_synthesis>
</advanced_techniques>
```

### LEVEL 5 - SPECIALIZED
```xml
<specialized_techniques>
  <prefilling>Strict formatting, Consistency, Style matching</prefilling>
  <prompt_caching>Repetitive tasks, 1-hour cache</prompt_caching>
  <maieutic_prompting>Socratic questioning</maieutic_prompting>
  <contrastive_consistency>Multiple reasoning → Compare → Most robust solution</contrastive_consistency>
</specialized_techniques>
```

## The Process

### Phase 1: Deep Analysis

Analyze the query to understand:
- **Complexity**: simple|moderate|complex|research-grade
- **Domain**: single|interdisciplinary|emergent
- **Type**: factual|analytical|creative|procedural|strategic
- **Output requirements**: brief|detailed|structured|iterative
- **Ambiguity level**: clear|moderate|high

### Phase 2: Technique Selection

Choose appropriate level(s) based on:

| Task Type | Primary | Secondary | Avoid |
|-----------|---------|-----------|--------|
| Factual Questions | Clear & Direct | Examples | CoT |
| Analysis | Structured CoT | XML Tags | Unguided |
| Creative | Role + Context | Few Examples | Over-structure |
| Mathematics | Guided CoT | Verification | Single-pass |
| Code | Examples + Format | Chain for complex | Vague specs |
| Research | Extended Thinking | Decomposition | Single query |
| Document Analysis | XML Structure | Chaining | Unstructured |
| Decision Making | Tree of Thought | Contrastive | Linear |
| Process Design | Least-to-Most | Verification | All-at-once |

### Phase 3: Prompt Construction

**Basic Template (Level 1-2)**:
```xml
<system>[Role if needed]</system>
<context>[Complete background information]</context>
<task>[Specific task + Success criteria]</task>
<examples>[2-3 Input/Output pairs if helpful]</examples>
<output_format>[Exact format specifications]</output_format>
<instructions>[Step-by-step + Quality checks]</instructions>
```

**Advanced Template (Level 3-4)**:
```xml
<phase_1>
  <objective>[Sub-goal 1]</objective>
  <thinking>[Explicit thinking steps]</thinking>
  <output>[Structured intermediate result]</output>
</phase_1>

<phase_2>
  <input>{{phase_1.output}}</input>
  <objective>[Sub-goal 2]</objective>
  <thinking>[Processing]</thinking>
  <output>[Further processed result]</output>
</phase_2>

<synthesis>
  <inputs>{{all_phases.outputs}}</inputs>
  <final_analysis>[Consolidation]</final_analysis>
  <deliverable>[Final result]</deliverable>
</synthesis>
```

### Phase 4: Optimization & Validation

Checklist:
- [ ] Clarity: Would a colleague understand this?
- [ ] Completeness: All necessary context present?
- [ ] Structure: XML tags used meaningfully?
- [ ] Efficiency: Minimal complexity for maximum output?
- [ ] Measurability: Success criteria defined?
- [ ] Debugging: Thinking process traceable?

### Phase 5: Reflection Loop (Level 3+ prompts)

Self-critique cycle for quality improvement:

```xml
<reflection_cycle max_iterations="3">
  <generator>
    <draft>{{constructed_prompt}}</draft>
  </generator>

  <critic>
    <evaluate_against>
      - Technique Selection: Does level match complexity?
      - Clarity: Are instructions unambiguous?
      - Completeness: Missing critical context?
      - Structure: Is XML structure optimal?
      - Edge Cases: Are boundaries handled?
      - Output Format: Is format precisely defined?
    </evaluate_against>
    <feedback>
      <quality_score>[1-10]</quality_score>
      <is_acceptable>[true if score >= 8]</is_acceptable>
    </feedback>
  </critic>

  <refiner condition="!is_acceptable AND iteration < max">
    <improved_prompt>[Enhanced version]</improved_prompt>
  </refiner>
</reflection_cycle>
```

**When to use Reflection:**
- Level 3+ prompts (Complex, Advanced, Specialized)
- Production use prompts
- Critical business applications
- When initial quality < 8/10

**When NOT to use:**
- Simple Level 1-2 prompts
- Quick prototypes
- One-off ad-hoc requests

## Confidence Scoring

Each generated prompt includes:
- **Confidence**: 0-100% based on information completeness
- **Performance Impact**: Minimal|Moderate|Significant
- **Thinking Requirements**: None|Standard|Extended
- **Caching Potential**: Low|Medium|High

## Critical Success Factors

### Must-Haves
1. **Thinking Output**: Without output, no thinking - ALWAYS explicitly request
2. **Context Completeness**: Claude knows NOTHING outside prompt content
3. **Clear Success Metrics**: How do you recognize success?

### Common Pitfalls
- **Over-Engineering**: Don't use Level 5 for Level 1 problems
- **Under-Specifying**: "Do something" is not a prompt
- **Format Ambiguity**: Define exact output structure
- **Hidden Complexity**: Multi-step disguised as single-step
- **Thinking Overhead**: Extended thinking for simple questions

### Performance Trade-offs
```
Simple Query → Minimal Structure → Fast Response
Complex Analysis → CoT + XML → Moderate Latency
Research Task → Extended Thinking → Accept Latency
Repetitive Task → Caching Setup → Initial Overhead, then Fast
```

## Usage

Activate naturally with phrases like:
- "Erstelle einen Prompt für..."
- "Optimize this prompt..."
- "I need a prompt that..."

Or explicitly:
```
@prompt-pro-framework
```

## Output Format

The framework provides:
1. **Analysis**: Query classification and requirements
2. **Technique Recommendation**: Level + specific techniques
3. **Constructed Prompt**: Ready-to-use prompt with XML structure
4. **Performance Metrics**: Expected latency and resource usage
5. **Alternative Approaches**: When multiple options exist
6. **Quality Score**: Self-assessed quality rating

## Progressive Disclosure

- **SKILL.md** (this file) - Core framework and process
- **reference.md** - Complete technique catalog, advanced patterns
- **examples.md** - Practical demonstrations across domains

## Related Skills

- [Research Orchestrator](research-orchestrator.md) - Research component for prompt optimization
- [Template Creator](template-creator.md) - Create prompts for system components
- [Brainstorming](brainstorming.md) - Collaborative design before prompt creation

---

<small>Source: `frameworks:prompt-pro-framework`</small>
