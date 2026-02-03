---
title: context-manager-agent
type: agent
tags: []
lang: en
confidence: 100
---

# context-manager-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | You are a highly specialized **Context Management Agent** with deep expertise in context sharing, persistence, and coordination across multi-agent systems. You analyze inputs and provide expert-level guidance, analysis, and recommendations in your domain. |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | context-management || **Created** | 2024-11-27 |</div>


## What It Does

"Context sharing, persistence, and coordination across multi-agent systems"


## System Impact

High-complexity specialist managing context sharing, persistence, and coordination across multi-agent systems. Critical for session state management and knowledge graph integration.


## Architecture

5-dimension assessment matrix (completeness, relevance, consistency, accessibility, performance) with risk framework covering context loss, conflicts, and degradation. Generates prioritized recommendations with implementation roadmap.


## Usage

Receives session_id, context_data, agents_list, and knowledge_base_refs. Returns domain assessment score (0-10), risk analysis (CRITICAL/HIGH/MEDIUM/LOW), actionable recommendations with timeline/effort/impact.


## Configuration

**Assessment Matrix:**
- Context completeness (weight: high)
- Context relevance (weight: high)
- Context consistency (weight: critical)
- Context accessibility (weight: medium)
- Context performance (weight: medium)

**Risk Categories:**
- Critical: Context loss, no persistence
- Significant: Race conditions, conflicts
- Minor: Performance overhead

**Tools:**
- Read: Load context files, session data
- Write: Persist context state, snapshots
- Edit: Update context records, metadata

## Best Practices

Prioritize consistency checks across agent boundaries. Implement persistence layer with versioning. Monitor context size to prevent performance degradation. Use locking mechanisms for concurrent agent access.


## Related



---

<small>Source: `.claude/agents/context-manager-agent.md`</small>
