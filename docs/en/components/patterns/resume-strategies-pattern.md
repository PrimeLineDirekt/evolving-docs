---
title: resume-strategies-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# resume-strategies-pattern


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

**Capabilities Provided:**
- Structured approach to component creation
- Automated validation and best practices
- Standardized output format
- Integration with system architecture

**When to Use:**
- Creating new system components
- Standardizing component structure
- Ensuring consistency across codebase
- Automating repetitive creation tasks



## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
Context Full
    │
    ├── TRIM (Threshold-based)
    │   └── Tool-Results > N chars → Placeholder
    │
    ├── SMART-TRIM (LLM-powered)
    │   └── LLM identifiziert was entfernt werden kann
    │
    └── ROLLOVER (Fresh Start)
        └── Neue Session mit Lineage-Pointer
```


#### Example



**Code:**
```python
def trim_and_create_session(
    agent,           # "claude" oder "codex"
    input_file,      # Original Session JSONL
    target_tools,    # ["Read", "Bash"] - welche Tools trimmen
    threshold,       # 500-2000 chars - ab wann trimmen
    output_dir=None,
    trim_assistant_messages=None,  # Optional: auch Assistant trimmen
    min_token_savings=300          # Minimum Ersparnis
):
    """
    Returns: (session_id, output_file, num_tools_trimmed, chars_saved, tokens_saved)
    """
```


#### Example



**Code:**
```python
# Für Tool-Results:
f"[Results from {tool_name} tool suppressed - original content was {length} characters]"

# Für Assistant Messages (wenn aktiviert):
f"[Claude response trimmed - original was {length} characters]"
```


#### Example



**Code:**
```json
{
  "trim_metadata": {
    "parent_file": "/path/to/original/session.jsonl",
    "trimmed_at": "2025-12-27T14:30:00Z",
    "trim_params": {
      "target_tools": ["Read", "Bash"],
      "threshold": 1000,
      "trim_assistant_messages": false
    },
    "stats": {
      "original_tokens": 45000,
      "trimmed_tokens": 28000,
      "tools_trimmed": 15,
      "chars_saved": 85000
    }
  }
}
```


#### Example



**Code:**
```python
def identify_trimmable_lines_cli(input_file):
    """
    Nutzt CLI-Agent um trimmbare Zeilen zu identifizieren.

    Returns: List[(line_idx, rationale, description)]

    Beispiel Output:
    [
        (42, "Tool result no longer referenced", "Read tool output for config.json"),
        (156, "Exploratory code attempt abandoned", "Failed API call exploration"),
        (203, "Replaced by later implementation", "Old version of parse function")
    ]
    """

def trim_lines(input_file, line_indices, output_file, parent_file=None, descriptions=None):
    """
    WICHTIG: Löscht KEINE Zeilen - ersetzt nur CONTENT fields!

    Das erhält:
    - Session-Struktur
    - Turn-Reihenfolge
    - Conversation Flow
    """
```


#### Example



**Code:**
```python
def rollover_session(input_file, summary=None):
    """
    Erstellt neue Session mit:
    1. continue_metadata (Pointer auf Parent)
    2. Optionale Zusammenfassung als erstes System-Message
    3. Lineage-Chain für Kontext
    """
```


#### Example



**Code:**
```json
{
  "continue_metadata": {
    "parent_file": "/path/to/original.jsonl",
    "continued_at": "2025-12-27T15:00:00Z",
    "continuation_type": "rollover",
    "summary_included": true
  }
}
```


#### Example



**Code:**
```python
@dataclass
class SessionNode:
    session_file: Path
    derivation_type: Optional[str]  # "trimmed", "continued", None
    exported_file: Optional[Path]   # Falls exportiert
    parent: Optional['SessionNode'] = None
```


#### Example



**Code:**
```python
def get_parent_info(session_file: Path) -> Tuple[Optional[Path], Optional[str], Optional[Path]]:
    """
    Extrahiert aus erster Zeile:
    - Parent file path
    - Derivation type ("trimmed" oder "continued")
    - Exported file (falls vorhanden)
    """

