---
title: /review
type: command
tags: []
lang: en
confidence: 100
---

# /review


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Manual Spaced Repetition Review - review due learnings |
| **Complexity** | high |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Triggers manual spaced repetition review cycle. Presents due experiences, rules, and learnings for reinforcement.

## System Impact

Reads spaced repetition schedule, presents due items, updates intervals based on user responses.

## Architecture




## Usage


### Examples

#### Usage







## Configuration



## Best Practices

- Review regularly to maintain knowledge retention
- Use confirm/skip actions to adjust intervals
- Practice active recall for better learning

## Related

- [`knowledge/patterns/spaced-repetition-pattern.md`](#knowledge/patterns/spaced-repetition-pattern.md) - Algorithmus
- [`_memory/experiences/SCHEMA.md`](#_memory/experiences/schema.md) - Experience Schema v2.1
- [`knowledge/rules/staging/_index.json`](#knowledge/rules/staging/_index.json) - Staged Rules
- [`.claude/rules/domain-memory-bootup.md`](#.claude/rules/domain-memory-bootup.md) - Auto-Review bei Start


---

<small>Source: `.claude/commands/review.md`</small>
