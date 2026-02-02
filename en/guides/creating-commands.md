---
title: Creating Commands
description: Build user-invocable actions for the Evolving system
---

# Creating Commands

Commands are user-invocable actions that provide shortcuts to common workflows. This guide shows you how to create, configure, and integrate custom commands.

## What are Commands?

Commands are markdown files with YAML frontmatter that define:

- **Name** - How users invoke it (`/command-name`)
- **Agent** - Which specialist executes it (optional)
- **Model** - Which Claude model to use
- **Behavior** - What the command does

## Command Structure

### Basic Template

```markdown
---
name: my-command
description: Short description of what it does
agent: specialist-agent  # Optional
model: haiku            # Optional: haiku, sonnet, opus
---

# Command Name

What the command does and how to use it.

## Parameters

- `param1`: Description
- `param2`: Description

## Examples

```bash
/my-command param1 param2
```

## Behavior

Detailed instructions for the executing agent.
```

### Complete Example

```markdown
---
name: validate
description: Validate code, configs, and data structures
agent: validator
model: haiku
---

# Validate

Validates the specified files for correctness using appropriate tools.

## Parameters

- `files`: File paths to validate (glob patterns supported)
- `type`: Optional validation type (code|config|data)

## Examples

```bash
# Validate specific file
/validate src/auth.ts

# Validate with glob
/validate "src/**/*.ts"

# Validate with type hint
/validate config.json --type=config
```

## Behavior

1. Identify file types
2. Determine appropriate validation tools
3. Run validation with confidence scoring
4. Report findings (errors, warnings, suggestions)
5. Provide fix suggestions only if requested

## Output Format

```markdown
## Validation Results

**File**: {path}
**Status**: PASS|FAIL

### Errors
- Line {n}: {issue} [Confidence: {%}]

### Warnings
- Line {n}: {issue} [Confidence: {%}]
```
```

## Command Types

### 1. Direct Commands

Execute immediately without delegation:

```markdown
---
name: hello
description: Simple greeting
---

# Hello

Say hello to the user.

Just respond with a friendly greeting.
```

### 2. Agent Commands

Delegate to specialist:

```markdown
---
name: explore-code
description: Analyze codebase structure
agent: Explore
model: haiku
---

# Explore Code

Use the Explore agent to analyze the codebase.
```

### 3. Workflow Commands

Multi-step processes:

```markdown
---
name: feature-pipeline
description: Full feature development pipeline
---

# Feature Pipeline

1. Create feature branch
2. Generate implementation plan
3. Execute with code-architect
4. Review with code-reviewer
5. Create PR
```

### 4. Utility Commands

System operations:

```markdown
---
name: health-dashboard
description: Show system health metrics
---

# Health Dashboard

Display:
- Memory usage
- Active agents
- Context stats
- Hook status
```

## Parameter Handling

### Simple Parameters

```markdown
## Parameters

- `file`: File to process
- `mode`: Operation mode (read|write)
```

Usage:
```bash
/process-file src/main.ts --mode=read
```

### Optional Parameters

```markdown
## Parameters

- `input`: Input file (required)
- `output`: Output file (optional, defaults to stdout)
- `format`: Format type (optional, auto-detect)
```

Usage:
```bash
/convert input.json
/convert input.json --output=result.yaml
/convert input.json --output=result.yaml --format=yaml
```

### Flags

```markdown
## Parameters

- `--verbose`: Show detailed output
- `--dry-run`: Preview without executing
- `--force`: Skip confirmations
```

Usage:
```bash
/migrate --dry-run
/migrate --verbose --force
```

## Agent Integration

### Selecting the Right Agent

| Task Type | Agent | Model |
|-----------|-------|-------|
| Code exploration | Explore | haiku |
| Debugging | debugger | sonnet |
| Code review | code-reviewer | sonnet |
| Architecture | code-architect | sonnet |
| General tasks | general-purpose | sonnet |

### Agent Configuration

```markdown
---
name: review-code
description: Comprehensive code review
agent: feature-dev:code-reviewer
model: sonnet
---

# Review Code

Execute thorough code review focusing on:
- Code quality
- Best practices
- Potential bugs
- Performance
```

### Multiple Agents

```markdown
---
name: full-analysis
description: Multi-agent code analysis
---

# Full Analysis

1. Explore with Explore agent (structure)
2. Review with code-reviewer (quality)
3. Analyze types with type-analyzer (safety)
4. Check errors with silent-failure-hunter (robustness)
```

## Plain-Text Detection

Make commands invocable via natural language:

### Detection Index

Add to `.claude/detection-index.json`:

```json
{
  "commands": [
    {
      "name": "validate",
      "triggers": [
        "validate",
        "check",
        "verify",
        "lint"
      ],
      "patterns": [
        "validate (this|the) (file|code)",
        "check (if|whether) .* (is )?(valid|correct)",
        "verify (the )?(syntax|format)"
      ],
      "confidence_boost": 10
    }
  ]
}
```

