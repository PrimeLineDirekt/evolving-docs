---
title: n8n-expert-agent
type: agent
tags: []
lang: en
confidence: 100
---

# n8n-expert-agent


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

"n8n workflow analysis, optimization, and validation with automatic documentation fetching"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "workflow_directory": "string (path to n8n workflows)",
  "workflow_files": ["array of .json workflow file paths"],
  "n8n_version": "string (e.g., '1.15.0') or null",
  "integration_context": {
    "webhook_calls": [
      {
        "file": "src/api/route.ts",
        "line": 42,
        "url": "https://app.n8n.cloud/webhook/profile-analysis",
        "method": "POST",
        "payload_structure": {
          "userId": "string",
          "profileData": "object"
        }
      }
    ],
    "expected_responses": [
      {
        "webhook": "profile-analysis",
        "expected_fields": ["analysis", "recommendations", "score"],
        "data_types": {
          "analysis": "object",
          "recommendations": "array",
          "score": "number"
        }
      }
    ]
  },
  "frontend_expectations": {
    "data_structures": ["TypeScript interfaces or schemas"],
    "error_handling": "description of error handling"
  },
  "context_path": "string (knowledge/external-projects/{slug}/)"
}
```


#### Example



**Code:**
```json
{
  "agent_id": "n8n-expert",
  "execution_id": "uuid",
  "priority_level": "HIGH",
  "time_allocation": "Varies by workflow_count",
  "success_criteria": "Error-free workflows + best practices + integration validation"
}
```


#### Example



**Code:**
```python
def fetch_n8n_docs(workflow_data):
    """
    Automatically fetch relevant n8n documentation for workflow analysis.
    """
    docs_cache = {}

    # 1. Identify unique nodes in workflows
    unique_nodes = extract_unique_node_types(workflow_data)

    # 2. Fetch docs for each node type
    for node_type in unique_nodes:
        # Example: "n8n-nodes-base.httpRequest"
        node_name = node_type.replace("n8n-nodes-base.", "")
        doc_url = f"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.{node_name}/"

        # Fetch using WebFetch
        docs_cache[node_type] = WebFetch(
            url=doc_url,
            prompt=f"Extract key information about the {node_name} node: parameters, best practices, common issues, examples"
        )

    # 3. Fetch general best practices
    docs_cache["best_practices"] = WebFetch(
        url="https://docs.n8n.io/workflows/best-practices/",
        prompt="Extract n8n workflow best practices: performance, error handling, naming, organization"
    )

    # 4. Fetch error handling guide
    docs_cache["error_handling"] = WebFetch(
        url="https://docs.n8n.io/workflows/error-handling/",
        prompt="Extract error handling patterns, retry logic, error workflows"
    )

    return docs_cache
```


#### Example



**Code:**
```python
def extract_unique_node_types(workflow_files):
    """
    Parse workflows and extract all unique node types.
    """
    node_types = set()

    for workflow_file in workflow_files:
        workflow = Read(workflow_file)
        workflow_json = json.loads(workflow)

        for node in workflow_json.get("nodes", []):
            node_type = node.get("type")
            if node_type:
                node_types.add(node_type)

    return list(node_types)
```


#### Example



**Code:**
```python
def analyze_node(node, workflow_context, docs):
    analysis = {
        "node_id": node["id"],
        "node_name": node.get("name", "Unnamed"),
        "node_type": node["type"],
        "issues": [],
        "warnings": [],
        "optimization_opportunities": []
    }

    # 1. Check for missing credentials
    if node.get("credentials") is None and requires_credentials(node["type"]):
        analysis["issues"].append({
            "type": "missing_credentials",
            "severity": "critical",
            "message": f"Node '{node['name']}' requires credentials but none configured"
        })

    # 2. Validate parameters against documentation
    node_doc = docs.get(node["type"])
    if node_doc:
        required_params = extract_required_params(node_doc)
        node_params = node.get("parameters", {})

        for param in required_params:
            if param not in node_params:
                analysis["issues"].append({
                    "type": "missing_parameter",
                    "severity": "high",
                    "message": f"Missing required parameter: {param}"
                })

    # 3. Check for deprecated nodes
    if is_deprecated(node["type"], docs):
        analysis["warnings"].append({
            "type": "deprecated_node",
            "message": f"Node type {node['type']} is deprecated",
            "recommendation": get_replacement_node(node["type"], docs)
        })

    # 4. Performance optimization checks
    if node["type"] == "n8n-nodes-base.httpRequest":
        # Check timeout configuration
        timeout = node.get("parameters", {}).get("timeout", 300)
        if timeout > 60000:  # 60 seconds
            analysis["warnings"].append({
                "type": "long_timeout",
                "message": f"Timeout set to {timeout}ms, consider reducing"
            })

        # Check for batching opportunities
        if not node.get("parameters", {}).get("batching"):
            analysis["optimization_opportunities"].append({
                "type": "enable_batching",
                "impact": "medium",
                "message": "Enable batching for better performance with multiple items"
            })

    # 5. Error handling check
    if not node.get("continueOnFail", False) and is_critical_node(node, workflow_context):
        analysis["warnings"].append({
            "type": "no_error_handling",
            "message": "Critical node without error handling (continueOnFail: false)"
        })

    return analysis
