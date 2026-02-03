---
title: Claude Code Rules
type: rule
tags: []
lang: en
confidence: 100
---

# Claude Code Rules


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | ```
.claude/rules/                    # CORE: Auto-load bei Session-Start (~2K Tokens)
├── core-principles.md            # Arbeitsweise
├── workflow-detection.md         # Command-Erkennung
├── domain |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

```
.claude/rules/                    # CORE: Auto-load bei Session-Start (~2K Tokens)
├── core-principles.md            # Arbeitsweise
├── workflow-detection.md         # Command-Erkennung
├── domain-memory-bootup.md       # Session-Start
└── README.md                     # Diese Datei


## System Impact

**When It Triggers:**
- Session start (auto-loads core rules from `.claude/rules/`)
- Keyword match (context router loads on-demand rules from `knowledge/rules/`)

**Behavior Enforced:**
- Token-optimized two-tier loading (core ~2K, on-demand ~0K default)
- Prevents loading all rules at session start (saves ~25K tokens)
- Context router enables dynamic rule loading based on task keywords
- Separates critical always-needed rules from contextual rules

**Integration Points:**
- `.claude/rules/` - Auto-loaded at session start (4 core rules)
- `knowledge/rules/` - Loaded via context router when keywords match
- `_graph/cache/context-router.json` - Keyword-based routing configuration
- `.claude/summaries/rules/` - Quick reference summaries


## Architecture




## Usage




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/rules/README.md`</small>
