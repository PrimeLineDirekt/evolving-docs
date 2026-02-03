---
title: /review-plan
type: command
tags: []
lang: en
confidence: 100
---

# /review-plan


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Start Dual-Claude review for a plan through a skeptical "Staff Engineer Critic" |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | memory |</div>


## What It Does

Spawns a critical review agent (Staff Engineer persona) to challenge and improve a plan before execution.

## System Impact

Creates sub-agent with critical mindset. Reviews plan for gaps, risks, and improvements. Updates plan based on findings.

## Architecture




## Usage


### Examples

#### Usage





#### Examples







## Configuration



## Best Practices

- Use before executing complex plans
- Address critical findings before proceeding
- Iterate on plan based on review feedback
- Combine with interview-plan for comprehensive validation

## Related

- [`.claude/rules/domain-memory-bootup.md`](#.claude/rules/domain-memory-bootup.md) - Plan Mode Integration
- [`knowledge/patterns/interview-before-implement-pattern.md`](#knowledge/patterns/interview-before-implement-pattern.md) - Ähnliches Konzept


---

<small>Source: `.claude/commands/review-plan.md`</small>
