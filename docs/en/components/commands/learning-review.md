---
title: /learning-review
type: command
tags: []
lang: en
confidence: 100
---

# /learning-review


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Review system learning, accuracy metrics, and model performance. |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Reviews system learning accuracy by comparing predictions vs actual outcomes. Calculates accuracy metrics, analyzes error patterns, and tracks model refinements over time.

## System Impact

Reads prediction logs and experience memory to generate learning dashboards. Identifies improving/degrading patterns and suggests optimization areas.

## Architecture

Loads last 30 days of predictions, compares against actuals, calculates accuracy (within 5%, within 10%, directional), analyzes root causes of errors, reviews experience memory updates.

## Usage

Generates comprehensive learning dashboard with accuracy trends, error analysis, and model refinements.

### Examples

#### Basic Review







## Configuration

Uses Sonnet model. Timeframe and accuracy thresholds are configurable.

## Best Practices

- Run monthly to track improvement trends
- Compare predictions vs actuals systematically
- Document high-error patterns for learning
- Adjust model based on consistent errors
- Archive old predictions for historical analysis
- Use insights to refine future forecasting

## Related

- `/macro-forecast` - Generate predictions
- `/memory-stats` - Memory system health
- Experience memory system


---

<small>Source: `.claude/commands/learning-review.md`</small>
