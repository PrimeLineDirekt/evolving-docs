# Extending the System

The Evolving system is designed to grow. This guide shows you how to add new components while maintaining consistency across the entire system.

## Integration Matrix

When adding a new component, it must be registered in **multiple places** to be fully integrated.

### The 7 Registration Points

| # | File | Purpose |
|---|------|---------|
| 1 | `_stats.json` | Update count (single source of truth) |
| 2 | `_graph/cache/context-router.json` | Make discoverable via keywords |
| 3 | `.claude/detection-index.json` | Enable natural language triggering |
| 4 | `_graph/knowledge-nodes.json` | Add entity to knowledge graph |
| 5 | `_graph/edges.json` | Connect to related entities |
| 6 | `.claude/SYSTEM-MAP.md` | Add to inventory + changelog |
| 7 | `knowledge/index.md` | Add to KB index (if applicable) |

### What Needs What?

| Component Type | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|----------------|---|---|---|---|---|---|---|
| Command        | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| Agent          | ✅ | ✅ | - | ✅ | ✅ | ✅ | - |
| Skill          | ✅ | ✅ | - | ✅ | ✅ | ✅ | - |
| Template       | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ |
| Pattern        | ✅ | ✅ | - | ✅ | ✅ | - | ✅ |
| Learning       | ✅ | ✅ | - | ✅ | ✅ | - | ✅ |
| Hook           | ✅ | - | - | - | - | ✅ | - |
| Rule           | ✅ | ✅ | - | ✅ | - | ✅ | - |
| Blueprint      | ✅ | ✅ | - | ✅ | ✅ | ✅ | - |

## Step-by-Step: Adding a Command

Let's walk through adding a complete command to the system.

### 1. Create Command File

```bash
# .claude/commands/my-command.md
```

```markdown
---
name: my-command
description: Does something useful
allowed-tools:
  - Read
  - Bash
---

# My Command

## Purpose
Explain what it does and why.

## Steps
1. Do this
2. Then that
3. Finally this
```

### 2. Update Stats

```json
// _stats.json
{
  "commands": 64  // Was 63, now 64
}
```

### 3. Add Context Router Entry

```json
// _graph/cache/context-router.json
{
  "routes": {
    "my-feature": {
      "keywords": ["my", "feature", "useful"],
      "primary": {
        "commands": ["/my-command"]
      },
      "confidence_boost": 10
    }
  }
}
```

### 4. Add Detection Triggers

```json
// .claude/detection-index.json
{
  "commands": [
    {
      "name": "my-command",
      "triggers": [
        "my command",
        "do my thing",
        "run my feature"
      ],
      "confidence": {
        "high": ["my command", "/my-command"],
        "medium": ["do my thing"],
        "low": ["my feature"]
      }
    }
  ]
}
```

### 5. Create Knowledge Node

```json
// _graph/knowledge-nodes.json
{
  "nodes": [
    {
      "id": "command-my-command",
      "type": "command",
      "name": "/my-command",
      "description": "Does something useful",
      "domain": ["utilities"],
      "tags": ["command", "utility", "helper"],
      "created": "2026-02-03"
    }
  ]
}
```

### 6. Add Graph Edges

```json
// _graph/edges.json
{
  "edges": [
    {
      "from": "command-my-command",
      "to": "agent-helper",
      "type": "delegates_to",
      "strength": 0.8
    },
    {
      "from": "command-my-command",
      "to": "pattern-react",
      "type": "applies",
      "strength": 0.6
    }
  ]
}
```

### 7. Update SYSTEM-MAP

```markdown
<!-- .claude/SYSTEM-MAP.md -->

## Commands (64)

| Command | Purpose |
|---------|---------|
| /my-command | Does something useful |
| ... | ... |

## Changelog

### 2026-02-03
- Added `/my-command` for useful functionality
```

### 8. Test Integration

```bash
# Direct invocation
/my-command

# Natural language
"Run my command"
→ Should detect and offer /my-command

# Via Context Scout
User mentions "my feature"
→ Context Router should load command
```

## Step-by-Step: Adding an Agent

### 1. Create Agent File

```bash
# .claude/agents/my-agent.md
```

```markdown
---
name: my-agent
description: Specialized agent for X
model: sonnet
capabilities:
  - capability_1
  - capability_2
tools:
  - Read
  - Bash
---

# My Agent

## Role
You are a specialist in X.

## Approach
1. Analyze
2. Execute
3. Report
```

### 2. Update Stats

```json
// _stats.json
{
  "agents": 66  // Was 65, now 66
}
```

### 3. Add Context Router Entry

```json
// _graph/cache/context-router.json
{
  "routes": {
    "my-specialty": {
      "keywords": ["specialty", "expert"],
      "primary": {
        "agents": ["my-agent"]
      }
    }
  }
}
```

### 4. Create Knowledge Node

```json
// _graph/knowledge-nodes.json
{
  "id": "agent-my-agent",
  "type": "agent",
  "name": "my-agent",
  "description": "Specialized agent for X",
  "domain": ["specialty"],
  "tags": ["agent", "specialist"],
  "model": "sonnet"
}
```

### 5. Add Graph Edges

```json
// _graph/edges.json
{
  "from": "agent-my-agent",
  "to": "command-analyze",
  "type": "used_by",
  "strength": 0.9
}
```

### 6. Update SYSTEM-MAP

```markdown
<!-- .claude/SYSTEM-MAP.md -->

## Agents (66)

| Agent | Model | Purpose |
|-------|-------|---------|
| my-agent | sonnet | Specialized for X |
```

