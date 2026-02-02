---
title: meta-analyst-agent
type: agent
tags: []
lang: en
confidence: 100
---

# meta-analyst-agent


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
def detect_narrative_discrepancy(msm_headlines, hard_data):
    """
    Example:
    MSM: "Inflation remains elevated" (CPI 3.2%)
    Reality: CPI Shelter +6.1% (lagged), Real Rents -2.3% (current)

    Discrepancy: Official data overstates inflation by ~2-3pp due to lag
    Market Implication: Fed has more room to cut than consensus expects
    → Bullish for risk assets (positioning opportunity)
    """
```


#### Example



**Code:**
```bash
Narrative Lag Alert:
  MSM says: "Inflation sticky"
  Reality: CPI Shelter lagged, Real Rents falling
  Edge: Fed has cut room consensus doesn't see
  Confidence: 78%
```


#### Example



**Code:**
```bash
Ukraine War (2022):
  → Europe cuts Russian gas
  → Buys US LNG (3x price)
  → European energy costs surge
  → Manufacturing uncompetitive
  → EU recession
  → ECB forced to cut rates
  → EUR weakens
  → USD strengthens
  → Gold/BTC correlation shifts

Middle East Conflict:
  → Oil supply concerns
  → Brent crude spikes
  → Inflation reaccelerates
  → Fed delays cuts
  → Risk-off sentiment
  → Gold UP (safe haven), BTC DOWN (risk asset)
```


#### Example



**Code:**
```bash
Cui Bono Alert: [SEC vs XRP]
  Official: "Investor Protection"
  Reality: Eliminates Ripple competition for CBDCs
  Winners: Traditional finance, Fed/ECB
  Losers: XRP holders (short-term), Ripple (partnerships)
  Market Implication: XRP suppressed but don't short (regulatory clarity coming)
  Confidence: 72%
```


#### Example



**Code:**
```bash
Policy Action → 1st Order Effect → 2nd Order Effect → 3rd Order → Market Reaction

Example: Fed Rate Hikes (2022-2023)

1st Order: Borrowing costs ↑ → Consumer spending ↓ → Markets down

2nd Order: Regional banks hold long-duration bonds (mortgages) →
           Rate hikes → Bond prices collapse → Unrealized losses mount

3rd Order: Bank run (SVB, Signature) → Credit crunch fears → Contagion risk

Market Reaction:
  - Initially: Risk-off (BTC down, Gold up)
  - Then: Fed forced to provide liquidity (BTFP program)
  - Finally: Liquidity injection → BTC rallies 40% in 3 weeks
```


#### Example



**Code:**
```bash
Contrarian Alert: BTC Fear & Greed = 18 (Extreme Fear)

Historical Pattern: Last 5 times F&G <20:
  - 2018 Dec: BTC $3,200 → $13k in 6 months (+306%)
  - 2020 Mar: BTC $3,800 → $64k in 12 months (+1,584%)
  - 2022 Nov: BTC $15,500 → $31k in 6 months (+100%)

Current Setup:
  - Sentiment: Extreme Fear (retail capitulation)
  - Liquidity: Expanding (Fed balance sheet +$200B in 3 months)
  - Technicals: BTC at 200-week MA (historically strong support)

Contrarian Play: Accumulate BTC now (market hates it, setup is bullish)
Confidence: 75%
```


#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────┐
│  HIDDEN DRIVERS (Meta-Analysis)                │
├─────────────────────────────────────────────────┤
│  🔴 Narrative Discrepancy:                     │
│    MSM: "Inflation sticky" | Reality: Shelter lag
│    → Fed has more cut room than consensus       │
│                                                 │
│  ⚠️  Geopolitical Chain:                       │
│    Middle East tension → Oil $85 → Inflation   │
│    → Fed delay cuts → Short-term bearish BTC   │
│                                                 │
│  📊 Pattern Match: 2020 Election Cycle         │
│    Similar setup: Election + Fed cuts + Halving│
│    → BTC +300% in 12 months (historical)       │
│                                                 │
│  🎯 Contrarian Signal: Extreme Fear (F&G = 18)│
│    Retail capitulation → Bottom forming        │
│    → Accumulate BTC (75% confidence)           │
└─────────────────────────────────────────────────┘
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/meta-analyst-agent.md`</small>
