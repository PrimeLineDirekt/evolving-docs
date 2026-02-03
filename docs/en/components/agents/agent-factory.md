---
title: agent-factory
type: agent
tags: []
lang: en
confidence: 100
---

# agent-factory


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Dynamic agent composition from the trait system. Generates complete, ready-to-use agent prompts by combining Expertise, Personality, and Approach traits. |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agent-creation |</div>


## What It Does

The Agent Factory is a specialist agent that dynamically composes agents from the trait system. It takes a combination of Expertise (what the agent knows), Personality (how it communicates), and Approach (how it works) and generates a complete, production-ready agent prompt.

**Key Capabilities:**
- Validates trait combinations against taxonomy
- Loads trait definitions from JSON sources
- Fills dynamic agent templates with trait-specific content
- Handles disclaimers for sensitive domains (legal, security, medical)
- Provides helpful error messages for invalid traits


## System Impact

- **Enables 480 possible agent combinations** from 10 expertise × 8 personality × 6 approach traits
- **Powers the `/compose-agent` command** for on-demand agent creation
- **Reduces agent creation overhead** from manual prompt engineering to simple trait selection
- **Enforces consistency** through standardized templates and voice mappings
- **Critical for delegation system** - enables trait-based agent selection in workflows


## Architecture

**Model:** Sonnet (medium complexity, requires reasoning for template composition)

**Data Sources:**
- `knowledge/agents/trait-taxonomy.json` - Core trait definitions (expertise, personality, approach)
- `knowledge/agents/voice-mappings.json` - Tone characteristics and communication markers
- `knowledge/agents/disclaimers.json` - Legal disclaimers for sensitive domains

**Template:**
- `.claude/templates/agents/dynamic-agent.md` - Master template with placeholders

**Orchestration:**
- Invoked via Task tool with `subagent_type: "general-purpose"` and agent-factory traits
- Returns complete agent prompt as markdown output

**Process Flow:**
1. Parse trait combination from input
2. Validate traits against taxonomy
3. Load trait data from JSON sources
4. Check if disclaimer required
5. Fill template placeholders
6. Return composed agent prompt


## Usage

**Direct Invocation (via command):**
```bash
/compose-agent researcher skeptical systematic
```

**From Delegation System:**
When a task-type maps to traits (e.g., `bug_fix → engineer+precise+iterative`), the delegation system uses Agent Factory to generate the appropriate agent on-demand.

**Input Format:**
```
{expertise} {personality} {approach}
```

**Defaults:**
- personality: `direct` (if not specified)
- approach: `systematic` (if not specified)

**Example Combinations:**
| Traits | Use Case |
|--------|----------|
| `researcher skeptical systematic` | Academic research with rigorous validation |
| `engineer precise iterative` | Code quality-focused development |
| `security cautious adversarial` | Threat modeling and vulnerability assessment |
| `creative creative exploratory` | Innovation and ideation sessions |


## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| **model** | sonnet | Medium complexity requires reasoning |
| **requires_validation** | true | All traits validated against taxonomy |
| **default_personality** | direct | Used when personality not specified |
| **default_approach** | systematic | Used when approach not specified |

**Trait Validation:**
```python
VALID_EXPERTISE = [
  "researcher", "architect", "engineer", "analyst",
  "strategist", "legal", "creative", "security",
  "communications", "medical"
]

VALID_PERSONALITY = [
  "precise", "creative", "cautious", "direct",
  "thorough", "contrarian", "empathetic", "skeptical"
]

VALID_APPROACH = [
  "systematic", "exploratory", "iterative",
  "parallel", "adversarial", "consultative"
]
```

**Disclaimer Triggers:**
Domains requiring disclaimers: `legal`, `security`, `medical`


## Best Practices

**Do:**
- Use recommended combinations for common use cases (e.g., `engineer+precise+iterative` for code quality)
- Validate trait combinations before invoking Agent Factory
- Leverage voice mappings for consistent communication style
- Check disclaimer requirements for sensitive domains
- Use Agent Factory for on-demand agent creation rather than pre-defining all combinations

**Don't:**
- Don't create agents for trivial tasks - use direct execution instead
- Don't bypass trait validation - invalid combinations will fail
- Don't ignore disclaimer requirements for legal/security/medical domains
- Don't manually compose agent prompts when Agent Factory can generate them
- Don't use conflicting traits (e.g., `cautious` personality with `adversarial` approach may need careful consideration)




## Related


---

<small>Source: `.claude/agents/agent-factory.md`</small>
