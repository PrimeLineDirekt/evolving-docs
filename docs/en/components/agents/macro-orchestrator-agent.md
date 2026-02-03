---
title: macro-orchestrator-agent
type: agent
tags: [orchestration, market-analysis, macro, automation]
lang: en
confidence: 100
---

# macro-orchestrator-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Orchestrator agent that coordinates all Macro-Analyse agents and synthesizes comprehensive market analysis through multi-phase execution. |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | market-analysis |
| **Domain** | agent-coordination-and-synthesis |</div>


## What It Does

The Macro Orchestrator Agent coordinates 7 specialized market analysis agents to generate comprehensive, multi-scenario market forecasts with continuous learning and self-improvement.

**Core Principle:** Orchestrated analysis - parallel data collection, multi-perspective analysis, pattern recognition, and synthesis into actionable forecasts.

**Agents Coordinated:**
- `macro-data-collector-agent` - Fetches real-time data (crypto, metals, macro, events, news)
- `market-technical-analyst-agent` - Calculates technical scores (price action, indicators)
- `macro-economist-agent` - Analyzes liquidity, inflation, Fed policy
- `meta-analyst-agent` - Identifies narratives, geopolitics, cui bono analysis
- `pattern-recognizer-agent` - Finds historical patterns and contrarian signals
- `forecast-synthesizer-agent` - Combines all inputs into multi-scenario forecasts
- `learning-optimizer-agent` - Tracks accuracy, updates model weights


## System Impact

- **Powers Macro-Analyse dashboard** - Real-time market analysis with hourly updates
- **Generates daily PDF reports** - Comprehensive market analysis at 18:00 Vietnam time
- **Enables self-improving forecasts** - Learns from prediction accuracy over time
- **Coordinates 7 specialized agents** - Parallel execution where possible
- **Maintains prediction accuracy tracking** - Continuous performance monitoring


## Architecture

**Model:** Sonnet (high complexity orchestration)

**Execution Modes:**
- **Hourly:** Real-time data updates and analysis (parallel execution)
- **Daily:** Full analysis + PDF report generation (18:00 Vietnam = 11:00 UTC)
- **Weekly:** Backtest, accuracy review, model refinement

**6-Phase Orchestration:**

```
PARALLEL PHASE 1: Collect (30s timeout)
└─ macro-data-collector-agent
   ├─ Crypto data (BTC, XRP, XLM, XDC)
   ├─ Metals data (Gold, Silver)
   ├─ Macro data (CPI, Fed rates, Yields, Treasury)
   ├─ Events (SEC, FOMC, Elections)
   └─ News (Reuters, Reddit, CryptoPanic)

PARALLEL PHASE 2: Analyze (60s timeout)
├─ market-technical-analyst-agent → Technical scores
├─ macro-economist-agent → Liquidity, inflation analysis
└─ meta-analyst-agent → Narratives, geopolitics

PARALLEL PHASE 3: Patterns & Context
└─ pattern-recognizer-agent → Historical patterns, contrarian signals

SEQUENTIAL PHASE 4: Synthesize (45s)
└─ forecast-synthesizer-agent
   → Input: Technical (67), Macro (63), Patterns, Narratives
   → Output: Multi-scenario forecasts with confidence

SEQUENTIAL PHASE 5: Learning (Daily)
└─ learning-optimizer-agent
   → Review previous forecasts
   → Update model weights
   → Calculate accuracy metrics

SEQUENTIAL PHASE 6: Output
└─ Orchestrator generates:
   ├─ Dashboard updates (hourly)
   ├─ PDF report (daily at 18:00)
   └─ Experience memory entries
```


## Usage

### Hourly Execution (Real-time Data)

**Trigger:** Every hour (automated)

**Workflow:**
1. Collect real-time data from all sources (Binance, Zillow, FRED)
2. Validate data quality (must be >85%)
3. Run parallel analysis (technical, macro, meta)
4. Find patterns and synthesize forecast
5. Update dashboard widgets

