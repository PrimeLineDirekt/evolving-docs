# Writing Commands

Commands are the primary way users interact with the Evolving system. This guide shows you how to create powerful, discoverable commands that integrate seamlessly.

## Command File Structure

Commands live in `.claude/commands/` and use markdown format with YAML frontmatter:

```markdown
---
name: status
description: Show current project status and health
allowed-tools:
  - Read
  - Bash
  - Grep
args:
  - name: detail
    description: Level of detail (quick|full)
    required: false
    default: quick
---

# Status Command

## Purpose
Display the current state of the active project including progress, issues, and next steps.

## Steps

1. **Load Domain Memory**
   - Read `_memory/index.json` → active project
   - Read `_memory/projects/{active}.json` → state

2. **Check Git Status**
   - Run `git status --short`
   - Count uncommitted changes

3. **Analyze Task State**
   - Load active tasks (if any)
   - Count pending vs completed

4. **Report Health**
   - Recent failures
   - Known blockers
   - Recommendations

## Output Format

```
📊 Project: {name}
Phase: {current_phase}
Progress: {completed}/{total} features

🔧 Uncommitted Changes: {count}
📋 Active Tasks: {pending}/{total}

⚠️ Issues: {count}
💡 Next: {recommendation}
```

## Examples

```bash
# Quick status (default)
/status

# Detailed status
/status full
```
```

## Required Frontmatter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Command name (lowercase, no slash) |
| `description` | string | ✅ | What the command does (1-2 sentences) |
| `allowed-tools` | array | ❌ | Tools the command can use |
| `args` | array | ❌ | Command arguments/options |
| `agent` | string | ❌ | Pre-defined agent to delegate to |

## Arguments and Options

Define command arguments for flexibility:

```yaml
args:
  - name: target          # Positional arg
    description: What to analyze
    required: true

  - name: depth           # Optional arg with default
    description: Analysis depth
    required: false
    default: shallow

  - name: format          # Choice argument
    description: Output format
    required: false
    default: markdown
    choices: [markdown, json, yaml]
```

**Usage:**
```bash
/analyze src/auth.ts          # target only
/analyze src/auth.ts deep     # target + depth
/analyze src/auth.ts deep json # all args
```

## Command Body Structure

After frontmatter, define the command behavior:

```markdown
# {Command Name}

## Purpose
Why this command exists and what problem it solves.

## Steps
1. **Step Name**: What to do
   - Details
   - Sub-steps

2. **Next Step**: Continue...

## Output Format
How results should be presented to the user.

## Examples
Concrete usage examples with explanations.

## Notes
Edge cases, warnings, or additional context.
```

## Detection Index Registration

Make your command discoverable via natural language:

### 1. Add to Detection Index

```json
// .claude/detection-index.json
{
  "commands": [
    {
      "name": "status",
      "triggers": [
        "status",
        "project status",
        "current state",
        "what's the status",
        "show me progress"
      ],
      "confidence": {
        "high": ["status", "project status"],
        "medium": ["current state", "show progress"],
        "low": ["what's going on", "update"]
      }
    }
  ]
}
```

### 2. Confidence Levels

| Level | Confidence | Behavior |
|-------|------------|----------|
| **high** | 90-100% | Offer command immediately |
| **medium** | 60-89% | Ask "Did you mean /command?" |
| **low** | 30-59% | Don't suggest (ambiguous) |

### 3. Trigger Patterns

```json
{
  "triggers": [
    "exact phrase",                    // Exact match
    "pattern with {variable}",         // Variable part
    "starts with this",                // Prefix match
    "contains keyword anywhere"        // Contains match
  ]
}
```

## Integration Steps

After creating your command, integrate it:

### 1. Update Stats

```json
// _stats.json
{
  "commands": 64  // Increment count
}
```

### 2. Add to Context Router

```json
// _graph/cache/context-router.json
{
  "routes": {
    "project-status": {
      "keywords": ["status", "progress", "health"],
      "primary": {
        "commands": ["/status"]
      }
    }
  }
}
```

### 3. Create Knowledge Graph Node

```json
// _graph/knowledge-nodes.json
{
  "id": "command-status",
  "type": "command",
  "name": "/status",
  "description": "Show current project status",
  "domain": ["project-management"],
  "tags": ["command", "status", "reporting"]
}
```

### 4. Add Graph Edges

```json
// _graph/edges.json
{
  "from": "command-status",
  "to": "memory-domain",
  "type": "reads_from",
  "strength": 1.0
}
```

### 5. Update COMMANDS.md

