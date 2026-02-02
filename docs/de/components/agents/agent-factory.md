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
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents |</div>


## What It Does

"Dynamic agent composition from trait system"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Input: "researcher skeptical systematic"

Parsed:
  expertise: "researcher"
  personality: "skeptical"
  approach: "systematic"
```


#### Example



**Code:**
```python
VALID_EXPERTISE = ["researcher", "architect", "engineer", "analyst",
                   "strategist", "legal", "creative", "security",
                   "communications", "medical"]

VALID_PERSONALITY = ["precise", "creative", "cautious", "direct",
                     "thorough", "contrarian", "empathetic", "skeptical"]

VALID_APPROACH = ["systematic", "exploratory", "iterative",
                  "parallel", "adversarial", "consultative"]

if expertise not in VALID_EXPERTISE:
    return Error: "Ungültige Expertise: {expertise}"
# ... analog für personality und approach
```


#### Example



**Code:**
```bash
1. knowledge/agents/trait-taxonomy.json
   → expertise[{key}] → description, core_skills, tools, output_style
   → personality[{key}] → description, tone, markers, avoids
   → approach[{key}] → description, execution_pattern, steps, best_for

2. knowledge/agents/voice-mappings.json
   → personalities[{key}] → tone_characteristics, sentence_structure,
                            vocabulary, markers (opening/transition/conclusion),
                            avoids, example_response

3. knowledge/agents/disclaimers.json (wenn requires_disclaimer)
   → disclaimers[{domain}] → short, full, inline_markers
```


#### Example



**Code:**
```python
REQUIRES_DISCLAIMER = ["legal", "security", "medical"]

if expertise in REQUIRES_DISCLAIMER:
    disclaimer = load_disclaimer(expertise)
    include_disclaimer = True
else:
    include_disclaimer = False
```


#### Example



**Code:**
```yaml
# Expertise
{EXPERTISE_KEY}: expertise
{EXPERTISE_NAME}: expertise.capitalize()
{EXPERTISE_DESCRIPTION}: trait_taxonomy.expertise[key].description
{EXPERTISE_CORE_SKILLS}: ", ".join(trait_taxonomy.expertise[key].core_skills)
{EXPERTISE_TOOLS_LIST}: format_tools(trait_taxonomy.expertise[key].tools)
{EXPERTISE_OUTPUT_STYLE}: trait_taxonomy.expertise[key].output_style

# Personality
{PERSONALITY_KEY}: personality
{PERSONALITY_NAME}: personality.capitalize()
{PERSONALITY_DESCRIPTION}: trait_taxonomy.personality[key].description
{PERSONALITY_TONE_CHARACTERISTICS}: format_list(voice_mappings[key].tone_characteristics)
{PERSONALITY_VOCABULARY}: voice_mappings[key].vocabulary
{PERSONALITY_AVOIDS}: format_list(voice_mappings[key].avoids)
{PERSONALITY_MARKERS_OPENING}: format_list(voice_mappings[key].markers.opening)
{PERSONALITY_MARKERS_TRANSITION}: format_list(voice_mappings[key].markers.transition)
{PERSONALITY_MARKERS_CONCLUSION}: format_list(voice_mappings[key].markers.conclusion)

# Approach
{APPROACH_KEY}: approach
{APPROACH_NAME}: approach.capitalize()
{APPROACH_DESCRIPTION}: trait_taxonomy.approach[key].description
{APPROACH_EXECUTION_PATTERN}: trait_taxonomy.approach[key].execution_pattern
{APPROACH_STEPS}: format_numbered_list(trait_taxonomy.approach[key].steps)
{APPROACH_BEST_FOR}: format_list(trait_taxonomy.approach[key].best_for)

# Disclaimer (conditional)
{IF_REQUIRES_DISCLAIMER}: include if disclaimer needed
{ENDIF_REQUIRES_DISCLAIMER}: end conditional block
{DISCLAIMER_SHORT}: disclaimers[expertise].short
{DISCLAIMER_FULL}: disclaimers[expertise].full
{DISCLAIMER_INLINE_MARKERS}: format_list(disclaimers[expertise].inline_markers)

# Metadata
{TIMESTAMP}: current ISO date
```


#### Example



**Code:**
```bash
IF invalid_trait_detected:
  List valid options for that trait type
  Suggest closest match if typo detected
  Return helpful error message
```


#### Example



**Code:**
```bash
Error: Ungültige Expertise "developer"
Meintest du: "engineer"?

Gültige Expertise-Optionen:
researcher, architect, engineer, analyst, strategist,
legal, creative, security, communications, medical
```


#### Example



**Code:**
```bash
IF expertise missing:
  Return error with usage example
  List all expertise options
```


#### Example



**Code:**
```bash
/compose-agent researcher skeptical systematic
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/agent-factory.md`</small>
