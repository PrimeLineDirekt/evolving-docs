---
title: safety-hooks-framework-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# safety-hooks-framework-pattern


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
Tool Call
    │
    ├── PreToolUse Hook
    │   ├── check_rm_command()
    │   ├── check_git_checkout_command()
    │   ├── check_git_add_command()
    │   ├── check_git_commit_command()
    │   ├── check_env_file_access()
    │   └── check_file_length_limit()
    │
    └── Entscheidung
        ├── "approve" → Tool ausführen
        ├── "ask" → User-Approval anfordern
        └── "block/deny" → Tool blockieren mit Reason
```


#### Example



**Code:**
```python
def main():
    data = json.load(sys.stdin)

    if data.get("tool_name") != "Bash":
        return {"decision": "approve"}

    command = data.get("tool_input", {}).get("command", "")

    # Alle Checks ausführen
    checks = [
        check_rm_command,
        check_git_add_command,
        check_git_checkout_command,
        check_git_commit_command,
        check_env_file_access,
    ]

    block_reasons = []
    ask_reasons = []

    for check_func in checks:
        decision, reason = check_func(command)
        if decision == "block":
            block_reasons.append(reason)
        elif decision == "ask":
            ask_reasons.append(reason)

    # Priorität: block > ask > allow
    if block_reasons:
        return {"decision": "deny", "reason": combined_reason}
    elif ask_reasons:
        return {"decision": "ask", "reason": combined_reason}
    else:
        return {"decision": "approve"}
```


#### Example



**Code:**
```json
{
  "description": "Safety hooks to block or require approval",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{
          "type": "command",
          "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/bash_hook.py",
          "timeout": 10
        }]
      },
      {
        "matcher": "Edit",
        "hooks": [{
          "type": "command",
          "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/file_length_limit_hook.py",
          "timeout": 10
        }]
      },
      {
        "matcher": "Write",
        "hooks": [{
          "type": "command",
          "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/file_length_limit_hook.py",
          "timeout": 10
        }]
      }
    ]
  }
}
```


#### Example



**Code:**
```python
def check_rm_command(command):
    """
    Patterns die gematched werden:
    - rm ...
    - /bin/rm ...
    - command && rm ...
    """
    if re.search(r'(^|[;&|]\s*)(/\S*/)?rm\b', normalized_cmd):
        reason = (
            "Instead of using 'rm':\n"
            "- MOVE files to TRASH directory\n"
            "- Add entry to TRASH-FILES.md with reason"
        )
        return True, reason
    return False, None
```


#### Example



**Code:**
```python
env_patterns = [
    # Reading
    r'\bcat\s+.*\.env\b',
    r'\bless\s+.*\.env\b',
    r'\bhead\s+.*\.env\b',
    r'\btail\s+.*\.env\b',

    # Editors
    r'\bnano\s+.*\.env\b',
    r'\bvi\s+.*\.env\b',
    r'\bvim\s+.*\.env\b',
    r'\bcode\s+.*\.env\b',

    # Writing
    r'>\s*\.env\b',
    r'>>\s*\.env\b',
    r'\bsed\s+.*-i.*\.env\b',
    r'\bcp\s+.*\.env\b',
    r'\bmv\s+.*\.env\b',

    # Searching
    r'\bgrep\s+.*\.env\b',
    r'\brg\s+.*\.env\b',
    r'\bfind\s+.*-name\s+["\']?\.env',
]
```


#### Example



**Code:**
```python
# IMMER blockieren:
dangerous_patterns = [
    (r'\bgit\s+checkout\s+(-f|--force)\b',
     "FORCES checkout and DISCARDS all uncommitted changes!"),
    (r'\bgit\s+checkout\s+\.',
     "Will DISCARD ALL changes in current directory!"),
    (r'\bgit\s+checkout\s+.*\s+--\s+\.',
     "Will DISCARD ALL changes!"),
]

# Bei uncommitted changes: Warnung + Alternativen
if has_changes:
    warning = f"WARNING: {num_changes} uncommitted change(s)!"
    warning += "\nOptions:"
    warning += "\n1. git stash"
    warning += "\n2. git commit -am 'message'"
    warning += "\n3. git restore <files>"
    warning += "\n4. git switch (safer)"
    return True, warning
```


#### Example



**Code:**
```python
# Beispiele die geprüft werden:
# - git add . (alles hinzufügen)
# - git add -A (alles inkl. deletions)
# - git add *.log (sensitive files)
```


#### Example



**Code:**
```python
# Beispiele:
# - Commit ohne Message
# - Commit mit sensitive Dateien im Staging
# - Force-Commits
```


#### Example



**Code:**
```python
MAX_FILE_LINES = 10000

SOURCE_CODE_EXTENSIONS = {
    '.py', '.tsx', '.ts', '.jsx', '.js',
    '.rs', '.c', '.cpp', '.go', '.java',
    '.kt', '.swift', '.rb', '.php', '.cs'
}

def check_file_length_limit(data):
    tool_name = data.get("tool_name")  # Edit oder Write

    # Berechne resultierende Zeilenzahl
    if tool_name == "Write":
        lines = count_lines(tool_input.get("content", ""))
    elif tool_name == "Edit":
        # Simuliere Edit und zähle Zeilen
        lines = calculate_edit_result_lines(...)

    if lines > MAX_FILE_LINES:
        # Speed Bump Pattern: Erstes Mal blockieren, zweites Mal erlauben
        if not flag_file.exists():
            flag_file.touch()
            return block_with_refactoring_suggestion()
        else:
            flag_file.unlink()
            return allow()
```


#### Example



**Code:**
```python
TRIGGERS = (">resume", ">continue", ">handoff")

def main():
    if prompt.startswith(">resume"):
        # Session ID in Clipboard kopieren
        copy_to_clipboard(session_id)

        # Prompt blockieren mit Anweisungen
        return {
            "decision": "block",
            "reason": (
                "Session ID copied to clipboard!\n\n"
                "To continue:\n"
                "1. Quit Claude (Ctrl+D twice)\n"
                "2. Run: aichat resume <paste>"
            )
        }
```


#### Example



**Code:**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Detailed reason..."
  }
}
```


#### Example



**Code:**
```json
{
  "decision": "block",
  "reason": "Message to show user..."
}
```


#### Example



**Code:**
```python
try:
    # Hook-Logik
except Exception as e:
    # Bei Fehler: IMMER approve um Claude nicht zu brechen!
    print(json.dumps({
        "decision": "approve",
        "error": str(e)
    }))
```


#### Example



**Code:**
```bash
# .claude/hooks/safety-hooks/
├── hooks.json
├── bash_hook.py        # Unified Bash Hook
├── rm_block_hook.py
├── env_protection.py
├── git_safety.py
└── file_length.py
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/safety-hooks-framework-pattern.md`</small>
