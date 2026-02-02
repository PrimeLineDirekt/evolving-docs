---
title: recall
type: command
tags: []
lang: en
confidence: 100
---

# recall


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
{count} Experiences gefunden:

[{type}] {id} ({relevance_score}) - {summary}
  Tags: {tags}
  Created: {created}

[{type}] {id} ({relevance_score}) - {summary}
  Tags: {tags}
  Created: {created}

...
```


#### Example



**Code:**
```bash
/recall typescript error
→ 5 Experiences gefunden:
  [solution] exp-2025-001 (85) - TypeScript Property Error Fix
  [gotcha] exp-2025-012 (78) - useEffect async Trap
  ...

/recall --type solution
→ Alle Solutions sortiert nach Score

/recall --project dashboard --recent 7d
→ Dashboard-Experiences der letzten Woche

/recall react hooks
→ Alle Experiences zu React Hooks
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/recall.md`</small>
