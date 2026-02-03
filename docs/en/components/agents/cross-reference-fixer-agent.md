---
title: cross-reference-fixer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# cross-reference-fixer-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Automatically repairs inconsistencies between master documents based on findings from Cross-Reference Checker Agent. |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | general |</div>


## What It Does

Repairs count mismatches, adds missing entries, removes orphan entries, and fixes broken references across master documents with configurable autonomy levels.


## System Impact

Automated maintenance agent reducing manual sync overhead. Operates with MEDIUM autonomy: auto-fixes counts, batch-approves entry changes, individually confirms structural modifications.


## Architecture

Four fix strategies: count mismatches (auto), missing entries (batch approval), orphan entries (batch), broken references (individual). Paired with cross-reference-checker-agent for findings input.


## Usage

Receives findings in JSON format with severity/type/details. Applies fixes according to autonomy level, validates post-fix, returns summary of applied/skipped/failed operations.


## Configuration

**Autonomy Levels:**
- Auto-fix: Count updates in _stats.json, doc headers, alphabetic sorting
- Batch-approval: New/orphan entries (5 at a time)
- Individual-approval: Broken references, structural changes

**Fix Types:**
- count_mismatch: Update _stats.json then propagate to all docs
- missing_entry: Extract metadata, create entry, insert alphabetically
- orphan_entry: Verify and remove from docs
- broken_reference: Find alternative target or remove with comment

## Best Practices

Always validate after fixes with actual file counts. Use auto-fix for safe operations, batch approval for efficiency, individual review for structural changes. Pair with cross-reference-checker for continuous validation.


## Related



---

<small>Source: `.claude/agents/cross-reference-fixer-agent.md`</small>