def get_continuation_lineage(session_file: Path) -> List[SessionNode]:
    """
    Traversiert Parent-Chain rückwärts.
    Gibt chronologische Liste zurück (älteste zuerst).
    """

def get_full_lineage_chain(session_file: Path) -> List[Tuple[Path, str]]:
    """
    Komplette Kette inklusive aller Trims und Continues.
    """
```


#### Example



**Code:**
```python
def inject_lineage_into_first_user_message(output_file, input_file, agent, derivation_type):
    """
    Fügt [SESSION LINEAGE] Block zur ersten User-Message hinzu.

    Format:
    [SESSION LINEAGE]
    This session continues from previous work:
    1. session-abc123.jsonl (continued)
    2. session-def456.jsonl (trimmed)
    3. session-ghi789.jsonl (current)

    Context from parent sessions may be relevant.
    [/SESSION LINEAGE]
    """
```


#### Example



**Code:**
```python
# Trigger: ">resume", ">continue", ">handoff"

def main():
    # 1. Prompt auf Trigger prüfen
    if prompt.startswith(">resume"):
        # 2. Session ID in Clipboard kopieren
        copy_to_clipboard(session_id)
        # 3. Prompt blocken mit Anweisungen
        return {
            "decision": "block",
            "reason": "Session ID copied! Run: aichat resume <paste>"
        }
```


#### Example



**Code:**
```json
{"sessionId": "abc123", "type": "user", "message": {"role": "user", "content": "..."}}
{"sessionId": "abc123", "type": "assistant", "message": {"role": "assistant", "content": "..."}}
{"sessionId": "abc123", "type": "tool_result", "message": {"tool_name": "Read", "content": "..."}}
```


#### Example



**Code:**
```bash
# Threshold-based Trim
aichat trim <session-id> --threshold 1000 --tools Read,Bash

# Smart Trim (LLM-powered)
aichat smart-trim <session-id>

# Rollover (Fresh Start)
aichat rollover <session-id> --with-summary

# Lineage anzeigen
aichat lineage <session-id>

# Session suchen
aichat search "keyword"
```


#### Example



**Code:**
```bash
Context > 80% Full?
    │
    ├── Viele große Tool-Results?
    │   └── TRIM mit threshold=1000
    │
    ├── Gemischter Content?
    │   └── SMART-TRIM (LLM entscheidet)
    │
    └── Kompletter Neustart nötig?
        └── ROLLOVER mit Summary
```


#### Example



**Code:**
```bash
# .claude/hooks/resume-hook.sh
# Bei ">resume" Trigger:
# 1. Session ID speichern
# 2. Ledger aktualisieren
# 3. Handoff erstellen
```




## Configuration

**Trade-offs:**

| Strategy | Token-Reduktion | Kontext-Erhalt | Geschwindigkeit | Kosten |
|----------|-----------------|----------------|-----------------|--------|
| TRIM | 40-60% | Mittel | Schnell | Keine |
| SMART-TRIM | 30-50% | Hoch | Langsam | LLM-Kosten |
| ROLLOVER | 90%+ | Niedrig | Schnell | Optional LLM |

---

**Configuration Options:**

| Option | Default | Description |
|--------|---------|-------------|
| max_iterations | 10 | Maximum agent iterations |
| min_confidence | 0.7 | Minimum confidence threshold |
| timeout_seconds | 300 | Maximum execution time |



## Best Practices

**Do:**
- Use for multi-expert coordination requiring diverse perspectives
- Apply when problem benefits from iterative refinement
- Combine with proper state management and validation
- Monitor blackboard size to prevent context overflow

**Don't:**
- Use for simple single-agent tasks
- Apply to strictly sequential workflows
- Ignore controller bottleneck risks
- Forget to handle write conflicts in concurrent scenarios




## Related


---

<small>Source: `knowledge/patterns/resume-strategies-pattern.md`</small>
