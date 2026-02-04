---
title: Writing Skills
type: skill
tags: [meta, creation, workflow]
lang: en
confidence: 95
---

# Writing Skills

![Writing Skills Skill](../../shared/assets/infographics/skills/writing-skills.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Create reusable skill files for workflows |
| **Complexity** | Medium |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The Writing Skills skill helps create new skill files that capture reusable workflows. Skills are loaded on-demand when invoked, providing contextual guidance without bloating the base context.

## Skill File Anatomy

```yaml
---
name: skill-name
description: "When to use this skill"
model: sonnet  # optional: haiku, sonnet, opus
---

# Skill Title

## Overview
What this skill does

## The Process
Step-by-step workflow

## Key Principles
Core guidelines

## Usage
How to invoke
```

## Skill Lifecycle

| Phase | Description |
|-------|-------------|
| **Draft** | Create skill file |
| **Test** | Invoke and verify behavior |
| **Deploy** | Move to skills directory |
| **Maintain** | Update as needed |

## Key Principles

- **Reusable Workflows** - Capture repeatable processes
- **Contextual Loading** - Only loaded when invoked
- **Model Selection** - Choose appropriate model for complexity
- **Clear Triggers** - Description explains when to use

## Skill Location

```
.claude/skills/
├── plugin-name/
│   └── skill-name/
│       └── skill.md
```

## Usage

```
/writing-skills
```

## Related Skills

- [Brainstorming](brainstorming.md) - Design the skill workflow first
- [Verification Before Completion](verification-before-completion.md) - Test before deploying

---

<small>Source: `superpowers:writing-skills`</small>
