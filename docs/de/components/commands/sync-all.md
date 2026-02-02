---
title: sync-all
type: command
tags: []
lang: en
confidence: 100
---

# sync-all


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




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
# Via Claude
/sync-all

# Direkt im Terminal
.claude/scripts/full-sync.sh

# Erst prüfen was passieren würde
.claude/scripts/full-sync.sh --dry-run
```


#### Example



**Code:**
```bash
[SYNC] Phase 1: Scanning filesystem...
  Commands:    60
  Agents:      57
  Patterns:    53
  ...

[SYNC] Phase 2: Detecting orphan nodes...
[!] Found 5 orphan nodes (file deleted)
[✓] Removed 5 orphan nodes

[SYNC] Phase 3: Adding missing nodes...
[!] Adding: pattern-new-pattern
[!] Adding: learning-new-learning
[✓] Added 12 nodes

[SYNC] Phase 4: Regenerating indexes...
[✓] Indexes regenerated

[SYNC] Phase 5: Updating Master Documents...
[✓] README.md updated
[✓] COMMANDS.md updated
[✓] SYSTEM-MAP.md updated

[SYNC] ════════════════════════════════════════════════════════════
[✓] FULL SYNC COMPLETE
[SYNC] ════════════════════════════════════════════════════════════

  Filesystem:
    Commands:    60
    Agents:      57
    ...

  Graph:
    Nodes:       433
    Edges:       317
    Routes:      41

  Changes:
    Added:       12 nodes
    Removed:     5 orphans
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/sync-all.md`</small>
