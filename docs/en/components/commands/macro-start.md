---
title: /macro-start
type: command
tags: []
lang: en
confidence: 100
---

# /macro-start


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Starts complete macro analysis dashboard (backend + frontend) |
| **Complexity** | low |
| **Model** | claude-sonnet-4-5 |
| **Category** | documentation |</div>


## What It Does

Starts the complete macro analysis dashboard. Launches backend services and frontend interface for market analysis and monitoring.


## System Impact

- Starts backend services on configured ports
- Launches frontend in browser
- Requires dependencies installed
- Runs in background until stopped


## Architecture

Uses Sonnet for service orchestration. Implements startup sequence with health checks and dependency validation.


## Usage

Run without arguments to start full dashboard stack.

### Examples

#### Basic Usage



**Code:**
```bash
/macro-start
```




## Configuration

Uses Sonnet model. Service ports and configurations are set in project config.

## Best Practices

- Verify dependencies before starting
- Check port availability
- Monitor startup logs for errors
- Use `/macro-stop` for clean shutdown
- Access dashboard after services ready
- Keep services running during analysis

## Related

- `/macro-stop` - Stop dashboard
- `/macro-forecast` - Generate forecasts


---

<small>Source: `.claude/commands/macro-start.md`</small>
