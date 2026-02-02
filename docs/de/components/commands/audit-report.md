---
title: audit-report
type: command
tags: []
lang: en
confidence: 100
---

# audit-report


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

Generiere Audit-Report aus vorherigen Audit-Ergebnissen


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
$ARGUMENTS:
- --format: md | html | json [default: md]
- --type: summary | detailed | roadmap | all [default: all]
- --from: audit-id oder "latest" [default: latest]
```


#### Example



**Code:**
```python
# Suche nach Audit-Ergebnissen
audit_data_locations = [
    ".audit/",
    "audit-reports/",
    "_audit-cache/"
]

if no_audit_data_found:
    "Keine Audit-Daten gefunden.
     Führe zuerst `/full-audit` oder `/quick-audit` aus."
    return
```


#### Example



**Code:**
```markdown
## Generating Report

**Source**: {audit_id}
**Date**: {original_audit_date}
**Format**: {format}
**Type**: {type}

Generating...
```


#### Example



**Code:**
```markdown
# Audit Report: {project}
[Full markdown report]
```


#### Example



**Code:**
```html
<!DOCTYPE html>
<html>
<head><title>Audit Report</title></head>
<body>
  <h1>Audit Report: {project}</h1>
  <!-- Styled report -->
</body>
</html>
```


#### Example



**Code:**
```json
{
  "audit_id": "audit-2026-01-06",
  "project": "project-name",
  "scores": { ... },
  "findings": [ ... ],
  "recommendations": [ ... ]
}
```


#### Example



**Code:**
```markdown
## Report Generated

**Format**: {format}
**Type**: {type}

### Generated Files:
- audit-summary-{date}.{ext}
- audit-detailed-{date}.{ext}
- remediation-roadmap-{date}.{ext}

### Quick Stats:
- Health Score: {score}/100
- CRITICAL: {n}
- HIGH: {n}

Open report? [Y/n]
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/audit-report.md`</small>
