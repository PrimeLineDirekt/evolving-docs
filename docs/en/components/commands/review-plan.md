---
title: review-plan
type: command
tags: []
lang: en
confidence: 100
---

# review-plan


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | commands |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
/review-plan                    # Reviewt Plan aus aktuellem Context
/review-plan path/to/plan.md    # Reviewt spezifischen Plan
```


#### Example



**Code:**
```markdown
Du bist ein skeptischer Staff Engineer der Pläne kritisch reviewed.

## Deine Aufgabe
Review den folgenden Plan mit gesunder Skepsis:

1. **Vollständigkeit**: Fehlen wichtige Schritte?
2. **Feasibility**: Ist das realistisch umsetzbar?
3. **Edge Cases**: Was könnte schiefgehen?
4. **Assumptions**: Welche Annahmen werden gemacht?
5. **Alternatives**: Gibt es bessere Ansätze?

## Output Format
{
  "result": "APPROVED|NEEDS_REVISION",
  "confidence": 85,
  "strengths": ["..."],
  "concerns": ["..."],
  "suggestions": ["..."]
}

Sei KRITISCH. Lieber einmal zu viel nachfragen als einen schlechten Plan durchwinken.
```


#### Example



**Code:**
```markdown
---
## Review (Auto-Generated)

**Reviewer**: Plan Agent (Staff Engineer Critic)
**Result**: APPROVED / NEEDS_REVISION
**Confidence**: X%
**Date**: YYYY-MM-DD

### Strengths
- Punkt 1
- Punkt 2

### Concerns
- Concern 1
- Concern 2

### Suggestions (optional)
- Suggestion 1
---
```


#### Example



**Code:**
```bash
User: /review-plan
Claude: [Lädt Plan aus Context, startet Critic-Agent]
        "🔍 Starte Plan-Review mit Staff Engineer Critic..."
        [Nach Review]
        "✅ Plan APPROVED (Confidence: 92%)
         Strengths: Klare Phasen, gute Testabdeckung
         Concerns: Phase 3 könnte parallelisiert werden"

User: /review-plan plans/feature-x.md
Claude: [Lädt spezifischen Plan]
        "🔍 Reviewing plans/feature-x.md..."
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/review-plan.md`</small>
