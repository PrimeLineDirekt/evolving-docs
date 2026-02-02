# Installation

This guide will walk you through installing and setting up the Evolving system.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Claude Code CLI**: The official Claude CLI tool
  - Install via: `npm install -g @anthropic-ai/claude-code`
  - Verify: `claude --version`

- **Git**: For version control and repository cloning
  - Verify: `git --version`

- **Python 3.12+**: Required for hooks and automation scripts
  - Verify: `python --version`

- **Node.js 18+**: For MCP servers and some automation
  - Verify: `node --version`

## Installation Steps

### 1. Clone the Repository

```bash
# Clone to your preferred location
cd ~/Buisiness  # or your preferred directory
git clone <repository-url> Evolving
cd Evolving
```

### 2. Create Symlinks

The Evolving system uses symlinks to make components globally available across all your projects.

```bash
# Create symlink directory if it doesn't exist
mkdir -p ~/.claude

# Create symlinks for all components
ln -s "$(pwd)/.claude/commands" ~/.claude/commands
ln -s "$(pwd)/.claude/agents" ~/.claude/agents
ln -s "$(pwd)/.claude/skills" ~/.claude/skills
ln -s "$(pwd)/.claude/rules" ~/.claude/rules
ln -s "$(pwd)/.claude/blueprints" ~/.claude/blueprints
ln -s "$(pwd)/.claude/hooks" ~/.claude/hooks
```

**Why symlinks?**
- Makes all 47+ commands available in any project
- Centralizes updates - change once, apply everywhere
- Allows project-specific overrides when needed

### 3. Verify Installation

```bash
# Check symlinks
ls -la ~/.claude/

# You should see:
# commands -> /path/to/Evolving/.claude/commands
# agents -> /path/to/Evolving/.claude/agents
# skills -> /path/to/Evolving/.claude/skills
# rules -> /path/to/Evolving/.claude/rules
# blueprints -> /path/to/Evolving/.claude/blueprints
# hooks -> /path/to/Evolving/.claude/hooks

# Check component counts
wc -l _stats.json

# Should show stats for all components
```

### 4. Set Up Environment Variables (Optional)

For persistent task lists across sessions:

```bash
# Add to your ~/.bashrc or ~/.zshrc
export CLAUDE_CODE_TASK_LIST_ID=evolving

# Reload shell
source ~/.bashrc  # or source ~/.zshrc
```

## Troubleshooting

### Symlinks Not Working

**Issue**: Commands not detected in new projects

**Solution**:
```bash
# Verify symlinks exist
ls -la ~/.claude/

# If broken, recreate them
rm -rf ~/.claude/commands ~/.claude/agents  # etc.
# Then run step 2 again
```

### Python Version Issues

**Issue**: Hooks failing with import errors

**Solution**:
```bash
# Check Python version
python --version

# If < 3.12, install newer version
# macOS with Homebrew:
brew install python@3.12

# Update PATH if needed
export PATH="/opt/homebrew/opt/python@3.12/bin:$PATH"
```

### Permission Errors

**Issue**: Cannot create symlinks or execute hooks

**Solution**:
```bash
# Make hooks executable
chmod +x .claude/hooks/*.sh
chmod +x .claude/hooks/*.py

# If symlink creation fails, check directory permissions
ls -la ~/.claude/
```

### Detection Index Not Found

**Issue**: Plain-text command detection not working

**Solution**:
```bash
# Verify detection index exists
cat .claude/detection-index.json

# If missing, regenerate it (command coming in future version)
# For now, ensure you cloned the full repository
```

## Next Steps

- [Quick Start Guide](./quick-start.md) - Your first session
- [Configuration](./configuration.md) - Customize the system
- [Architecture Overview](../architecture/index.md) - Understand the system

## Verification Checklist

Before proceeding, verify:

- [ ] Claude Code CLI installed and accessible
- [ ] Repository cloned successfully
- [ ] Symlinks created in `~/.claude/`
- [ ] Python 3.12+ available
- [ ] Hooks are executable (`chmod +x`)
- [ ] `_stats.json` readable and contains component counts
- [ ] `.claude/detection-index.json` exists

If all checks pass, you're ready for the [Quick Start Guide](./quick-start.md)!
