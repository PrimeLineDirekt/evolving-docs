---
title: macro-economist-agent
type: agent
tags: []
lang: en
confidence: 100
---

# macro-economist-agent


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
Net Liquidity = Fed Balance Sheet Size - Treasury General Account - Reverse Repo

Example (Dec 2024):
Fed BS: $7,200B
TGA: $900B (account balance holding idle funds)
RRP: $500B (reverse repos draining liquidity)

Net Liquidity = $7,200B - $900B - $500B = $5,800B

Trend: +$200B in past 3 months → EXPANDING (Bullish)
```


#### Example



**Code:**
```bash
Expanding Liquidity:
  ✓ More capital available
  ✓ Lower borrowing costs
  ✓ Risk assets rally (equities, crypto)
  → BTC bullish

Contracting Liquidity:
  ✗ Less capital available
  ✗ Higher borrowing costs
  ✗ Risk-off environment
  → BTC bearish
```


#### Example



**Code:**
```bash
CPI Shelter: +6.1% YoY (official, 9-month lag)
Real-time Rents: -2.3% YoY (Zillow, Apartment List)

Discrepancy: +8.4pp
Implication: Official CPI overstates inflation by ~2-3pp

Market Edge: Fed will cut sooner than consensus expects
→ This is the HIDDEN PATTERN most miss
```


#### Example



**Code:**
```bash
Current Target Rate: 5.25-5.50%
Implied Fed Funds (futures): 4.75-5.00% (market pricing 2-3 cuts in 2025)

Assessment: Fed "higher for longer" → But data suggests cuts coming Q1 2025
```


#### Example



**Code:**
```bash
If Fed balance sheet expanding → Liquidity positive → Risk assets rally
If Fed balance sheet shrinking → Liquidity negative → Risk assets pressured

Current: +$200B in 3 months → LIQUIDITY POSITIVE
```


#### Example



**Code:**
```bash
Latest FOMC Statement: "Inflation remains elevated"
BUT: "Data-dependent" language added → Pivot signal

Historical Pattern: "Data-dependent" → 90 days later → Rate cuts begin
→ Probability: 80% (historical accuracy)
```


#### Example



**Code:**
```bash
Real Yield = Nominal Yield - Expected Inflation

10-Year Real Yield:
  Treasury Nominal: 4.1%
  Expected Inflation: 2.0% (CPI 2yr forward)
  Real Yield: 2.1%

Impact on Gold:
  Higher Real Yields = Headwind for gold (lower returns vs bonds)
  Lower Real Yields = Tailwind for gold (bonds unattractive)

Current 2.1% = Slightly pressuring gold, but not extreme
```


#### Example



**Code:**
```python
macro_score = (
    liquidity_trend * 0.35 +           # 65 pts (expanding)
    inflation_trend * 0.25 +            # 70 pts (falling)
    fed_policy_stance * 0.20 +          # 60 pts (pivot coming)
    real_yields * 0.20                  # 55 pts (neutral)
) = 63/100

Interpretation: Moderately bullish macro, pivot coming
```


#### Example



**Code:**
```bash
Yield Curve Inversion: -0.5% (inverted for 18+ months)
  → Recession risk elevated, but timing uncertain

Unemployment: 4.2% (stable)
  → No immediate labor market weakness

Consumer Spending: +2.1% YoY
  → Still growing, but slowing

Credit Conditions: Tightening slightly
  → But not stressed

Overall Recession Risk: MEDIUM (30-40% chance in next 12 months)
```


#### Example



**Code:**
```bash
If Recession Occurs:
  BTC: Mixed (Initially down, then bounces on Fed emergency cuts)
  Gold: Strong (Flight to safety)
  Equities: Down sharply

Probability: 35% (not base case)
→ Factor into bear case scenario
```


#### Example



**Code:**
```bash
Current: 103.5 (strong dollar)

Impact:
  Strong USD → Gold pressure (priced in USD)
  Strong USD → Emerging market pressure (debt burden)
  Strong USD → Crypto less attractive in emerging markets

If USD weakens → Gold rallies, commodities rally
If USD strengthens → Asset prices pressure (bonds attractive)

Current Trend: Flat (no clear direction)
Forecast: Weakening if Fed cuts (rate differential narrows)
```


#### Example



**Code:**
```json
{
  "macro_score": 63,
  "components": {
    "liquidity_trend": 65,
    "inflation_trend": 70,
    "fed_policy": 60,
    "real_yields": 55
  },
  "key_insights": [
    "CPI Shelter lag creates hidden bullish setup",
    "Liquidity expanding (last 3 months)",
    "Fed pivot coming in 90 days (80% historical prob)",
    "Real yields neutral, not pressuring risk assets"
  ],
  "risks": [
    "Recession probability 35%",
    "Unexpected CPI reacceleration",
    "Geopolitical shock to oil"
  ],
  "opportunities": [
    "Narrative lag: Market too hawkish",
    "Fed cuts create rally catalyst",
    "Asset prices cheap on recession fears"
  ]
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/macro-economist-agent.md`</small>