**Typical Execution Time:** ~2-3 minutes

### Daily Execution (PDF Report)

**Trigger:** 18:00 Vietnam Time (11:00 UTC, 06:00 EST)

**Workflow:**
1. Run full hourly execution with fresh post-market data
2. Learning optimizer reviews previous forecasts
3. Model weights updated based on accuracy
4. Generate comprehensive PDF report
5. Save to `reports/{YYYY}-{MM}-{DD}-market-special.pdf`
6. Update domain memory with latest forecast

**Typical Execution Time:** ~5-7 minutes

### Weekly Execution (Backtest & Refinement)

**Trigger:** Every week (automated)

**Workflow:**
1. Deep learning review of past 7 days
2. Calculate accuracy metrics
3. Identify model weak points
4. Run refined forecast with recent learnings
5. Update PDF report with learning insights

**Typical Execution Time:** ~10-15 minutes

### Output Format

**Dashboard Update (Hourly):**
```json
{
  "technical_score": 67,
  "macro_score": 63,
  "confidence": 65,
  "scenarios": {
    "bull_case": {"price": 51000, "probability": 0.25},
    "base_case": {"price": 45000, "probability": 0.50},
    "bear_case": {"price": 38000, "probability": 0.25}
  },
  "next_catalyst": "CPI on Jan 12",
  "timestamp": "2025-01-15T10:23:00Z"
}
```

**System Health:**
```json
{
  "system_status": "healthy",
  "agent_status": {
    "data_collector": "✓ 100%",
    "technical_analyst": "✓ 100%",
    "macro_economist": "✓ 100%",
    "meta_analyst": "✓ 100%",
    "pattern_recognizer": "✓ 100%",
    "forecast_synthesizer": "✓ 100%",
    "learning_optimizer": "✓ 100%"
  },
  "data_quality": "87%",
  "forecast_confidence": "65%",
  "next_catalyst": "CPI on Jan 12"
}
```


## Configuration

### Quality Gates Before Output

**Validation Checks:**
- Technical/macro scores: 0 < score ≤ 100
- Confidence: 30% < confidence < 95% (prevents overfit/underfit)
- Scenario probabilities: Must sum to 100%
- Price logic: bear_case < base_case < bull_case
- Minimum 3 key assumptions present
- Minimum 2 next catalysts identified

**If validation fails:** Raise error, don't publish invalid forecast

### Error Recovery

**Single Agent Failure:**
- Technical analyst timeout → Use neutral default (50)
- Macro data unavailable → Use last known good
- Log error and store experience entry

**Multiple Agent Failures (≥3):**
- Skip forecast generation
- Send system alert
- Use previous forecast with warning marker
- Log degraded system state

### Performance Metrics

**Tracked Continuously:**
- Execution time per phase
- Data quality score (%)
- Agent success rate (7/7)
- Forecast confidence (%)
- 30-day model accuracy (%)
- System uptime (%)


## Best Practices

- **Parallel execution Phase 1-3** - Faster than sequential analysis
- **Validate data quality first** - Don't analyze bad data (>85% quality threshold)
- **Use defaults for single failures** - Continue with available data
- **Stop on multiple failures** - Better to skip than publish bad forecast
- **Track accuracy continuously** - Self-improving system needs feedback
- **Update model weights weekly** - Learn from recent prediction errors


## Related

- [market-technical-analyst-agent](market-technical-analyst-agent.md) - Technical analysis
- [macro-economist-agent](macro-economist-agent.md) - Macro analysis
- [forecast-synthesizer-agent](forecast-synthesizer-agent.md) - Synthesis
- [learning-optimizer-agent](learning-optimizer-agent.md) - Self-improvement
- [macro-analyse scenario](../../scenarios/macro-analyse.md) - Full system setup
- [multi-agent-orchestration-pattern](../../patterns/multi-agent-orchestration-pattern.md) - Pattern template

---

<small>Source: `.claude/agents/macro-orchestrator-agent.md`</small>
