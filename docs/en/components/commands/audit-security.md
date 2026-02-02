---
title: audit-security
type: command
tags: []
lang: en
confidence: 100
---

# audit-security


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

Fokussierter Security Audit mit erweitertem Scope


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
$ARGUMENTS:
- path: Projekt-Pfad (default: .)
- --owasp: Nur OWASP Top 10 Checks
- --secrets: Nur Secrets Detection
- --deps: Nur Dependency Audit
- --all: Alle Checks [default]
```


#### Example



**Code:**
```markdown
## Security Audit: {path}

**Mode**: {owasp|secrets|deps|all}

### Scanning...
- [✓] OWASP Top 10 Checks
- [✓] Secrets Detection
- [⏳] Dependency Analysis
- [ ] API Security Review
- [ ] DSGVO Compliance
```


#### Example



**Code:**
```python
SECRET_PATTERNS = {
    "aws_key": r"AKIA[0-9A-Z]{16}",
    "github_token": r"ghp_[a-zA-Z0-9]{36}",
    "jwt_secret": r"(jwt|JWT).*(secret|SECRET).*['\"][^'\"]{20,}['\"]",
    "api_key": r"(api[_-]?key|apikey).*['\"][a-zA-Z0-9]{20,}['\"]",
    "password": r"(password|passwd|pwd).*['\"][^'\"]{8,}['\"]"
}
```


#### Example



**Code:**
```markdown
# Security Audit Report

## Summary

**Security Score**: {score}/100
**CRITICAL**: {n} | **HIGH**: {n} | **MEDIUM**: {n}

## Critical Findings

### SEC-001: SQL Injection
**CVSS**: 9.8 | **CWE**: CWE-89
**File**: src/api/users.ts:42

[Details + Fix]

---

## Secrets Found

| Type | File | Line | Status |
|------|------|------|--------|
| AWS Key | .env.local | 5 | EXPOSED |
| JWT Secret | config.ts | 12 | HARDCODED |

⚠️ Rotate these credentials immediately!

---

## Vulnerable Dependencies

| Package | Current | Fixed | Severity |
|---------|---------|-------|----------|
| lodash | 4.17.15 | 4.17.21 | HIGH |
| axios | 0.21.0 | 0.21.2 | MEDIUM |

Run: `npm audit fix`

---

## Recommendations

### Immediate (24h)
1. Rotate exposed secrets
2. Fix SQL injection
3. Update critical deps

### This Week
4. Add auth to unprotected routes
5. Implement rate limiting
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/audit-security.md`</small>
