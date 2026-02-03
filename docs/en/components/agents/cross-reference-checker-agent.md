---
title: cross-reference-checker-agent
type: agent
tags: []
lang: en
confidence: 100
---

# cross-reference-checker-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | System integrity specialist that validates consistency between ALL master documents, _stats.json, and actual file structure. |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | system-integrity |</div>


## What It Does

Validates consistency across all master docs, _stats.json, and actual structure. Checks 7 master documents for count accuracy, detection index coverage, and cross-reference integrity.


## System Impact

Critical infrastructure validator ensuring documentation reflects reality. Detects sync gaps, missing entries, orphaned references, and count mismatches across the entire Evolving system.




## Architecture

**Model:** Sonnet (medium complexity, requires reasoning for consistency analysis)

**Capabilities:**
- `count-validation` - Validate counts across 7 master documents
- `detection-coverage-check` - Verify all commands have detection entries
- `reference-integrity-check` - Find broken internal references
- `auto-sync-gap-analysis` - Detect missed synchronization

**Data Sources (Read-only):**
- `_stats.json` - Single Source of Truth for all counts
- `.claude/COMMANDS.md` - Command documentation with header count
- `.claude/SYSTEM-MAP.md` - Component inventory with tables
- `.claude/README.md` - Stats section
- `.claude/detection-index.json` - Command detection keywords
- `knowledge/index.md` - Knowledge base index
- `.claude/CONTEXT.md` - Technical architecture

**7 Master Documents Matrix:**
| Document | Contains Counts | Purpose |
|----------|----------------|---------|
| `_stats.json` | YES (authoritative) | Single Source of Truth |
| `COMMANDS.md` | YES (header) | Command documentation |
| `SYSTEM-MAP.md` | YES (tables) | Component inventory |
| `README.md` | YES (stats section) | Overview with statistics |
| `detection-index.json` | YES (implicit) | Command detection via array length |
| `knowledge/index.md` | YES (categories) | Knowledge base index |
| `CONTEXT.md` | NO | Technical architecture docs |

**Process Flow:**
1. Count actual files in filesystem for each category
2. Compare with `_stats.json` (authoritative)
3. Compare with other 6 master documents
4. Check detection index coverage (all commands have entries)
5. Validate SYSTEM-MAP tables (all components listed)
6. Find broken internal references (`@agent-name`, `/command`)
7. Analyze auto-sync gaps (hook notifications vs actual updates)
8. Generate severity-ranked issue list with recommendations

**Orchestration:**
- Called by `/evolving-audit` command for full system integrity check
- Can be invoked standalone for cross-reference validation
- Returns structured report with integrity score and fix recommendations


## Usage

**Primary Invocation:**
```bash
# Via command
/evolving-audit --focus=cross-reference

# Direct agent invocation
@cross-reference-checker-agent
{
  "check_scope": "full",
  "include_suggestions": true
}
```

**Check Dimensions:**

1. **Count Validation** - All 7 sources must agree on component counts
2. **_stats.json Authority** - Authoritative source, if wrong all others inherit errors
3. **Detection Index Coverage** - Every command must have detection entry with ≥3 keywords
4. **SYSTEM-MAP Accuracy** - All component tables must list actual files
5. **Broken References** - Internal references (@agent, /command) must point to existing files
6. **Auto-Sync Gap Analysis** - Hook notifications vs actual updates

**Output Example:**
```markdown
# Cross-Reference Audit Report

## Summary
- Master-Docs checked: 7
- Component categories: 10
- Total checks: 147
- Passed: 128
- Failed: 19
- Integrity Score: 87/100

## _stats.json Validation
| Component | Actual | _stats.json | Status |
|-----------|--------|-------------|--------|
| Commands  | 63     | 58          | ❌ OUTDATED (-5) |
| Agents    | 60     | 36          | ❌ OUTDATED (-24) |
| Skills    | 6      | 6           | ✅ OK |
```


## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/agents/cross-reference-checker-agent.md`</small>
