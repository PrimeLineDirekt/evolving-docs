# Configuration

Learn how to customize the Evolving system for your needs.

## Configuration Files Overview

The Evolving system uses multiple configuration files, each serving a specific purpose:

| File | Purpose | Scope |
|------|---------|-------|
| `CLAUDE.md` | Project-level instructions | Per project |
| `~/.claude/CLAUDE.md` | Global user instructions | All projects |
| `.claude/hooks/*.{sh,py}` | Automation and quality gates | System-wide |
| `_memory/index.json` | Active context tracking | Per project |
| `_graph/cache/*.json` | Routing and indexing | System-wide |
| `_stats.json` | Component inventory | System-wide |

## CLAUDE.md Customization

### Project-Level Configuration

Create a `CLAUDE.md` in your project root to customize behavior:

```markdown
# My Project

## User: YourName

Role/Context about you

## Session-Verhalten

### Memory Location
- Domain Memory: `_memory/`
- Knowledge Base: `knowledge/`

### Project-Specific Rules
- Always use TypeScript strict mode
- Prefer functional components in React
- Test coverage minimum: 80%

## Tech Stack
- Frontend: React + TypeScript + Tailwind
- Backend: Node.js + Express
- Database: PostgreSQL + Prisma
- Testing: Vitest + React Testing Library
```

### Global User Configuration

Your `~/.claude/CLAUDE.md` applies to ALL projects:

```markdown
# Global Claude Configuration

## User: Robin

AI-First Developer | Location | Projects: X, Y, Z
**Stil**: Sparring > Ja-Sagen | Chain of Thought | 80/20 Fokus

## Core Principles

### Sparring > Ja-Sagen
- Radikale Ehrlichkeit
- Annahmen hinterfragen
- Konstruktive Kritik

### 80/20 Prinzip
- Fokus auf High-Impact
- Over-Engineering vermeiden

## Default Behavior
- Always explain reasoning (Chain of Thought)
- Use German for communication, English for code
- Prefer delegation for exploration tasks
```

**Priority**: Project `CLAUDE.md` overrides global settings.

## Hook Configuration

Hooks run automatically to enforce quality and automate workflows.

### Available Hooks

Located in `.claude/hooks/`:

| Hook | Trigger | Purpose |
|------|---------|---------|
| `check-comments.py` | Write/Edit | Prevent over-commenting (>25%) |
| `delegation-enforcer.py` | Session end | Track delegation gaps |
| `auto-cross-reference.sh` | Write/Edit | Detect doc sync needs |
| `session-summary.sh` | Session end | Create handoff if work done |
| `todo-enforcer.sh` | Session end | Warn about incomplete todos |

### Configuring Hooks

Hooks use configuration from their docstrings or separate config files:

**Example: check-comments.py threshold**
```python
# .claude/hooks/check-comments.py
MAX_COMMENT_RATIO = 0.25  # 25% max

# To customize:
# Edit this value directly in the hook file
```

**Example: delegation-enforcer.py config**
```python
# Uses _graph/cache/delegation-config.json
{
  "task_types": {
    "exploration": {
      "agent": "Explore",
      "model": "haiku",
      "keywords": ["find", "search", "explore"]
    }
  }
}
```

### Disabling Hooks

To disable a hook temporarily:

```bash
# Rename to add .disabled extension
mv .claude/hooks/check-comments.py .claude/hooks/check-comments.py.disabled
```

To re-enable:
```bash
mv .claude/hooks/check-comments.py.disabled .claude/hooks/check-comments.py
```

**Warning**: Disabling quality hooks (`check-comments.py`) may lead to degraded code quality.

## MCP Server Setup

The Evolving system can integrate with MCP (Model Context Protocol) servers for extended capabilities.

### Firecrawl Integration

For web scraping and content extraction:

```bash
# Install MCP server
npm install -g @modelcontextprotocol/server-firecrawl

# Configure in Claude Code settings
# Add to ~/.claude/mcp-servers.json:
{
  "firecrawl": {
    "command": "mcp-server-firecrawl",
    "env": {
      "FIRECRAWL_API_KEY": "your-api-key"
    }
  }
}
```

**Usage**: Tools like `firecrawl_scrape`, `firecrawl_search` become available.

### Custom MCP Servers

Create project-specific MCP servers:

```bash
# In your project
mkdir mcp-servers
cd mcp-servers

# Create server
npm init -y
npm install @modelcontextprotocol/sdk

# Implement server.js
# Register in ~/.claude/mcp-servers.json
```

