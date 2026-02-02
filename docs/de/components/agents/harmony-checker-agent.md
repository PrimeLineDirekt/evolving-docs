---
title: harmony-checker-agent
type: agent
tags: []
lang: en
confidence: 100
---

# harmony-checker-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2026-01-08 |</div>


## What It Does

"Prüft Style-Konsistenz mit dynamischem Domain-Expert via Trait-System"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "finding": {
    "name": "Context-Manager",
    "type": "agent",
    "path": ".claude/agents/context-manager-agent.md",
    "source_repo": "github.com/some/repo",
    "tags": ["llm-proc", "context", "Memory"],
    "description": "This amazing agent manages context for LLM processing!",
    "frontmatter": {
      "agent_version": "1.0",
      "model": "opus"
    }
  }
}
```


#### Example



**Code:**
```python
def check_harmony(finding):
    checks = {}
    scores = []

    # 0. Domain Detection + Expert Composition (NEW!)
    domain_context = detect_domain(finding)
    domain_expert = compose_domain_expert(domain_context)

    checks["domain"] = domain_context

    # 1. Naming Style (generisch)
    checks["naming"] = check_naming_style(finding)
    scores.append(checks["naming"]["score"])

    # 2. Tag Consistency (mit Domain-Expert!)
    checks["tags"] = check_tag_consistency(finding, domain_expert)
    scores.append(checks["tags"]["score"])

    # 3. Schema Validation (generisch)
    checks["schema"] = check_schema(finding)
    scores.append(checks["schema"]["score"])

    # 4. Relation Suggestions (mit Domain-Expert!)
    checks["relations"] = suggest_relations(finding, domain_expert)
    # Relations don't affect score, just suggestions

    # Calculate overall score
    harmony_score = sum(scores) / len(scores)

    # Collect suggestions
    suggestions = []
    for check_name, result in checks.items():
        if result.get("suggestions"):
            suggestions.extend(result["suggestions"])

    # Determine if auto-fixable
    auto_fixable = all(
        s.get("auto_fix", False) for s in suggestions
    ) if suggestions else True

    return {
        "harmony_score": round(harmony_score, 1),
        "domain_expert": domain_expert,
        "checks": checks,
        "suggestions": suggestions,
        "auto_fixable": auto_fixable
    }
```


#### Example



**Code:**
```python
def detect_domain(finding):
    source_repo = finding.get("source_repo", "")
    tags = finding.get("tags", [])
    keywords = finding.get("keywords", [])
    description = finding.get("description", "")

    # Alle Signale sammeln
    signals = tags + keywords + source_repo.split("/") + description.lower().split()

    # Domain-Mapping
    domain_patterns = {
        "rag": ["rag", "retrieval", "embedding", "vector", "chunk", "document"],
        "llm": ["llm", "prompt", "token", "context", "model", "inference"],
        "web-scraping": ["scrape", "crawl", "spider", "extract", "parse", "html"],
        "api": ["api", "rest", "graphql", "endpoint", "request", "response"],
        "automation": ["workflow", "automation", "pipeline", "orchestration", "n8n"],
        "security": ["security", "auth", "token", "encrypt", "vulnerability"],
        "data": ["data", "analytics", "etl", "transform", "pipeline", "database"],
        "frontend": ["react", "vue", "angular", "component", "ui", "css"],
        "backend": ["fastapi", "django", "express", "server", "middleware"],
        "devops": ["docker", "kubernetes", "ci", "cd", "deploy", "infra"],
        "ml": ["machine-learning", "training", "model", "tensorflow", "pytorch"]
    }

    # Score berechnen
    domain_scores = {}
    for domain, patterns in domain_patterns.items():
        score = sum(1 for s in signals if any(p in s.lower() for p in patterns))
        if score > 0:
            domain_scores[domain] = score

    # Top Domain(s)
    if not domain_scores:
        return {"domain": "general", "confidence": 0.5, "signals": []}

    top_domain = max(domain_scores, key=domain_scores.get)
    confidence = min(1.0, domain_scores[top_domain] / 5)

    return {
        "domain": top_domain,
        "confidence": round(confidence, 2),
        "signals": [s for s in signals if any(p in s.lower() for p in domain_patterns.get(top_domain, []))][:5],
        "all_domains": domain_scores
    }
