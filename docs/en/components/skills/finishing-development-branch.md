---
title: Finishing Development Branch
type: skill
tags: [git, workflow, completion]
lang: en
confidence: 95
---

# Finishing Development Branch

![Finishing Development Branch Skill](../../shared/assets/infographics/skills/finishing-development-branch.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Complete feature branches with clean history |
| **Complexity** | Medium |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

The Finishing Branch skill handles the completion of feature branches: final review, merge strategy decision (squash vs merge), PR creation, and cleanup. It ensures clean git history and proper branch hygiene.

## Completion Workflow

### 1. Final Review
- Run code-reviewer agent
- Fix any remaining issues
- Ensure all tests pass

### 2. Squash Decision

| Strategy | When to Use |
|----------|-------------|
| **Squash** | Many small commits, WIP commits, messy history |
| **Merge** | Important commit history, co-authored work |

### 3. Create PR
- Clear title and description
- Link related issues
- Request reviewers

### 4. Cleanup
```bash
# After merge
git branch -d feature/name
git worktree remove ../feature-name  # if using worktrees
```

## Decision Tree

```
Feature Complete?
     │
     ├─ No → Keep working
     │
     └─ Yes → Final Review
              │
              └─ Clean? → Squash or Merge?
                          │
                          ├─ Squash → Single commit
                          │
                          └─ Merge → Preserve history
                                    │
                                    └─ Create PR → Cleanup
```

## Key Principles

- **Clean History** - Squash WIP commits
- **Proper Cleanup** - Delete merged branches
- **Final Validation** - Review before merge

## Usage

```
/finishing-a-development-branch
```

## Related Skills

- [Git Worktrees](using-git-worktrees.md) - Create the branch
- [Code Review](code-review.md) - Final review process

---

<small>Source: `superpowers:finishing-a-development-branch`</small>
