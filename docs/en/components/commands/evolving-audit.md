---
title: evolving-audit
type: command
tags: []
lang: en
confidence: 100
---

# evolving-audit


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

Maßgeschneiderter System-Audit für Evolving mit 5 spezialisierten Agents


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
$ARGUMENTS:
- --quick: Nur kritische Checks (Cross-Ref + Graph)
- --deep: Alle 5 Agents [default]
- --focus: Einzelner Agent
  - cross-ref: Cross-Reference Checker
  - graph: Knowledge Graph Validator
  - memory: Memory Schema Validator
  - detection: Detection Index Checker
  - hygiene: File Hygiene Auditor
  - all: Alle Agents [default]
```


#### Example



**Code:**
```markdown
## Pre-Flight Check

1. **Working Directory**: Evolving root?
2. **Core Files exist**:
   - [ ] _stats.json
   - [ ] .claude/detection-index.json
   - [ ] _graph/core-nodes.json
   - [ ] _memory/index.json

3. **Estimated Duration**:
   - Quick: ~5 min
   - Deep: ~15 min
```


#### Example



**Code:**
```bash
┌─────────────────────────────────────┐
│ BATCH 1 (PARALLEL)                  │
├──────────────────┬──────────────────┤
│ cross-reference- │ knowledge-graph- │
│ checker [Sonnet] │ validator [Sonnet]│
└──────────────────┴──────────────────┘
```


#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────┐
│ BATCH 1 (PARALLEL) - Core Integrity                 │
├─────────────────┬─────────────────┬─────────────────┤
│ cross-reference-│ knowledge-graph-│ file-hygiene-   │
│ checker [Sonnet]│ validator [Snnt]│ auditor [Haiku] │
└─────────────────┴─────────────────┴─────────────────┘

┌─────────────────────────────────────┐
│ BATCH 2 (PARALLEL) - Detail Checks  │
├──────────────────┬──────────────────┤
│ memory-schema-   │ detection-index- │
│ validator [Haiku]│ checker [Haiku]  │
└──────────────────┴──────────────────┘
```


#### Example



**Code:**
```markdown
## Audit Progress

**Mode**: Deep (5 Agents)

### Batch 1: Core Integrity
- [✓] cross-reference-checker (32s) - 12 issues
- [✓] knowledge-graph-validator (28s) - 8 issues
- [⏳] file-hygiene-auditor (running...)

### Batch 2: Detail Checks
- [ ] memory-schema-validator (pending)
- [ ] detection-index-checker (pending)

**Elapsed**: 1m 05s
```


#### Example



**Code:**
```bash
audit-reports/
├── evolving-audit-{date}.md      # Full detailed report
├── evolving-summary-{date}.md    # Executive summary
└── evolving-remediation-{date}.md # Action plan
```


#### Example



**Code:**
```markdown
# Evolving System Audit Complete ✓

## Health Scores

| Dimension | Score | Status |
|-----------|-------|--------|
| Cross-Reference Integrity | 72/100 | ⚠️ |
| Knowledge Graph Health | 85/100 | ✅ |
| Memory Schema Validity | 90/100 | ✅ |
| Detection Index Coverage | 78/100 | ⚠️ |
| File Hygiene | 65/100 | ⚠️ |
| **Overall System Health** | **78/100** | ⚠️ |

## Critical Findings (Immediate Action)

### 1. _stats.json is Single Point of Failure
- **Problem**: Outdated counts propagate to all docs
- **Evidence**: Commands: 63 actual vs 58 in stats
- **Fix**: Regenerate _stats.json from filesystem
- **Effort**: 5 minutes

### 2. Auto-Sync is NOT Automatic
- **Problem**: Hook only reminds, doesn't update
- **Evidence**: 15 sync reminders ignored
- **Fix**: Implement actual auto-update hooks
- **Effort**: 30 minutes

## Findings by Severity

| Severity | Count | Examples |
|----------|-------|----------|
| CRITICAL | 2 | _stats.json, Auto-Sync broken |
| HIGH | 8 | Count mismatches, Missing entries |
| MEDIUM | 15 | Orphan nodes, Stale backups |
| LOW | 12 | Minor inconsistencies |

## Quick Wins (< 30 min total)

1. **Regenerate _stats.json** (5 min)
   ```bash
   # Script to count actual files and update stats
   ```

2. **Delete 53 stale backups** (2 min)
   ```bash
   find _memory -name "*.backup_*" -mtime +7 -delete
   ```

3. **Remove 14 orphan edges** (5 min)
   - Edit _graph/edges.json
   - Remove edges with invalid targets

4. **Archive legacy graph files** (5 min)
   - Move nodes-legacy.json → _backup/
   - Move edges-legacy.json → _backup/

5. **Add 5 missing detection entries** (10 min)
   - /evolving-audit
   - [4 other new commands]

## Generated Reports

- 📄 `audit-reports/evolving-audit-2026-01-07.md`
- 📋 `audit-reports/evolving-summary-2026-01-07.md`
- 🛠️ `audit-reports/evolving-remediation-2026-01-07.md`

## Recommended Next Steps

1. **Immediate**: Run quick wins (30 min)
2. **Today**: Fix CRITICAL issues
3. **This Week**: Implement auto-sync hooks
4. **Follow-up**: Re-run `/evolving-audit --quick` in 7 days

---
Run `/audit-fix --evolving` for automated remediation
```


#### Example



**Code:**
```bash
Input:
- .claude/COMMANDS.md
- .claude/SYSTEM-MAP.md
- .claude/README.md
- _stats.json
- .claude/detection-index.json
- knowledge/index.md

Output:
- Count mismatches
- Orphan entries
- Broken references
- Auto-sync gaps
```


#### Example



**Code:**
```bash
Input:
- _graph/core-nodes.json
- _graph/knowledge-nodes.json
- _graph/edges.json
- _graph/nodes-legacy.json
- _stats.json

Output:
- Node count validation
- Orphan nodes/edges
- Legacy migration status
- Missing edges
```


#### Example



**Code:**
```bash
Input:
- _memory/projects/*.json
- _memory/experiences/exp-*.json
- _memory/projects/*.backup_*

Output:
- Schema violations
- Progress overflow
- Stale backups
- Expired experiences
```


#### Example



**Code:**
```bash
Input:
- .claude/detection-index.json
- .claude/commands/*.md
- .claude/COMMANDS.md
- _stats.json

Output:
- Coverage percentage
- Missing entries
- Orphan entries
- Duplicate keywords
```


#### Example



**Code:**
```bash
Input:
- .claude/**/*
- _graph/**/*
- _memory/**/*

Output:
- Overload files
- Legacy files
- Stale backups
- Duplicates
```


#### Example



**Code:**
```python
if agent.fails():
    if agent.is_critical():  # cross-ref, graph
        retry(max=2)
        if still_fails:
            partial_results_with_warning()
    else:  # memory, detection, hygiene
        skip_with_note()
        continue_other_agents()
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/evolving-audit.md`</small>