### Confidence Scoring

```
User: "Validate this config file"
    ↓
Match: "validate" trigger (exact)
Confidence: 90%
    ↓
Claude: "Should I run /validate?"
```

```
User: "Check if this JSON is valid"
    ↓
Match: "check if ... valid" pattern
Confidence: 75%
    ↓
Claude: "Should I run /validate?"
```

## Registration Steps

### 1. Create Command File

```bash
.claude/commands/my-command.md
```

### 2. Update Stats

```json
// _stats.json
{
  "commands": 81  // Increment
}
```

### 3. Add to Detection Index

```json
// .claude/detection-index.json
{
  "commands": [
    {
      "name": "my-command",
      "triggers": ["keyword1", "keyword2"],
      "patterns": ["pattern.*regex"]
    }
  ]
}
```

### 4. Create Graph Node

```json
// _graph/knowledge-nodes.json
{
  "nodes": [
    {
      "id": "command-my-command",
      "type": "command",
      "name": "my-command",
      "description": "What it does",
      "domain": ["category"],
      "tags": ["command", "tag1", "tag2"]
    }
  ]
}
```

### 5. Add Graph Edges

```json
// _graph/edges.json
{
  "edges": [
    {
      "from": "command-my-command",
      "to": "agent-specialist",
      "type": "uses",
      "strength": 0.9
    }
  ]
}
```

### 6. Update SYSTEM-MAP

```markdown
<!-- .claude/SYSTEM-MAP.md -->

## Commands

| Command | Agent | Purpose |
|---------|-------|---------|
| /my-command | specialist | What it does |
```

## Testing Commands

### Manual Test

```bash
# Direct invocation
/my-command param1 param2
```

### Via Plain-Text

```
User: "Run my command with these params"
Claude: "Should I run /my-command?"
User: "Yes"
→ Command executes
```

### Test Agent Delegation

```markdown
---
agent: Explore
---

# My Command

Test that Explore agent receives this task.
```

Verify in output:
```
[Agent: Explore]
[Model: haiku]
[Task: ...]
```

## Advanced Features

### Conditional Execution

```markdown
## Behavior

1. Check if prerequisites exist
2. If missing, install dependencies
3. Then execute main task
```

### Error Handling

```markdown
## Error Handling

- Missing file → Ask user for path
- Invalid format → Show expected format
- Permission denied → Request sudo
```

### Context Awareness

```markdown
## Behavior

Check context usage:
- If < 60%: Full analysis
- If 60-80%: Summary only
- If > 80%: Defer to next session
```

## Command Composition

### Chaining Commands

```bash
/explore-code src/ && /review-code src/ && /generate-tests src/
```

### Command Aliases

```json
{
  "aliases": {
    "ec": "explore-code",
    "rc": "review-code",
    "gt": "generate-tests"
  }
}
```

### Command Macros

```markdown
---
name: full-pipeline
description: Run complete development pipeline
---

# Full Pipeline

Executes:
1. /explore-code
2. /review-code
3. /generate-tests
4. /validate
```

## Best Practices

### DO

✅ **Clear, descriptive names**
```markdown
---
name: validate-config
description: Validate configuration files
---
```

✅ **Specify agent when appropriate**
```markdown
---
agent: validator
model: haiku
---
```

✅ **Document parameters**
```markdown
## Parameters
- `file`: Path to validate (required)
- `strict`: Strict mode (optional)
```

✅ **Add examples**
```markdown
## Examples
/validate-config app.json
/validate-config app.json --strict
```

### DON'T

❌ **Vague names**
```markdown
---
name: do-stuff
---
```

❌ **Missing documentation**
```markdown
---
name: complex-command
---

# Complex Command
(no explanation of what it does)
```

❌ **Wrong agent for task**
```markdown
---
name: debug-issue
agent: Explore  # Should use debugger
---
```

## Command Library

### Code Quality

- `/review-code` - Code quality review
- `/validate` - Syntax and format validation
- `/check-types` - Type system analysis
- `/find-bugs` - Bug detection

### Development

- `/explore-code` - Codebase analysis
- `/generate-tests` - Test generation
- `/refactor` - Code refactoring
- `/optimize` - Performance optimization

### Project Management

- `/health-dashboard` - System status
- `/whats-next` - Create handoff
- `/memory-status` - Check memory
- `/context-stats` - Token usage

### Utilities

- `/inventory-report` - List all components
- `/graph-analyze` - Knowledge graph insights
- `/experience-query` - Search learned solutions

## Next Steps

- [Creating Agents](creating-agents.md) - Build specialists
- [Using Patterns](using-patterns.md) - Apply prompt patterns
- [Writing Commands](writing-commands.md) - More command techniques
- [Extending System](extending-system.md) - Full integration
