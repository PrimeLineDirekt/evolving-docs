---
title: Systematic Debugging
type: skill
tags: [debugging, troubleshooting, quality]
lang: en
confidence: 95
---

# Systematic Debugging

![Systematic Debugging Skill](../../shared/assets/infographics/skills/systematic-debugging.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Scientific approach to finding and fixing bugs |
| **Complexity** | High |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The Systematic Debugging skill applies scientific method to bug hunting. No guessing, no shotgun debugging. Observe, hypothesize, test, verify. Every fix must be backed by evidence.

## The Scientific Debugging Process

### 1. OBSERVE
- Read error messages and stack traces
- Check logs and git diffs
- Understand what's actually happening vs. expected

### 2. HYPOTHESIZE
- Form a specific, testable hypothesis
- "The bug occurs because X when Y happens"
- Write it down before testing

### 3. TEST
- Design experiments to prove/disprove hypothesis
- Add logging, use debugger, write test cases
- Gather evidence

### 4. VERIFY
- Confirm the fix actually works
- Run full test suite
- Check for regression

## The 3-Strike Rule

| Attempt | Action |
|---------|--------|
| **1-2** | Self-fix with evidence |
| **3** | **STOP** - Spawn sub-agents for analysis |
| **4** | Escalate to user with findings |

## Key Principles

- **Evidence Before Claims** - Never claim "fixed" without proof
- **No Guessing** - Every change must have reasoning
- **Binary Search** - Narrow down systematically
- **Fresh Eyes** - Sub-agents bring new perspective

## Usage

```
/systematic-debugging
```

Or trigger when encountering bugs, test failures, or unexpected behavior.

## Related Skills

- [Verification Before Completion](verification-before-completion.md) - Ensure fixes are verified
- [Dispatching Parallel Agents](dispatching-parallel-agents.md) - Get fresh perspective

---

<small>Source: `superpowers:systematic-debugging`</small>
