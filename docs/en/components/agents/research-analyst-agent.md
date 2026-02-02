---
title: research-analyst-agent
type: agent
tags: []
lang: en
confidence: 100
---

# research-analyst-agent


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

"Multi-source research and validation agent with confidence scoring"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "research_topic": "string",
  "research_depth": "surface|standard|deep",
  "source_requirements": {
    "minimum_sources": "number",
    "source_types": ["array"],
    "recency": "string"
  },
  "focus_areas": ["array"],
  "constraints": {
    "time_limit": "X minutes",
    "output_format": "string"
  }
}
```


#### Example



**Code:**
```json
{
  "agent_id": "multi-domain-research",
  "execution_id": "uuid",
  "priority_level": "HIGH",
  "success_criteria": "Multi-source validated findings with confidence scores"
}
```


#### Example



**Code:**
```python
def plan_research(query, depth):
    strategy = {
        "surface": {
            "sources": 3-5,
            "validation": "Cross-check key facts",
            "time": "5-10 minutes"
        },
        "standard": {
            "sources": 5-10,
            "validation": "Multi-source validation",
            "time": "15-30 minutes"
        },
        "deep": {
            "sources": 10+,
            "validation": "Comprehensive validation",
            "time": "30-60 minutes"
        }
    }
    return strategy[depth]
```


#### Example



**Code:**
```python
def collect_data(research_plan):
    findings = []

    for query in research_plan.queries:
        # Execute search
        results = search(query, source_types)

        # Filter and rank
        relevant = filter_by_relevance(results)
        ranked = rank_by_authority(relevant)

        # Extract information
        for source in ranked[:max_per_query]:
            finding = extract_information(source)
            finding.metadata = capture_metadata(source)
            findings.append(finding)

    return findings
```


#### Example



**Code:**
```python
def validate_finding(finding, all_findings):
    confidence_score = 0

    # Source authority (0-30 points)
    authority_score = assess_source_authority(finding.source)

    # Cross-validation (0-40 points)
    corroboration = count_corroborating_sources(finding, all_findings)
    validation_score = min(corroboration * 10, 40)

    # Recency (0-15 points)
    recency_score = assess_recency(finding.date)

    # Consistency (0-15 points)
    consistency_score = check_internal_consistency(finding)

    confidence_score = (
        authority_score +
        validation_score +
        recency_score +
        consistency_score
    )

    return {
        "confidence": confidence_score,
        "level": categorize_confidence(confidence_score),
        "factors": {
            "authority": authority_score,
            "validation": validation_score,
            "recency": recency_score,
            "consistency": consistency_score
        }
    }
```


#### Example



**Code:**
```python
def identify_patterns(findings):
    patterns = {
        "consensus": [],
        "contradictions": [],
        "trends": [],
        "gaps": []
    }

    # Group by topic
    topics = group_by_topic(findings)

    for topic, topic_findings in topics.items():
        # Find consensus
        consensus = find_agreement(topic_findings)
        if consensus:
            patterns["consensus"].append(consensus)

        # Find contradictions
        conflicts = find_contradictions(topic_findings)
        patterns["contradictions"].extend(conflicts)

        # Detect trends
        if has_temporal_data(topic_findings):
            trend = analyze_trend(topic_findings)
            patterns["trends"].append(trend)

        # Identify gaps
        gaps = identify_information_gaps(topic, topic_findings)
        patterns["gaps"].extend(gaps)

    return patterns
```


#### Example



**Code:**
```markdown
# Multi-Domain Research Report

## Executive Summary

**Research Topic**: {TOPIC}
**Research Depth**: {DEPTH}
**Sources Analyzed**: {NUMBER}
**Overall Confidence**: {PERCENTAGE}%
**Key Finding**: {PRIMARY_INSIGHT}

### Top 3 Insights:
1. {INSIGHT_1} - Confidence: {X}%
2. {INSIGHT_2} - Confidence: {X}%
3. {INSIGHT_3} - Confidence: {X}%

## 1. Research Scope & Methodology

### Research Questions:
1. {QUESTION_1}
2. {QUESTION_2}
3. {QUESTION_3}

### Methodology:
- **Sources**: {NUMBER} sources across {TYPES}
- **Validation**: Multi-source cross-validation
- **Timeframe**: {RECENCY_REQUIREMENT}
- **Depth**: {DEPTH_LEVEL}

## 2. Key Findings

### Finding 1: {FINDING_TITLE}
**Confidence**: {XX}% ({LEVEL})

**Summary**: {FINDING_DESCRIPTION}

**Supporting Evidence**:
- {SOURCE_1}: {EVIDENCE}
- {SOURCE_2}: {EVIDENCE}
- {SOURCE_3}: {EVIDENCE}

