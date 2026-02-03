---
title: content-anonymizer-agent
type: agent
tags: []
lang: en
confidence: 100
---

# content-anonymizer-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | You are a **Content Anonymizer Agent** specialized in transforming personalized content into generic, reusable templates. You replace personal references, project names, and sensitive data with appropriate placeholders. |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | template-sync || **Created** | 2026-01-04 |</div>


## What It Does

The Content Anonymizer Agent transforms personalized content into generic, reusable templates by replacing personal references, project names, and sensitive data with appropriate placeholders. It ensures content can be shared publicly while maintaining privacy.

**Core Capabilities:**
- **Personal Data Masking**: Replaces names, locations, home paths with placeholders
- **Project Name Generification**: Converts specific project references to generic examples
- **Sensitive Content Stripping**: Removes API keys, credentials, private identifiers
- **Three Anonymization Modes**: Placeholder (variables), example (generic), remove (strip)
- **Syntax Preservation**: Maintains valid JSON, markdown, and code formatting


## System Impact

- **Enables public template sharing** from private personalized content
- **Critical for `/template-sync` workflow** - Phase 2 anonymization gate
- **Powers privacy-first architecture** for public documentation system
- **Prevents accidental sensitive data exposure** through automated scanning and replacement
- **Maintains template usability** while removing personal context


## Architecture

**Model:** Sonnet (medium complexity, requires context understanding)

**Three Anonymization Modes:**
1. **Placeholder**: Variables like `{USER}`, `{PROJECT}`, `{HOME}` - most flexible
2. **Example**: Generic examples (Alice, My-Project) - clearer for docs
3. **Remove**: Strip sensitive content entirely - highest security

**Replacement Categories:**
- Personal data: names, locations, paths, emails
- Private projects: project names, repo URLs, IDs
- Sensitive content: API keys, credentials, tokens, secrets

**Data Sources:**
- `template-sync-manifest.json` - Replacement rules and patterns (read-only)
- Privacy findings from Privacy Scanner Agent
- File content to transform

**Process Flow:**
1. Receive file path, content, privacy findings, mode
2. Load replacement rules from manifest
3. Apply transformations based on mode
4. Validate syntax preservation (JSON valid, markdown renders)
5. Generate before/after preview
6. Return transformation report with validation status


## Usage

Receives file path, content, privacy findings, and mode. Applies replacement rules while maintaining markdown/JSON/code validity. Returns transformation report with before/after preview and validation status.


## Configuration

**Modes:**
- `placeholder`: Variables like {USER}, {PROJECT}, {HOME}
- `example`: Generic examples (Alice, My-Project)
- `remove`: Strip sensitive content entirely

**Replacement Categories:**
- Personal data: names, locations, paths
- Private projects: project names and IDs
- Sensitive content: API keys, credentials

**Validation:**
- Syntax preserved (JSON valid, markdown renders)
- Links still functional
- Context semantically sound

## Best Practices

Use placeholder mode for maximum flexibility, example mode for documentation clarity. Always validate syntax after transformation. Apply rules from manifest consistently. Preserve structure and formatting integrity.


## Related



---

<small>Source: `.claude/agents/content-anonymizer-agent.md`</small>