```


#### Example



**Code:**
```python
def compose_domain_expert(domain_context):
    domain = domain_context["domain"]

    # Domain → Trait Mapping
    trait_mapping = {
        # Domain: (expertise, personality, approach)
        "rag":          ("researcher", "thorough", "systematic"),
        "llm":          ("researcher", "precise", "exploratory"),
        "web-scraping": ("engineer", "cautious", "systematic"),
        "api":          ("architect", "precise", "systematic"),
        "automation":   ("engineer", "direct", "iterative"),
        "security":     ("security", "cautious", "adversarial"),
        "data":         ("analyst", "thorough", "systematic"),
        "frontend":     ("engineer", "creative", "iterative"),
        "backend":      ("architect", "precise", "systematic"),
        "devops":       ("engineer", "cautious", "systematic"),
        "ml":           ("researcher", "skeptical", "exploratory"),
        "general":      ("analyst", "direct", "systematic")
    }

    expertise, personality, approach = trait_mapping.get(domain, trait_mapping["general"])

    # Compose Agent via Task Tool
    expert_prompt = f"""
    Du bist ein Domain-Expert für {domain.upper()}.

    Trait-Profil:
    - Expertise: {expertise}
    - Personality: {personality}
    - Approach: {approach}

    Deine Aufgabe: Analysiere Findings aus dieser Domain und schlage vor:
    1. Passende Tags (aus deinem Domain-Wissen)
    2. Sinnvolle Relationen zu existierenden Patterns/Learnings
    3. Domain-spezifische Namenskonventionen

    Antworte IMMER mit strukturiertem JSON.
    """

    return {
        "domain": domain,
        "expertise": expertise,
        "personality": personality,
        "approach": approach,
        "prompt": expert_prompt,
        "model": "haiku"  # Schnell + günstig für Tag/Relation Vorschläge
    }
```


#### Example



**Code:**
```python
def get_domain_tags(domain):
    """Domain-spezifische Tag-Vorschläge"""
    domain_tags = {
        "rag": ["retrieval", "embedding", "chunking", "vector-store", "document-processing"],
        "llm": ["prompt-engineering", "token-optimization", "context-window", "inference"],
        "web-scraping": ["scraping", "parsing", "extraction", "crawling", "html-processing"],
        "api": ["rest-api", "endpoints", "request-handling", "response-format"],
        "automation": ["workflow", "orchestration", "pipeline", "scheduling"],
        "security": ["authentication", "authorization", "encryption", "vulnerability"],
        "data": ["data-processing", "etl", "transformation", "analytics"],
        "frontend": ["ui-components", "styling", "state-management", "rendering"],
        "backend": ["server", "middleware", "database", "routing"],
        "devops": ["deployment", "containerization", "ci-cd", "infrastructure"],
        "ml": ["training", "model", "dataset", "evaluation", "optimization"]
    }
    return domain_tags.get(domain, [])
```


#### Example



**Code:**
```python
def check_naming_style(finding):
    name = finding["name"]
    ftype = finding["type"]
    is_external = finding.get("source_repo") is not None

    issues = []
    suggestions = []
    score = 10

    # 1. Case Check (should be kebab-case)
    if not is_kebab_case(name):
        issues.append("Not kebab-case")
        score -= 3
        suggestions.append({
            "type": "naming",
            "issue": "Invalid case",
            "current": name,
            "suggested": to_kebab_case(name),
            "auto_fix": True
        })

    # 2. Suffix Check
    expected_suffix = get_expected_suffix(ftype)
    if expected_suffix and not name.endswith(expected_suffix):
        issues.append(f"Missing {expected_suffix} suffix")
        score -= 2
        suggestions.append({
            "type": "naming",
            "issue": "Missing suffix",
            "current": name,
            "suggested": f"{name}-{expected_suffix.strip('-')}",
            "auto_fix": True
        })

    # 3. External Prefix
    if is_external and not name.startswith("ext-"):
        issues.append("External finding should have ext- prefix")
        score -= 1
        suggestions.append({
            "type": "naming",
            "issue": "Missing ext- prefix",
            "current": name,
            "suggested": f"ext-{name}",
            "auto_fix": True
        })

    return {
        "score": max(1, score),
        "issues": issues,
        "suggestions": suggestions
    }

def is_kebab_case(s):
    return s == s.lower() and " " not in s and "_" not in s

def to_kebab_case(s):
    # CamelCase -> kebab-case
    import re
    s = re.sub(r'([A-Z])', r'-\1', s).lower()
    s = re.sub(r'[_\s]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')

def get_expected_suffix(ftype):
    suffixes = {
        "agent": "-agent",
        "pattern": "-pattern"
    }
    return suffixes.get(ftype)
