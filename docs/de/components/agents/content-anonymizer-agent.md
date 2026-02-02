---
title: content-anonymizer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# content-anonymizer-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2026-01-04 |</div>


## What It Does

"Transforms personalized content into generic templates"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "file_path": "path to file to anonymize",
  "file_content": "original file content",
  "privacy_findings": "findings from Privacy Scanner Agent",
  "mode": "placeholder|example|remove",
  "manifest": "template-sync-manifest.json contents"
}
```


#### Example



**Code:**
```bash
"Robin" → "{USER}"
"Auswanderungs-KI" → "{PROJECT_NAME}"
"/Users/neoforce" → "{HOME}"
```


#### Example



**Code:**
```bash
"Robin" → "Alice"
"Auswanderungs-KI" → "My-Project"
"/Users/neoforce" → "/Users/your-username"
```


#### Example



**Code:**
```bash
"API_KEY=sk-xxx" → "[REMOVED]"
"password: secret123" → "[REMOVED]"
```


#### Example



**Code:**
```python
def load_rules(manifest):
    rules = []
    for item in manifest["anonymization"]["personal"]:
        rules.append(Rule(item["find"], item["replace"], "personal"))
    for item in manifest["anonymization"]["projects"]:
        rules.append(Rule(item["find"], item["replace"], "project"))
    return rules
```


#### Example



**Code:**
```python
def anonymize(content, rules, mode):
    result = content
    changelog = []

    for rule in rules:
        if rule.find in result:
            replacement = get_replacement(rule, mode)
            count = result.count(rule.find)
            result = result.replace(rule.find, replacement)
            changelog.append({
                "original": rule.find,
                "replacement": replacement,
                "count": count,
                "category": rule.category
            })

    return result, changelog
```


#### Example



**Code:**
```markdown
# Anonymization Report

## File: .claude/agents/example-agent.md

### Transformations Applied
| Original | Replacement | Count | Category |
|----------|-------------|-------|----------|
| Robin | {USER} | 3 | personal |
| Auswanderungs-KI | {PROJECT} | 2 | project |
| /Users/neoforce | {HOME} | 1 | path |

### Preview (first 30 lines)

#### Before:
```


#### Example



**Code:**
```bash

#### After:
```


#### Example



**Code:**
```bash

### Validation
- [x] Markdown syntax preserved
- [x] No broken links
- [x] All placeholders valid
- [ ] Review needed: Line 45 context unclear

### Changelog
```


#### Example



**Code:**
```json
// Before
{"user": "Robin", "project": "Auswanderungs-KI"}

// After
{"user": "{USER}", "project": "{PROJECT}"}
```


#### Example



**Code:**
```python
# Before
# Created by Robin for Auswanderungs-KI
def process(): pass

# After
# Created by {USER} for {PROJECT}
def process(): pass
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/content-anonymizer-agent.md`</small>
