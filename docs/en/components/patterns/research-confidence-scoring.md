---
title: research-confidence-scoring
type: pattern
tags: ["[research", " validation", " quality-control", " multi-source]"]
lang: en
confidence: 100
---

# research-confidence-scoring


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns || **Created** | 2024-11-22 |</div>

<div class="component-tags">
<span class="tag tag-[research">[research</span>
<span class="tag tag--validation"> validation</span>
<span class="tag tag--quality-control"> quality-control</span>
<span class="tag tag--multi-source]"> multi-source]</span>
</div>

## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Confidence Score = (Source Quality × Source Agreement × Recency × Validation) / 100

Where:
- Source Quality: Expert sources (10) > Industry blogs (7) > Forums (4)
- Source Agreement: All agree (10) > Majority (7) > Mixed (4)
- Recency: 2024-2025 (10) > 2023 (7) > older (4)
- Validation: Case studies (10) > Data (7) > Opinion (4)
```


#### Example



**Code:**
```markdown
TIER 1 (Weight: 10)
- Official Documentation
- Expert Analysis (verified professionals)
- Case Studies $100K+ revenue

TIER 2 (Weight: 7)
- Industry Publications
- Reputable Blogs
- Academic Research

TIER 3 (Weight: 4)
- Forums (Reddit, Quora)
- User Reviews
- Anecdotal Evidence
```


#### Example



**Code:**
```bash
Claim: "Fresh Pins get 90%+ traffic on Pinterest"
- Source 1 (Tier 1): Pinterest Creator Academy (confirmed)
- Source 2 (Tier 1): $168K Case Study (88-92% fresh pins)
- Source 3 (Tier 2): Pinterest SEO Expert (85-95% estimate)

Agreement: High (88-95% range)
Confidence: 92%
```


#### Example



**Code:**
```bash
2024-2025: Weight 10 (current)
2023: Weight 7 (recent)
2022 or older: Weight 4 (outdated for fast-moving platforms)
```


#### Example



**Code:**
```markdown
## Feature: {Name}
**Confidence Score**: 92%
**Sources**: 18 (Tier-1: 5, Tier-2: 10, Tier-3: 3)
**Last Updated**: 2024-11-20
**Validated**: Yes (case study + real data)

**Contradictions**: None
**Assumptions**: Pinterest algorithm stable for 6+ months
**Review Date**: 2025-05-01 (algorithm updates)
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/patterns/research-confidence-scoring.md`</small>
