---
title: Template Creator
type: skill
tags: [core, automation, templates]
lang: en
confidence: 95
---

# Template Creator

![Template Creator Skill](../../shared/assets/infographics/skills/template-creator.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Create system components from standardized templates |
| **Complexity** | Low-Medium |
| **Model** | sonnet |
| **Category** | core |
</div>

## What It Does

The Template Creator skill enables rapid creation of new Agents, Commands, Hooks, and Skills from standardized templates. It uses auto-detection to identify creation intent and progressive disclosure to keep context efficient while providing comprehensive guidance.

## Key Features

- **Auto-Detection** - Recognizes creation intent from natural language (e.g., "erstelle einen agent")
- **Progressive Disclosure** - Main file for 90% of use cases, reference.md for details, examples.md for walkthroughs
- **Placeholder Replacement** - Automatically replaces `{PLACEHOLDERS}` with user-provided or generated values
- **Validation** - Ensures all required fields are filled and file structure is preserved
- **Template Library** - Supports 10+ template types across 4 component categories

## Template Types

### Agents (3 Types)

**specialist-agent.md**
- Domain expert with deep specialized knowledge
- Use for: SEO specialist, Legal advisor, Finance expert
- Features: Risk assessment, expert recommendations, quality validation

**research-agent.md**
- Multi-source research and validation
- Use for: Market research, Competitive analysis, Fact-checking
- Features: Confidence scoring, cross-validation, source citation

**orchestrator-agent.md**
- Multi-agent coordination and workflow
- Use for: Complex multi-step processes, Agent delegation
- Features: Task decomposition, agent selection, result synthesis

### Commands (2 Types)

**workflow-command.md**
- Multi-step user workflow with data capture
- Use for: /idea-new, /project-add, /knowledge-add
- Features: Input validation, file creation, index updates

**analysis-command.md**
- Data analysis and insights generation
- Use for: /idea-list, /knowledge-search, /project-stats
- Features: Metrics calculation, pattern detection, recommendations

### Hooks (2 Types)

**post-tool-use.sh**
- Event-driven automation after tool usage
- Features: Tool filtering, path monitoring, background execution

**stop-hook.sh**
- Session summary on conversation end
- Features: Metadata collection, summary generation, archival

### Skills (2 Types)

**simple-skill/SKILL.md**
- Single-file skill for straightforward use cases
- Features: Guidelines, examples, quick reference

**progressive-skill/**
- Three-file structure (SKILL.md, reference.md, examples.md)
- Features: Entry point, detailed docs, practical examples

## The Process

### 1. Detection
- User expresses creation intent (e.g., "erstelle einen SEO agent")
- Skill activates with confidence score 9-10
- Template type is identified

### 2. Information Gathering
- Domain/specialization
- Purpose and functionality
- Tools and dependencies
- Required placeholders

### 3. Template Application
- Read appropriate template file
- Replace all `{PLACEHOLDERS}`
- Validate completeness
- Preserve structure and formatting

### 4. File Creation
- Write to correct location
- Ensure directory exists
- Confirm with user

## Usage

Activate naturally with phrases like:
- "erstelle einen agent"
- "neuer command"
- "create hook"
- "i need a skill for {domain}"

Or explicitly:
```
/create-agent {domain}
/create-command {name}
/create-hook {type}
/create-skill {name}
```

## Common Placeholders

- `{DOMAIN}` - Domain/specialization (e.g., "SEO", "Legal")
- `{DESCRIPTION}` - Brief description of purpose
- `{PROJECT_NAME}` - Name of command/workflow
- `{TIMESTAMP}` - Current date (YYYY-MM-DD)
- `{SKILL_NAME}` - Name of skill being created

See reference.md for complete placeholder list.

## Validation Checklist

Before creating files, the skill verifies:
- All placeholders replaced (no braces remain)
- Frontmatter YAML is valid (if applicable)
- File path follows naming conventions
- Directory exists or will be created
- No duplicate files in target location
- User confirmed key parameters

## Output Example

```
✓ SEO Specialist Agent erfolgreich erstellt!

Datei: .claude/agents/seo-agent.md
Typ: Specialist Agent
Domain: SEO
Tools: WebSearch, Read, Write

Nächste Schritte:
→ Aktiviere den Agent mit @seo-agent
→ Teste mit: "Analysiere diese URL auf SEO-Optimierung"
→ Passe Expertise-Bereiche an in der Agent-Datei

Dokumentation: Siehe .claude/templates/agents/specialist-agent.md
```

## Best Practices

**Do:**
- Always ask before proceeding
- Validate all inputs
- Use descriptive names (seo-agent.md not agent1.md)
- Preserve template structure
- Create directories if needed

**Don't:**
- Auto-create without confirmation
- Leave placeholders unfilled
- Skip validation
- Overwrite files silently
- Mix template types

## Progressive Disclosure

- **SKILL.md** (this file) - Essential info for 90% of use cases
- **reference.md** - Complete placeholder reference, advanced customization
- **examples.md** - Step-by-step walkthroughs, domain-specific adaptations

Load additional files only when needed to keep context efficient.

## Related Skills

- [Research Orchestrator](research-orchestrator.md) - Research component requirements
- [Prompt Pro Framework](prompt-pro-framework.md) - Optimize prompts for new components

---

<small>Source: `core:template-creator`</small>
