---
title: compatibility-checker-agent
type: agent
tags: []
lang: en
confidence: 100
---

# compatibility-checker-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Specialized compatibility checker for the Evolving System. Validates external findings (from `/analyze-repo`) for integration conflicts BEFORE they enter the system. |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | compatibility-analysis |
| **Created** | 2026-01-08 |</div>


## What It Does

The Compatibility Checker Agent performs preventive conflict detection before integrating external findings into the system. It validates against four critical areas: tool mutex conflicts, naming collisions, pattern/keyword overlaps, and sub-agent delegation efficiency.

**Core Principle:** Detect problems before they exist - prevent integration conflicts proactively.

**4 Critical Checks:**
1. **Tool-Mutex**: Detects conflicting browser automation, file system tools
2. **Naming**: Identifies exact matches and high-similarity names (≥70%)
3. **Pattern-Overlap**: Finds keyword overlaps that would trigger wrong commands
4. **Sub-Agent Usage**: Evaluates delegation efficiency and token savings potential

**3-Tier Severity System:**
- 🟢 **CLEAN**: No conflicts, auto-proceed
- 🟡 **FIXABLE**: Conflicts resolvable with automated fixes
- 🔴 **NON-FIXABLE**: Fundamental incompatibility, requires user decision


## System Impact

- **Prevents breaking changes** from external integration (tool conflicts, naming collisions)
- **Powers `/analyze-repo` safety** - Phase 3.5 compatibility gate before integration
- **Saves debugging time** - catches conflicts before they cause system failures
- **Enables safe external learning** - validate findings from other repos without risk
- **Optimizes token usage** - identifies poor delegation patterns (potential 13K+ token savings per run)


## Architecture

**Model:** Sonnet (medium complexity, requires reasoning for conflict analysis and fix suggestions)

**Capabilities:**
- `tool-mutex-check` - Validate against tool conflict rules
- `naming-check` - Detect exact and fuzzy name matches
- `pattern-overlap-check` - Identify keyword collision risks
- `subagent-audit` - Evaluate delegation efficiency

**Data Sources (Read-only):**
- `.claude/tools/tool-mutex.json` - Tool conflict rules
- `.claude/detection-index.json` - Command keywords
- `_graph/nodes.json` - All entity names
- `.claude/SYSTEM-MAP.md` - Current system tools

**Process Flow:**
1. Receive finding metadata (name, type, tools, keywords)
2. Run 4 parallel checks
3. Aggregate severity (NON-FIXABLE > FIXABLE > CLEAN)
4. Generate report with fix suggestions
5. Return action: BLOCK_AND_ASK / WARN_AND_OFFER_FIX / PROCEED

**Orchestration:**
- Called by `/analyze-repo` command in Phase 3.5
- Receives extracted metadata from findings
- Returns JSON report with severity and fixes


## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| **model** | sonnet | Medium complexity conflict analysis |
| **similarity_threshold** | 0.7 | 70%+ name similarity triggers FIXABLE |
| **keyword_overlap_threshold** | 0.7 | 70%+ keyword overlap = NON-FIXABLE |
| **delegation_score_threshold** | 7.0 | Score <7 triggers FIXABLE for poor delegation |
| **read_only** | true | Agent never writes, only reports |

**Severity Aggregation:**
```
Overall Severity = MAX(tool_mutex, naming, pattern_overlap, subagent)
NON-FIXABLE > FIXABLE > CLEAN
```

**Tool Mutex Groups Example:**
```json
{
  "browser_automation": {
    "tools": ["mcp__puppeteer__*", "mcp__claude-in-chrome__*"],
    "conflict_type": "NON-FIXABLE",
    "resolution_options": ["reject", "replace existing", "abstract as template"]
  }
}
```


## Best Practices

**Do:**
- Run compatibility check on ALL external findings before integration
- Trust the 3-tier severity system (don't bypass NON-FIXABLE warnings)
- Apply automated fixes for FIXABLE conflicts when offered
- Review sub-agent delegation suggestions for token savings
- Use similarity threshold to catch typos before they cause issues

**Don't:**
- Don't skip compatibility check to save time (prevents future debugging pain)
- Don't manually edit mutex/detection files after findings flagged (breaks consistency)
- Don't ignore pattern overlap warnings (causes wrong command triggers)
- Don't integrate findings with NON-FIXABLE conflicts without user approval
- Don't bypass delegation suggestions without reason (wastes tokens on every run)




## Related


---

<small>Source: `.claude/agents/compatibility-checker-agent.md`</small>
