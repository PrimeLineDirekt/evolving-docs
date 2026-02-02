---
title: context-stats
type: command
tags: []
lang: en
confidence: 100
---

# context-stats


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

Context Window Usage mit visuellem Balken und Empfehlungen


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
# Finde neueste Context-File für aktuelle Session
ls -t /tmp/claude-context-pct-*.txt 2>/dev/null | head -1 | xargs cat 2>/dev/null || echo "0"
```


#### Example



**Code:**
```bash
filled = round(percentage * 30 / 100)
empty = 30 - filled
bar = "█" * filled + "░" * empty
```


#### Example



**Code:**
```bash
╔═══════════════════════════════════════════════════════╗
║            CONTEXT WINDOW USAGE                       ║
╠═══════════════════════════════════════════════════════╣
║ {bar}  {pct}%                                        ║
║                                                       ║
║ Tokens: ~{tokens}K / 200K                            ║
║ Status: {status_icon} {status_text}                  ║
╠═══════════════════════════════════════════════════════╣
║ {recommendations}                                     ║
╚═══════════════════════════════════════════════════════╝
```


#### Example



**Code:**
```bash
CAPACITY
  Good capacity for complex tasks
  Multi-step operations safe
```


#### Example



**Code:**
```bash
RECOMMENDATIONS
  Consider /clear or /whats-next soon
  Avoid starting new complex tasks
  Current work can continue
```


#### Example



**Code:**
```bash
ACTION REQUIRED
  Run /whats-next to create handoff
  Then /clear to reset context
  Resume with saved context
```


#### Example



**Code:**
```bash
╔═══════════════════════════════════════════════════════╗
║            CONTEXT WINDOW USAGE                       ║
╠═══════════════════════════════════════════════════════╣
║ ████████████░░░░░░░░░░░░░░░░░░░  38%                 ║
║                                                       ║
║ Tokens: ~76K / 200K                                  ║
║ Status: ✅ Healthy                                    ║
╠═══════════════════════════════════════════════════════╣
║ CAPACITY                                              ║
║   Good capacity for complex tasks                     ║
║   Multi-step operations safe                          ║
╚═══════════════════════════════════════════════════════╝
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/context-stats.md`</small>
