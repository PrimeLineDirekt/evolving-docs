---
title: /onboard-process
type: command
tags: []
lang: en
confidence: 100
---

# /onboard-process


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Onboarding processing engine - reads completed questionnaire and integrates information into the system |
| **Complexity** | high |
| **Model** | sonnet |
| **Category** | memory |</div>


## What It Does

Processes completed onboarding questionnaire from `_ONBOARDING.md`. Extracts personal info, preferences, goals, and constraints, then integrates into system memory and configuration.


## System Impact

- Reads `_ONBOARDING.md` file
- Creates/updates personal knowledge files
- Sets system preferences
- Updates project configuration
- May create initial project structure


## Architecture

Uses Sonnet for intelligent extraction. Implements structured parsing with validation and smart categorization of onboarding data.


## Usage

Run after completing `_ONBOARDING.md` questionnaire to integrate information.

### Examples

#### Basic Usage



**Code:**
```bash
/onboard-process
```




## Configuration

Uses Sonnet model. Extraction rules and integration targets are configurable.

## Best Practices

- Complete questionnaire thoroughly before processing
- Review extracted data for accuracy
- Update preferences if system misinterprets
- Rerun if questionnaire significantly changes
- Keep onboarding file as reference
- Archive after successful processing

## Related

- `/project-add` - Add new projects
- `/preferences` - Update preferences
- Personal knowledge system


---

<small>Source: `.claude/commands/onboard-process.md`</small>
