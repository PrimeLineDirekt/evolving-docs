---
title: /audit-report
type: command
tags: []
lang: en
confidence: 100
---

# /audit-report


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Generiere oder regeneriere Audit-Reports basierend auf gecachten Ergebnissen. |
| **Complexity** | medium |
| **Model** | haiku |
| **Category** | workflow |</div>


## What It Does

Generates or regenerates audit reports from previously cached audit results without re-running the full audit. Supports multiple formats (markdown, HTML, JSON) and report types (summary, detailed, roadmap).


## System Impact

### Components Affected
- **.audit/**: Reads cached audit data from previous audits
- **audit-reports/**: Writes generated report files
- **_audit-cache/**: Alternative cache location for audit results

### Dependencies
- Requires existing audit data from `/full-audit` or `/quick-audit`
- No re-analysis performed - purely report generation from cache

## Architecture

### Report Generation Pipeline

```
1. Locate Audit Data → 2. Load Results → 3. Generate Report → 4. Write Output
```

**Flow Details:**

1. **Locate Audit Data**: Checks .audit/, audit-reports/, _audit-cache/ for cached results
2. **Load Results**: Reads findings JSON, scores/metrics, metadata
3. **Generate Report**: Applies templates, populates sections, formats code snippets
4. **Write Output**: Creates files with naming pattern: `audit-{type}-{date}.{ext}`

### Report Types

| Type | Content | Use Case |
|------|---------|----------|
| **summary** | Health score, top 5 issues, quick wins | Executive overview |
| **detailed** | All findings with evidence, code snippets | Development team |
| **roadmap** | Phased plan, effort estimates, dependencies | Sprint planning |
| **all** | Generates all three types | Complete documentation |

## Usage

### Arguments

| Argument | Values | Default | Description |
|----------|--------|---------|-------------|
| `--format` | md, html, json | md | Output format |
| `--type` | summary, detailed, roadmap, all | all | Report type |
| `--from` | audit-id or "latest" | latest | Source audit data |

### Examples

#### Basic Usage

Generate default report (markdown, all types):

**Code:**
```bash
/audit-report
```

#### Format Conversion

**Code:**
```bash
# Convert to HTML for stakeholders
/audit-report --format html

# Get JSON for CI integration
/audit-report --format json --type summary
```

#### Specific Report Type

**Code:**
```bash
# Roadmap only for sprint planning
/audit-report --type roadmap

# Summary for executives
/audit-report --type summary --format html
```

#### Historical Reports

**Code:**
```bash
# Regenerate from specific audit
/audit-report --from audit-2026-01-15
```

## Configuration

No configuration file needed. Report generation is stateless and driven by cached audit data.

File naming convention: `audit-{type}-{date}.{ext}`

## Best Practices

1. **Format Selection**: Use markdown for development, HTML for stakeholders, JSON for automation
2. **Type Selection**: Start with summary, drill down to detailed only when needed
3. **Version Control**: Commit reports to track quality improvements over time
4. **Post-Fix Refresh**: Regenerate reports after manual fixes to document progress




## Related

- [`/full-audit`](#full-audit) - Run new audit
- [`/quick-audit`](#quick-audit) - Quick scan
- [`/audit-security`](#audit-security) - Security focus


---

<small>Source: `.claude/commands/audit-report.md`</small>
