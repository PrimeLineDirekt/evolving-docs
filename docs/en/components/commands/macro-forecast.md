---
title: /macro-forecast
type: command
tags: []
lang: en
confidence: 100
---

# /macro-forecast


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Generate 30-day probability-weighted forecast for BTC, Gold, XRP, etc. |
| **Complexity** | low |
| **Model** | claude-sonnet-4-5 |
| **Category** | workflow |</div>


## What It Does

Generates 30-day probability-weighted forecasts for BTC, Gold, XRP, etc. Provides bull/base/bear scenarios with catalysts, confidence levels, and key events to watch.

## System Impact

Accesses macro intelligence system for latest data. Creates forecast entries that can be backtested. Feeds into learning-review for accuracy tracking.

## Architecture

Pulls current market data, applies scenario analysis framework (bull/base/bear), weights by probability, identifies next catalysts, outputs structured forecast with confidence metrics.

## Usage

No arguments needed. Generates comprehensive 30-day outlook for tracked assets with scenarios and weighted predictions.

### Examples

#### Generate Forecast







## Configuration

Uses Sonnet model. Forecast timeframe and probability bands are configurable.

## Best Practices

- Use for strategic planning not trading signals
- Review underlying assumptions
- Track forecast accuracy over time
- Consider multiple scenarios
- Update forecasts as conditions change
- Not financial advice

## Related

- `/macro-start` - Start macro dashboard
- `/learning-review` - Track forecast accuracy
- Market analysis workflows


---

<small>Source: `.claude/commands/macro-forecast.md`</small>
