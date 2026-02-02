---
title: github-repo-analyzer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# github-repo-analyzer-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2025-12-01 |</div>


## What It Does

"Dual-System Repository Analyzer with SYSTEM-MAP integration and contextual findings"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "repo_source": "{GitHub URL or local path}",
  "analysis_depth": "deep",
  "focus_areas": ["patterns", "architecture", "documentation", "testing"],
  "context": "Evolving Knowledge Management System",
  "output": "Integration Roadmap with SYSTEM-MAP update"
}
```


#### Example



**Code:**
```python
def load_system_context():
    system_map = Read(".claude/SYSTEM-MAP.md")

    context = {
        "agents": extract_agents(system_map),
        "skills": extract_skills(system_map),
        "commands": extract_commands(system_map),
        "hooks": extract_hooks(system_map),
        "templates": extract_templates(system_map),
        "prompts": extract_prompts(system_map),
        "patterns": extract_patterns(system_map),
        "knowledge_structure": extract_kb_structure(system_map),
        "integration_points": extract_integration_points(system_map),
        "naming_conventions": extract_conventions(system_map)
    }

    return context
```


#### Example



**Code:**
```python
def analyze_remote_repo(github_url):
    # Extract owner/repo
    owner, repo = parse_github_url(github_url)
    base_raw = f"https://raw.githubusercontent.com/{owner}/{repo}/main"

    # Core files
    readme = WebFetch(f"{base_raw}/README.md")
    package_json = WebFetch(f"{base_raw}/package.json")  # or pyproject.toml

    # Structure analysis via GitHub
    structure = WebFetch(github_url)  # Parse directory listing

    # Key files based on structure
    for important_file in identify_key_files(structure):
        content = WebFetch(f"{base_raw}/{important_file}")
        analyze_file(content)

    return findings
```


#### Example



**Code:**
```python
def analyze_local_repo(repo_path):
    # Structure
    files = Glob(f"{repo_path}/**/*")

    # Key files
    readme = Read(f"{repo_path}/README.md")
    config = Read(f"{repo_path}/package.json")  # or equivalent

    # Pattern search
    patterns = Grep(pattern="class|function|export", path=repo_path)

    # Git metadata
    git_log = Bash(f"cd {repo_path} && git log --oneline -20")

    return findings
```


#### Example



**Code:**
```python
def map_finding_to_system(finding, system_context):
    mapping = {
        "finding": finding.name,
        "description": finding.description,
        "category": None,  # NEU, BESSER, ANDERS, REDUNDANT
        "evolving_equivalent": None,
        "comparison": None,
        "integration": None,
        "action": None
    }

    # Check if we have equivalent
    equivalent = find_equivalent(finding, system_context)

    if not equivalent:
        mapping["category"] = "NEU"
        mapping["integration"] = suggest_integration_point(finding, system_context)
        mapping["action"] = f"Add to {mapping['integration']}"

    elif is_better_than(finding, equivalent):
        mapping["category"] = "BESSER"
        mapping["evolving_equivalent"] = equivalent
        mapping["comparison"] = compare(finding, equivalent)
        mapping["action"] = f"Upgrade {equivalent} with {finding.improvements}"

    elif is_different_approach(finding, equivalent):
        mapping["category"] = "ANDERS"
        mapping["evolving_equivalent"] = equivalent
        mapping["comparison"] = {
            "their_approach": finding.approach,
            "our_approach": equivalent.approach,
            "tradeoffs": analyze_tradeoffs(finding, equivalent)
        }
        mapping["action"] = "Evaluate and decide"

    else:
        mapping["category"] = "REDUNDANT"
        mapping["evolving_equivalent"] = equivalent
        mapping["action"] = "Document for reference only"

    return mapping
