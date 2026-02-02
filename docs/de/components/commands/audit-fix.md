---
title: audit-fix
type: command
tags: []
lang: en
confidence: 100
---

# audit-fix


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

Führe Audit-Remediation durch mit dynamischem Fixer-Team


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
$ARGUMENTS parsing:
- audit-report: Pfad zum Audit-Report (default: letzter Report in audit-reports/)
- --dry-run: Nur Plan zeigen, keine Änderungen
- --category: security|code_quality|architecture|performance|documentation|api|tests|config
- --severity: CRITICAL|HIGH|MEDIUM|LOW (minimum severity)
- --max-fixers: Maximale Team-Größe (default: 5)
```


#### Example



**Code:**
```bash
# Suche letzten Audit-Report
ls -t audit-reports/audit-report-*.md | head -1

# Oder im Projekt-Root
ls -t *audit*.md | head -1
```


#### Example



**Code:**
```bash
# Lies vorherige Failure-Logs für Kontext
cat .audit-fix/*/failures.json 2>/dev/null
```


#### Example



**Code:**
```markdown
## Audit Report Analysis

**Source**: audit-report-2026-01-06.md
**Total Findings**: 23
**Previous Failures**: 2 (will inform fixers)

### Findings by Category
| Category | CRIT | HIGH | MED | LOW | Total |
|----------|------|------|-----|-----|-------|
| Security | 2 | 3 | 0 | 0 | 5 |
| Code Quality | 0 | 4 | 6 | 2 | 12 |
| Performance | 0 | 1 | 3 | 0 | 4 |
| Documentation | 0 | 0 | 1 | 1 | 2 |
```


#### Example



**Code:**
```python
CATEGORY_TRAITS = {
    "security":      ("security",       "cautious", "remediation", "opus",   "LOW"),
    "code_quality":  ("engineer",       "precise",  "remediation", "sonnet", "MEDIUM"),
    "architecture":  ("architect",      "cautious", "remediation", "opus",   "LOW"),
    "performance":   ("engineer",       "direct",   "remediation", "sonnet", "MEDIUM"),
    "documentation": ("communications", "direct",   "remediation", "haiku",  "HIGH"),
    "api":           ("engineer",       "precise",  "remediation", "sonnet", "MEDIUM"),
    "tests":         ("engineer",       "thorough", "remediation", "sonnet", "MEDIUM"),
    "config":        ("engineer",       "direct",   "remediation", "haiku",  "HIGH"),
}
```


#### Example



**Code:**
```markdown
## Fixer Team Composition

**Team Size**: 4 fixers (max 5)
**Estimated Duration**: 20-30 minutes

| # | Category | Traits | Model | Autonomy | Findings |
|---|----------|--------|-------|----------|----------|
| 1 | Security | security + cautious + remediation | Opus | LOW | 5 (2 CRIT) |
| 2 | Code Quality | engineer + precise + remediation | Sonnet | MEDIUM | 12 |
| 3 | Performance | engineer + direct + remediation | Sonnet | MEDIUM | 4 |
| 4 | Documentation | communications + direct + remediation | Haiku | HIGH | 2 |

### Execution Order
1. **Security** (LOW autonomy) - individual approval per fix
2. **Code Quality** (MEDIUM autonomy) - batch approval (5 per batch)
3. **Performance** (MEDIUM autonomy) - batch approval
4. **Documentation** (HIGH autonomy) - auto-apply

Soll ich mit der Remediation starten?
```


#### Example



**Code:**
```bash
# 1. Check git status
git status --porcelain

# 2. Stash if needed
git stash push -m "audit-fix-session-$(date +%s)"

# 3. Create session directory
mkdir -p .audit-fix/session-$(date +%Y%m%d-%H%M%S)/
```


#### Example



**Code:**
```markdown
### Security Fixer - Finding 1/5

**SEC-001** (CRITICAL): SQL Injection vulnerability
**File**: src/api/users.ts:42
**Current Code**:
```


#### Example



**Code:**
```bash

**Proposed Fix**:
```


#### Example



**Code:**
```bash

Apply this fix? [Y/n/edit]
```


#### Example



**Code:**
```markdown
### Code Quality Fixer - Batch 1/3 (5 fixes)

| # | Finding | File | Fix |
|---|---------|------|-----|
| 1 | CQ-001 | src/utils.ts:15 | Add error handling |
| 2 | CQ-002 | src/api.ts:88 | Fix type annotation |
| 3 | CQ-003 | src/db.ts:23 | Remove unused import |
| 4 | CQ-004 | src/auth.ts:56 | Add null check |
| 5 | CQ-005 | src/config.ts:12 | Use const instead of let |

Apply these 5 fixes? [Y/n/select]
```


#### Example



**Code:**
```markdown
### Documentation Fixer - Auto-applying 2 fixes...

- [✓] DOC-001: Added missing JSDoc to exported function
- [✓] DOC-002: Updated README installation section

(Auto-applied, verification running...)
```


#### Example



**Code:**
```bash
# After each successful fix:
git add -A
git commit -m "fix(security): SEC-001 - Use parameterized queries

Finding: SQL injection vulnerability in user input
File: src/api/users.ts:42

Audit-Fix-Session: session-2026-01-06-143022"

# Run verification
npm test && npm run lint

# If verification fails:
git revert HEAD --no-edit
# Log failure to .audit-fix/session-*/failures.json
```


#### Example



**Code:**
```markdown
## Remediation Progress

