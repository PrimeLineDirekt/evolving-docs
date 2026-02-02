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
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2024-11-27 |</div>


## What It Does

"External codebase analysis with context persistence, n8n detection, and multi-agent orchestration"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "codebase_path": "string (absolute path to external project)",
  "project_name": "string (optional, for reference)",
  "analysis_depth": "quick|standard|deep",
  "focus_areas": ["architecture", "dependencies", "quality", "patterns", "security", "n8n"],
  "context_path": "string (path to knowledge/external-projects/{slug}/)",
  "force_refresh": "boolean (ignore existing context, re-analyze)",
  "detect_n8n": "boolean (auto-detect n8n workflows, default: true)",
  "constraints": {
    "time_limit": "number (optional, in minutes)",
    "scope_filter": "string (optional, e.g., 'src/**/*.ts')"
  }
}
```


#### Example



**Code:**
```json
{
  "agent_id": "codebase-analyzer",
  "execution_id": "uuid",
  "priority_level": "HIGH",
  "time_allocation": "Varies by analysis_depth and context availability",
  "success_criteria": "Comprehensive understanding + actionable recommendations + context persistence"
}
```


#### Example



**Code:**
```bash
knowledge/external-projects/{project-slug}/
├── analysis-report.md          # User-readable comprehensive report
├── context.json                # Machine-readable context for agent
├── architecture.md             # Detailed architecture documentation
├── dependencies.json           # Full dependency matrix
├── upgrade-plan.md             # Current upgrade plan with status tracking
├── n8n-workflows/              # n8n-specific analysis (if detected)
│   ├── analysis-report.md      # n8n workflow analysis
│   ├── workflows/              # Analyzed workflow copies
│   │   ├── workflow-1.json
│   │   └── workflow-2.json
│   └── recommendations.md      # n8n-specific recommendations
├── sessions/                   # Session-specific work logs
│   └── YYYY-MM-DD-{topic}.md
└── metadata.json               # Project metadata and tracking
```


#### Example



**Code:**
```json
{
  "version": "1.0",
  "project_name": "string",
  "project_slug": "string",
  "codebase_path": "string (absolute)",
  "last_analyzed": "ISO 8601 timestamp",
  "last_git_commit": "string (commit hash)",
  "analysis_depth": "quick|standard|deep",

  "structure": {
    "total_files": "number",
    "total_lines": "number (estimated)",
    "languages": {
      "typescript": "number of files",
      "javascript": "number of files"
    },
    "key_directories": ["array of important dirs"],
    "entry_points": ["array of main files"]
  },

  "architecture": {
    "pattern": "string (MVC, MVVM, etc.)",
    "confidence": "number (0-100)",
    "layers": {
      "presentation": ["directories"],
      "business_logic": ["directories"],
      "data_access": ["directories"],
      "infrastructure": ["directories"]
    },
    "design_patterns": ["array of identified patterns"],
    "anti_patterns": ["array of issues"]
  },

  "tech_stack": {
    "runtime": {"name": "string", "version": "string"},
    "framework": {"name": "string", "version": "string"},
    "build_tool": {"name": "string", "version": "string"},
    "package_manager": "string"
  },

  "dependencies": {
    "production_count": "number",
    "dev_count": "number",
    "outdated_count": "number",
    "vulnerable_count": "number",
    "critical_packages": ["array of key dependencies"]
  },

  "quality_scores": {
    "documentation": "number (1-10)",
    "test_coverage": "number (1-10)",
    "maintainability": "number (1-10)",
    "overall_health": "number (1-10)"
  },

  "n8n_integration": {
    "detected": "boolean",
    "workflow_count": "number",
    "workflow_paths": ["array of paths"],
    "webhook_endpoints": ["array of webhook URLs found in code"],
    "n8n_version": "string or null",
    "last_n8n_analysis": "ISO 8601 timestamp or null"
  },

  "known_issues": [
    {
      "id": "uuid",
      "type": "security|performance|quality|debt|n8n",
      "severity": "critical|high|medium|low",
      "title": "string",
      "status": "open|in-progress|resolved",
      "created": "timestamp",
      "resolved": "timestamp or null"
    }
  ],

  "file_hashes": {
    "package.json": "md5 hash",
    "tsconfig.json": "md5 hash"
  },

  "analysis_stats": {
    "files_analyzed": "number",
    "tokens_used": "number",
    "duration_seconds": "number",
    "agents_invoked": ["codebase-analyzer", "n8n-expert"]
  }
}
```


#### Example



**Code:**
```json
{
  "workflow_directory": "{codebase_path}/workflows/ or detected path",
  "workflow_files": ["array of .json workflow files"],
  "integration_context": {
    "webhook_calls": [
      {
        "file": "src/api/emigration.ts",
        "line": 42,
        "url": "https://app.n8n.cloud/webhook/emigration-profile",
        "method": "POST",
        "payload_structure": {
          "profileData": "object",
          "userId": "string"
        }
      }
    ],
    "expected_responses": [
      {
        "webhook": "emigration-profile",
        "expected_fields": ["analysis", "recommendations", "score"]
      }
    ]
  },
  "frontend_expectations": {
    "data_structures": ["extracted from TypeScript interfaces"],
    "error_handling": "how frontend handles n8n errors"
  },
  "context_path": "knowledge/external-projects/{slug}/"
}
```


#### Example



**Code:**
```markdown
## @n8n-expert-agent Invocation

