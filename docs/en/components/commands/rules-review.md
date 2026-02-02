---
title: rules-review
type: command
tags: []
lang: en
confidence: 100
---

# rules-review


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

"--force, --all, --status=CANDIDATE|TRIAL|STABLE"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
/rules-review [ACTION] [RULE_ID] [FLAGS]
```


#### Example



**Code:**
```bash
STAGING RULES OVERVIEW
═════════════════════════════════════════════════════════════

Status Summary:
  CANDIDATE  3 rules  (0-2 applications)
  TRIAL      2 rules  (3-5 applications)
  STABLE     1 rule   (6+ applications)
  ─────────────────────────────────────────────────
  TOTAL      6 staged rules

Rules by Status:
─────────────────────────────────────────────────────────────

┌─ CANDIDATE ──────────────────────────────────────────────┐
│                                                          │
│ ID: delegation-0115                                     │
│ Title: Parallel Task Delegation                         │
│ Created: 2026-01-15  |  Age: 17 days                    │
│ Metrics:                                                │
│   Applied: 3 times | Success: 3/3 (100%) | Failure: 0  │
│ Confidence: 92%                                         │
│ Next Step: → Promote to TRIAL (threshold 3 met)        │
│                                                          │
│ Status: CANDIDATE  |  Ready for: Promotion             │
│                                                          │
└──────────────────────────────────────────────────────────┘

┌─ TRIAL ───────────────────────────────────────────────────┐
│                                                           │
│ ID: context-scout-0108                                  │
│ Title: Adaptive Context Loading                         │
│ Created: 2026-01-08  |  Age: 24 days                    │
│ Metrics:                                                │
│   Applied: 8 times | Success: 7/8 (87%) | Failure: 1   │
│ Confidence: 87%                                         │
│ Next Step: → Monitor for 2 more cycles                  │
│                                                          │
│ Status: TRIAL  |  Ready for: Promotion (if stable)     │
│                                                          │
└──────────────────────────────────────────────────────────┘

┌─ STABLE ───────────────────────────────────────────────────┐
│                                                           │
│ ID: hook-validation-0101                                │
│ Title: Hook Execution Validation                        │
│ Created: 2025-12-20  |  Age: 42 days                    │
│ Metrics:                                                │
│   Applied: 23 times | Success: 22/23 (96%) | Failure: 1 │
│ Confidence: 94%                                         │
│ Next Step: → Promote to Production (ready!)             │
│                                                          │
│ Status: STABLE  |  Ready for: Finalization              │
│                                                          │
└──────────────────────────────────────────────────────────┘

Available Commands:
  /rules-review list                  # Show all (or current view)
  /rules-review list --status=STABLE  # Show only stable rules
  /rules-review promote delegation-0115
  /rules-review archive context-router-old
  /rules-review edit delegation-0115
  /rules-review stats
```


#### Example



**Code:**
```bash
/rules-review promote delegation-0115
```


#### Example



**Code:**
```bash
CANDIDATE (0-2 apps)
    ↓
TRIAL (3-5 apps)
    ↓
STABLE (6+ apps)
    ↓
PRODUCTION (knowledge/rules/{category}/)
```


#### Example



**Code:**
```bash
PROMOTING RULE
═════════════════════════════════════════════════════════════

Rule: delegation-0115 "Parallel Task Delegation"
Current Status: CANDIDATE (3 applications)
Target Status: TRIAL

Pre-Promotion Validation:
  ✓ Success Rate: 100% (3/3 applications)
  ✓ Confidence: 92%
  ✓ Age: 17 days (threshold: 3 days for CANDIDATE)
  ✓ No critical failures
  ✓ All validation checks passed

Target Location:
  knowledge/rules/delegation/parallel-task-delegation.md

Proceed with promotion? (Y/N)
[With --force flag, automatically proceeds]

→ Promotes rule to TRIAL status
→ Updates knowledge/rules/staging/_index.json
→ Logs promotion in system audit
```


#### Example



**Code:**
```bash
/rules-review archive context-router-old
```


#### Example



**Code:**
```bash
ARCHIVING RULE
═════════════════════════════════════════════════════════════

Rule: context-router-old
Status: CANDIDATE
Reason: Low success rate (25%)

Archive Details:
  From: knowledge/rules/staging/context-router-old.md
  To: _archive/rules/unused/context-router-old-20260201.md
  Timestamp: 2026-02-01T22:45:00Z

Archive Entry:
  - Rule content preserved
  - Metadata recorded (created, archived, reason)
  - Removed from staging index

Proceed with archival? (Y/N)
[With --force flag, automatically proceeds]

→ Archives rule to _archive/
→ Removes from knowledge/rules/staging/
→ Updates _index.json
```


#### Example



**Code:**
```bash
/rules-review edit delegation-0115
```


#### Example



**Code:**
```bash
EDITING RULE
═════════════════════════════════════════════════════════════

