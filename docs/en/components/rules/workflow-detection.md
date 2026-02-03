---
title: Workflow Detection
type: rule
tags: []
lang: en
confidence: 100
---

# Workflow Detection


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Rule |
| **Purpose** | Detect slash commands from natural language using confidence scoring |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | rules |</div>


## What It Does

Workflow Detection automatically recognizes when user input matches slash command patterns using the detection-index.json (47 commands). It scores confidence based on keyword matches and pattern similarity, then asks the user for confirmation before executing. The rule enforces conservative triggering (confidence ≥9 for high, 6-8 for medium) and never auto-executes without explicit user approval.


## System Impact

**When It Triggers:**
Every user input (parsed for command patterns)

**Behavior Enforced:**
- Load detection-index.json for keyword/pattern matching
- Calculate confidence score (0-10)
- High confidence (9-10): Ask "Should I use /workflow?"
- Medium confidence (6-8): Tentatively ask "Do you mean /workflow?"
- Low confidence (1-5): Ignore, respond normally
- NEVER auto-execute without user confirmation

**Integration Points:**
- .claude/detection-index.json (47 commands)
- .claude/COMMANDS.md (full command docs)
- User confirmation (required before execution)


## Architecture

**Trigger:** Every user input

**Dependencies:**
- detection-index.json (keyword/pattern mappings)
- COMMANDS.md (command documentation)

**Detection Flow:**
1. **Parse Input**: Extract keywords from user message
2. **Match**: Compare against detection-index patterns
3. **Score**: Calculate confidence (0-10)
4. **Decide**: High/Medium/Low action
5. **Confirm**: Ask user before executing
6. **Execute**: Run command only after approval


## Usage

**Confidence Levels:**

| Confidence | Action | Example |
|------------|--------|---------|
| 9-10 (High) | Ask "Should I use /workflow?" | "I have a new idea" → /idea-new |
| 6-8 (Medium) | Ask "Do you mean /workflow?" | "Show my ideas" → /idea-list |
| 1-5 (Low) | Ignore, respond normally | "I need to check..." |

**Multi-Match:**
If multiple commands match, present options:
```
"Your input matches multiple commands:
 1. /idea-new (create new idea)
 2. /note-new (create new note)
 Which did you mean?"
```

**Conservative Triggering:**
Better to not trigger than to trigger incorrectly. Respect user intent.


## Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| High Confidence | 9-10 | Strong match, confident suggestion |
| Medium Confidence | 6-8 | Possible match, tentative question |
| Low Confidence | 1-5 | No action |
| Detection Index | .claude/detection-index.json | 47 commands |
| Auto-Execute | NEVER | Always require confirmation |
| Multi-Match Behavior | Ask user | Present options |


## Best Practices

**Do:**
- Parse every user input for patterns
- Use confidence-based responses
- Always ask before executing
- Present options for multi-match
- Be conservative (better to miss than false positive)

**Don't:**
- Auto-execute commands without confirmation
- Trigger on low confidence matches
- Ignore multi-match situations
- Override user's explicit non-command intent


## Related


---

<small>Source: `.claude/rules/workflow-detection.md`</small>
