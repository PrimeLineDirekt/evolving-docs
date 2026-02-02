---
title: full-audit
type: command
tags: []
lang: en
confidence: 100
---

# full-audit


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

Umfassender Multi-Dimensions Projekt-Audit mit 8-10 spezialisierten Agents


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
$ARGUMENTS parsing:
- path: Projekt-Pfad (default: aktuelles Verzeichnis)
- --quick: Schneller Modus (5 Agents, ~5-8 Min)
- --deep: Tiefer Modus (8-10 Agents, ~10-15 Min) [default]
- --focus: security | quality | architecture | performance | documentation | all [default: all]
```


#### Example



**Code:**
```bash
"Welches Projekt soll ich auditieren?
- Aktuelles Verzeichnis: $(pwd)
- Oder gib einen Pfad an"
```


#### Example



**Code:**
```markdown
## Project Profile

**Pfad**: {path}
**Tech Stack**: {languages}, {frameworks}
**Complexity**: {score}/100
**Features**: {detected_features}

**Recommended Agents** ({count}):
{agent_list}

**Estimated Duration**: {min}-{max} minutes

Soll ich den Audit starten?
```


#### Example



**Code:**
```bash
┌─────────────────┬─────────────────┬─────────────────┐
│ security-       │ code-quality-   │ architecture-   │
│ auditor [Opus]  │ auditor [Sonnet]│ auditor [Opus]  │
└─────────────────┴─────────────────┴─────────────────┘
```


#### Example



**Code:**
```bash
┌─────────────────┬─────────────────┬─────────────────┐
│ performance-    │ documentation-  │ business-logic- │
│ auditor [Sonnet]│ auditor [Haiku] │ auditor [Opus]  │
└─────────────────┴─────────────────┴─────────────────┘
Conditions: has_database, always, has_requirements
```


#### Example



**Code:**
```bash
┌─────────────────┬─────────────────┐
│ prompt-auditor  │ api-routes-     │
│ [Sonnet]        │ auditor [Sonnet]│
└─────────────────┴─────────────────┘
Conditions: has_ai_integration, has_api_endpoints
```


#### Example



**Code:**
```markdown
## Audit Progress

**Phase 2**: Parallel Audits
- [✓] security-auditor (45s) - 2 CRITICAL, 5 HIGH
- [✓] code-quality-auditor (32s) - 0 CRITICAL, 8 HIGH
- [⏳] architecture-auditor (running...)
- [ ] performance-auditor (pending)
- [ ] documentation-auditor (pending)

**Elapsed**: 1m 15s
```


#### Example



**Code:**
```bash
{project}/audit-reports/
├── audit-report-{date}.md      # Full detailed report
├── audit-summary-{date}.md     # Executive summary
└── remediation-roadmap-{date}.md  # Action plan
```


#### Example



**Code:**
```markdown
# Audit Complete ✓

## Health Score: {score}/100 {emoji}

### Findings Summary
| Severity | Count |
|----------|-------|
| CRITICAL | {n} |
| HIGH | {n} |
| MEDIUM | {n} |
| LOW | {n} |

### Top 5 Issues
1. {issue_1} - {severity} - {file}
2. {issue_2} - {severity} - {file}
...

### Quick Wins (< 1 Day)
1. {quick_win_1}
2. {quick_win_2}

### Generated Reports
- audit-report-{date}.md
- audit-summary-{date}.md
- remediation-roadmap-{date}.md

### Next Steps
1. Review CRITICAL issues immediately
2. Run `/audit-fix` for automated fixes
3. Schedule follow-up audit: {date + 2 weeks}
```


#### Example



**Code:**
```python
if agent.priority == "critical":
    retry(agent, max_attempts=2)
    if still_failed:
        abort_with_partial_results()
elif agent.priority == "high":
    retry(agent, max_attempts=1)
    if still_failed:
        continue_with_warning()
else:
    skip_gracefully()
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/full-audit.md`</small>