```


#### Example



**Code:**
```python
def calculate_best_practices_score(workflow, best_practices_checklist):
    total_checks = len(best_practices_checklist)
    passed_checks = sum(1 for check in best_practices_checklist if check["passed"])

    score = (passed_checks / total_checks) * 10
    return round(score, 1)
```


#### Example



**Code:**
```json
{
  "priority": "critical|high|medium|low",
  "category": "performance|reliability|maintainability|security",
  "workflow": "workflow-name",
  "node": "node-name (if applicable)",
  "issue": "Description of current state",
  "recommendation": "What to do",
  "impact": "Expected improvement",
  "effort": "Implementation effort (hours)",
  "implementation": "Step-by-step guide"
}
```


#### Example



**Code:**
```markdown
# n8n Workflow Analysis: {PROJECT_NAME}

**Analyzed**: {TIMESTAMP}
**Workflows**: {COUNT}
**n8n Version**: {VERSION}
**Overall Health**: {SCORE}/10 {🟢|🟡|🟠|🔴}

---

## 📊 Executive Summary

**Total Workflows**: {COUNT}
**Healthy Workflows**: {COUNT} 🟢
**Workflows with Issues**: {COUNT} 🟠
**Critical Issues**: {COUNT} 🔴

### 🎯 Top Priorities:
1. **{ISSUE_1}** - {SEVERITY} - {WORKFLOW_NAME}
2. **{ISSUE_2}** - {SEVERITY} - {WORKFLOW_NAME}
3. **{ISSUE_3}** - {SEVERITY} - {WORKFLOW_NAME}

### 🔗 Integration Status:
**Webhook Mapping**: {X}/{Y} endpoints matched
**Data Structure Alignment**: {GOOD|ISSUES|CRITICAL}
**Frontend Compatibility**: {SCORE}/10

---

## 🔍 Workflow Inventory

| Workflow | Nodes | Health | Issues | Webhooks |
|----------|-------|--------|--------|----------|
| {NAME_1} | {N}   | 🟢     | 0      | /webhook/path-1 |
| {NAME_2} | {N}   | 🟠     | 3      | /webhook/path-2 |
| {NAME_3} | {N}   | 🔴     | 8      | -               |

---

## 🚨 Critical Issues

### 1. {ISSUE_TITLE}

**Workflow**: {NAME}
**Node**: {NODE_NAME}
**Severity**: Critical
**Type**: {ISSUE_TYPE}

**Problem**:
{DETAILED_DESCRIPTION}

**Impact**:
{WHAT_BREAKS}

**Fix**:
```


#### Example



**Code:**
```bash

**Priority**: Fix immediately before production use

---

### 2. {ISSUE_TITLE}

{SAME_STRUCTURE}

---

## ⚠️ Warnings & Optimization Opportunities

### Performance

- **{WORKFLOW_NAME}**: Enable batching on HTTP Request node
  - Impact: 50% reduction in execution time
  - Effort: 5 minutes

- **{WORKFLOW_NAME}**: Reduce timeout from 300s to 60s
  - Impact: Faster failure detection
  - Effort: 2 minutes

### Reliability

- **{WORKFLOW_NAME}**: Add retry logic to API call
  - Impact: Handle transient failures
  - Effort: 10 minutes

### Maintainability

- **{WORKFLOW_NAME}**: Rename nodes for clarity
  - Current: "HTTP Request", "HTTP Request1", "HTTP Request2"
  - Recommended: "Fetch User Profile", "Get Recommendations", "Send Email"
  - Effort: 5 minutes

---

## 🔗 Integration Analysis

### Webhook Mapping

| Frontend Call | Workflow | Status | Issues |
|---------------|----------|--------|--------|
| POST /webhook/profile | Profile Analysis | ✅ | None |
| POST /webhook/visa | Visa Workflow | ⚠️ | Method mismatch |
| POST /webhook/finance | - | ❌ | Not found |

### Data Structure Alignment

**Profile Analysis Workflow**:
- ✅ Returns `analysis` (object)
- ✅ Returns `recommendations` (array)
- ✅ Returns `score` (number)
- ❌ Missing `timestamp` field expected by frontend

**Recommendations**:
1. Add timestamp to response: `{{ $now.toISO() }}`
2. Update frontend to make timestamp optional (alternative)

---

## ✅ Best Practices Assessment

