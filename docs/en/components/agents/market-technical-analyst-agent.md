---
title: market-technical-analyst-agent
type: agent
tags: [market-analysis, technical-analysis, indicators]
lang: en
confidence: 100
---

# market-technical-analyst-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Specialist agent that analyzes price action, support/resistance, momentum indicators to provide technical context for market forecasts. |
| **Complexity** | medium |
| **Model** | haiku |
| **Category** | market-analysis |
| **Domain** | technical-indicators-and-chart-analysis |</div>


## What It Does

The Market Technical Analyst Agent analyzes cryptocurrency and metals markets using technical indicators (moving averages, RSI, MACD, Bollinger Bands) and on-chain metrics to generate technical scores (0-100) that feed into forecast confidence calculations.

**Core Principle:** Evidence-based technical analysis - only use data from official sources, never invent data.

**Key Indicators:**
- **Moving Averages** - Trend direction (20-day, 50-day, 200-day)
- **RSI** - Momentum and overbought/oversold levels
- **MACD** - Trend strength and reversals
- **Bollinger Bands** - Volatility and price extremes
- **Support/Resistance** - Key price levels
- **On-Chain Metrics** - SOPR, exchange flows, hashrate, active addresses


## System Impact

- **Powers technical score calculation** - 30% weight in forecast confidence
- **Identifies key price levels** - Support/resistance for scenarios
- **Tracks momentum shifts** - Early warning for trend changes
- **Validates macro analysis** - Technical confirmation of macro narratives
- **Called by macro-orchestrator** - Part of Phase 2 parallel analysis


## Architecture

**Model:** Haiku (medium complexity, fast execution)

**Data Sources:**
- **Binance API** - OHLCV data (Open, High, Low, Close, Volume)
- **Blockchain.com** - On-chain metrics (SOPR, exchange flows, hashrate)
- **CoinGecko** - Market cap, dominance metrics

**Analysis Components:**

```
Technical Analysis
├─ Moving Averages (30% weight)
│  └─ 20-day EMA, 50-day SMA, 200-day SMA alignment
├─ Momentum Indicators (30% weight)
│  └─ RSI (14), MACD crossovers
├─ Support/Resistance (20% weight)
│  └─ Key levels, proximity to S/R
└─ Volatility (20% weight)
   └─ Bollinger Bands, ATR

Technical Score = Weighted Average → 0-100
```


## Usage

### BTC Technical Analysis

**Moving Averages:**
```
20-day EMA: $45,300
50-day SMA: $44,800
200-day SMA: $42,100

Signal:
- Price > 200-day MA → Uptrend context
- 20-day > 50-day > 200-day → Bullish alignment (70 pts)
```

**Momentum (RSI, MACD):**
```
RSI (14): 58 (Neutral zone, 30-70 is healthy range)
- > 70 = Overbought (short risk)
- < 30 = Oversold (long opportunity)
- 40-60 = Consolidation (65 pts)

MACD: Bullish crossover forming (75 pts)
- Blue > Red = Bullish
- Red > Blue = Bearish
```

**Support & Resistance:**
```
Resistance Levels:
  - $48,000 (recent swing high)
  - $51,000 (psychological level)
  - $52,000 (Feb 2024 high)

Support Levels:
  - $42,000 (200-week MA)
  - $40,000 (December low)
  - $38,000 (2024 cycle low)

Proximity Score: 75 pts (healthy distance from extremes)
```

**Bollinger Bands:**
```
Price: $45,123
Upper Band: $48,500
Lower Band: $41,700
Width: 6,800 (normal volatility)

Signal: Within bands → no extreme, consolidating (60 pts)
```

**On-Chain Data (BTC):**
```
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

### Gold Technical Analysis

```
Resistance: $2,100 (recent high)
Support: $2,000 (key level)
Real Yield Impact: 2.1% (pressure on gold)

Signal: Sideways, waiting for macro clarity
```

### Technical Score Calculation

```python
technical_score = (
    moving_average_alignment * 0.30 +  # 70 pts
    momentum_score * 0.30 +             # 65 pts
    support_resistance_proximity * 0.20 +  # 75 pts
    volatility_level * 0.20             # 60 pts
) = 67/100
```

### Output Format (Dashboard Widget)

```
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

### Data Source Priority

**Primary (Real-time):**
- Binance API - Price, volume, OHLCV
- Blockchain.com - On-chain metrics

**Secondary (Backup):**
- CoinGecko - Market data
- CryptoCompare - Alternative pricing

### Integration into Forecast Confidence

Technical Score feeds macro-orchestrator forecast calculation:

```python
confidence = (
    technical_score * 0.30 +      # 67 → +20.1 pts
    macro_score * 0.35 +          # 63 → +22.05 pts
    catalyst_proximity * 0.20 +   # 75 → +15 pts
    model_accuracy * 0.15         # 68 → +10.2 pts
) = 67.35% confidence
```

**Confidence Adjustments:**
- High technical alignment (>70) → +10% confidence
- Mixed signals (40-60) → -5% confidence
- Weak technical (<40) → -15% confidence


## Best Practices

- **Never invent data** - All metrics from official API sources only
- **Use multiple indicators** - No single indicator is sufficient
- **Weight moving averages highest** - Most reliable trend indicator (30%)
- **Check on-chain metrics** - Confirms or contradicts price action
- **Update hourly** - Fresh data for real-time analysis
- **Validate data quality** - Check API response completeness before analyzing


## Related

- [macro-orchestrator-agent](macro-orchestrator-agent.md) - Calls this agent in Phase 2
- [forecast-synthesizer-agent](forecast-synthesizer-agent.md) - Uses technical score
- [meta-analyst-agent](meta-analyst-agent.md) - Provides market context
- [macro-analyse scenario](../../scenarios/macro-analyse.md) - Full system

---

<small>Source: `.claude/agents/market-technical-analyst-agent.md`</small>
