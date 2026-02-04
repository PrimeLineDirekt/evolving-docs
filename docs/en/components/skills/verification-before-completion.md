---
title: Verification Before Completion
type: skill
tags: [quality, verification, testing]
lang: en
confidence: 95
---

# Verification Before Completion

![Verification Before Completion Skill](../../shared/assets/infographics/skills/verification-before-completion.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Ensure work is truly complete before claiming done |
| **Complexity** | Medium |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The Verification skill prevents premature completion claims. Before marking any task as done, it enforces a checklist of evidence requirements. No assumptions, no guessing, only verified facts.

## The Verification Checklist

| Check | Evidence Required |
|-------|-------------------|
| ✅ Tests Pass | `npm test` exit code 0 |
| ✅ Build Succeeds | `npm build` exit code 0 |
| ✅ No New Warnings | Linter output clean |
| ✅ Git Clean | No unexpected changes |

## Key Principles

- **Evidence Required** - Every claim needs proof
- **No Assumptions** - Don't assume it works
- **Verified Complete** - Run the actual checks
- **Never Claim Fixed** - Without running the test

## Anti-Patterns

❌ "I think that should work now"
❌ "The logic looks correct"
❌ "Based on my changes, this is fixed"

✅ "Tests pass: `npm test` returned 0"
✅ "Build succeeds: no errors in output"
✅ "Verified fix: reproduced issue, applied fix, confirmed resolved"

## Verification Flow

```
Code Complete
     │
     ▼
┌─────────────┐
│ Run Tests   │──→ Fail? → Fix first
└──────┬──────┘
       │ Pass
       ▼
┌─────────────┐
│ Run Build   │──→ Fail? → Fix first
└──────┬──────┘
       │ Pass
       ▼
┌─────────────┐
│ Check Lint  │──→ Warnings? → Fix first
└──────┬──────┘
       │ Clean
       ▼
   ✅ VERIFIED
```

## Usage

Applied automatically before marking tasks complete or claiming fixes.

## Related Skills

- [Systematic Debugging](systematic-debugging.md) - Find root cause first
- [Test-Driven Development](test-driven-development.md) - Tests prove behavior

---

<small>Source: `superpowers:verification-before-completion`</small>
