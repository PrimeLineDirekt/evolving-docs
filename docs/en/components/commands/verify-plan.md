---
title: verify-plan
type: command
tags: []
lang: en
confidence: 100
---

# verify-plan


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




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
/verify-plan                    # Verifikation für aktuellen Branch
/verify-plan feature-name       # Verifikation für spezifisches Feature
```


#### Example



**Code:**
```markdown
# Verification Report: {Feature}

**Date**: YYYY-MM-DD
**Branch**: feature/xyz
**Compared to**: main

## Summary
- Tests Passed: X/Y
- Coverage: Z%
- Edge Cases: Verified/Not Verified
- **Confidence**: HIGH/MEDIUM/LOW

## Test Results
| Test Suite | Status | Notes |
|------------|--------|-------|
| Unit | ✅ 42/42 | |
| Integration | ✅ 8/8 | |
| E2E | ⚠️ 5/6 | Flaky: auth-flow |

## Edge Cases Verified
- [ ] Empty input handling
- [x] Large dataset performance
- [x] Concurrent access
- [ ] Network failure recovery

## Manual Verification
- [x] UI renders correctly
- [x] Error messages displayed
- [ ] Accessibility check

## Issues Found
1. **Minor**: Typo in error message
2. **None blocking**

## Recommendation
READY FOR MERGE / NEEDS WORK
```


#### Example



**Code:**
```bash
User: Ist das Feature ready für den PR?
Claude: "Soll ich /verify-plan nutzen für eine systematische Verifikation?"

User: /verify-plan auth-system
Claude: [Startet Verification Mode]
        "🔍 Starte Verifikation für auth-system..."
        [Führt Tests durch]
        [Generiert Report]
        "✅ Verification complete. Confidence: HIGH
         42/42 tests passed, 3/3 edge cases verified.
         Recommendation: READY FOR MERGE"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/verify-plan.md`</small>
