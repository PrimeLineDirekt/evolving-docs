---
title: Guides
description: Step-by-step tutorials for common tasks
---

# Guides

Practical guides to help you get the most out of the Evolving system.

## Getting Started

| Guide | Description | Time |
|-------|-------------|------|
| [Quick Start](../getting-started/quick-start.md) | Your first session with Evolving | 5 min |
| [Configuration](../getting-started/configuration.md) | Customize your setup | 10 min |

## Creating Components

| Guide | Description | Time |
|-------|-------------|------|
| [Creating Agents](creating-agents.md) | Build autonomous task executors | 15 min |
| [Writing Commands](writing-commands.md) | Add user-invocable actions | 10 min |
| [Using Patterns](using-patterns.md) | Apply reusable solutions | 10 min |
| [Extending the System](extending-system.md) | Add new capabilities | 20 min |

## Working with Memory

| Guide | Description | Time |
|-------|-------------|------|
| Domain Memory Basics | Track project state | 10 min |
| Experience Memory | Learn from solutions | 15 min |
| Session Handoffs | Preserve context | 5 min |

## Agent Workflows

| Guide | Description | Time |
|-------|-------------|------|
| Delegation Patterns | When and how to delegate | 15 min |
| Multi-Agent Tasks | Coordinate agent swarms | 20 min |
| Review Pipelines | Automatic code review | 10 min |

## Automation

| Guide | Description | Time |
|-------|-------------|------|
| Hook Development | Create event triggers | 15 min |
| Workflow Detection | Natural language commands | 10 min |
| Auto-Learning Setup | Generate rules from corrections | 10 min |

## Best Practices

### Do

- ✅ Start with Domain Memory for project tracking
- ✅ Use delegation for multi-file tasks
- ✅ Let hooks handle repetitive checks
- ✅ Review auto-generated rules periodically

### Don't

- ❌ Load everything at session start
- ❌ Delegate trivial 1-2 line changes
- ❌ Ignore hook warnings
- ❌ Skip the verification step

## Quick Reference

### Common Commands

```bash
/health-dashboard     # System health
/context-stats        # Token usage
/inventory-report     # All components
/whats-next          # Create handoff
```

### Delegation Score

| Factor | Points |
|--------|--------|
| Scope > 2 files | +2 |
| Bulk operation | +2 |
| Research task | +2 |
| Code review | +2 |
| Critical keywords | -10 |
| User wants to see | -5 |

**Score ≥ 3 = Delegate**

### Memory Paths

```
_memory/
├── index.json           # Active context
├── projects/{name}.json # Project state
├── experiences/         # Learned solutions
└── workflows/active.json
```

## Need More?

- Browse [Components](../components/index.md) for available tools
- Check [Architecture](../architecture/index.md) for system design
- Explore [Features](../features/index.md) for capabilities

## Contributing Guides

Have a workflow that works well? Consider contributing a guide:

1. Write in Markdown
2. Include practical examples
3. Estimate time to complete
4. Submit via PR

We welcome community contributions!
