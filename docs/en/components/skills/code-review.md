---
title: Code Review
type: skill
tags: [review, quality, collaboration]
lang: en
confidence: 95
---

# Code Review

![Code Review Skill](../../shared/assets/infographics/skills/code-review.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Request and receive code reviews effectively |
| **Complexity** | Medium |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The Code Review skill covers both requesting reviews (preparing your code for review) and receiving reviews (responding to feedback). It ensures reviews are actionable, confidence-filtered, and focused on what matters.

## Requesting Code Review

### Preparation Checklist
- [ ] Tests pass
- [ ] Build succeeds
- [ ] Self-review completed
- [ ] Clear PR description

### What Reviewers Check
| Area | Focus |
|------|-------|
| **Conventions** | Project style guide adherence |
| **Bugs** | Logic errors, edge cases |
| **Security** | Vulnerabilities, data exposure |
| **Performance** | Bottlenecks, inefficiencies |

## Receiving Code Review

### Response Guidelines
- Address all comments
- Ask for clarification if needed
- Don't take feedback personally
- Thank reviewers for their time

### Confidence Filtering
Only issues with **>70% confidence** are reported. This reduces noise and focuses on real problems.

## Proactive Reviews

Reviews are triggered automatically:
- After completing todo lists with code
- Before creating PRs
- At phase boundaries in plans

## Review Agents

| Agent | Purpose |
|-------|---------|
| `code-reviewer` | General code quality |
| `type-design-analyzer` | Type system design |
| `silent-failure-hunter` | Error handling gaps |
| `comment-analyzer` | Documentation quality |

## Usage

```
/requesting-code-review
/receiving-code-review
```

## Related Skills

- [Verification Before Completion](verification-before-completion.md) - Pre-review checks
- [Finishing Development Branch](finishing-development-branch.md) - After review approval

---

<small>Source: `superpowers:requesting-code-review`, `superpowers:receiving-code-review`</small>
