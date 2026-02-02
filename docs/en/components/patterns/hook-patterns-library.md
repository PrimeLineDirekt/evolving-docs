---
title: hook-patterns-library
type: pattern
tags: []
lang: en
confidence: 100
---

# hook-patterns-library


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
```bash
# PreToolUse - Alle Tools
echo "[$(date)] $CLAUDE_TOOL_NAME" >> ~/.claude/activity.log
```


#### Example



**Code:**
```bash
# PreToolUse - Edit|MultiEdit
[[ -f "$CLAUDE_TOOL_FILE_PATH" ]] && \
  cp "$CLAUDE_TOOL_FILE_PATH" "$CLAUDE_TOOL_FILE_PATH.$(date +%s).bak" 2>/dev/null || true
```


#### Example



**Code:**
```bash
# PostToolUse - Edit
if [[ "$CLAUDE_TOOL_FILE_PATH" =~ \.(js|ts)$ ]]; then
  npx prettier --write "$CLAUDE_TOOL_FILE_PATH" 2>/dev/null || true
elif [[ "$CLAUDE_TOOL_FILE_PATH" == *.py ]]; then
  black "$CLAUDE_TOOL_FILE_PATH" 2>/dev/null || true
fi
```


#### Example



**Code:**
```bash
# PostToolUse - Edit|Write
git rev-parse --git-dir >/dev/null 2>&1 && \
  git add "$CLAUDE_TOOL_FILE_PATH" 2>/dev/null || true
```


#### Example



**Code:**
```bash
# PostToolUse - *
if command -v osascript >/dev/null; then
  osascript -e 'display notification "$CLAUDE_TOOL_NAME completed" with title "Claude Code"'
elif command -v notify-send >/dev/null; then
  notify-send "Claude Code" "$CLAUDE_TOOL_NAME completed"
fi
```


#### Example



**Code:**
```bash
# PostToolUse - Edit
if [[ -f package.json ]]; then
  npm test 2>/dev/null || yarn test 2>/dev/null || true
elif [[ -f pytest.ini ]]; then
  pytest 2>/dev/null || true
fi
```


#### Example



**Code:**
```bash
# PostToolUse - Edit
if [[ -f package.json ]] && grep -q '"build"' package.json; then
  npm run build 2>/dev/null || true
elif [[ -f Makefile ]]; then
  make 2>/dev/null || true
fi
```


#### Example



**Code:**
```bash
# PostToolUse - Edit|Write
if command -v gitleaks >/dev/null; then
  gitleaks detect --source="$CLAUDE_TOOL_FILE_PATH" --no-git 2>/dev/null || true
fi
grep -qE '(password|secret|key)\s*=' "$CLAUDE_TOOL_FILE_PATH" && \
  echo "⚠️ Potential secrets in $CLAUDE_TOOL_FILE_PATH" || true
```


#### Example



**Code:**
```bash
# PreToolUse - Edit|Write
for p in '/etc/*' '/usr/bin/*' '*.production.*' '*prod*config*' '/node_modules/*'; do
  [[ "$CLAUDE_TOOL_FILE_PATH" == $p ]] && \
    echo "Error: Protected file" >&2 && exit 1
done
```


#### Example



**Code:**
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{"type": "command", "command": "BACKUP_PATTERN"}]
    }],
    "PostToolUse": [
      {"matcher": "Edit", "hooks": [{"type": "command", "command": "FORMAT_PATTERN"}]},
      {"matcher": "Edit|Write", "hooks": [{"type": "command", "command": "GIT_ADD_PATTERN"}]}
    ]
  }
}
```


#### Example



**Code:**
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{"type": "command", "command": "PROTECT_PATTERN"}]
    }],
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{"type": "command", "command": "SECURITY_PATTERN"}]
    }]
  }
}
```


#### Example



**Code:**
```bash
2>/dev/null || true
```


#### Example



**Code:**
```bash
[[ -f "$CLAUDE_TOOL_FILE_PATH" ]] && ...
```


#### Example



**Code:**
```bash
command -v gitleaks >/dev/null && ...
```


#### Example



**Code:**
```json
{"matcher": "Edit|Write", "hooks": [...]}
```


#### Example



**Code:**
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit",
      "hooks": [{
        "type": "command",
        "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/auto-format.sh"
      }]
    }]
  }
}
```


#### Example



**Code:**
```bash
.claude/hooks/
├── backup.sh
├── auto-format.sh
├── git-add.sh
├── security-scan.sh
└── protect.sh
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/hook-patterns-library.md`</small>
