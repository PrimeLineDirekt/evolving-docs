---
title: Subagent Router
type: hook
tags: ["general", "python"]
lang: en
confidence: 100
---

# Subagent Router


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Hook |
| **Purpose** | SubagentStop Router Hook for Claude Code |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | hooks |</div>

<div class="component-tags">
<span class="tag tag-general">general</span>
<span class="tag tag-python">python</span>
</div>

## What It Does

SubagentStop Router Hook for Claude Code
========================================= Automatically routes subagent outputs to categorized folders based on
content classification and agent type hints. Overview
--------
When a subagent (Task tool) completes, this hook:
1. Extracts the output from the agent's transcript (JSONL file)
2. Classifies content using keyword matching + agent type hints
3. Saves output to category-specific folder with metadata
4. Logs routing decision for audit trail Input Payload (stdin JSON)
--------------------------
{ "hook_event_name": "SubagentStop", "session_id": "uuid", "transcript_path": "/path/to/session.jsonl",      # Parent session transcript "agent_transcript_path": "/path/to/agent-X.jsonl", # Agent-specific transcript "agent_id": "a1b2c3d",                            # Unique agent identifier "cwd": "/working/directory", "permission_mode": "default|plan|acceptEdits|...", "stop_hook_active": false
} Output Files
------------
- Routed content: knowledge/{category}/{prefix}-YYYY-MM-DD-HHMMSS.md
- Routing log: _memory/routing/subagent-routing.log (JSONL)
- Debug log: ~/.claude/hooks/subagent-router-debug.log (if enabled) Configuration
-------------
- Config file: .claude/hooks/subagent-router.json
- Categories, keywords, weights, and agent type hints are configurable
- See config file for detailed options Debug Mode
----------
Enable debug logging via: - Environment: SUBAGENT_ROUTER_DEBUG=1 - File marker: touch ~/.claude/hooks/.debug-subagent-router Exit Codes
---------- 0 = Success (always - routing is passive, never blocks) Usage in settings.json
----------------------
{ "hooks": { "SubagentStop": [{ "matcher": "", "hooks": [{ "type": "command", "command": "python3 .claude/hooks/subagent-router.py", "timeout": 10 }] }] }
} Author: Robin (Evolving Project)
Version: 2.0.0
Last Updated: 2026-01-06

### Key Features

- Type: general
- Language: python

## System Impact




## Architecture




## Usage


### Examples

#### Implementation



**Code:**
```python
def load_config
```




## Configuration



## Best Practices




## Related


---

<small>Source: `.claude/hooks/subagent-router.py`</small>
