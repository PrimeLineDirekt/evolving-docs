---
title: /repo-screen
type: command
tags: []
lang: en
confidence: 100
---

# /repo-screen


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Quick relevance check for GitHub repos before deep analysis |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | workflow |</div>


## What It Does

Performs fast screening of GitHub repositories to assess relevance, quality, and value before committing to full analysis.

## System Impact

Reads repo metadata, README, and structure. Provides relevance score and recommendation.

## Architecture

Fetches README + repo structure remotely (no clone), checks for .claude/, MCP, agents, skills indicators, calculates relevance score 0-10, outputs recommendation.

## Usage

Pass GitHub URL. Returns relevance score and recommendation whether to proceed with full /analyze-repo.

### Examples

#### Screen Repository







## Configuration



## Best Practices

- Screen before deep analysis to save time
- Check stars, activity, and maintenance status
- Review dependencies for compatibility

## Related


---

<small>Source: `.claude/commands/repo-screen.md`</small>
