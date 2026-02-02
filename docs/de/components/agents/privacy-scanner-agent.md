---
title: privacy-scanner-agent
type: agent
tags: []
lang: en
confidence: 100
---

# privacy-scanner-agent


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

"Scans files for sensitive/personal content - before sync AND validates entire template after sync"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "mode": "pre-sync|post-sync|full-audit",
  "files_to_scan": ["array of file paths"],
  "target_path": "/path/to/Evolving-Template",
  "manifest": "template-sync-manifest.json contents",
  "scan_depth": "full|quick"
}
```


#### Example



**Code:**
```python
def pre_sync_scan(files_to_sync, patterns):
    """Scan only files about to be synced"""
    findings = []
    for file in files_to_sync:
        findings.extend(scan_file(file, patterns))
    return findings
```


#### Example



**Code:**
```python
def post_sync_audit(template_path, patterns):
    """
    Scan ENTIRE template repository after sync.
    This catches any leaks that slipped through.
    """
    findings = []

    # Scan all text files in template
    all_files = glob(f"{template_path}/**/*", recursive=True)

    for file in all_files:
        if is_text_file(file):
            findings.extend(scan_file(file, patterns))

    # Special attention to common leak locations
    critical_paths = [
        ".claude/agents/*.md",
        ".claude/commands/*.md",
        ".claude/scenarios/**/*",
        "knowledge/**/*.md",
        "_graph/*.json",
        "*.json",
        "*.md"
    ]

    return findings
```


#### Example



**Code:**
```python
def scan_file(file_path, patterns):
    findings = []
    with open(file_path) as f:
        for line_num, line in enumerate(f, 1):
            for pattern in patterns:
                if match := pattern.search(line):
                    findings.append({
                        "file": file_path,
                        "line": line_num,
                        "match": match.group(),
                        "context": get_context(line),
                        "severity": pattern.severity,
                        "category": pattern.category
                    })
    return findings
```


#### Example



**Code:**
```markdown
# Pre-Sync Privacy Scan Report

## Files Scanned: 15

## Summary
| Severity | Count | Action |
|----------|-------|--------|
| CRITICAL | 0 | BLOCK |
| HIGH | 3 | ANONYMIZE |
| MEDIUM | 5 | ANONYMIZE |

## Findings by File
[... detailed findings ...]

## Recommendations
1. Run Content Anonymizer on flagged files
2. Proceed with sync after anonymization
```


#### Example



**Code:**
```markdown
# Post-Sync Template Audit Report

## Template Path: /path/to/Evolving-Template
## Files Scanned: 847
## Scan Date: 2026-01-04 10:45:00

## AUDIT STATUS: PASSED / FAILED

## Summary
| Severity | Count | Status |
|----------|-------|--------|
| CRITICAL | 0 | OK |
| HIGH | 0 | OK |
| MEDIUM | 2 | WARNING |

## Critical Issues (MUST FIX)
None found.

## High Priority Issues
None found.

## Medium Priority Issues (Warnings)

### File: knowledge/patterns/example.md
- Line 42: `/Users/neoforce` (absolute path)
  - Recommendation: Replace with `{HOME}` or relative path

### File: _graph/nodes.json
- Line 156: Reference to old project ID
  - Recommendation: Remove or anonymize node

## Areas Checked
- [x] All .md files scanned
- [x] All .json files scanned
- [x] Graph data verified
- [x] Agent definitions checked
- [x] Command definitions checked
- [x] No API keys found
- [x] No passwords found

## Template Safety Score: 98/100

## Recommendations
1. Fix 2 MEDIUM issues for 100% score
2. Template is SAFE for public sharing
```


#### Example



**Code:**
```bash
# Full template scan for API keys
grep -rn "sk-\|api_key\|apiKey\|API_KEY" $TEMPLATE_PATH

# Scan for personal names
grep -rn "Robin\|Mandy" $TEMPLATE_PATH

# Scan for project references
grep -rn "Auswanderungs-KI\|ThriveVibesArt\|nhien-bistro\|didit-medical" $TEMPLATE_PATH

# Scan for absolute paths
grep -rn "/Users/neoforce\|/home/" $TEMPLATE_PATH

# Count total files
find $TEMPLATE_PATH -type f \( -name "*.md" -o -name "*.json" \) | wc -l
```


#### Example



**Code:**
```bash
[6/6] Post-Sync Validation...

Running full template audit...
Scanning 847 files...

✓ No CRITICAL issues found
✓ No HIGH issues found
⚠ 2 MEDIUM issues found (see report)

Template Audit: PASSED

The template is safe for public sharing.
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/privacy-scanner-agent.md`</small>