| Category | Score | Status |
|----------|-------|--------|
| Naming Conventions | 7/10 | 🟡 Needs improvement |
| Organization | 9/10 | 🟢 Good |
| Error Handling | 4/10 | 🔴 Poor |
| Performance | 6/10 | 🟡 Fair |
| Security | 8/10 | 🟢 Good |
| Maintainability | 7/10 | 🟡 Fair |

**Overall Best Practices Score**: {X}/10

### Detailed Assessment:

**Error Handling** (4/10):
- ❌ Only 30% of external API calls have error handling
- ❌ No error workflows configured
- ✅ Most nodes log errors properly

**Recommendations**:
1. Enable `continueOnFail: true` on all HTTP Request nodes
2. Create error workflow for critical failures
3. Add retry logic with exponential backoff

---

## 📚 Documentation References

**Fetched from docs.n8n.io**:

- [HTTP Request Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/)
- [Webhook Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/)
- [Best Practices](https://docs.n8n.io/workflows/best-practices/)
- [Error Handling](https://docs.n8n.io/workflows/error-handling/)

---

## 📝 Next Steps

### Immediate (This Week):
- [ ] Fix critical issue: {ISSUE}
- [ ] Add missing webhook: {WEBHOOK}
- [ ] Enable error handling on critical nodes

### Short-term (This Month):
- [ ] Implement all performance optimizations
- [ ] Standardize naming conventions
- [ ] Add workflow documentation

### Long-term (This Quarter):
- [ ] Refactor complex workflows
- [ ] Extract reusable sub-workflows
- [ ] Implement comprehensive error workflows

---

**Full Recommendations**: See [recommendations.md](recommendations.md)

**Workflow Copies**: See [workflows/](workflows/) directory
```


#### Example



**Code:**
```markdown
# n8n Optimization Recommendations: {PROJECT_NAME}

**Generated**: {TIMESTAMP}

---

## 🔴 Critical Priority (Fix Now)

### 1. {RECOMMENDATION_TITLE}

**Workflow**: {NAME}
**Node**: {NODE_NAME}
**Category**: Security
**Effort**: 10 minutes

**Current State**:
{DESCRIPTION}

**Recommended Action**:
{DETAILED_STEPS}

**Implementation**:
1. Open workflow "{WORKFLOW_NAME}"
2. Select node "{NODE_NAME}"
3. Enable "Continue on Fail" in settings
4. Add error branch connection
5. Test with failed scenario

**Expected Impact**:
- Prevent workflow crashes
- Graceful error handling
- Better user experience

---

{MORE_RECOMMENDATIONS}

---

## 🟠 High Priority

{HIGH_PRIORITY_RECOMMENDATIONS}

---

## 🟡 Medium Priority

{MEDIUM_PRIORITY_RECOMMENDATIONS}

---

## 🟢 Low Priority (Nice to Have)

{LOW_PRIORITY_RECOMMENDATIONS}

---

## Summary

**Total Recommendations**: {COUNT}
- Critical: {COUNT}
- High: {COUNT}
- Medium: {COUNT}
- Low: {COUNT}

**Estimated Total Effort**: {HOURS} hours

**Quick Wins** (< 30 min, high impact):
- {RECOMMENDATION_1}
- {RECOMMENDATION_2}
- {RECOMMENDATION_3}
```


#### Example



**Code:**
```python
def copy_workflows_to_analysis_dir(workflow_files, context_path):
    """
    Copy analyzed workflows to knowledge/external-projects/{slug}/n8n-workflows/workflows/
    for reference and version tracking.
    """
    target_dir = f"{context_path}/n8n-workflows/workflows/"

    for workflow_file in workflow_files:
        filename = os.path.basename(workflow_file)
        target_path = os.path.join(target_dir, filename)

        # Copy file
        content = Read(workflow_file)
        Write(target_path, content)
```


#### Example



**Code:**
```python
# Fetch specific node documentation
node_doc = WebFetch(
    url=f"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.{node_name}/",
    prompt=f"Extract key information about {node_name} node: parameters, best practices, common issues"
)

# Fetch best practices
best_practices = WebFetch(
    url="https://docs.n8n.io/workflows/best-practices/",
    prompt="Extract n8n workflow best practices"
)
```


#### Example



**Code:**
```bash
IF workflow JSON is invalid:
  Log specific parsing error
  Skip workflow, continue with others
  Report in analysis with error details
```


#### Example



**Code:**
```bash
IF WebFetch fails for docs.n8n.io:
  Use cached knowledge of common n8n patterns
  Flag as "limited analysis - docs unavailable"
  Provide generic recommendations
```


#### Example



**Code:**
```bash
IF integration_context is empty or null:
  Skip integration validation phase
  Focus on workflow-internal analysis only
  Note in report: "Integration validation skipped"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/n8n-expert-agent.md`</small>
