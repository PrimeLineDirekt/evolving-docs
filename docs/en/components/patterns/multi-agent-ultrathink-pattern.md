---
title: multi-agent-ultrathink-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# multi-agent-ultrathink-pattern


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




## System Impact

**Capabilities Provided:**
- Structured approach to component creation
- Automated validation and best practices
- Standardized output format
- Integration with system architecture

**When to Use:**
- Creating new system components
- Standardizing component structure
- Ensuring consistency across codebase
- Automating repetitive creation tasks



## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
                    ┌─────────────────┐
                    │   Coordinator   │
                    │     Agent       │
                    └────────┬────────┘
                             │
         ┌───────────┬───────┴───────┬───────────┐
         ▼           ▼               ▼           ▼
    ┌─────────┐ ┌─────────┐   ┌─────────┐ ┌─────────┐
    │Architect│ │Research │   │  Coder  │ │ Tester  │
    │  Agent  │ │  Agent  │   │  Agent  │ │  Agent  │
    └─────────┘ └─────────┘   └─────────┘ └─────────┘
```


#### Example



**Code:**
```markdown
## Reasoning Transcript
- Decision points
- Analysis journey
- Agent contributions

## Final Answer
- Concrete implementation steps
- Code changes (in Markdown)

## Next Actions
- Follow-up tasks
- Open questions
```


#### Example



**Code:**
```bash
/ultrathink Implementiere User Authentication mit OAuth2

Coordinator:
1. Architect Agent → Designs OAuth2 Flow, Token Storage, Middleware
2. Research Agent → Findet Best Practices, Security Considerations
3. Coder Agent → Implementiert basierend auf Design + Research
4. Tester Agent → Designt Auth-Tests, Edge Cases

Synthesis:
- Alle 4 Perspektiven kombiniert
- Konkrete Implementation mit Tests
- Follow-up: Rate Limiting, Audit Logging
```




## Configuration



## Best Practices

**Do:**
- Use for multi-expert coordination requiring diverse perspectives
- Apply when problem benefits from iterative refinement
- Combine with proper state management and validation
- Monitor blackboard size to prevent context overflow

**Don't:**
- Use for simple single-agent tasks
- Apply to strictly sequential workflows
- Ignore controller bottleneck risks
- Forget to handle write conflicts in concurrent scenarios




## Related


---

<small>Source: `knowledge/patterns/multi-agent-ultrathink-pattern.md`</small>
