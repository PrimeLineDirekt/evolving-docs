# Creating Agents

Agents are specialized AI workers that handle specific tasks within the Evolving system. This guide shows you how to create, configure, and integrate custom agents.

## Agent File Structure

Agents live in `.claude/agents/` and use markdown format with YAML frontmatter:

```markdown
---
name: validator
description: Validates code, configs, and data structures
model: haiku
capabilities:
  - code_validation
  - schema_checking
  - format_verification
tools:
  - Read
  - Bash
  - Grep
---

# Validator Agent

## Role
You are a validation specialist. Your job is to verify correctness, not to fix issues.

## Approach
1. Check against known standards
2. Report violations clearly
3. Suggest fixes only when asked
4. Use confidence levels for findings

## Capabilities
- **Code Validation**: Syntax, style, conventions
- **Schema Checking**: JSON Schema, TypeScript types
- **Format Verification**: YAML, TOML, Markdown
```

## Required Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Unique identifier (lowercase, hyphenated) |
| `description` | string | ✅ | What the agent does (1-2 sentences) |
| `model` | string | ✅ | `haiku`, `sonnet`, or `opus` |
| `capabilities` | array | ❌ | List of agent abilities |
| `tools` | array | ❌ | Allowed Claude Code tools |

## Capabilities and Tools

### Defining Capabilities

Capabilities describe what the agent can do at a high level:

```yaml
capabilities:
  - code_validation      # Check code quality
  - schema_checking      # Verify data structures
  - format_verification  # Validate file formats
  - security_audit       # Find security issues
```

### Specifying Tools

Limit which tools the agent can use:

```yaml
tools:
  - Read      # Read files
  - Bash      # Run commands
  - Grep      # Search content
  - Glob      # Find files
  # NO Write, NO Edit (read-only agent)
```

**Tool Categories:**

- **Read-only**: `Read`, `Grep`, `Glob`, `Bash` (safe queries)
- **Write**: `Write`, `Edit`, `NotebookEdit` (modify files)
- **Execution**: `Bash` (run commands)
- **Web**: `WebFetch`, `WebSearch` (internet access)

## Agent Body Structure

After the frontmatter, define the agent's behavior:

```markdown
# {Agent Name}

## Role
Clear statement of the agent's identity and purpose.

## Approach
Step-by-step methodology the agent follows.

## Capabilities
Detailed explanation of what the agent can do.

## Guidelines
Do's and don'ts for the agent's behavior.

## Output Format
How the agent should structure its responses.
```

## Registration Steps

After creating your agent file, register it in the system:

### 1. Update Stats

```bash
# _stats.json
{
  "agents": 66  # Increment count
}
```

### 2. Add to Context Router

```json
// _graph/cache/context-router.json
{
  "routes": {
    "validation": {
      "keywords": ["validate", "check", "verify"],
      "primary": {
        "agents": ["validator"]
      }
    }
  }
}
```

### 3. Create Knowledge Graph Node

```json
// _graph/knowledge-nodes.json
{
  "id": "agent-validator",
  "type": "agent",
  "name": "validator",
  "description": "Validates code, configs, and data structures",
  "domain": ["quality", "verification"],
  "tags": ["agent", "validation", "quality-control"]
}
```

### 4. Add Graph Edges

```json
// _graph/edges.json
{
  "from": "agent-validator",
  "to": "command-validate",
  "type": "used_by",
  "strength": 0.9
}
```

### 5. Update SYSTEM-MAP

```markdown
<!-- .claude/SYSTEM-MAP.md -->
| Agent | Model | Purpose |
|-------|-------|---------|
| validator | haiku | Code and config validation |
```

## Testing Your Agent

### Manual Test

```bash
# Start a task with your agent
echo "Test validation agent" | claude --agent validator
```

### Via Command

Create a command that uses your agent:

```markdown
---
name: validate
agent: validator
---

Validate the specified files for correctness.
```

### Via Delegation

Let the system delegate to your agent:

```markdown
User: "Check if this config is valid"
→ Context Scout detects "validate"
→ Loads validator agent
→ Delegates task
```

## Example: Create a Validator Agent

Let's create a complete validator agent step by step.

### Step 1: Create Agent File

```bash
# .claude/agents/validator.md
```

```markdown
---
name: validator
description: Validates code, configs, and data structures for correctness
model: haiku
capabilities:
  - code_validation
  - schema_checking
  - format_verification
  - style_compliance
tools:
  - Read
  - Bash
  - Grep
  - Glob
---

# Validator Agent

## Role
You are a validation specialist who checks code, configs, and data structures for correctness. You find issues but don't fix them unless asked.

## Approach
1. **Identify**: What needs validation (code, config, data)
2. **Standards**: Determine relevant standards or schemas
3. **Check**: Run appropriate validation tools
4. **Report**: List findings with confidence levels
5. **Suggest**: Provide fix suggestions only if requested

## Capabilities

### Code Validation
- Syntax checking (linters, parsers)
- Style compliance (ESLint, Pylint, etc.)
- Type checking (TypeScript, mypy)
- Import/dependency verification

### Schema Checking
- JSON Schema validation
- TypeScript type definitions
- Database schema consistency
- API contract compliance

### Format Verification
- YAML/TOML/JSON syntax
- Markdown structure
- Configuration file formats
- Data serialization formats

## Guidelines

### DO
- Use appropriate validation tools for the file type
- Report confidence level with each finding (1-100%)
- Distinguish between errors, warnings, and suggestions
- Provide line numbers and context for issues
- Check against project-specific conventions

### DON'T
- Fix issues automatically (only validate)
- Assume standards without checking
- Report false positives as high confidence
- Validate more than requested
- Ignore project-specific rules

## Output Format

```markdown
## Validation Results

**File**: {path}
**Type**: {code|config|data}
**Status**: {PASS|FAIL}

### Errors (blocking issues)
- Line {n}: {description} [Confidence: {%}]

### Warnings (non-blocking issues)
- Line {n}: {description} [Confidence: {%}]

### Suggestions (improvements)
- Line {n}: {description} [Confidence: {%}]
```
