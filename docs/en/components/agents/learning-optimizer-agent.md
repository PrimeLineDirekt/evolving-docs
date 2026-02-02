---
title: learning-optimizer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# learning-optimizer-agent


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
Forecast Generated (Day 0)
    ↓
After 30 Days: Compare Predicted vs Actual (Day 30)
    ↓
Calculate Error & Root Cause (Learning)
    ↓
/remember solution → Experience Memory
    ↓
Auto-Suggest on Next Similar Scenario
    ↓
Model Weights Adjusted
```


#### Example



**Code:**
```json
{
  "date": "2025-01-15",
  "asset": "BTC",
  "forecast_type": "30-day",
  "predictions": {
    "bull_case": {
      "probability": 0.30,
      "target_low": 52000,
      "target_high": 58000
    },
    "base_case": {
      "probability": 0.50,
      "target_low": 45000,
      "target_high": 50000
    },
    "bear_case": {
      "probability": 0.20,
      "target_low": 38000,
      "target_high": 42000
    },
    "weighted_forecast": 47400,
    "confidence_score": 0.65
  },
  "key_assumptions": [
    "CPI expected at 3.1%",
    "Fed maintains hawkish tone",
    "No major regulatory news"
  ],
  "confidence_factors": {
    "technical_alignment": 0.68,
    "macro_environment": 0.62,
    "catalyst_clarity": 0.58,
    "model_accuracy_recent": 0.71
  }
}
```


#### Example



**Code:**
```python
def analyze_prediction_error(prediction, actual_price):
    error_pct = (actual_price - prediction.weighted_forecast) / prediction.weighted_forecast * 100

    # Categorize error
    if error_pct < 5:
        category = "ACCURATE"
    elif error_pct < 10:
        category = "ACCEPTABLE"
    elif error_pct < 15:
        category = "MACRO_MISS"
    else:
        category = "EVENT_MISS"

    # Root cause analysis
    root_cause = identify_root_cause(prediction.key_assumptions, actual_events)

    return {
        "error_pct": error_pct,
        "category": category,
        "root_cause": root_cause,
        "learning": derive_learning(root_cause)
    }
```


#### Example



**Code:**
```bash
Prediction (Day 0):
  BTC: $47.4k weighted forecast, Confidence: 65%
  Key Assumption: "Fed stays hawkish until March"

Actual (Day 30):
  BTC price: $52.1k
  Error: +9.9% (ACCEPTABLE category)

What Actually Happened:
  - Fed signaled pivot earlier than expected
  - Banking crisis fears → Liquidity injection sooner
  - Bitcoin ETF inflows accelerated

Root Cause:
  Underestimated Fed pivot speed
  Missed: "Banking stress could trigger emergency pivot"

Learning Extracted:
  /remember solution
  - Problem: "Fed pivot speed underestimated in 65% confidence forecast"
  - Root Cause: "Focused on CPI data, missed banking stress signals"
  - Solution: "Add banking stress monitor to macro inputs"
  - Failed Approaches: "Relying solely on CPI for Fed pivot"
```


#### Example



**Code:**
```python
@dataclass
class PredictionError:
    type = "solution"
    problem: str         # "BTC forecast -9.9% due to Fed pivot"
    root_cause: str      # "Banking crisis triggered emergency pivot"
    solution: str        # "Add banking stress indicators to model"
    failed_approaches: list  # ["Relying on CPI only"]
    confidence: int      # 85% (how sure this will help)
    applicable_to: list  # ["Fed pivot forecasts", "Risk asset timing"]
```


#### Example



**Code:**
```bash
New Forecast Setup:
  - Fed hawkish stance expected
  - Banking stress rising
  - CPI coming next week

System detects: Similar to Jan 2025 prediction error

Auto-Suggest:
  "Last time Fed pivoted faster than expected.
   Current setup has banking stress again.
   → Increase pivot probability by 15%
   → Reduce confidence threshold by 10%"
```


#### Example



**Code:**
```python
def backtest_system(start_date, end_date):
    """
    Simulate: System was running for past 2 years
    Measure: What accuracy would it have achieved?
    """

    for date in date_range(start_date, end_date):
        # Get data available as of that date
        historical_data = get_data_until(date)

        # Generate forecast as if running live
        forecast = generate_forecast(historical_data)

        # 30 days later, get actual price
        actual = get_price_at(date + 30)

        # Compare
        error = calculate_error(forecast, actual)
        accuracy_metrics.append(error)

    return {
        "accuracy_within_5pct": 68.2,  # %
        "accuracy_within_10pct": 84.1,  # %
        "directional_accuracy": 72.3,  # % up/down correct
        "worst_case_drawdown": -24.5,  # % (bear case materialized)
        "best_case_return": +156,  # % (bull case + more)
        "sharpe_ratio": 1.42
    }
```


#### Example



**Code:**
```markdown
## Backtest Results (2023-2025)

Total Predictions: 730 (daily)

### Accuracy Metrics
- Within 5%: 68.2% (498/730)
- Within 10%: 84.1% (614/730)
- Directional: 72.3% (528/730)

### Performance by Market Regime
- Bull markets: 78.5% accuracy
- High liquidity: 81.2% accuracy
- Black swan events: 42.1% accuracy (expected)

### Model Adjustments Made (from experience memory)
1. +15% weight on SEC news (after XRP lawsuit impact)
2. +8% weight on banking stress (after SVB collapse)
3. -12% weight on Twitter sentiment (too noisy)
4. +20% weight on CPI shelter lag detection
```


#### Example



**Code:**
```python
# Tracked over time, adjusted if diverging

correlations = {
    "BTC_liquidity": 0.83,      # Historical: 83%
    "BTC_CPI": 0.42,            # Historical: 42%
    "Gold_RealYields": -0.82,   # Historical: -82%
    "BTC_FedBalance": 0.76      # Updated monthly
}

# If BTC_liquidity drops to 0.65 for 2 months → flag & adjust
```


#### Example



**Code:**
```python
# Technical analysis weights
technical_weights = {
    "RSI": 0.20,
    "MACD": 0.25,
    "MovingAverages": 0.25,
    "SupportResistance": 0.30
}

# If RSI consistently leads price moves → increase to 0.25
# If MACD fails during X events → decrease to 0.20
```


#### Example



**Code:**
```bash
_memory/experiences/exp-YYYY-NNN.json

Types stored:
- solution: Prediction failures + fixes
- pattern: Successfully identified patterns
- decision: Model parameter adjustments
- gotcha: Traps that led to errors
- workaround: Temporary fixes until permanent solution
```


#### Example



**Code:**
```bash
_memory/projects/macro-analyse.json

Updates:
- prediction_accuracy: Tracks monthly %
- known_failures: What causes model to fail
- recent_progress: What worked last month
- next_refinements: Planned improvements
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/learning-optimizer-agent.md`</small>