Rule: delegation-0115
File: knowledge/rules/staging/delegation-0115.md

Opening in editor...
[User edits file]

Changes detected:
  ✓ Content updated
  ✓ Frontmatter valid
  ✓ No conflicts

Updating metadata:
  - last_modified: 2026-02-01T22:45:00Z
  - last_editor: robin
  - edit_count: 5

Updated rule saved.
```


#### Example



**Code:**
```bash
/rules-review stats
```


#### Example



**Code:**
```bash
STAGING SYSTEM STATISTICS
═════════════════════════════════════════════════════════════

Overall Metrics:
  Total Staged: 6 rules
  Promoted (Lifetime): 12 rules
  Archived (Lifetime): 4 rules
  Success Rate: 85% (avg across all rules)

Distribution by Status:
  CANDIDATE  50% (3 rules)  ▓▓▓░░░░░░░
  TRIAL      33% (2 rules)  ▓▓░░░░░░░░
  STABLE     17% (1 rule)   ▓░░░░░░░░░

Age Distribution:
  < 7 days:    1 rule   (new)
  7-30 days:   3 rules  (active)
  30+ days:    2 rules  (mature)

Performance Metrics:
  Average Success Rate:   87%
  Average Confidence:     89%
  Average Time to Stable: 28 days

Top Candidates for Promotion:
  1. hook-validation-0101     (STABLE, 96% success)
  2. context-scout-0108       (TRIAL, 87% success)
  3. delegation-0115          (CANDIDATE, 100% success)

Recently Added:
  • delegation-0115          (17 days old)
  • task-persistence-0118    (9 days old)

At Risk (Low Success Rate):
  • (none currently)

System Configuration:
  Promotion Threshold: 3 applications
  Failure Threshold: 2 failures
  Decay Rate: 0.01/day
  Archive Days: 30
  Min Confidence: 60%
```


#### Example



**Code:**
```bash
/rules-review list delegation-0115
```


#### Example



**Code:**
```bash
RULE DETAILS
═════════════════════════════════════════════════════════════

Basic Info:
  ID: delegation-0115
  Title: Parallel Task Delegation
  Category: delegation
  Created: 2026-01-15 by robin
  Status: CANDIDATE

Content Preview:
  (First 500 chars of rule)
  ---
  Rule für automatische Delegation bei Score >= 3...
  ...

Validation Metrics:
  Applied: 3 times
  Success: 3/3 (100%)
  Failure: 0
  Success Rate: 100%
  Confidence: 92%
  Decay Score: 0.92

Timeline:
  Created: 2026-01-15T14:20:00Z (17 days ago)
  Last Applied: 2026-02-01T10:30:00Z (2 hours ago)
  Modification Count: 2

Related Rules:
  • auto-delegation (similar domain)
  • task-orchestration (related)

Promotion History:
  - CANDIDATE: Applied 3 times, 100% success
  - Ready for: TRIAL promotion

Actions:
  /rules-review promote delegation-0115
  /rules-review edit delegation-0115
  /rules-review archive delegation-0115
```


#### Example



**Code:**
```bash
# Nach Status filtern
/rules-review list --status=STABLE

# Alle inkl. archivierter
/rules-review list --all

# Mit Dry-Run vor Aktion
/rules-review promote --dry-run delegation-0115
```


#### Example



**Code:**
```yaml
---
name: rule-name
status: archived
archived_date: 2026-02-01
archived_reason: "Low success rate"
original_status: CANDIDATE
total_applications: 2
success_rate: 25
---
```


#### Example



**Code:**
```bash
/rules-review promote delegation-0115

✓ Validation passed
✓ Rule promoted: CANDIDATE → TRIAL
✓ Updated _index.json
✓ Logged in audit trail

Next steps:
  Monitor rule application
  Check back in 2-3 days
  /rules-review list delegation-0115 (for updated metrics)
```


#### Example



**Code:**
```bash
/rules-review list --status=STABLE

3 stable rules ready for production promotion:
  1. hook-validation-0101 (96% success, 23 applications)
  2. observation-order-0103 (91% success, 17 applications)
  3. context-budget-0110 (88% success, 12 applications)

Next: /rules-review promote hook-validation-0101
```


#### Example



**Code:**
```bash
/rules-review archive context-router-old

✓ Archived to: _archive/rules/unused/context-router-old-20260201.md
✓ Removed from staging
✓ Updated index

This rule can be restored later if needed.
```


#### Example



**Code:**
```bash
python3 "$CLAUDE_PROJECT_DIR"/.claude/hooks/rules-review.py \
  --action ${action:-list} \
  ${rule_id:+--rule_id "$rule_id"} \
  ${flags}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/rules-review.md`</small>
