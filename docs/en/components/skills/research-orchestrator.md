---
title: Research Orchestrator
type: skill
tags: [framework, research, validation, confidence-scoring]
lang: en
confidence: 95
---

# Research Orchestrator

![Research Orchestrator Skill](../../shared/assets/infographics/skills/research-orchestrator.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Coordinate systematic multi-domain research with confidence scoring |
| **Complexity** | High |
| **Model** | sonnet |
| **Category** | frameworks |
| **Tools** | WebSearch, WebFetch, Task, Read, Write, Grep, Glob |
| **Context** | fork |
| **Timeout** | 600s |
</div>

## What It Does

The Research Orchestrator is an elite research coordinator that specializes in systematic multi-domain research with confidence scoring. It plans strategic research, executes quality-driven investigations with minimum 3 premium sources, and generates actionable implementation-ready outputs.

## Core Responsibilities

### 1. Strategic Research Planning
- Analyze research requests across multiple domains
- Break down complex goals into actionable phases
- Prioritize based on impact and confidence gaps
- Coordinate specialized research agents

### 2. Quality-Driven Execution
- Ensure **current** data (2024/2025)
- Validate with **minimum 3 premium sources**
- Calculate **confidence scores** (target: ≥90%)
- Resolve contradictions in findings

### 3. Actionable Output Generation
- Translate research to **implementation-ready updates**
- Generate code snippets, template updates, config changes
- Document findings in structured markdown reports
- Update confidence scores

## Research Framework

### Phase 1: Request Analysis & Planning

The orchestrator analyzes:
- **Domain**: Primary subject area
- **Complexity**: Simple|Moderate|Complex|Research-grade
- **Confidence Gap**: Current vs. required confidence level
- **Impact Potential**: Expected ROI of research
- **Urgency**: Priority level

Then creates a plan with:
- **Phases**: Decomposed research stages
- **Required Sources**: Source types needed
- **Success Criteria**: Definition of success
- **Estimated Depth**: Surface|Standard|Deep

**Research Depth Levels:**
- **Surface** (3-5 sources, 15min): Quick validation, trend check
- **Standard** (5-10 sources, 30-45min): Comprehensive understanding
- **Deep** (10+ sources, 1-2h): Exhaustive analysis, contradictions resolved

### Phase 2: Multi-Source Research Execution

For each research phase:
1. Fetch authoritative sources
2. Cross-validate findings
3. Calculate confidence scores
4. Filter by minimum confidence threshold

**Confidence Scoring Formula:**
```
Confidence Score (0-100%) =
  Source Authority (0-30) +
  Cross-Validation (0-40) +
  Recency (0-15) +
  Internal Consistency (0-15)

Levels:
  90-100%: Very High (3+ authoritative sources, recent, consistent)
  70-89%:  High (2+ good sources, validated)
  50-69%:  Moderate (partial validation, some uncertainty)
  30-49%:  Low (limited validation, conflicts)
  0-29%:   Very Low (single source, unvalidated)
```

### Phase 3: Synthesis & Pattern Recognition

The orchestrator identifies:
- **Consensus**: Where 80%+ sources agree
- **Contradictions**: Conflicting information requiring resolution
- **Trends**: Temporal patterns across data
- **Gaps**: Areas needing additional research
- **Insights**: Actionable conclusions

**Contradiction Resolution:**
- Authority-weighted consensus methodology
- Multiple source triangulation
- Explicit documentation of resolution process

### Phase 4: Actionable Output Generation

Generates comprehensive research report with:

**Executive Summary:**
- Research topic
- Overall confidence level
- Key finding
- Recommended action

**Key Findings:**
- Each finding with confidence score
- Supporting evidence from multiple sources
- Confidence breakdown (Authority/Validation/Recency/Consistency)
- Actionable insight

**Synthesis & Analysis:**
- Consensus areas with source counts
- Contradictions with resolution analysis
- Identified trends with projections
- Knowledge gaps requiring further research

**Implementation Plan:**
- Immediate actions (high priority)
- Short-term actions (medium priority)
- Long-term considerations

**Source Documentation:**
- High authority sources with metadata
- Supporting sources list
- URL references

**Confidence Assessment:**
- Overall confidence percentage
- High certainty areas
- Areas requiring validation
- Research quality strengths and limitations

**Next Steps:**
- Priority research topics
- Suggested methodology

## Domain-Specific Workflows

### Market Research
```
Phase 1: Market Intelligence → Size, Growth, Trends
Phase 2: Competitive Analysis → Players, Positioning, Gaps
Phase 3: Customer Intelligence → Needs, Pain points, Behavior
Phase 4: Opportunity Mapping → White spaces, Entry strategies
```

### Technical Research
```
Phase 1: Technology Landscape → Current state, Emerging tech
Phase 2: Implementation Patterns → Best practices, Case studies
Phase 3: Integration Analysis → Compatibility, Dependencies
Phase 4: Risk Assessment → Technical debt, Scalability
```

### Product Research
```
Phase 1: Feature Analysis → Core capabilities, Differentiation
Phase 2: User Experience → Usability, Satisfaction, Pain points
Phase 3: Performance Metrics → Speed, Reliability, Quality
Phase 4: Optimization Opportunities → Improvements, Roadmap
```

## Quality Assurance

Before finalizing research, verify:
- [ ] Minimum source count met (3+ for standard, 5+ for deep)
- [ ] All sources from 2024/2025 (or explicitly dated)
- [ ] Contradictions identified and resolved
- [ ] Confidence scores calculated for all findings
- [ ] Actionable insights generated
- [ ] Implementation plan provided
- [ ] Knowledge gaps documented
- [ ] Sources properly cited with URLs

## Usage

Activate naturally with phrases like:
- "Research {topic}"
- "I need market research on..."
- "Investigate {subject}"

Or explicitly:
```
@research-orchestrator
```

## Performance Optimization

- Use parallel research agents for multi-domain requests
- Cache frequently researched topics
- Leverage Task tool for deep dives
- WebSearch for broad discovery
- WebFetch for deep analysis

## Meta-Instructions

**For Research Orchestrator:**
1. ALWAYS start with current year data (2024/2025)
2. NEVER single-source critical findings
3. ALWAYS calculate confidence scores
4. ALWAYS resolve contradictions explicitly
5. ALWAYS provide actionable next steps

## Output Example

```markdown
# Research Report: AI Coding Assistants Market 2024

## Executive Summary
**Research Topic**: AI Coding Assistants Market
**Confidence Level**: 92% (Very High)
**Key Finding**: Market growing at 35% CAGR, GitHub Copilot dominant with 70% share
**Recommended Action**: Focus on specialized niche vs. general-purpose

## Key Findings

### Finding 1: Market Size & Growth
**Confidence**: 93% (Very High)

**Summary**: Global AI coding assistant market valued at $1.2B in 2024, projected to reach $4.8B by 2028.

**Supporting Evidence**:
- Gartner: $1.25B current, 35% CAGR projection
- IDC: $1.18B current, 37% CAGR projection
- Forrester: $1.15B current, 33% CAGR projection

**Confidence Breakdown**:
- Authority: 28/30 (Top-tier analyst firms)
- Validation: 38/40 (3 sources, <6% variance)
- Recency: 15/15 (All Q1 2024)
- Consistency: 12/15 (Minor projection variance)

**Actionable Insight**: High-growth market with consensus validation supports investment decision
```

## Progressive Disclosure

- **SKILL.md** (this file) - Core framework and methodology
- **reference.md** - Complete research protocols, advanced techniques
- **examples.md** - Domain-specific templates, case studies

## Related Skills

- [Prompt Pro Framework](prompt-pro-framework.md) - Optimize research queries
- [Brainstorming](brainstorming.md) - Define research questions
- [Template Creator](template-creator.md) - Create research agent templates

---

<small>Source: `frameworks:research-orchestrator`</small>
