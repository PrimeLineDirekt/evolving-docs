---
title: template-diff-agent
type: agent
tags: []
lang: en
confidence: 100
---

# template-diff-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents || **Created** | 2026-01-04 |</div>


## What It Does

"Intelligent diff analysis between source and target repositories"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```json
{
  "source_path": "/path/to/Evolving",
  "target_path": "/path/to/Evolving-Template",
  "files_to_check": ["array of relative file paths"],
  "template_protected": ["array of protected files"],
  "manifest": "template-sync-manifest.json contents"
}
```


#### Example



**Code:**
```bash
# Check if file exists in both
[ -f "$SOURCE/$file" ] && [ -f "$TARGET/$file" ]
```


#### Example



**Code:**
```bash
# Get modification timestamps
SOURCE_MTIME=$(stat -f "%m" "$SOURCE/$file")
TARGET_MTIME=$(stat -f "%m" "$TARGET/$file")

# Compare
if [ $SOURCE_MTIME -gt $TARGET_MTIME ]; then
    echo "UPDATED"
fi
```


#### Example



**Code:**
```bash
# Check if files differ
diff -q "$SOURCE/$file" "$TARGET/$file"

# Get detailed diff
diff -u "$TARGET/$file" "$SOURCE/$file"
```


#### Example



**Code:**
```python
def is_diverged(source_mtime, target_mtime, last_sync):
    return source_mtime > last_sync and target_mtime > last_sync
```


#### Example



**Code:**
```markdown
# Template Diff Report

## Summary
| Category | Count | Files |
|----------|-------|-------|
| NEW | 12 | To be synced |
| UPDATED | 8 | To be updated |
| DIVERGED | 1 | Manual review |
| TEMPLATE-ONLY | 8 | Protected |
| IDENTICAL | 45 | No action |

## NEW Files (sync to template)
| File | Size | Type |
|------|------|------|
| `.claude/agents/new-agent.md` | 4.2KB | Agent |
| `.claude/commands/new-cmd.md` | 1.8KB | Command |
| `knowledge/patterns/new.md` | 2.1KB | Pattern |

## UPDATED Files (update in template)
| File | Source Date | Target Date | Lines Changed |
|------|-------------|-------------|---------------|
| `.claude/CONTEXT.md` | 2026-01-04 | 2026-01-02 | +47 -12 |
| `.claude/detection-index.json` | 2026-01-04 | 2026-01-01 | +156 -23 |

## DIVERGED Files (manual review required)
| File | Source Date | Target Date | Conflict Type |
|------|-------------|-------------|---------------|
| `.claude/agents/example.md` | 2026-01-04 | 2026-01-03 | Both modified |

### Diff Preview: .claude/agents/example.md
```


#### Example



**Code:**
```bash

## TEMPLATE-ONLY Files (protected, skip)
- README.md
- START-SMALL.md
- BEGINNER-GUIDE.md
- _ONBOARDING.md
- knowledge/personal/about-me.md
- knowledge/personal/system-instructions.md
- .claude/CLAUDE.md

## Recommendations
1. Sync 12 NEW files
2. Update 8 UPDATED files
3. Manually review 1 DIVERGED file
4. Skip 8 TEMPLATE-ONLY files
```


#### Example



**Code:**
```bash
# Compare file modification times
stat -f "%m %N" $FILE

# Quick diff check
diff -q $SOURCE/$FILE $TARGET/$FILE

# Detailed diff with context
diff -u $TARGET/$FILE $SOURCE/$FILE | head -50

# Count changed lines
diff $TARGET/$FILE $SOURCE/$FILE | grep -c "^[<>]"
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/template-diff-agent.md`</small>