**Input**:
```


#### Example



**Code:**
```bash

**Expected Output**:
```


#### Example



**Code:**
```bash

**Usage**:
```


#### Example



**Code:**
```bash
START
  |
  ├─→ Context exists?
  │     |
  │     NO ──→ FULL ANALYSIS (Phase 1-5)
  │     |       ├─→ Phase 1: Discovery + n8n Detection
  │     |       ├─→ If n8n detected → Invoke n8n-Expert
  │     |       └─→ Create context + all reports
  │     |
  │     YES ──→ force_refresh?
  │               |
  │               YES ──→ FULL ANALYSIS
  │               |
  │               NO ──→ Detect changes
  │                       |
  │                       ├─→ No changes: Load context, report status
  │                       └─→ Changes detected: INCREMENTAL ANALYSIS
  │                             ├─→ n8n workflows changed? → Invoke n8n-Expert
  │                             └─→ Update context + affected reports
END
```


#### Example



**Code:**
```markdown
# Full-Stack Analysis: {PROJECT_NAME}

**Last Analyzed**: {TIMESTAMP}
**Analysis Type**: {FULL|INCREMENTAL}
**Components**: Frontend/Backend + n8n Workflows
**Overall Health**: {SCORE}/10 {🟢|🟡|🟠|🔴}

---

## 📊 Executive Summary

**Codebase Health**: {X}/10
**n8n Workflow Health**: {X}/10 (if detected)
**Integration Status**: {🟢 Healthy | 🟡 Issues | 🔴 Critical}

### 🎯 Top Priorities:
1. **{ACTION_1}** (Codebase) - {IMPACT}
2. **{ACTION_2}** (n8n) - {IMPACT}
3. **{ACTION_3}** (Integration) - {IMPACT}

### 🔗 n8n Integration Status:
**Detected**: {YES|NO}
- Workflows: {COUNT}
- Webhook Endpoints: {COUNT}
- Integration Health: {SCORE}/10

**Details**: See [n8n-workflows/analysis-report.md](n8n-workflows/analysis-report.md)

---

## 🏗️ Architecture

**Pattern**: {IDENTIFIED_PATTERN}
**Stack**: {TECH_STACK}

### Integration Flow:
```


#### Example



**Code:**
```bash

**Architecture Details**: [architecture.md](architecture.md)

---

## 📦 Dependencies

**Codebase**: {COUNT} total ({OUTDATED} outdated)
**n8n**: Version {VERSION} (Latest: {LATEST})

**Critical Updates**:
| Package | Current | Latest | Severity |
|---------|---------|--------|----------|
| {PKG}   | {VER}   | {VER}  | {LEVEL}  |

**Full Details**: [dependencies.json](dependencies.json)

---

## ✅ Code Quality

| Component | Score | Status |
|-----------|-------|--------|
| Frontend Code | {X}/10 | {🟢|🟡|🔴} |
| n8n Workflows | {X}/10 | {🟢|🟡|🔴} |
| Integration | {X}/10 | {🟢|🟡|🔴} |

---

## 🚀 Unified Upgrade Plan

**Full Roadmap**: [upgrade-plan.md](upgrade-plan.md)

### Phase 1: Critical (This Week)
- [ ] {CODEBASE_ACTION}
- [ ] {N8N_ACTION}
- [ ] {INTEGRATION_FIX}

### Phase 2: Structural (This Month)
- [ ] {IMPROVEMENT_1}
- [ ] {IMPROVEMENT_2}

### Phase 3: Major Upgrades (This Quarter)
- [ ] {MAJOR_UPGRADE}

---

## 📝 Next Steps

⚠️ **All changes require explicit approval**

**Ready to start?** Say:
- "Arbeite an {project-slug}" or
- "Start Phase 1 for {project-slug}"

---

**Context**: `knowledge/external-projects/{slug}/`
**Agents Used**: codebase-analyzer, n8n-expert (if applicable)
```


#### Example



**Code:**
```bash
Task(
  subagent_type="n8n-expert-agent",
  prompt=f"""
Analyze n8n workflows for project: {project_name}

{json.dumps(n8n_context, indent=2)}

Write analysis to: knowledge/external-projects/{slug}/n8n-workflows/
"""
)
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/codebase-analyzer-agent.md`</small>
