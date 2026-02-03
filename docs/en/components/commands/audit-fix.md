---
title: /audit-fix
type: command
tags: []
lang: en
confidence: 100
---

# /audit-fix


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Remediation Orchestrator - analyzes audit findings and performs semi-automated fixes with dynamically composed fixer team. |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | memory |</div>


## What It Does

Semi-automated remediation of audit findings with a dynamically composed fixer team:

1. **Parses audit report** - Extracts findings by ID, severity, category, file, and message
2. **Composes fixer team** - Trait-based agent selection per category (security, code quality, architecture, performance, documentation, API, tests, config)
3. **Executes remediation** - Three autonomy levels:
   - **LOW** (Security/Architecture): Individual approval per fix
   - **MEDIUM** (Code Quality/Performance): Batch approval (5 fixes per batch)
   - **HIGH** (Documentation/Config): Auto-apply with verification
4. **Git workflow** - Creates commits per fix with test+lint verification, auto-reverts on failure
5. **Session tracking** - Logs progress, failures (for future learning), and skipped items

Supports dry-run mode, category/severity filtering, team size limits, and session resume.


## System Impact

- Enables automated remediation workflow for audit findings
- Integrates with @team-composer-agent for dynamic fixer team assembly
- Critical for maintaining code health after audits
- Preserves git history with detailed commit messages per fix
- Feeds failure data into Experience Memory for continuous improvement


## Architecture

**Dependencies:**
- Audit reports in `audit-reports/` or project root
- @team-composer-agent for trait-based fixer selection
- @remediation-orchestrator-agent for execution logic
- Git for versioning and rollback on verification failures
- Previous failure logs in `.audit-fix/*/failures.json` for context

**Data Flow:**
1. Find audit report (latest or specified) → Parse findings
2. Check previous failures for context
3. Compose fixer team based on category traits + model selection
4. Execute per autonomy level (LOW=individual, MEDIUM=batch, HIGH=auto)
5. Per fix: Apply → Git commit → Verify (test+lint) → Revert if failed
6. Log session (progress, failures, summary) to `.audit-fix/session-YYYYMMDD-HHMMSS/`

**Triggers:** Manual via `/audit-fix` with optional arguments


## Usage

**Syntax:**
```bash
/audit-fix [audit-report] [--dry-run] [--category CAT] [--severity SEV] [--max-fixers N]
```

**Arguments:**
- `audit-report`: Path to audit report (default: latest in audit-reports/)
- `--dry-run`: Show execution plan without making changes
- `--category`: Filter by category (security|code_quality|architecture|performance|documentation|api|tests|config)
- `--severity`: Minimum severity (CRITICAL|HIGH|MEDIUM|LOW)
- `--max-fixers`: Maximum team size (default: 5)

### Examples

#### Basic Usage

Fix all findings from latest audit report:

**Code:**
```bash
/audit-fix
```

**Output:**
```markdown
## Audit Report Analysis

**Source**: audit-report-2026-02-03.md
**Total Findings**: 23
**Previous Failures**: 2

### Findings by Category
| Category | CRIT | HIGH | MED | LOW | Total |
|----------|------|------|-----|-----|-------|
| Security | 2 | 3 | 0 | 0 | 5 |
| Code Quality | 0 | 4 | 6 | 2 | 12 |
| Performance | 0 | 1 | 3 | 0 | 4 |

## Fixer Team Composition

**Team Size**: 4 fixers
**Estimated Duration**: 20-30 minutes

Soll ich mit der Remediation starten?
```

#### Dry-Run Mode

Show execution plan without applying fixes:

**Code:**
```bash
/audit-fix --dry-run
```

#### Security-Only Fixes

Fix only security findings with critical/high severity:

**Code:**
```bash
/audit-fix --category security --severity HIGH
```

#### Resume Interrupted Session

Continue from last interrupted session:

**Code:**
```bash
/audit-fix --resume session-2026-02-03-143022
```


## Configuration

**Category Traits Mapping:**
| Category | Expertise | Personality | Approach | Model | Autonomy |
|----------|-----------|-------------|----------|-------|----------|
| security | security | cautious | remediation | opus | LOW |
| code_quality | engineer | precise | remediation | sonnet | MEDIUM |
| architecture | architect | cautious | remediation | opus | LOW |
| performance | engineer | direct | remediation | sonnet | MEDIUM |
| documentation | communications | direct | remediation | haiku | HIGH |
| api | engineer | precise | remediation | sonnet | MEDIUM |
| tests | engineer | thorough | remediation | sonnet | MEDIUM |
| config | engineer | direct | remediation | haiku | HIGH |

**Autonomy Levels:**
- **LOW**: Individual approval per fix (critical categories)
- **MEDIUM**: Batch approval (5 fixes at a time)
- **HIGH**: Auto-apply with post-verification

**Session Files:**
- `.audit-fix/session-YYYYMMDD-HHMMSS/progress.json`
- `.audit-fix/session-YYYYMMDD-HHMMSS/failures.json`
- `.audit-fix/session-YYYYMMDD-HHMMSS/summary.md`


## Best Practices

**Do:**
- Run `--dry-run` first to preview execution plan
- Check git status before starting (must be clean or will auto-stash)
- Review LOW autonomy fixes individually (security, architecture)
- Let HIGH autonomy fixes auto-apply for efficiency (docs, config)
- Check session summary for failed fixes and manual remediation steps
- Re-run `/quick-audit` after session to verify improvements

**Don't:**
- Skip dry-run for first-time usage on critical codebases
- Ignore failed fixes (they're logged for good reasons)
- Apply fixes without understanding the findings
- Use `--force` to bypass autonomy levels (defeats safety purpose)
- Delete session directories (they contain valuable failure context)



## Related

- [`/full-audit`](#full-audit) - Umfassender Projekt-Audit
- [`/quick-audit`](#quick-audit) - Schneller Security & Quality Check
- [`/audit-report`](#audit-report) - Report aus vorherigen Ergebnissen
- [`/compose-agent`](#compose-agent) - Manuell Agent mit Traits komponieren


---

<small>Source: `.claude/commands/audit-fix.md`</small>