```


#### Example



**Code:**
```python
def check_tag_consistency(finding, domain_expert=None):
    tags = finding.get("tags", [])
    taxonomy = json.loads(Read("_graph/taxonomy.json"))
    valid_tags = set(taxonomy.get("tags", []))

    # NEU: Domain-spezifische Tags hinzufügen
    if domain_expert:
        domain_tags = get_domain_tags(domain_expert["domain"])
        valid_tags.update(domain_tags)

    issues = []
    suggestions = []
    score = 10

    normalized_tags = []

    for tag in tags:
        # 1. Case Check
        if tag != tag.lower():
            issues.append(f"Tag '{tag}' not lowercase")
            score -= 1
            tag_normalized = tag.lower()
        else:
            tag_normalized = tag

        # 2. Format Check
        if "_" in tag_normalized or " " in tag_normalized:
            issues.append(f"Tag '{tag}' not kebab-case")
            score -= 1
            tag_normalized = tag_normalized.replace("_", "-").replace(" ", "-")

        # 3. Taxonomy Check
        if tag_normalized not in valid_tags:
            # Find similar valid tag
            similar = find_similar_tag(tag_normalized, valid_tags)
            if similar:
                suggestions.append({
                    "type": "tag",
                    "issue": "Non-standard tag",
                    "current": tag,
                    "suggested": similar,
                    "auto_fix": True
                })
                score -= 0.5
                tag_normalized = similar
            else:
                # New tag - suggest adding to taxonomy
                suggestions.append({
                    "type": "tag",
                    "issue": "Unknown tag (consider adding to taxonomy)",
                    "current": tag_normalized,
                    "suggested": tag_normalized,
                    "auto_fix": False
                })

        normalized_tags.append(tag_normalized)

    # 4. Count Check
    if len(tags) > 5:
        issues.append(f"Too many tags ({len(tags)}, max 5)")
        score -= 1
        suggestions.append({
            "type": "tag",
            "issue": "Too many tags",
            "current": tags,
            "suggested": normalized_tags[:5],
            "auto_fix": True
        })

    # 5. Marketing Check
    marketing_words = ["amazing", "best", "powerful", "ultimate", "perfect"]
    for tag in tags:
        if any(m in tag.lower() for m in marketing_words):
            issues.append(f"Marketing tag '{tag}'")
            score -= 2

    return {
        "score": max(1, score),
        "issues": issues,
        "suggestions": suggestions,
        "normalized_tags": list(set(normalized_tags))[:5]
    }

def find_similar_tag(tag, valid_tags, threshold=0.7):
    """Find most similar valid tag"""
    best_match = None
    best_score = 0

    for valid in valid_tags:
        sim = calculate_similarity(tag, valid)
        if sim > best_score and sim >= threshold:
            best_match = valid
            best_score = sim

    return best_match
```


#### Example



**Code:**
```python
def check_schema(finding):
    ftype = finding["type"]
    frontmatter = finding.get("frontmatter", {})

    required_fields = get_required_fields(ftype)
    issues = []
    suggestions = []
    score = 10

    # Check each required field
    for field in required_fields:
        # Check in frontmatter first, then in finding itself
        if field not in frontmatter and field not in finding:
            issues.append(f"Missing required field: {field}")
            score -= 2

            # Suggest default value
            default = get_default_value(field, ftype)
            suggestions.append({
                "type": "schema",
                "issue": f"Missing {field}",
                "field": field,
                "suggested_value": default,
                "auto_fix": default is not None
            })

    # Check description quality
    desc = finding.get("description", frontmatter.get("description", ""))
    if desc:
        desc_issues = check_description_quality(desc)
        issues.extend(desc_issues["issues"])
        suggestions.extend(desc_issues["suggestions"])
        score -= len(desc_issues["issues"]) * 0.5

    return {
        "score": max(1, score),
        "issues": issues,
        "suggestions": suggestions
    }

def get_required_fields(ftype):
    schemas = {
        "agent": ["agent_version", "agent_type", "model", "description"],
        "command": ["description"],
        "template": ["description"],
        "pattern": ["description"],
        "learning": ["description"]
    }
    return schemas.get(ftype, ["description"])

def get_default_value(field, ftype):
    defaults = {
        "agent_version": "1.0",
        "agent_type": "specialist",
        "model": "sonnet"
    }
    return defaults.get(field)

