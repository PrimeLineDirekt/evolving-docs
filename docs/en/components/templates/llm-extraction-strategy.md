---
title: llm-extraction-strategy
type: template
tags: []
lang: en
confidence: 100
---

# llm-extraction-strategy


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
                    │   HTML/Markdown │
                    │   Content       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Chunking      │
                    │   (if needed)   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
         ┌────────┐    ┌────────┐    ┌────────┐
         │Chunk 1 │    │Chunk 2 │    │Chunk N │
         └────┬───┘    └────┬───┘    └────┬───┘
              │              │              │
              ▼              ▼              ▼
         ┌────────────────────────────────────┐
         │          LLM Processing            │
         │  (parallel with rate limiting)     │
         └────────────────┬───────────────────┘
                          │
                          ▼
                    ┌─────────────────┐
                    │  Structured     │
                    │  JSON Output    │
                    └─────────────────┘
```


#### Example



**Code:**
```bash
Input: HTML einer Seite
Output: [
  {
    "index": 0,
    "tags": ["introduction"],
    "content": ["First paragraph..."]
  },
  {
    "index": 1,
    "tags": ["pricing"],
    "content": ["Our plans start at..."]
  }
]
```


#### Example



**Code:**
```bash
Schema (Pydantic-style):
{
  "title": "string",
  "price": "number",
  "features": ["string"]
}

Input: Product page HTML
Output: {
  "title": "Pro Plan",
  "price": 29.99,
  "features": ["Unlimited users", "24/7 support"]
}
```


#### Example



**Code:**
```bash
Instruction: "Extract all pricing information
              including tiers, features, and limitations"

Output: Freiform JSON basierend auf Content
```


#### Example



**Code:**
```bash
1. Content → Token Estimation
2. Wenn > threshold:
   └── Split in Chunks (mit overlap)
3. Pro Chunk:
   └── LLM Extraction
4. Merge Results
```


#### Example



**Code:**
```bash
Given the HTML content:
1. Identify logical content blocks
2. For each block:
   - Assign semantic tags
   - Extract text content EXACTLY
   - Maintain original order
3. Output as JSON array
```


#### Example



**Code:**
```bash
Given the content and schema:
1. Parse the content for matching data
2. Extract values matching schema types
3. Validate against schema constraints
4. Return structured JSON
```


#### Example



**Code:**
```bash
try:
    blocks = parse_json(response)
except:
    parsed, unparsed = split_and_parse_json_objects(response)
    if unparsed:
        blocks.append({
            "error": True,
            "content": unparsed
        })
```


#### Example



**Code:**
```bash
Track per extraction:
├── prompt_tokens
├── completion_tokens
├── total_tokens
└── per-request breakdown

Aggregiert:
├── total_usage (Session)
└── usage_history (pro Request)
```


#### Example



**Code:**
```bash
Chunks 1-N → Parallel LLM Calls → Merge Results

Benefits:
- Faster für große Seiten
- Nutzt async HTTP optimal
- Rate-limiting beachten
```


#### Example



**Code:**
```bash
Chunk 1 → wait → Chunk 2 → wait → ...

Wann: Groq und andere rate-limited Providers
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/templates/llm-extraction-strategy.md`</small>