```markdown
<!-- .claude/COMMANDS.md -->
### /status
Show current project status and health.

**Args**: `[detail]` (quick|full)
**Example**: `/status full`
```

## Command Types

### 1. Query Commands
Read and report information (no side effects).

```yaml
name: list-agents
allowed-tools: [Read, Grep]
```

### 2. Action Commands
Perform operations (modify state).

```yaml
name: create-agent
allowed-tools: [Write, Edit, Bash]
```

### 3. Delegation Commands
Delegate to specialized agents.

```yaml
name: review-code
agent: code-reviewer
```

### 4. Workflow Commands
Multi-step orchestration.

```yaml
name: feature-complete
allowed-tools: [Read, Write, Bash, Task]
```

## Do's and Don'ts

### DO
- ✅ Start with clear purpose
- ✅ Break into numbered steps
- ✅ Specify output format
- ✅ Provide usage examples
- ✅ Handle edge cases
- ✅ Register in detection index
- ✅ Add to knowledge graph

### DON'T
- ❌ Make commands do too much
- ❌ Assume tools are allowed
- ❌ Skip error handling
- ❌ Forget to update stats
- ❌ Use destructive operations without confirmation
- ❌ Duplicate existing command functionality

## Example: Create a Status Command

Let's create a complete status command step by step.

### Step 1: Create Command File

```bash
# .claude/commands/status.md
```

```markdown
---
name: status
description: Show current project status, progress, and health metrics
allowed-tools:
  - Read
  - Bash
  - Grep
args:
  - name: detail
    description: Level of detail (quick|full)
    required: false
    default: quick
---

# Status Command

## Purpose
Provide a quick overview of the current project state including progress, git status, active tasks, and any issues or blockers.

## Steps

### 1. Load Domain Memory
```bash
Read _memory/index.json
Extract: active_context.project
```

```bash
Read _memory/projects/{active}.json
Extract:
  - goals
  - current_phase
  - features (status counts)
  - recent_progress (last 3 entries)
  - known failures
```

### 2. Check Git Status
```bash
Bash: git status --short --branch
Count:
  - Uncommitted changes (M, A, D)
  - Untracked files (??)
  - Branch ahead/behind
```

### 3. Load Active Tasks (if exists)
```bash
TaskList
Count:
  - Pending tasks
  - In-progress tasks
  - Completed tasks (this session)
```

### 4. Analyze Health

**Signals:**
- Recent failures > 2 → ⚠️ Warning
- Uncommitted changes > 10 → 💡 Suggest commit
- No progress entries recent → 💡 Suggest update

### 5. Generate Report

**Quick Mode:**
```
📊 Project: {name}
Phase: {current_phase}
Features: {passing}/{total} passing

🔧 Changes: {uncommitted}
📋 Tasks: {pending} pending

Next: {next_step}
```

**Full Mode:**
```
📊 PROJECT STATUS

Project: {name}
Phase: {current_phase}
Started: {start_date}

🎯 GOALS
{goals list}

✨ FEATURES ({passing}/{total} passing)
✅ {passing features}
🔄 {in_progress features}
❌ {failing features}

📝 RECENT PROGRESS
{last 3 progress entries}

🔧 GIT STATUS
Branch: {branch} [{ahead/behind}]
Uncommitted: {count}
Untracked: {count}

📋 ACTIVE TASKS
Pending: {count}
In Progress: {count}
Completed: {count}

⚠️ ISSUES
{known failures}

💡 NEXT STEPS
{next_step recommendations}
```

## Examples

```bash
# Quick status
/status

# Full detailed status
/status full
```

## Notes

- Gracefully handle missing files (fresh project)
- Show "No active project" if index.json missing
- Cache-friendly (reads only, no writes)
```

### Step 2: Register in Detection Index

```json
// .claude/detection-index.json
{
  "commands": [
    {
      "name": "status",
      "triggers": [
        "status",
        "project status",
        "current status",
        "what's the status",
        "show me status",
        "show progress",
        "project health",
        "where are we"
      ],
      "confidence": {
        "high": ["status", "project status", "/status"],
        "medium": ["current status", "show progress", "project health"],
        "low": ["where are we", "what's up"]
      }
    }
  ]
}
```

### Step 3: Test Command

```bash
# Direct invocation
/status

# Natural language (should detect)
"Show me the project status"
→ Claude: "Did you mean /status?"

# With arguments
/status full
```

## Related

- [Creating Agents](creating-agents.md) - For delegation commands
- [Using Patterns](using-patterns.md) - Apply patterns in commands
- [Extending System](extending-system.md) - Integration checklist
