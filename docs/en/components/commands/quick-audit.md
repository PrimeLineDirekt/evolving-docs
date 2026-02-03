---
title: /quick-audit
type: command
tags: []
lang: en
confidence: 100
---

# /quick-audit


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Fast project audit with the top 5 essential agents |
| **Complexity** | low |
| **Model** | sonnet |
| **Category** | analysis |</div>


## What It Does

Schneller Security & Quality Check mit 5 Core-Agents (5-8 Minuten)


## System Impact

Runs 5 core audit agents in parallel. Completes in 5-8 minutes. Produces security and quality findings.

## Architecture

Parallel agent execution for fast results. Covers critical security, code quality, and architectural concerns.

## Usage


### Examples

#### Basic Usage



**Code:**
```bash
/quick-audit
```




## Configuration



## Best Practices

- Run before deployments or major releases
- Use as first pass before full audit
- Address critical findings immediately
- Follow up with full-audit for comprehensive coverage

## Related

- [`/full-audit`](#full-audit) - Vollständiger Deep Audit
- [`/audit-security`](#audit-security) - Nur Security Focus


---

<small>Source: `.claude/commands/quick-audit.md`</small>
