---
title: pattern-recognizer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# pattern-recognizer-agent


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




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "pattern": "Election Cycle Pattern",
  "match_score": 87,
  "historical_outcomes": [
    {"year": 2020, "btc_return_6m": "+125%"},
    {"year": 2016, "btc_return_6m": "+156%"},
    {"year": 2012, "btc_return_6m": "+79%"}
  ],
  "current_probability": 0.75,
  "confidence": "HIGH",
  "recommendation": "Accumulate BTC (3 tailwinds aligned)"
}
```


#### Example



**Code:**
```bash
Contrarian Alert (Confidence: 75%)

Setup: Extreme Fear (F&G = 18)
Historical: Last 5 occurrences
  - 2018 Dec: +306% in 6 months
  - 2020 Mar: +1,584% in 12 months
  - 2022 Nov: +100% in 6 months

Current Conditions:
  ✓ Sentiment: Bearish (retail capitulation)
  ✓ Liquidity: Expanding (Fed pivot)
  ✓ Technicals: Support holding

Recommendation: Contrarian accumulate
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/pattern-recognizer-agent.md`</small>
