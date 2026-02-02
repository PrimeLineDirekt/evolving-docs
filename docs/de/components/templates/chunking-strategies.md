---
title: chunking-strategies
type: template
tags: []
lang: en
confidence: 100
---

# chunking-strategies


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Template |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | templates |</div>


## What It Does




## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
                    ┌─────────────────┐
                    │   Input Text    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Select Strategy │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
   ┌──────────┐       ┌──────────┐       ┌──────────┐
   │  Fixed   │       │ Semantic │       │ Sliding  │
   │  Length  │       │  (NLP)   │       │ Window   │
   └────┬─────┘       └────┬─────┘       └────┬─────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                    ┌─────────────────┐
                    │   Chunk List    │
                    │   [c1, c2, ...]│
                    └─────────────────┘
```


#### Example



**Code:**
```bash
f(text) = [text]
```


#### Example



**Code:**
```bash
Patterns: ["\n\n", "---", "##"]

Input: "Para 1\n\nPara 2\n\nPara 3"
Output: ["Para 1", "Para 2", "Para 3"]
```


#### Example



**Code:**
```bash
Input: "First sentence. Second one! Third?"
Output: ["First sentence.", "Second one!", "Third?"]
```


#### Example



**Code:**
```bash
Input: Long document about multiple topics
Output: [
  "Topic 1 content...",
  "Topic 2 content...",
  "Topic 3 content..."
]
```


#### Example



**Code:**
```bash
[
  ("Topic content...", ["keyword1", "keyword2", "keyword3"]),
  ...
]
```


#### Example



**Code:**
```bash
chunk_size = 100 words

Input: 350 words
Output: [chunk_100, chunk_100, chunk_100, chunk_50]
```


#### Example



**Code:**
```bash
window_size = 100, step = 50

Text: [w1...w100...w150...w200]
Chunk 1: [w1-w100]
Chunk 2: [w51-w150]  ← 50% overlap
Chunk 3: [w101-w200]
```


#### Example



**Code:**
```bash
window_size = 1000, overlap = 100

Chunk N ends at position X
Chunk N+1 starts at position X - 100
```


#### Example



**Code:**
```bash
Durchschnittlich: 1 Wort ≈ 0.75 Tokens (Englisch)
                  1 Wort ≈ 1.0-1.5 Tokens (Deutsch)

Konservativ: 1 Wort ≈ 1.3 Tokens
```


#### Example



**Code:**
```bash
                    ┌──────────────────┐
                    │ Chunk Results    │
                    │ [r1, r2, r3]     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Deduplication    │
                    │ (Overlap-Bereich)│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Merge Strategy   │
                    │ (Concat/Union)   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Final Result     │
                    └──────────────────┘
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/templates/chunking-strategies.md`</small>
