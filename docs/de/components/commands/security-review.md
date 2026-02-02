---
title: security-review
type: command
tags: []
lang: en
confidence: 100
---

# security-review


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

Security Code Review mit False-Positive Filtering


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
/security-review [branch|commit-range|files]

Beispiele:
/security-review feature/user-auth
/security-review HEAD~5..HEAD
/security-review src/api/
```


#### Example



**Code:**
```markdown
# Security Review: {branch/range}

**Reviewed**: {date}
**Scope**: {files count} files, {lines} lines changed
**Confidence Threshold**: 80%+

---

## Executive Summary

| Severity | Count |
|----------|-------|
| CRITICAL | {n} |
| HIGH | {n} |
| MEDIUM | {n} |

**Gesamtbewertung**: {PASS | NEEDS ATTENTION | CRITICAL ISSUES}

---

## Findings

### Finding 1: {TITLE}

**Location:** `{file}:{line}`
**Severity:** CRITICAL | HIGH | MEDIUM
**Category:** {OWASP Category}
**Confidence:** {8-10}/10

#### Description
{Was das Problem ist}

#### Vulnerable Code
```


#### Example



**Code:**
```bash

#### Exploit Scenario
{Wie ein Angreifer das ausnutzen könnte}

#### Recommendation
{Wie es gefixt werden sollte}

#### Fixed Code
```


#### Example



**Code:**
```bash

---

## Excluded (False Positives Filtered)

{Liste von Dingen die geprüft aber als False Positive eingestuft wurden}

---

## Recommendations

1. {Empfehlung 1}
2. {Empfehlung 2}
```


#### Example



**Code:**
```bash
User: /security-review feature/auth-refactor

Claude:
[Phase 1: Context Research]
- Found: bcrypt for password hashing
- Found: JWT middleware
- Pattern: Input validation via express-validator

[Phase 2: Comparative Analysis]
- 8 files changed, 234 lines added
- New endpoint: POST /api/users/reset-password

[Phase 3: Vulnerability Assessment]
- 5 potential issues identified
- After filtering: 2 findings (Confidence ≥ 8)

# Security Review: feature/auth-refactor

**Reviewed**: 2025-12-16
**Scope**: 8 files, 234 lines
**Confidence Threshold**: 80%+

## Executive Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| HIGH | 1 |
| MEDIUM | 1 |

**Gesamtbewertung**: NEEDS ATTENTION

## Findings

### Finding 1: Timing Attack in Password Reset

**Location:** `src/api/auth.ts:145`
**Severity:** HIGH
**Category:** A07:2021 - Identification and Authentication Failures
**Confidence:** 9/10

#### Description
Password reset token comparison uses `===` instead of timing-safe comparison.

#### Vulnerable Code
```


#### Example



**Code:**
```bash

#### Exploit Scenario
Attacker can measure response times to guess valid tokens character by character.

#### Recommendation
Use timing-safe comparison.

#### Fixed Code
```


#### Example



**Code:**
```bash

---

### Finding 2: Missing Rate Limit on Reset Endpoint

**Location:** `src/api/auth.ts:140`
**Severity:** MEDIUM
**Category:** A07:2021 - Identification and Authentication Failures
**Confidence:** 8/10

[...]
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/security-review.md`</small>
