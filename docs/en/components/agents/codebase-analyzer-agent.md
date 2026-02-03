---
title: codebase-analyzer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# codebase-analyzer-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | You are a highly specialized **Codebase Analysis Agent** with deep expertise in understanding, mapping, and assessing external codebases. You provide comprehensive architectural insights, identify patterns, assess code quality, and plan upgrade paths while maintaining a strict read-only approach until explicitly authorized to make changes. |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | codebase-analysis || **Created** | 2024-11-27 |</div>


## What It Does

Highly specialized agent for comprehensive external codebase analysis. Provides architectural insights, identifies patterns, assesses code quality, and plans upgrade paths. Key innovation: context persistence across sessions + automatic n8n workflow detection and orchestration.

**Core Capabilities:**
- **Architecture Mapping**: Project structure, component relationships, data flow
- **Dependency Analysis**: Tech stack identification, package dependencies, version tracking
- **Pattern Recognition**: Design patterns, architectural patterns, anti-patterns
- **Code Quality Assessment**: Maintainability, documentation, test coverage estimation
- **Technical Debt Identification**: Legacy code, outdated dependencies, security vulnerabilities
- **n8n Detection**: Automatic identification of n8n workflows with specialized analysis
- **Multi-Agent Orchestration**: Seamlessly coordinates with n8n-Expert Agent


## System Impact

- **Enables persistent project understanding** across multiple sessions via context management
- **80%+ token reduction** for incremental analysis of unchanged projects
- **Powers `/analyze-repo` command** for external codebase assessment
- **Orchestrates n8n-Expert Agent** when workflow integrations detected
- **Creates comprehensive upgrade plans** with risk assessments and phased approaches
- **Critical for external project integration** - all findings flow through this agent


## Architecture

**Model:** Sonnet (high complexity, requires deep reasoning)

**Context Management:**
- Persists analysis data in `knowledge/external-projects/{slug}/`
- Includes: analysis-report.md, context.json, architecture.md, dependencies.json, upgrade-plan.md
- Special n8n-workflows/ subdirectory when workflows detected
- Session-specific work logs in sessions/

**Multi-Agent Orchestration:**
- Detects n8n workflows in Phase 1 (discovery)
- Prepares integration context (webhook calls, data structures, endpoints)
- Invokes @n8n-expert-agent via Task tool
- Merges n8n findings into unified report

**Analysis Framework:**
1. Phase 1: Discovery + n8n detection
2. Phase 2: Dependency analysis
3. Phase 3: Architecture mapping + integration mapping
4. Phase 4: Code quality assessment
5. Phase 5: n8n expert orchestration (if detected)
6. Phase 6: Synthesis & unified report generation

**Safety Protocol:**
- READ-ONLY by default - no modifications without explicit approval
- Explicit approval gate before ANY file changes
- Risk assessment for all proposed changes


## Usage

**Primary Invocation:**
```json
{
  "codebase_path": "/absolute/path/to/project",
  "project_name": "optional-name",
  "analysis_depth": "quick|standard|deep",
  "focus_areas": ["architecture", "dependencies", "quality", "patterns", "security", "n8n"],
  "context_path": "knowledge/external-projects/{slug}/",
  "force_refresh": false,
  "detect_n8n": true
}
```

**Analysis Depth Options:**
- **quick**: Structure scan, tech stack ID, basic dependency check (~5-10 min)
- **standard**: Full analysis minus deep code review (~15-30 min)
- **deep**: Comprehensive analysis including pattern deep-dive (~45-90 min)

**Context Reuse:**
If context exists and no force_refresh:
- Loads existing context.json
- Detects changes via git commit hash + file hashes
- Performs incremental analysis only on changed areas
- Massive token savings for unchanged projects

**n8n Detection Triggers:**
- Workflow JSON files matching n8n structure
- Webhook URLs containing `.n8n.cloud` or `n8n.io`
- n8n dependencies in package.json
- .n8n/ configuration directories


## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| **model** | sonnet | High complexity requires deep reasoning |
| **analysis_depth** | standard | Balance between thoroughness and speed |
| **detect_n8n** | true | Automatic n8n workflow detection |
| **force_refresh** | false | Ignore existing context, re-analyze |
| **safety_mode** | strict | READ-ONLY until explicit approval |

**Context Structure:**
```
knowledge/external-projects/{slug}/
├── analysis-report.md (comprehensive report)
├── context.json (machine-readable state)
├── architecture.md (detailed architecture docs)
├── dependencies.json (dependency matrix)
├── upgrade-plan.md (upgrade roadmap with status)
├── n8n-workflows/ (if n8n detected)
│   ├── analysis-report.md
│   ├── workflows/ (analyzed workflow copies)
│   └── recommendations.md
├── sessions/ (session-specific logs)
└── metadata.json (project tracking)
```

**n8n Handoff Criteria:**
```python
should_invoke_n8n_expert = (
    n8n_workflows_found > 0 or
    n8n_webhooks_found > 0 or
    n8n_dependency_present or
    user_explicitly_requested
)
```


## Best Practices

**Do:**
- Use context persistence for repeated analysis (massive token savings)
- Let the agent detect n8n integration automatically
- Review and approve upgrade plans before execution
- Use `force_refresh: true` when major codebase restructuring occurred
- Focus analysis with `focus_areas` parameter to save time
- Trust the multi-agent orchestration for n8n workflows

**Don't:**
- Don't expect modifications without explicit approval (safety-first)
- Don't bypass context management - it's designed for efficiency
- Don't manually analyze n8n workflows - let n8n-Expert handle it
- Don't ignore incremental analysis results - they're accurate for unchanged code
- Don't force full re-analysis unless necessary (wastes tokens)
- Don't proceed with upgrades without reviewing risk assessment




## Related


---

<small>Source: `.claude/agents/codebase-analyzer-agent.md`</small>
