---
title: Using Git Worktrees
type: skill
tags: [git, isolation, workflow]
lang: en
confidence: 95
---

# Using Git Worktrees

![Git Worktrees Skill](../../shared/assets/infographics/skills/using-git-worktrees.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Create isolated workspaces for feature development |
| **Complexity** | Medium |
| **Model** | sonnet |
| **Plugin** | superpowers |
</div>

## What It Does

Git worktrees allow multiple working directories from a single repository. Each worktree can be on a different branch, enabling parallel feature development without stashing or context switching.

## Benefits

| Benefit | Description |
|---------|-------------|
| **No Stash Needed** | Keep work in progress while switching |
| **Parallel Features** | Work on multiple features simultaneously |
| **Clean Context** | Each worktree is completely isolated |
| **Zero Conflicts** | No accidental cross-contamination |

## Workflow

### 1. Create Worktree
```bash
git worktree add ../feature-auth -b feature/auth
```

### 2. Work in Isolation
- Make changes in the worktree directory
- Commit as normal
- No impact on main worktree

### 3. Merge Back
```bash
cd ../main-repo
git merge feature/auth
```

### 4. Cleanup
```bash
git worktree remove ../feature-auth
git branch -d feature/auth
```

## When to Use

- Starting a new feature that might take multiple sessions
- Need to quickly fix something on main while working on feature
- Want to compare behavior between branches
- Running tests on one branch while developing on another

## Key Principles

- **Branch Isolation** - Each worktree = one branch
- **Shared History** - All worktrees share git objects
- **Independent State** - Staged changes don't cross worktrees

## Usage

```
/using-git-worktrees
```

## Related Skills

- [Finishing Development Branch](finishing-development-branch.md) - Complete the branch
- [Brainstorming](brainstorming.md) - Design before creating worktree

---

<small>Source: `superpowers:using-git-worktrees`</small>
