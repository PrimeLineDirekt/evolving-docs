---
title: Test-Driven Development
type: skill
tags: [testing, tdd, quality]
lang: en
confidence: 95
---

# Test-Driven Development

![Test-Driven Development Skill](../../shared/assets/infographics/skills/test-driven-development.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Implement features using the Red-Green-Refactor cycle |
| **Complexity** | Medium |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The TDD skill enforces disciplined test-first development. Write a failing test first, then write minimal code to make it pass, then refactor. This cycle ensures every feature has test coverage and keeps the codebase clean.

## The Red-Green-Refactor Cycle

### 1. RED - Write Failing Test
- Write a test that describes the desired behavior
- Run the test - it should FAIL
- If it passes, the test is wrong or feature already exists

### 2. GREEN - Make It Pass
- Write the **minimum** code to make the test pass
- Don't over-engineer or add extra features
- Just make the red turn green

### 3. REFACTOR - Clean Up
- Improve code structure while keeping tests green
- Remove duplication
- Improve naming and readability

## Test Pyramid

| Level | Count | Speed | Scope |
|-------|-------|-------|-------|
| **Unit** | Many | Fast | Single function/class |
| **Integration** | Some | Medium | Component interactions |
| **E2E** | Few | Slow | Full user flows |

## Key Principles

- **Fail First** - Never write implementation before a failing test
- **Minimal Code** - Only write what's needed to pass
- **Small Steps** - One test at a time
- **Continuous Refactoring** - Keep code clean as you go

## Usage

```
/test-driven-development
```

Or trigger naturally when implementing features.

## Related Skills

- [Systematic Debugging](systematic-debugging.md) - When tests fail unexpectedly
- [Verification Before Completion](verification-before-completion.md) - Ensure all tests pass

---

<small>Source: `superpowers:test-driven-development`</small>