**Session**: session-2026-01-06-143022
**Elapsed**: 12m 34s

### Security Fixer (Opus, LOW)
- [✓] SEC-001: SQL Injection → Fixed (abc123)
- [✓] SEC-002: Missing Auth → Fixed (def456)
- [✗] SEC-003: Exposed Secrets → FAILED
  - Error: Test config.test.ts failed
  - Reverted: ghi789
- [⏳] SEC-004: XSS Vulnerability → In progress...
- [ ] SEC-005: Rate Limiting → Pending

### Code Quality Fixer (Sonnet, MEDIUM)
- [ ] Batch 1 (5 fixes) → Pending
- [ ] Batch 2 (5 fixes) → Pending
- [ ] Batch 3 (2 fixes) → Pending

**Progress**: 3/23 (13%)
**Commits**: 2 successful, 1 reverted
```


#### Example



**Code:**
```markdown
# Remediation Session Complete

**Session ID**: session-2026-01-06-143022
**Duration**: 28 minutes
**Audit Source**: audit-report-2026-01-06.md

## Results

| Metric | Count |
|--------|-------|
| Total Findings | 23 |
| ✓ Fixed | 18 |
| ✗ Failed | 3 |
| ⊘ Skipped | 2 |
| **Success Rate** | **78%** |

## Commits Made (18)

```


#### Example



**Code:**
```bash

## Failed Fixes (3)

| Finding | Error | Suggested Next Step |
|---------|-------|---------------------|
| SEC-003 | Test expects env vars | Update test mocks first |
| PERF-002 | Breaks API contract | Needs API versioning |
| CQ-005 | Type error cascade | Fix upstream types first |

→ Failures logged to Experience Memory for future learning

## Skipped (2)

| Finding | Reason |
|---------|--------|
| DOC-003 | User declined |
| API-001 | User declined |

## Session Files

- `.audit-fix/session-2026-01-06-143022/progress.json`
- `.audit-fix/session-2026-01-06-143022/failures.json`
- `.audit-fix/session-2026-01-06-143022/summary.md`

## Next Steps

1. **Manual fixes needed** for 3 failed items (see failure analysis)
2. **Re-run audit** to verify improvements: `/quick-audit`
3. **Address skipped** items in next session
```


#### Example



**Code:**
```python
ERROR_HANDLING = {
    "no_audit_report": "Kein Audit-Report gefunden. Führe erst /full-audit oder /quick-audit aus.",
    "git_dirty": "Uncommitted changes. Committe oder stashe erst deine Änderungen.",
    "no_findings": "Keine Findings gefunden - Codebase ist clean!",
    "test_timeout": "Tests dauern zu lange (>5min). Überspringe Verification.",
    "all_failed": "Alle Fixes fehlgeschlagen. Möglicherweise fundamentales Problem."
}
```


#### Example



**Code:**
```bash
# Finde letzte Session
ls -t .audit-fix/session-*/progress.json | head -1

# Resume
/audit-fix --resume session-2026-01-06-143022
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/audit-fix.md`</small>
