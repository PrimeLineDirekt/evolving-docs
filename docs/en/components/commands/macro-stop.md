---
title: macro-stop
type: command
tags: []
lang: en
confidence: 100
---

# macro-stop


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
```yaml
project_path: /Users/neoforce/Buisiness/Projects/Macro-Analyse
backend_port: 8000
frontend_port: 3000
```


#### Example



**Code:**
```bash
kill -9 $(lsof -t -i :8000) 2>/dev/null
kill -9 $(lsof -t -i :3000) 2>/dev/null
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/macro-stop.md`</small>