### 7. Add to Delegation Config

```json
// _graph/cache/delegation-config.json
{
  "task_types": {
    "my_specialty": {
      "agent": "my-agent",
      "model": "sonnet",
      "keywords": ["specialty", "expert"]
    }
  }
}
```

## Step-by-Step: Adding a Pattern

### 1. Create Pattern File

```bash
# knowledge/patterns/my-pattern.md
```

```markdown
# My Pattern

## Core Loop
1. Step 1
2. Step 2
3. Repeat

## When to Use
Situations where this excels.

## When NOT to Use
Anti-patterns.
```

### 2. Update Stats

```json
// _stats.json
{
  "patterns": 8  // Increment
}
```

### 3. Add Context Router Entry

```json
// _graph/cache/context-router.json
{
  "routes": {
    "my-approach": {
      "keywords": ["approach", "methodology"],
      "primary": {
        "patterns": ["my-pattern"]
      }
    }
  }
}
```

### 4. Create Knowledge Node

```json
// _graph/knowledge-nodes.json
{
  "id": "pattern-my-pattern",
  "type": "pattern",
  "name": "my-pattern",
  "description": "Pattern for X",
  "domain": ["methodology"],
  "tags": ["pattern", "approach"]
}
```

### 5. Add Graph Edges

```json
// _graph/edges.json
{
  "from": "pattern-my-pattern",
  "to": "pattern-related",
  "type": "similar_to",
  "strength": 0.7
}
```

### 6. Update Knowledge Index

```markdown
<!-- knowledge/index.md -->

## Patterns

- [My Pattern](patterns/my-pattern.md) - Pattern for X
```

### 7. Create Pattern Summary

```json
// .claude/summaries/patterns/my-pattern.json
{
  "name": "my-pattern",
  "description": "Pattern for X",
  "core_loop": "Step 1 → Step 2 → Repeat",
  "when_to_use": ["Situation A", "Situation B"],
  "when_not": ["Anti-pattern"],
  "related": ["related-pattern"]
}
```

## Adding New Component Types

To add an entirely new component type:

### 1. Define Component Schema

```markdown
<!-- knowledge/references/schemas/my-type-schema.md -->

# My Type Schema

## Required Fields
- name (string)
- description (string)
- ...

## Optional Fields
- ...

## File Structure
File location and format
```

### 2. Update Stats Schema

```json
// _stats.json
{
  "my_types": 0  // Add new counter
}
```

### 3. Add to Context Router

```json
// _graph/cache/context-router.json
{
  "component_types": {
    "my_type": {
      "primary_key": "my_types",
      "file_pattern": "path/to/*.md"
    }
  }
}
```

### 4. Define Node Type

```json
// _graph/knowledge-nodes.json
{
  "node_types": {
    "my_type": {
      "required_fields": ["id", "name", "description"],
      "optional_fields": ["domain", "tags"]
    }
  }
}
```

### 5. Create Template

```bash
# knowledge/templates/my-type-template.md
```

### 6. Document in SYSTEM-MAP

```markdown
<!-- .claude/SYSTEM-MAP.md -->

## My Types (0)

New component type for...

| Name | Description |
|------|-------------|
| TBD | TBD |
```

## Testing Your Extension

### 1. Verification Checklist

After adding a component, verify:

- [ ] Stats count updated
- [ ] Context Router has entry
- [ ] Detection Index has triggers (if command)
- [ ] Knowledge Graph node exists
- [ ] Edges connect to related nodes
- [ ] SYSTEM-MAP.md updated
- [ ] KB index updated (if applicable)

### 2. Integration Tests

```bash
# Test Context Router
"Use my feature"
→ Should load your component

# Test Detection (commands)
"Run my command"
→ Should offer /my-command

# Test Graph Queries
# Check if node is reachable
grep "my-component" _graph/knowledge-nodes.json
grep "my-component" _graph/edges.json
```

### 3. Consistency Check

Run the built-in consistency checker:

```bash
/check-consistency
```

This validates:
- Stats match actual file counts
- All router entries have corresponding files
- All graph nodes have valid references
- No orphaned edges

## Maintaining Consistency

### Automated Hooks

The system has hooks that enforce consistency:

```bash
# .claude/hooks/auto-cross-reference.sh
# Triggers on file creation/deletion
# Reminds to update master docs
```

### Manual Audit

Periodically audit consistency:

```bash
# Count actual files vs stats
ls .claude/commands/*.md | wc -l
# Compare to _stats.json "commands" value

# Check router coverage
# Every command should have router entry
```

### Update Strategy

When updating multiple files:

1. **Batch Updates**: Update all 7 points in one session
2. **Atomic Commits**: One commit per component added
3. **Verification**: Test before and after
4. **Documentation**: Update changelog

## Common Pitfalls

### ❌ Partial Integration

```
Created command file ✅
Updated stats ✅
Forgot context router ❌
→ Component invisible to Context Scout!
```

### ❌ Inconsistent Naming

```
File: my-cool-command.md
Node ID: command-my_cool_cmd
Router: "my-command"
→ Nothing works together!
```

### ❌ Missing Edges

```
Created node ✅
No edges ❌
→ Component isolated, no relationships!
```

### ❌ Stale Stats

```
Added 3 commands
Forgot to update count
→ Stats diverge from reality!
```

## Related

- [Creating Agents](creating-agents.md) - Agent-specific integration
- [Writing Commands](writing-commands.md) - Command-specific integration
- [Architecture Overview](../architecture/index.md) - System structure
- [Knowledge Graph](../architecture/knowledge-graph.md) - Graph details
