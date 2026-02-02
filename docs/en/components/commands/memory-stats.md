---
title: memory-stats
type: command
tags: []
lang: en
confidence: 100
---

# memory-stats


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | commands |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Experience Memory Stats
=======================

Total: {count} Experiences
  - Solutions: {types.solution}
  - Patterns: {types.pattern}
  - Decisions: {types.decision}
  - Workarounds: {types.workaround}
  - Gotchas: {types.gotcha}
  - Preferences: {types.preference}

Scores:
  - Average: {avg_score}
  - Highest: {max_score} ({max_id})
  - Lowest: {min_score} ({min_id})

Most Accessed:
  - {most_accessed_id} ({access_count}x) - {summary}

Top Tags:
  1. {tag1} ({count1})
  2. {tag2} ({count2})
  ...

Cleanup Pending:
  - {cleanup_count} Experiences mit Score < 30
  - Naechster Cleanup: {next_cleanup_date}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/memory-stats.md`</small>
