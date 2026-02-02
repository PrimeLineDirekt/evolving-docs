# Quick Start Guide

Get up and running with Evolving in 5 minutes.

## Your First Session

### 1. Start Claude Code

```bash
cd /path/to/your/project
claude
```

Claude will automatically detect the Evolving system via symlinks in `~/.claude/`.

### 2. Domain Memory Bootup

On every session start, Claude will:

1. Read `_memory/index.json` to find the active project
2. Load project state from `_memory/projects/{active}.json`
3. Announce the current context

**Example output:**
```
Projekt: evolving-system | Phase: Documentation
Letzter Stand: Created architecture overview
Nächster Schritt: Create getting-started guides
```

This is the **Domain Memory Bootup** - Claude remembers where you left off!

### 3. Try a Simple Command

Let's explore available commands:

```
You: "show me all commands"
```

Claude will recognize this as a trigger for `/commands-list` and ask:

```
Das klingt nach dem /commands-list Command.
Soll ich es ausführen?
```

Type `yes` to proceed. You'll see a categorized list of all 47+ commands.

### 4. Use Plain-Text Detection

Instead of typing `/command-name`, you can use natural language:

**Examples:**

| You say | Claude detects | What happens |
|---------|---------------|--------------|
| "I have a new idea" | `/idea-new` | Creates idea in knowledge graph |
| "Show my ideas" | `/idea-list` | Lists all tracked ideas |
| "Start planning mode" | `/plan` | Activates Plan mode |
| "Create a new command" | `/command-new` | Guides you through command creation |

**Rule:** Claude NEVER auto-executes. It always asks for confirmation first.

### 5. Your First Task

Let's create a simple learning entry:

```
You: "I learned something new about Git hooks"

Claude: "Das klingt nach /learning-new. Soll ich es nutzen?"

You: "yes"

Claude: [Executes /learning-new command]
What did you learn? [...]
```

Follow the prompts to document your learning. It will be:
- Saved in `knowledge/learnings/`
- Added to the knowledge graph
- Indexed for future retrieval

### 6. Check Your Progress

View what you've accomplished:

```
You: "show me my recent progress"

Claude: [Reads _memory/projects/{active}.json]

"Recent progress:
- 2024-02-03: Created getting-started guides
- 2024-02-02: Implemented documentation system
- 2024-02-01: Set up MCP integration"
```

## Understanding the Output

### Hook Messages

You'll see hook messages during operations:

```
✓ PASS: comment-density acceptable (15%)
✓ PASS: delegation hints present
⚠ SYNC CHECK: Command - new-command.md
```

**What they mean:**
- **PASS**: Quality check succeeded
- **BLOCK**: Quality check failed, action prevented
- **SYNC CHECK**: Master docs may need updating
- **INFO**: Informational message

### Agent Delegation

When Claude delegates to specialized agents:

```
[Delegating to Explore agent with haiku model...]
```

**Why delegation?**
- Fresh context (no session history overhead)
- Specialized expertise (debugging, exploration, review)
- Cost-efficient (haiku for simple tasks, sonnet for complex)

### Context Scout

Before responding, Claude runs Context Scout to load relevant patterns/rules:

```
[Context Scout: Matched 'debugging' → loading observe-before-editing.md]
```

This happens automatically - no action needed from you.

## Common Workflows

### Starting a New Feature

```
You: "I want to implement user authentication"

Claude: [Context Scout loads relevant patterns]
        "Das klingt nach /plan. Soll ich Planning Mode starten?"

You: "yes"

Claude: [Enters Plan mode]
        "Describe the feature requirements..."
```

### Debugging an Issue

```
You: "The login endpoint is failing"

Claude: [Context Scout loads debugging rules]
        [Delegates to Explore agent to analyze codebase]

        "Found the issue in src/auth.ts line 42..."
```

### Documenting a Decision

```
You: "We decided to use Supabase instead of Firebase"

Claude: "Das klingt nach /decision-new. Soll ich es nutzen?"

You: "yes"

Claude: [Guides you through decision documentation]
```

## Next Steps

Now that you've completed your first session:

1. **Explore Commands**: Try `/commands-list` to see all available commands
2. **Customize**: Check the [Configuration Guide](./configuration.md)
3. **Learn Patterns**: Read about [Prompt Patterns](../core-concepts/prompt-patterns.md)
4. **Understand Memory**: Deep dive into [Domain Memory](../core-concepts/domain-memory.md)

## Tips for Success

### Do
- Use natural language - plain-text detection works great
- Let Domain Memory track your progress
- Trust the delegation system - agents are specialized
- Review hook messages - they prevent quality issues

### Don't
- Manually update `_stats.json` - let hooks handle it
- Skip Domain Memory bootup announcements - they're context!
- Fight the system - if Claude suggests a pattern, try it
- Auto-execute commands - confirmation is a safety feature

## Getting Help

### In-Session Help

```
You: "explain domain memory"

Claude: [Context Scout loads domain-memory-bootup.md]
        [Explains the concept with examples]
```

### Command-Specific Help

```
You: "how does /plan work?"

Claude: [Reads .claude/commands/plan.md]
        [Explains usage, examples, options]
```

### Browse Documentation

All documentation is in `docs/`:
- **Core Concepts**: `docs/en/core-concepts/`
- **Architecture**: `docs/en/architecture/`
- **Guides**: `docs/en/guides/`

## Troubleshooting

### "Command not detected"

**Issue**: Plain-text trigger didn't work

**Solution**: Try being more explicit:
```
Instead of: "show stuff"
Try: "show me all commands"
Or: "/commands-list"
```

### "No active project"

**Issue**: Domain Memory bootup failed

**Solution**:
```
Ensure _memory/index.json exists with active_context.project
Or create a new project via /project-new
```

### "Hook failed"

**Issue**: A hook blocked an operation

**Solution**: Read the hook message - it explains why:
```
✗ BLOCK: comment-density too high (75%)
→ Fix: Reduce comments, improve self-documenting code
```

## You're Ready!

You now know:
- ✅ How Domain Memory works
- ✅ How to use plain-text commands
- ✅ How delegation helps you
- ✅ How to track progress
- ✅ Where to get help

Start exploring! The system will guide you through each workflow.

**Recommended first commands to try:**
1. `/commands-list` - See all available commands
2. `/idea-new` - Track a new idea
3. `/learning-new` - Document something you learned
4. `/plan` - Plan your next feature

Happy evolving! 🚀
