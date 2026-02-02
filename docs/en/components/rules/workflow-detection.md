---
title: workflow-detection
type: rule
tags: []
lang: en
confidence: 100
---

# workflow-detection


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
User: "Ich habe eine neue Idee"
→ Confidence 9 → "Soll ich /idea-new nutzen?"

User: "Zeig mir meine Ideen"
→ Confidence 10 → "Soll ich /idea-list nutzen?"

User: "Ich muss mal schauen..."
→ Confidence 2 → Normal antworten
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/rules/workflow-detection.md`</small>
