---
title: comprehensive-audit-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# comprehensive-audit-pattern


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does



### Key Features

- **Tech Stack** (Python, Node.js, Java, Go, Rust, etc.)
- **Architecture** (Monolith, Microservices, Serverless, etc.)
- **Features** (`has_api`, `has_ml`, `has_tests`, `has_docs`, etc.)
- **Project Maturity** (MVP, Production, Legacy)
- **Security auditor**: Always
- **Code-quality auditor**: Always
- **Architecture auditor**: Always
- **Performance auditor**: If performance-sensitive (backend, ML)
- **Documentation auditor**: Always
- **Prompt auditor**: If ML/AI code detected
- **API routes auditor**: If REST/GraphQL API detected
- **Business-logic auditor**: If business logic complexity > threshold
- **Tier 1 (Opus)**: Security, Architecture, Business Logic (critical analysis)
- **Tier 2 (Sonnet)**: Code Quality, Performance, Documentation, Prompts, API Routes (standard)
- **Tier 3 (Haiku)**: Reporter (structured output)
- Cost-Performance Balance**: Uses Opus only for critical dimensions where reasoning depth matters most.
- **Root Cause Analysis**: "Architecture issue causing performance bottleneck"
- **Pattern Detection**: "Consistent error handling gaps across 3 dimensions"
- **Severity Scoring**: CVSS-like scoring across security, quality, architecture
- **Remediation Prioritization**: Quick wins vs. strategic improvements
- **Phase 1 (Week 1)**: Critical security fixes, high-impact quick wins
- **Phase 2 (Week 2-3)**: Architecture improvements, technical debt reduction
- **Phase 3 (Month 2)**: Optional enhancements, long-term scalability
- Effort estimate (hours/days)
- Dependencies on other fixes
- Success criteria
- Code pointers or file locations

## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────────────┐
│ PHASE 1: INTAKE (Sequential)                            │
│                                                         │
│ @audit-intake-agent                                     │
│ ├─ Analyze project structure                            │
│ ├─ Detect tech stack                                    │
│ ├─ Identify feature flags                               │
│ └─ Select auditors based on capabilities                │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│ PHASE 2: PARALLEL AUDITS (Parallel Execution)           │
│                                                         │
│ Batch 1 (Opus - Critical):                              │
│ ├─ @security-auditor                                    │
│ ├─ @architecture-auditor                                │
│ └─ @business-logic-auditor                              │
│                                                         │
│ Batch 2 (Sonnet - Standard):                            │
│ ├─ @code-quality-auditor                                │
│ ├─ @performance-auditor                                 │
│ └─ @documentation-auditor                               │
│                                                         │
│ Batch 3 (Sonnet - Optional):                            │
│ ├─ @prompt-auditor (if AI/ML code detected)             │
│ └─ @api-routes-auditor (if API detected)                │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│ PHASE 3: CORRELATION (Sequential)                       │
│                                                         │
│ @audit-coordinator                                      │
│ ├─ Synthesize findings across dimensions                │
│ ├─ Identify root causes (not just symptoms)             │
│ ├─ Cross-audit patterns                                 │
│ └─ Generate priority scoring                            │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│ PHASE 4: REPORT (Sequential)                            │
│                                                         │
│ @audit-reporter                                         │
│ ├─ Executive Summary (1 page)                           │
│ ├─ Detailed Findings (per dimension)                    │
│ ├─ Risk Prioritization (Critical/High/Medium/Low)       │
│ ├─ Quick Wins (top 3)                                   │
│ └─ Remediation Roadmap (phased, effort-estimated)       │
└─────────────────────────────────────────────────────────┘
```


#### Example



**Code:**
```bash
/full-audit ~/Projects/auswanderungs-ki-v2
/full-audit ~/Projects/auswanderungs-ki-v2 --deep  # Extended analysis
```


#### Example



**Code:**
```bash
/audit-security ~/Projects/my-app
/audit-security ~/Projects/my-app --owasp      # Only OWASP Top 10
/audit-security ~/Projects/my-app --secrets    # Only secrets
/audit-security ~/Projects/my-app --deps       # Only dependencies
```


#### Example



**Code:**
```bash
/audit-report                                   # Default: markdown, all sections
/audit-report --format html --type summary      # HTML, summary only
/audit-report --format json --from latest       # JSON from latest audit
```


#### Example



**Code:**
```json
"tier1": {
  "model": "opus",
  "agents": ["security-auditor", "my-critical-auditor"]
}
```


#### Example



**Code:**
```bash
/full-audit ~/Projects/production-candidate
→ Validates readiness for production
→ Identifies critical security/performance gaps
```


#### Example



**Code:**
```bash
/quick-audit ~/Projects/active-project
→ Fast daily check (5-8 min)
→ Catches regressions early
```


#### Example



**Code:**
```bash
/full-audit ~/Projects/acquired-codebase --deep
→ Complete assessment for valuation
→ Long-term maintenance planning
```


#### Example



**Code:**
```bash
/full-audit ~/Projects/legacy-system
→ Tech debt quantification
→ Modernization roadmap
→ Risk assessment
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/comprehensive-audit-pattern.md`</small>