```


#### Example



**Code:**
```python
def create_integration_plan(mapped_findings, system_context):
    plan = {
        "quick_wins": [],      # < 1h effort
        "medium_effort": [],   # 1-4h effort
        "larger_projects": []  # > 4h effort
    }

    for finding in mapped_findings:
        if finding["category"] in ["NEU", "BESSER"]:
            integration = {
                "finding": finding["finding"],
                "action": finding["action"],
                "target_location": determine_location(finding, system_context),
                "files_to_create": list_new_files(finding),
                "files_to_modify": list_modifications(finding),
                "effort": estimate_effort(finding),
                "priority": calculate_priority(finding)
            }

            if integration["effort"] == "quick":
                plan["quick_wins"].append(integration)
            elif integration["effort"] == "medium":
                plan["medium_effort"].append(integration)
            else:
                plan["larger_projects"].append(integration)

    return plan
```


#### Example



**Code:**
```markdown
# Repository Analysis Report: {REPO_NAME}

## Executive Summary

| Metric | Value |
|--------|-------|
| **Repository** | {owner/repo} |
| **Purpose** | {1-sentence description} |
| **Tech Stack** | {main technologies} |
| **Relevance for Evolving** | {X}/10 |
| **Integration Potential** | {X}/10 |
| **Actionable Findings** | {count} |

---

## Phase 1: Evolving System Context

SYSTEM-MAP.md loaded. Current system state:
- Agents: {count}
- Skills: {count}
- Commands: {count}
- Patterns: {list relevant patterns}

---

## Phase 2: Repository Deep Dive

### Purpose & Features
{Description of what the repo does}

### Tech Stack
| Technology | Purpose |
|------------|---------|
| {tech} | {purpose} |

### Architecture
{Key architectural decisions}

### Key Patterns Found
1. **{Pattern 1}**: {Description}
2. **{Pattern 2}**: {Description}

---

## Phase 3: Mapping & Abgleich

### 🟢 NEU - We Don't Have This

| Finding | Description | Integration Point | Action |
|---------|-------------|-------------------|--------|
| {name} | {desc} | {where in Evolving} | {what to do} |

### 🟡 BESSER - Upgrade Potential

| Finding | Our Current | Difference | Recommendation |
|---------|-------------|------------|----------------|
| {name} | {our version} | {what's better} | {suggested action} |

### 🔵 ANDERS - Alternative Approaches

| Finding | Our Approach | Their Approach | Assessment |
|---------|--------------|----------------|------------|
| {name} | {how we do it} | {how they do it} | {which is better and why} |

### ⚪ REDUNDANT - Already Have

| Finding | Our Equivalent |
|---------|----------------|
| {name} | {our version} |

---

## Phase 4: Integration Roadmap

### Quick Wins (< 1h)
- [ ] {Action 1} → {Target file/location}
- [ ] {Action 2} → {Target file/location}

### Medium Effort (1-4h)
- [ ] {Action 1}
  - Files to create: {list}
  - Files to modify: {list}

### Larger Projects (> 4h)
- [ ] {Project description}
  - Scope: {description}
  - Effort: {estimate}

---

## SYSTEM-MAP Update Required

Add to `.claude/SYSTEM-MAP.md` Changelog:

| Datum | Quelle | Finding | Integration | Status |
|-------|--------|---------|-------------|--------|
| {today} | {repo} | {finding 1} | {action} | Pending |
| {today} | {repo} | {finding 2} | {action} | Pending |

---

## Next Steps

1. {Immediate action}
2. {Follow-up action}
3. {Long-term consideration}

---

**Analysis Completed**: {timestamp}
**Findings**: {total count}
**Actionable**: {actionable count}
**SYSTEM-MAP Update**: Required
```


#### Example



**Code:**
```bash
IF .claude/SYSTEM-MAP.md not found:
  Warn user: "SYSTEM-MAP.md missing. Run system scan first."
  Offer to create it
```


#### Example



**Code:**
```bash
IF WebFetch fails:
  Try alternative URLs
  Suggest cloning locally for deep analysis
  Provide partial analysis with limitations noted
```


#### Example



**Code:**
```bash
IF all findings are REDUNDANT:
  Document the comparison
  Note "No actionable integrations"
  Update SYSTEM-MAP with analysis timestamp
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/github-repo-analyzer-agent.md`</small>
