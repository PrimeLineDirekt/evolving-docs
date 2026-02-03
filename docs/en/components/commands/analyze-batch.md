---
title: /analyze-batch
type: command
tags: []
lang: en
confidence: 100
---

# /analyze-batch


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Batch analysis of pending Macro-Analyse documents with Claude Code Subscription. |
| **Complexity** | medium |
| **Model** | claude-sonnet-4-5 |
| **Category** | workflow |</div>


## What It Does

Processes pending documents in the Macro-Analyse Dashboard inbox using the WZRD Intelligence Framework:

1. **Loads pending documents** from inbox index (filter: has_deep_analysis == false)
2. **Analyzes each document** with WZRD prompt extracting:
   - MSM narrative vs reality check
   - Signal strength & narrative contradiction scores
   - Cui bono analysis (follow the money)
   - Bullish/bearish signals for assets
   - Auto-tags and hidden connections
3. **Updates documents** with intelligence data and flags as analyzed
4. **Reports progress** with summary statistics

Maximum 20 documents per batch for context efficiency.


## System Impact

- Enables automated intelligence analysis workflow for macro documents
- Integrates with Macro-Analyse Dashboard at `http://localhost:3000`
- Critical for high-signal article identification and narrative gap detection
- Populates intelligence layer for `/inbox/high-signal` and other filtered views


## Architecture

**Dependencies:**
- Macro-Analyse project structure at `/Users/neoforce/Buisiness/Projects/Macro-Analyse/`
- WZRD Intelligence Framework prompt template
- Inbox index: `data/inbox/index.json`
- Document storage: `data/inbox/{category}/{doc_id}.json`

**Data Flow:**
1. Read inbox index → filter pending documents
2. For each document: Read → Analyze with WZRD → Parse JSON → Update file + index
3. Aggregate statistics → Report summary

**Triggers:** Plain-text patterns like "analysiere alle dokumente", "analyze pending documents", "batch analyse"


## Usage

**Basic syntax:**
```bash
/analyze-batch              # Analyze up to 20 pending documents
/analyze-batch 5            # Analyze only 5 documents
/analyze-batch --high-prio  # Prioritize actionable=true documents
```

### Examples

#### Basic Usage

Analyze all pending documents (up to 20):

**Code:**
```bash
/analyze-batch
```

**Output:**
```
📊 Scanning inbox...
Found: 50 documents pending analysis

Analyzing batch of 20...

[1/20] "Fed signals rate pause in 2025"
       Signal: 78% | Gap: 65% | Tags: fed, rates, policy

[2/20] "Bitcoin ETF inflows reach $2B"
       Signal: 85% | Gap: 42% | Tags: btc, etf, institutional

...

✅ Batch complete!

Summary:
- Analyzed: 20 documents
- High Signal (>70%): 8
- High Gap (>50%): 5
- Remaining: 30 documents

Run /analyze-batch again for next batch.
```


## Configuration

| Option | Default | Description |
|--------|---------|-------------|
| `batch_size` | 20 | Maximum documents per batch |
| `--high-prio` | false | Prioritize actionable documents |
| `limit` | (none) | Explicit document count (e.g., `/analyze-batch 5`) |

**File Paths:**
- Index: `/Users/neoforce/Buisiness/Projects/Macro-Analyse/data/inbox/index.json`
- Documents: `/Users/neoforce/Buisiness/Projects/Macro-Analyse/data/inbox/{category}/{doc_id}.json`


## Best Practices

**Do:**
- Use batch processing for efficient context management (20 documents at a time)
- Check dashboard at `http://localhost:3000` after batch completion
- Use `/analyze-batch --high-prio` when time-sensitive analysis is needed
- Review high signal (>70%) and high gap (>50%) documents first

**Don't:**
- Process more than 20 documents in one batch (context overflow risk)
- Skip verification of WZRD analysis JSON format
- Forget to update dashboard after analysis completion




## Related


---

<small>Source: `.claude/commands/analyze-batch.md`</small>
