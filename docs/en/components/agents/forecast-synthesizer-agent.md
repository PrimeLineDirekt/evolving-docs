---
title: forecast-synthesizer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# forecast-synthesizer-agent


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
```python
critical_levers = {
    'BTC': {
        'fed_policy': ('dovish', 'neutral', 'hawkish'),
        'liquidity': ('expanding', 'flat', 'contracting'),
        'regulatory': ('clarity', 'status_quo', 'crackdown'),
        'crypto_sentiment': ('bullish', 'neutral', 'bearish')
    },
    'GOLD': {
        'real_yields': ('falling', 'flat', 'rising'),
        'dxy': ('weakening', 'flat', 'strengthening'),
        'recession_risk': ('low', 'medium', 'high')
    }
}
```


#### Example



**Code:**
```bash
Bull Case (30%):
  - Fed signals rate cuts in Q1 2025 (Probability: 60%)
  - CPI comes in at 2.9% (Probability: 35%)
  - Bitcoin ETF inflows accelerate (Probability: 70%)
  → Combined Probability: 0.6 × 0.35 × 0.7 = 14.7%

Base Case (50%):
  - CPI at 3.1% as expected (Probability: 50%)
  - Fed maintains 'higher for longer' (Probability: 60%)
  - Consolidation continues (Probability: 60%)
  → Combined: 0.5 × 0.6 × 0.6 = 18%

Bear Case (20%):
  - CPI surprise at 3.4% (Probability: 25%)
  - SEC escalates enforcement (Probability: 40%)
  - Risk-off due to geopolitics (Probability: 30%)
  → Combined: 0.25 × 0.4 × 0.3 = 3%
```


#### Example



**Code:**
```bash
Base: $45,000 (current price)
Historical returns in bull scenarios: +15-20%
Target Range: $52k - $54k (30-day)

Confidence: 60% (Fed pivot uncertain)
```


#### Example



**Code:**
```bash
Weighted = (Bull_Target × Bull_Prob) +
           (Base_Target × Base_Prob) +
           (Bear_Target × Bear_Prob)

BTC = ($53k × 0.30) + ($47k × 0.50) + ($40k × 0.20)
    = $15.9k + $23.5k + $8k
    = $47.4k
```


#### Example



**Code:**
```python
def calculate_confidence(technical_score, macro_score, catalyst_clarity, model_accuracy):
    """
    High (80-100%): Strong technical + macro alignment, clear catalyst path
    Moderate (60-79%): Mixed signals, awaiting key data
    Low (40-59%): High uncertainty, conflicting indicators
    Speculative (<40%): Extreme scenarios, binary outcomes
    """
    return (
        technical_score * 0.30 +        # Technical alignment
        macro_score * 0.35 +             # Macro environment
        catalyst_clarity * 0.20 +        # Clear catalysts ahead
        model_accuracy * 0.15            # Recent accuracy of system
    )
```


#### Example



**Code:**
```json
{
  "next_catalysts": [
    {
      "event": "CPI Release",
      "date": "2025-01-12",
      "expected_impact": "HIGH",
      "bull_scenario": "CPI 2.9% → BTC accelerates",
      "bear_scenario": "CPI 3.4% → Risk-off"
    },
    {
      "event": "FOMC Decision",
      "date": "2025-01-31",
      "expected_impact": "VERY_HIGH",
      "bull_scenario": "Rate hold signals future cuts",
      "bear_scenario": "Hawkish surprise → Tech selloff"
    }
  ]
}
```


#### Example



**Code:**
```bash
┌─────────────────────────────────────────┐
│ BTC 30-Day Forecast                     │
├─────────────────────────────────────────┤
│ Bull Case (30%): $52k-$58k              │
│  Catalysts: Rate cuts, CPI miss         │
│                                         │
│ Base Case (50%): $45k-$50k              │
│  Catalysts: Consolidation, wait for Fed │
│                                         │
│ Bear Case (20%): $38k-$42k              │
│  Catalysts: Recession fears, SEC action │
│                                         │
│ Weighted Average: $47.4k                │
│ Confidence: 65% (Awaiting FOMC)         │
│                                         │
│ Key Risk: CPI surprise upside           │
│ Key Opportunity: Narrative lag catches  │
└─────────────────────────────────────────┘
```


#### Example



**Code:**
```markdown
## Forecast (30-Day)

### Bitcoin
- Bull Case (30%): $52k-$58k
  Drivers: Rate cuts accelerate, liquidity expands
- Base Case (50%): $45k-$50k
  Drivers: Consolidation, data-dependent Fed
- Bear Case (20%): $38k-$42k
  Drivers: Recession fears, regulatory crackdown

**Weighted Forecast**: $47.4k
**Confidence**: 65% (Moderate - awaiting key catalysts)

**Key Catalysts**:
- Jan 12: CPI Release (Major impact expected)
- Jan 31: FOMC Decision (Very high impact)
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/forecast-synthesizer-agent.md`</small>
