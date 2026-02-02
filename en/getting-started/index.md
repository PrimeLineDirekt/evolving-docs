---
title: Getting Started
description: Get up and running with Evolving in minutes
---

# Getting Started

This guide will help you install, configure, and start using the Evolving system with Claude Code.

## Prerequisites

Before you begin, ensure you have:

- **Claude Code CLI** installed and authenticated
- **Git** for cloning the repository
- **Python 3.12+** for generation scripts (optional)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/neoforce/evolving.git
cd evolving
```

### 2. Symlink Configuration (Recommended)

For the best experience, symlink the `.claude` directory to your home:

```bash
# Backup existing config if any
mv ~/.claude ~/.claude.backup

# Create symlink
ln -s $(pwd)/.claude ~/.claude
```

### 3. Start Claude Code

```bash
claude
```

That's it! Claude will automatically load the Evolving system via the CLAUDE.md file.

## What Happens at Startup

When you start a session, Evolving:

1. **Loads Domain Memory** - Reads your active project state from `_memory/`
2. **Initializes Context Router** - Prepares keyword-to-resource mapping
3. **Activates Hooks** - Enables event-triggered behaviors
4. **Announces State** - Shows current project, phase, and next steps

## Your First Commands

Try these commands to explore the system:

```
/health-dashboard     # Quick system health overview
/context-stats        # See context window usage
/inventory-report     # Full component inventory
```

## Next Steps

- [Installation Details](installation.md) - Full installation guide
- [Quick Start Tutorial](quick-start.md) - Hands-on walkthrough
- [Configuration](configuration.md) - Customize your setup

## Need Help?

- Check the [Architecture](../architecture/index.md) section to understand how things work
- Browse [Components](../components/index.md) to see what's available
- Read the [Guides](../guides/index.md) for specific tasks
