---
title: market-technical-analyst-agent
type: agent
tags: []
lang: en
confidence: 100
---

# market-technical-analyst-agent


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
```bash
20-day EMA: $45,300
50-day SMA: $44,800
200-day SMA: $42,100

Signal:
- Price > 200-day MA → Uptrend context
- 20-day > 50-day > 200-day → Bullish alignment
```


#### Example



**Code:**
```bash
RSI (14): 58 (Neutral zone, 30-70 is range)
- > 70 = Overbought (short risk)
- < 30 = Oversold (long opportunity)
- 40-60 = Consolidation

MACD: Bullish crossover forming
- Blue > Red = Bullish
- Red > Blue = Bearish
```


#### Example



**Code:**
```bash
Resistance Levels:
  - $48,000 (recent swing high)
  - $51,000 (psychological)
  - $52,000 (Feb 2024 high)

Support Levels:
  - $42,000 (200-week MA)
  - $40,000 (December low)
  - $38,000 (2024 cycle low)
```


#### Example



**Code:**
```bash
Price: $45,123
Upper Band: $48,500
Lower Band: $41,700
Width: 6,800 (normal volatility)

Signal: Within bands → no extreme, consolidating
```


#### Example



**Code:**
```bash
Resistance: $2,100 (recent high)
Support: $2,000 (key level)
Real Yield Impact: 2.1% (pressure on gold)

Signal: Sideways, waiting for macro clarity
```


#### Example



**Code:**
```python
technical_score = (
    moving_average_alignment * 0.30 +  # 70 pts
    momentum_score * 0.30 +             # 65 pts
    support_resistance_proximity * 0.20 +  # 75 pts
    volatility_level * 0.20             # 60 pts
) = 67/100

This feeds into Forecast Confidence:
confidence = (technical * 0.30) + (macro * 0.35) + (catalyst * 0.20) + (model_accuracy * 0.15)
```


#### Example



**Code:**
```bash
SOPR (Spent Output Profit Ratio): 1.02
- = 1.0: Market in balance
- > 1.0: Slight profit-taking
- < 1.0: HODLing accumulation

Exchange Inflows: -$250M (24h)
Signal: Accumulation (coins leaving exchanges to cold storage)

Hashrate: 680 EH/s (near ATH)
Signal: Network secure, long-term conviction

Active Addresses: 1.2M (stable)
```


#### Example



**Code:**
```bash
┌─────────────────────────────┐
│ BTC Technical Status        │
├─────────────────────────────┤
│ Price: $45,123              │
│ 24h: +2.3% | 7d: -1.2%      │
│                             │
│ Technical Score: 67/100     │
│                             │
│ MAs: 20>50>200 ✓ (Bullish)  │
│ RSI: 58 (Neutral)           │
│ MACD: Bullish crossover     │
│                             │
│ Resistance: $48k, $51k      │
│ Support: $42k (200-MA)      │
│                             │
│ SOPR: 1.02 (slight profit)  │
│ Exchange Outflows: -$250M   │
└─────────────────────────────┘
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/market-technical-analyst-agent.md`</small>