def check_description_quality(desc):
    issues = []
    suggestions = []

    # Too long
    if len(desc) > 200:
        issues.append("Description too long (>200 chars)")
        suggestions.append({
            "type": "description",
            "issue": "Too long",
            "current": desc,
            "suggested": desc[:200] + "...",
            "auto_fix": False
        })

    # Marketing speak
    marketing = ["amazing", "powerful", "best", "ultimate", "revolutionary"]
    for word in marketing:
        if word in desc.lower():
            issues.append(f"Marketing language: '{word}'")
            suggestions.append({
                "type": "description",
                "issue": f"Remove '{word}'",
                "auto_fix": False
            })

    # Starts with "This"
    if desc.strip().startswith("This"):
        issues.append("Description starts with 'This'")
        suggestions.append({
            "type": "description",
            "issue": "Avoid starting with 'This'",
            "current": desc,
            "suggested": desc.replace("This ", "", 1).capitalize(),
            "auto_fix": True
        })

    return {"issues": issues, "suggestions": suggestions}
```


#### Example



**Code:**
```python
def suggest_relations(finding, domain_expert=None):
    nodes = json.loads(Read("_graph/knowledge-nodes.json"))
    finding_tags = set(finding.get("tags", []))

    # NEU: Domain-Tags für besseres Matching hinzufügen
    if domain_expert:
        domain = domain_expert["domain"]
        domain_tags = get_domain_tags(domain)
        # Erweitere Finding-Tags mit passenden Domain-Tags
        finding_tags.update([t for t in domain_tags if any(
            t in tag or tag in t for tag in finding.get("tags", [])
        )])

    suggestions = []

    for node in nodes["nodes"]:
        node_tags = set(node.get("tags", []))
        overlap = finding_tags & node_tags

        # NEU: Domain-basiertes Boosting
        domain_boost = 0
        if domain_expert and node.get("domain") == domain_expert["domain"]:
            domain_boost = 1  # Nodes aus gleicher Domain bevorzugen

        relevance_score = len(overlap) + domain_boost

        if len(overlap) >= 1 or domain_boost > 0:  # Threshold gesenkt dank Domain-Kontext
            suggestions.append({
                "type": "relation",
                "target": node["id"],
                "target_name": node["name"],
                "shared_tags": list(overlap),
                "relation_type": determine_relation_type(finding, node),
                "domain_match": domain_boost > 0,
                "relevance_score": relevance_score,
                "auto_fix": True
            })

    # Sort by relevance (domain boost + shared tags)
    suggestions.sort(key=lambda x: -x["relevance_score"])

    return {
        "suggestions": suggestions[:5],  # Top 5
        "total_found": len(suggestions),
        "domain_context": domain_expert["domain"] if domain_expert else None
    }

def determine_relation_type(finding, node):
    if finding["type"] == node["type"]:
        return "sibling"
    if finding["type"] == "pattern" and node["type"] == "learning":
        return "implements"
    if finding["type"] == "learning" and node["type"] == "pattern":
        return "learned_from"
    return "related_to"
```


#### Example



**Code:**
```json
{
  "harmony_score": 7.5,
  "domain_expert": {
    "domain": "rag",
    "expertise": "researcher",
    "personality": "thorough",
    "approach": "systematic"
  },
  "checks": {
    "domain": {
      "domain": "rag",
      "confidence": 0.8,
      "signals": ["retrieval", "embedding", "chunk"]
    },
    "naming": {
      "score": 7,
      "issues": ["Not kebab-case"],
      "suggestions": [{"type": "naming", "current": "Context-Manager", "suggested": "context-manager"}]
    },
    "tags": {
      "score": 8,
      "issues": ["Tag 'llm-proc' not in taxonomy"],
      "suggestions": [{"type": "tag", "current": "llm-proc", "suggested": "llm-processing"}]
    },
    "schema": {
      "score": 8,
      "issues": ["Description starts with 'This'"],
      "suggestions": [...]
    },
    "relations": {
      "suggestions": [
        {
          "target": "pattern-context-window",
          "shared_tags": ["context", "llm"],
          "domain_match": true,
          "relevance_score": 3
        }
      ],
      "domain_context": "rag"
    }
  },
  "suggestions": [...],
  "auto_fixable": true
}
```


#### Example



**Code:**
```bash
@harmony-checker-agent
{
  "finding": {
    "name": "Context-Manager",
    "type": "agent",
    "path": ".claude/agents/context-manager-agent.md",
    "source_repo": "github.com/some/repo",
    "tags": ["llm-proc", "context"],
    "description": "This amazing agent...",
    "frontmatter": {...}
  }
}
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/harmony-checker-agent.md`</small>
