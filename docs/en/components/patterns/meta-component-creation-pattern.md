---
title: meta-component-creation-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# meta-component-creation-pattern


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
```markdown
---
name: {domain}-{role}
description: Use this agent when [specific trigger]. Specializes in [2-3 areas]. Examples: <example>Context: [situation] user: '[request]' assistant: '[response]' <commentary>[reasoning]</commentary></example>
color: {color}
---

You are a {Domain} specialist focusing on {specific expertise}.

Your core expertise areas:
- **{Area 1}**: {capabilities}
- **{Area 2}**: {capabilities}
- **{Area 3}**: {capabilities}

## When to Use This Agent

Use this agent for:
- {Use case 1}
- {Use case 2}
- {Use case 3}

## {Domain}-Specific Sections

### {Category 1}
{Implementation guidance, code examples}

### {Category 2}
{Best practices, patterns}

Always provide {specific deliverables} when working in this domain.
```


#### Example



**Code:**
```markdown
# {Action} {Target}

{Brief description} for $ARGUMENTS following {standards}.

## Task

I'll {action} including:
1. {Step 1}
2. {Step 2}
3. {Step 3}
4. {Step 4}

## Process

I'll follow these steps:
1. {Detailed step 1}
2. {Detailed step 2}
3. {Final step}

## {Category-Specific Sections}

### {Section 1}
- {Feature 1}
- {Feature 2}

## Best Practices

### {Practice Category}
- {Best practice 1}
- {Best practice 2}

I'll adapt to your project's {tools/framework}.
```


#### Example



**Code:**
```markdown
## Configuration Options

- **--config**: Custom configuration file path
- **--output**: Output directory or format
- **--verbose**: Enable detailed logging
- **--dry-run**: Preview without execution
- **--force**: Override safety checks
```


#### Example



**Code:**
```json
{
  "mcpServers": {
    "{Service} MCP": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-{service}@latest"
      ],
      "env": {
        "API_KEY": "{required}",
        "BASE_URL": "https://api.service.com/v1",
        "TIMEOUT": "30000"
      }
    }
  }
}
```


#### Example



**Code:**
```json
{
  "mcpServers": {
    "PostgreSQL MCP": {
      "command": "npx",
      "args": ["-y", "postgresql-mcp@latest"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@host:5432/db",
        "MAX_CONNECTIONS": "10",
        "ENABLE_SSL": "true"
      }
    }
  }
}
```


#### Example



**Code:**
```json
{
  "mcpServers": {
    "{Service} API MCP": {
      "command": "npx",
      "args": ["-y", "{service}-mcp@latest"],
      "env": {
        "API_TOKEN": "{token}",
        "RATE_LIMIT_REQUESTS": "5000",
        "RATE_LIMIT_WINDOW": "3600"
      }
    }
  }
}
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

<small>Source: `knowledge/patterns/meta-component-creation-pattern.md`</small>
