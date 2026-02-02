---
title: hook-development-reference
type: pattern
tags: []
lang: en
confidence: 100
---

# hook-development-reference


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Pattern |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | patterns |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "default|plan|acceptEdits|bypassPermissions",
  "hook_event_name": "PreToolUse",
  "tool_name": "string",
  "tool_input": {
    "file_path": "string",
    "command": "string"
  },
  "tool_use_id": "string"
}
```


#### Example



**Code:**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask",
    "permissionDecisionReason": "string",
    "updatedInput": {}
  },
  "continue": true,
  "stopReason": "string",
  "systemMessage": "string",
  "suppressOutput": true
}
```


#### Example



**Code:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "PostToolUse",
  "tool_name": "string",
  "tool_input": {},
  "tool_response": {
    "filePath": "string",
    "success": true,
    "output": "string",
    "exitCode": 0
  },
  "tool_use_id": "string"
}
```


#### Example



**Code:**
```json
{
  "decision": "block",
  "reason": "string",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "string"
  },
  "continue": true,
  "stopReason": "string",
  "suppressOutput": true
}
```


#### Example



**Code:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "string"
}
```


#### Example



**Code:**
```json
{
  "decision": "block",
  "reason": "string",
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "string"
  }
}
```


#### Example



**Code:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "SessionStart",
  "source": "startup|resume|clear|compact"
}
```


#### Example



**Code:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "SessionEnd",
  "reason": "clear|logout|prompt_input_exit|other"
}
```


#### Example



**Code:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "Stop",
  "stop_hook_active": false
}
```


#### Example



**Code:**
```json
{
  "decision": "block",
  "reason": "string"
}
```


#### Example



**Code:**
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "permission_mode": "string",
  "hook_event_name": "PreCompact",
  "trigger": "manual|auto",
  "custom_instructions": "string"
}
```


#### Example



**Code:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{
          "type": "command",
          "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/my-hook.sh",
          "timeout": 60
        }]
      }
    ]
  }
}
```


#### Example



**Code:**
```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{ "type": "command", "command": "/path/to/hook.sh" }]
    }]
  }
}
```


#### Example



**Code:**
```bash
#!/bin/bash
set -e
cd "$CLAUDE_PROJECT_DIR/.claude/hooks"
cat | npx tsx src/my-hook.ts
```


#### Example



**Code:**
```bash
#!/bin/bash
set -e
cat | python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/my-hook.py"
```


#### Example



**Code:**
```bash
# PreToolUse (Bash)
echo '{"tool_name":"Bash","tool_input":{"command":"ls"},"session_id":"test"}' | \
  .claude/hooks/my-hook.sh

# PostToolUse (Write)
echo '{"tool_name":"Write","tool_input":{"file_path":"test.md"},"tool_response":{"success":true},"session_id":"test"}' | \
  .claude/hooks/my-hook.sh

# SessionStart
echo '{"hook_event_name":"SessionStart","source":"startup","session_id":"test"}' | \
  .claude/hooks/session-start.sh

# UserPromptSubmit
echo '{"prompt":"test prompt","session_id":"test"}' | \
  .claude/hooks/prompt-submit.sh
```


#### Example



**Code:**
```python
#!/usr/bin/env python3
import json, sys

data = json.load(sys.stdin)
path = data.get('tool_input', {}).get('file_path', '')

BLOCKED = ['.env', 'secrets.json', '.git/']
if any(b in path for b in BLOCKED):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": f"Blocked: {path} is protected"
        }
    }))
else:
    print('{}')
```


#### Example



**Code:**
```bash
#!/bin/bash
INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

if [[ "$FILE" == *.ts ]] || [[ "$FILE" == *.tsx ]]; then
  npx prettier --write "$FILE" 2>/dev/null
fi

echo '{}'
```


#### Example



**Code:**
```bash
#!/bin/bash
echo "Git status:"
git status --short 2>/dev/null || echo "(not a git repo)"
echo ""
echo "Recent commits:"
git log --oneline -5 2>/dev/null || echo "(no commits)"
```


#### Example



**Code:**
```python
#!/usr/bin/env python3
import json, sys, subprocess

data = json.load(sys.stdin)

# Prevent infinite loops
if data.get('stop_hook_active'):
    print('{}')
    sys.exit(0)

result = subprocess.run(['npm', 'test'], capture_output=True)
if result.returncode != 0:
    print(json.dumps({
        "decision": "block",
        "reason": "Tests are failing. Please fix before stopping."
    }))
else:
    print('{}')
```


#### Example



**Code:**
```bash
#!/bin/bash
INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Index knowledge files immediately
if [[ "$FILE" == *"knowledge/"* ]] || [[ "$FILE" == *"_handoffs/"* ]]; then
  python3 scripts/index_file.py --file "$FILE" &
fi

echo '{}'
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/hook-development-reference.md`</small>