**Confidence Factors**:
- Authority: {SCORE}/30
- Validation: {SCORE}/40
- Recency: {SCORE}/15
- Consistency: {SCORE}/15

### Finding 2: {FINDING_TITLE}
**Confidence**: {XX}% ({LEVEL})

{Same structure as Finding 1}

### Finding 3: {FINDING_TITLE}
**Confidence**: {XX}% ({LEVEL})

{Same structure as Finding 1}

## 3. Synthesis & Analysis

### Consensus Areas:
Where multiple authoritative sources agree:

1. **{CONSENSUS_1}**
   - Supported by: {NUMBER} sources
   - Confidence: {XX}%
   - Implication: {INSIGHT}

2. **{CONSENSUS_2}**
   - Supported by: {NUMBER} sources
   - Confidence: {XX}%
   - Implication: {INSIGHT}

### Contradictions & Uncertainties:
Where sources disagree or evidence is mixed:

1. **{CONTRADICTION_1}**
   - Source A claims: {CLAIM}
   - Source B claims: {COUNTER_CLAIM}
   - Analysis: {RECONCILIATION_OR_EXPLANATION}
   - Recommendation: {FURTHER_RESEARCH_NEEDED}

### Identified Trends:
Patterns observed across data:

1. **{TREND_1}**
   - Pattern: {DESCRIPTION}
   - Evidence: {SUPPORTING_DATA}
   - Projection: {FUTURE_IMPLICATION}

### Knowledge Gaps:
Areas requiring additional research:

1. **{GAP_1}**: {DESCRIPTION}
2. **{GAP_2}**: {DESCRIPTION}

## 4. Detailed Source Analysis

### High Authority Sources:
1. **{SOURCE_1}**
   - Type: {PRIMARY|SECONDARY|TERTIARY}
   - Authority: {SCORE}/10
   - Recency: {DATE}
   - Key Contribution: {INSIGHT}
   - URL: {LINK}

2. **{SOURCE_2}**
   - Type: {PRIMARY|SECONDARY|TERTIARY}
   - Authority: {SCORE}/10
   - Recency: {DATE}
   - Key Contribution: {INSIGHT}
   - URL: {LINK}

### Supporting Sources:
{LIST_OF_ADDITIONAL_SOURCES}

### Sources Excluded:
{SOURCES_CONSIDERED_BUT_REJECTED_AND_WHY}

## 5. Actionable Insights

### Immediate Applications:
1. {ACTION_1} - Based on {FINDING}
2. {ACTION_2} - Based on {FINDING}

### Strategic Implications:
1. {IMPLICATION_1}
2. {IMPLICATION_2}

### Recommended Next Steps:
1. {NEXT_STEP_1}
2. {NEXT_STEP_2}
3. {NEXT_STEP_3}

## 6. Research Quality Assessment

**Strengths**:
- {STRENGTH_1}
- {STRENGTH_2}

**Limitations**:
- {LIMITATION_1}
- {LIMITATION_2}

**Confidence Assessment**:
- Overall research confidence: {XX}%
- Areas of high certainty: {AREAS}
- Areas requiring further validation: {AREAS}

## 7. Additional Research Recommendations

**Priority Research Topics**:
1. {TOPIC_1} - To address {GAP}
2. {TOPIC_2} - To validate {FINDING}

**Suggested Methodologies**:
- {METHODOLOGY_FOR_DEEPER_RESEARCH}

---

**Research Completed**: {TIMESTAMP}
**Total Sources**: {NUMBER}
**Average Confidence**: {XX}%
**Validation Level**: {COMPREHENSIVE|STANDARD|PRELIMINARY}
```


#### Example



**Code:**
```python
# 1. Initial broad search
results = WebSearch(query=primary_query)

# 2. Deep dive on promising sources
for source in high_value_sources:
    content = WebFetch(url=source.url)
    analyze(content)

# 3. Cross-reference with knowledge base
related = Read(file_path=knowledge_base_path)
validate_against_existing(related)
```


#### Example



**Code:**
```bash
IF sources_found < minimum_required:
  Extend search with alternative queries
  Lower source quality threshold (with transparency)
  Flag limitation in report
```


#### Example



**Code:**
```bash
IF major_contradictions_found:
  Present all perspectives
  Analyze reasons for disagreement
  Provide conditional recommendations
  Flag for expert review if critical
```


#### Example



**Code:**
```bash
IF overall_confidence < 50%:
  Explicitly state limitations
  Recommend additional research
  Provide preliminary findings with caveats
  Suggest expert consultation
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/research-analyst-agent.md`</small>
