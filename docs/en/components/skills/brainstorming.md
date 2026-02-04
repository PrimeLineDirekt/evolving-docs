---
title: Brainstorming
type: skill
tags: [creative, design, planning]
lang: en
confidence: 95
---

# Brainstorming

![Brainstorming Skill](../../shared/assets/infographics/skills/brainstorming.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Turn ideas into fully formed designs through collaborative dialogue |
| **Complexity** | Medium |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The Brainstorming skill transforms vague ideas into concrete, validated designs through structured dialogue. It uses a collaborative approach with one question at a time, multiple choice options where possible, and incremental validation of design sections.

## Key Principles

- **One question at a time** - Don't overwhelm with multiple questions
- **Multiple choice preferred** - Easier to answer than open-ended when possible
- **YAGNI ruthlessly** - Remove unnecessary features from all designs
- **Explore alternatives** - Always propose 2-3 approaches before settling
- **Incremental validation** - Present design in sections, validate each

## The Process

### 1. Understanding the Idea
- Check current project state (files, docs, recent commits)
- Ask questions one at a time to refine the idea
- Focus on: purpose, constraints, success criteria

### 2. Exploring Approaches
- Propose 2-3 different approaches with trade-offs
- Lead with recommended option and explain why
- Present options conversationally

### 3. Presenting the Design
- Break design into sections of 200-300 words
- Ask after each section whether it looks right
- Cover: architecture, components, data flow, error handling, testing

## Usage

```
/brainstorming
```

Or naturally trigger with phrases like:
- "I have an idea for..."
- "Help me design..."
- "Let's brainstorm..."

## Output

After validation, the skill:
1. Writes design to `docs/plans/YYYY-MM-DD-<topic>-design.md`
2. Commits the design document to git
3. Optionally continues to implementation with worktrees and plans

## Related Skills

- [Writing Plans](writing-plans.md) - Create implementation plans from designs
- [Executing Plans](executing-plans.md) - Execute the implementation
- [Git Worktrees](using-git-worktrees.md) - Isolated workspace for implementation

---

<small>Source: `superpowers:brainstorming`</small>