See [MCP Documentation](https://modelcontextprotocol.io/) for details.

## Memory System Setup

### Project Memory Initialization

Create memory structure for a new project:

```bash
# Create directories
mkdir -p _memory/projects
mkdir -p _memory/analytics
mkdir -p _memory/experiences

# Create index
cat > _memory/index.json << 'EOF'
{
  "active_context": {
    "project": "my-project",
    "workflow": null,
    "last_updated": "2024-02-03T10:00:00Z"
  }
}
EOF

# Create project memory
cat > _memory/projects/my-project.json << 'EOF'
{
  "name": "my-project",
  "description": "Project description",
  "current_phase": "Setup",
  "goals": [],
  "features": {},
  "state": {
    "current_phase": "Setup",
    "blockers": []
  },
  "progress": [],
  "failures": []
}
EOF
```

Or use the `/project-new` command to automate this.

### Experience Memory Configuration

Experiences decay over time based on trust and relevance:

**Decay configuration** in `_memory/experiences/SCHEMA.md`:
```markdown
Decay factors:
- trust_level: high (1.0), medium (0.8), low (0.5)
- age_factor: Exponential decay over 30 days
- effective_relevance = base * decay * trust
```

**Default thresholds**:
- Load experiences with `effective_relevance > 30`
- Archive if `< 10` and age > 60 days

To adjust, modify the bootup logic in `.claude/rules/domain-memory-bootup.md`.

### Knowledge Graph Setup

The knowledge graph requires initial indexing:

```bash
# Generate indices (future automation)
# For now, ensure these files exist:
ls _graph/
# Should show:
# - nodes.json
# - edges.json
# - taxonomy.json
# - index/by-type.json
# - index/by-domain.json
# - cache/context-router.json
```

Update `_graph/cache/context-router.json` to customize keyword routing:

```json
{
  "routes": {
    "debugging": {
      "keywords": ["debug", "bug", "error", "fix"],
      "primary": [
        "knowledge/rules/debugging/observe-before-editing.md",
        "knowledge/rules/debugging/evidence-before-claims.md"
      ],
      "secondary": [
        "knowledge/patterns/systematic-debugging-pattern.md"
      ]
    }
  }
}
```

## Advanced Configuration

### Task Persistence

Enable persistent task lists across terminal sessions:

```bash
# Add to ~/.bashrc or ~/.zshrc
export CLAUDE_CODE_TASK_LIST_ID=evolving

# Reload
source ~/.bashrc
```

**Effect**: Tasks survive terminal closure and reopening.

### Context Budget Limits

Configure degradation thresholds in `_graph/cache/orchestration-config.json`:

```json
{
  "context_thresholds": {
    "warning": 0.7,
    "critical": 0.85,
    "max_summary_only": 0.9
  },
  "model_limits": {
    "opus": 200000,
    "sonnet": 180000
  }
}
```

### Delegation Scoring

Customize delegation decisions in `_graph/cache/delegation-config.json`:

```json
{
  "score_factors": {
    "scope_multi_file": 2,
    "bulk_operation": 2,
    "research_task": 2
  },
  "score_threshold": 3,
  "task_types": {
    "exploration": {
      "agent": "Explore",
      "model": "haiku",
      "traits": null
    }
  }
}
```

### Plain-Text Detection Tuning

Adjust command detection confidence in `.claude/detection-index.json`:

```json
{
  "commands": [
    {
      "name": "idea-new",
      "triggers": ["new idea", "i have an idea"],
      "confidence_boost": 10,
      "anti_patterns": ["no ideas", "bad idea"]
    }
  ]
}
```

**Confidence levels**:
- `9-10`: Auto-suggest (high confidence)
- `6-8`: Ask user (medium)
- `1-5`: Ignore (low)

## Configuration Best Practices

### Do
- Keep project `CLAUDE.md` focused on project-specific rules
- Use global `~/.claude/CLAUDE.md` for personal preferences
- Test hook changes on non-critical files first
- Document custom MCP servers in project README
- Version control `CLAUDE.md` and `_memory/` structure

### Don't
- Hardcode API keys in configuration (use environment variables)
- Disable hooks without understanding their purpose
- Manually edit `_stats.json` (let hooks manage it)
- Ignore hook warnings - they prevent issues
- Over-configure - start simple, add as needed

## Validation

After configuration changes, verify:

```bash
# Check symlinks still work
ls -la ~/.claude/

# Verify hooks are executable
ls -la .claude/hooks/*.{sh,py}

# Test memory bootup
# Start Claude Code and check for:
# "Projekt: {name} | Phase: {phase}"

# Verify MCP servers
# In Claude Code session:
# Check available tools include MCP-provided ones
```

## Next Steps

- [Core Concepts](../core-concepts/index.md) - Understand the system
- [Architecture](../architecture/index.md) - How it all fits together
- [Guides](../guides/creating-commands.md) - Create custom components

## Troubleshooting

### "Configuration not loaded"

**Issue**: Project `CLAUDE.md` changes not reflected

**Solution**: Restart Claude Code session - config is read at startup.

### "Hook failed with import error"

**Issue**: Python dependencies missing

**Solution**:
```bash
# Check Python version
python --version  # Must be 3.12+

# Verify hook syntax
python .claude/hooks/check-comments.py --help
```

### "MCP server not responding"

**Issue**: MCP tools unavailable

**Solution**:
```bash
# Check server is running
ps aux | grep mcp-server

# Check configuration
cat ~/.claude/mcp-servers.json

# Restart Claude Code
```

## Configuration Checklist

Before starting development:

- [ ] Project `CLAUDE.md` created and customized
- [ ] Global `~/.claude/CLAUDE.md` reflects your preferences
- [ ] Hooks are executable (`chmod +x`)
- [ ] Memory structure initialized (`_memory/`)
- [ ] Knowledge graph indexed (`_graph/`)
- [ ] MCP servers configured (if needed)
- [ ] Task persistence enabled (optional)
- [ ] Configuration validated

You're now ready to use the fully configured Evolving system!
