---
title: create-hook
type: command
tags: []
lang: en
confidence: 100
---

# create-hook


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | commands |</div>


## What It Does

Erstellt neuen Hook aus Template


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
post-tool-use: .claude/templates/hooks/post-tool-use.sh
stop: .claude/templates/hooks/stop-hook.sh
custom: .claude/templates/hooks/post-tool-use.sh (als Basis)
```


#### Example



**Code:**
```bash
Pfade:
  - "ideas/" → Alle Dateien in ideas/
  - "*.md" → Alle Markdown-Dateien
  - "knowledge/.*\.md" → Regex pattern
  - "projects/.*/README.md" → Spezifisches Pattern
```


#### Example



**Code:**
```bash
Write Event:
  - Markdown validieren
  - Cross-References updaten
  - Index aktualisieren
  - Backup erstellen

Edit Event:
  - Änderungen loggen
  - Related files updaten
  - Validation triggern
```


#### Example



**Code:**
```bash
- knowledge/sessions/ → In Knowledge Base
- .sessions/ → Hidden directory
- logs/sessions/ → In logs
```


#### Example



**Code:**
```bash
# CONFIGURATION
MONITORED_TOOLS=("Write" "Edit")  # Anpassen
MONITORED_PATHS=(
  "ideas/"
  "knowledge/"
)  # Anpassen
LOG_FILE=".claude/hooks/logs/{hook-name}.log"  # Anpassen
DEBUG=0  # 0 oder 1
```


#### Example



**Code:**
```bash
process_write() {
  local file_path="$1"

  debug_log "Processing Write event for: $file_path"

  # Validate markdown
  if [[ "$file_path" =~ \.md$ ]]; then
    # Check frontmatter exists
    if ! grep -q "^---$" "$file_path"; then
      info_log "Missing frontmatter in $file_path"
    fi

    # Check for broken links (basic)
    if grep -q "\[.*\](.*404.*)" "$file_path"; then
      info_log "Potential broken link in $file_path"
    fi
  fi

  info_log "Write processed: $file_path"
}
```


#### Example



**Code:**
```bash
process_write() {
  local file_path="$1"

  debug_log "Processing Write event for: $file_path"

  # Update index if idea file
  if [[ "$file_path" =~ ideas/.*\.md$ ]]; then
    # Extract idea-id from filename
    local idea_id=$(basename "$file_path" .md)

    # Trigger index update (example - anpassen!)
    # python3 .claude/scripts/update_index.py "$idea_id"

    info_log "Index updated for: $idea_id"
  fi

  info_log "Write processed: $file_path"
}
```


#### Example



**Code:**
```bash
chmod +x .claude/hooks/{name}.sh
```


#### Example



**Code:**
```json
{
  "hooks": {
    "post_tool_use": [
      {
        "name": "{hook-name}",
        "script": ".claude/hooks/{hook-name}.sh",
        "enabled": true
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
    "stop": [
      {
        "name": "{hook-name}",
        "script": ".claude/hooks/{hook-name}.sh",
        "enabled": true
      }
    ]
  }
}
```


#### Example



**Code:**
```bash
✓ Hook erfolgreich erstellt!

Datei: .claude/hooks/{name}.sh
Typ: {post-tool-use|stop} Hook
Triggers: {TRIGGER_BESCHREIBUNG}
Monitored Paths: {LIST_OF_PATHS}

{Falls settings.json updated}
✓ Hook konfiguriert in .claude/settings.json

Nächste Schritte:
→ Hook ist bereits executable (chmod +x applied)
→ Teste: {TESTING_INSTRUCTION}
→ Check Logs: .claude/hooks/logs/{name}.log
→ Passe Logic an falls nötig

{Falls NICHT in settings.json}
Optional: Füge Hook zu .claude/settings.json hinzu für automatische Aktivierung

Debugging:
→ Enable DEBUG=1 in Hook-Datei für verbose logging
→ Monitor logs: tail -f .claude/hooks/logs/{name}.log
```


#### Example



**Code:**
```bash
✓ Hook erfolgreich erstellt!

Datei: .claude/hooks/markdown-validator.sh
Typ: post-tool-use Hook
Triggers: Write, Edit
Monitored Paths: ideas/, knowledge/

✓ Hook konfiguriert in .claude/settings.json

Nächste Schritte:
→ Hook ist bereits executable (chmod +x applied)
→ Teste: Bearbeite eine .md Datei in ideas/ oder knowledge/
→ Check Logs: .claude/hooks/logs/markdown-validator.log
→ Passe Validation-Logic an falls nötig

Debugging:
→ Enable DEBUG=1 in Hook-Datei für verbose logging
→ Monitor logs: tail -f .claude/hooks/logs/markdown-validator.log
```


#### Example



**Code:**
```bash
1. Read template file
2. Replace all placeholders
3. Validate bash syntax (basic)
4. Write hook file
5. Bash: chmod +x
6. (Optional) Read settings.json
7. (Optional) Edit settings.json
8. Confirm to user
```


#### Example



**Code:**
```bash
IF template_not_found:
  Liste verfügbare Hook-Templates
  Frage User welcher Template
  Retry
```


#### Example



**Code:**
```bash
IF syntax_error_detected:
  Zeige problematische Zeile
  Erkläre Fehler
  Biete Fix an oder frage User
  Retry
```


#### Example



**Code:**
```bash
IF chmod_fails:
  Warne User
  Gib manuelle Anleitung:
    "Führe aus: chmod +x .claude/hooks/{name}.sh"
  Hook wurde erstellt aber nicht executable
```


#### Example



**Code:**
```bash
IF settings_update_fails:
  Hook wurde trotzdem erstellt
  Gib manuelle Anleitung für settings.json
  Zeige JSON-Snippet zum Copy-Paste
```


#### Example



**Code:**
```json
{
  "type": "prompt",
  "prompt": "Evaluate if this tool use is appropriate: $TOOL_INPUT",
  "timeout": 30
}
```


#### Example



**Code:**
```json
{
  "type": "command",
  "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh",
  "timeout": 60
}
```


#### Example



**Code:**
```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.txt",
  "cwd": "/current/working/dir",
  "permission_mode": "ask|allow",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {"file_path": "/path/to/file"}
}
```


#### Example



**Code:**
```json
{
  "hookSpecificOutput": {
    "permissionDecision": "allow|deny|ask",
    "updatedInput": {"field": "modified_value"}
  },
  "systemMessage": "Explanation for Claude"
}
```


#### Example



**Code:**
```json
{
  "decision": "approve|block",
  "reason": "Explanation",
  "systemMessage": "Additional context"
}
```


#### Example



**Code:**
```json
{
  "continue": true,
  "suppressOutput": false,
  "systemMessage": "Message for Claude"
}
```


#### Example



**Code:**
```bash
bash ${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh
```


#### Example



**Code:**
```bash
#!/bin/bash
set -euo pipefail

input=$(cat)
tool_name=$(echo "$input" | jq -r '.tool_name')

# Validate tool name format
if [[ ! "$tool_name" =~ ^[a-zA-Z0-9_]+$ ]]; then
  echo '{"decision": "deny", "reason": "Invalid tool name"}' >&2
  exit 2
fi
```


#### Example



**Code:**
```bash
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

# Deny path traversal
if [[ "$file_path" == *".."* ]]; then
  echo '{"decision": "deny", "reason": "Path traversal detected"}' >&2
  exit 2
fi

# Deny sensitive files
if [[ "$file_path" == *".env"* ]]; then
  echo '{"decision": "deny", "reason": "Sensitive file"}' >&2
  exit 2
fi
```


#### Example



**Code:**
```bash
# GOOD: Quoted
echo "$file_path"
cd "$CLAUDE_PROJECT_DIR"

# BAD: Unquoted (injection risk)
echo $file_path
cd $CLAUDE_PROJECT_DIR
```


#### Example



**Code:**
```json
{
  "type": "command",
  "command": "bash script.sh",
  "timeout": 10
}
```


#### Example



**Code:**
```bash
should_process_path() {
  local path="$1"
  # Use explicit pattern matching, not wildcards
  for pattern in "${MONITORED_PATHS[@]}"; do
    [[ "$path" =~ $pattern ]] && return 0
  done
  return 1
}
```


#### Example



**Code:**
```json
"matcher": "Write"
```


#### Example



**Code:**
```json
"matcher": "Read|Write|Edit"
```


#### Example



**Code:**
```json
"matcher": "*"
```


#### Example



**Code:**
```json
"matcher": "mcp__.*__delete.*"  // All MCP delete tools
```


#### Example



**Code:**
```json
// All MCP tools
"matcher": "mcp__.*"

// Specific plugin's MCP tools
"matcher": "mcp__plugin_asana_.*"

// All file operations
"matcher": "Read|Write|Edit"

// Bash commands only
"matcher": "Bash"
```


#### Example



**Code:**
```json
{
  "PreToolUse": [
    {
      "matcher": "Write",
      "hooks": [
        {"type": "command", "command": "check1.sh"},  // Parallel
        {"type": "command", "command": "check2.sh"},  // Parallel
        {"type": "prompt", "prompt": "Validate..."}   // Parallel
      ]
    }
  ]
}
```


#### Example



**Code:**
```bash
claude --debug
```


#### Example



**Code:**
```bash
echo '{"tool_name": "Write", "tool_input": {"file_path": "/test"}}' | \
  bash .claude/hooks/your-hook.sh

echo "Exit code: $?"
```


#### Example



**Code:**
```bash
output=$(./your-hook.sh < test-input.json)
echo "$output" | jq .
```


#### Example



**Code:**
```bash
User: /create-hook markdown-validator

Typ: post-tool-use
Name: markdown-validator
Tools: Write, Edit
Pfade: ideas/, knowledge/
Logic: Validate frontmatter, check broken links

→ Erstellt: .claude/hooks/markdown-validator.sh
→ Executable: chmod +x applied
→ Config: Added to settings.json
```


#### Example



**Code:**
```bash
User: /create-hook session-summary

Typ: stop
Name: session-summary
Output: knowledge/sessions/
Format: markdown
Track: Timestamp, Tools, Files, Topics

→ Erstellt: .claude/hooks/session-summary.sh
→ Executable: chmod +x applied
→ Summaries: knowledge/sessions/session-YYYYMMDD-HHMMSS.md
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/create-hook.md`</small>
