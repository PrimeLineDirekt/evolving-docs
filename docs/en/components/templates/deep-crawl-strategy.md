---
title: deep-crawl-strategy
type: template
tags: []
lang: en
confidence: 100
---

# deep-crawl-strategy


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
                    │   Start URL     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  can_process?   │
                    │  (URL Validation)│
                    └────────┬────────┘
                             │ ✓
                             ▼
                    ┌─────────────────┐
                    │   Crawl Page    │
                    │   (Get Result)  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Link Discovery  │
                    │ (Extract Links) │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
         ┌────────┐    ┌────────┐    ┌────────┐
         │ Link 1 │    │ Link 2 │    │ Link N │
         └────┬───┘    └────┬───┘    └────┬───┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Depth Check    │
                    │  < max_depth?   │
                    └────────┬────────┘
                             │ ✓
                             ▼
                      [Recurse/Queue]
```


#### Example



**Code:**
```bash
Level 0: [Start URL]
         ↓
Level 1: [Link A, Link B, Link C]
         ↓
Level 2: [A1, A2, B1, B2, C1, C2]
```


#### Example



**Code:**
```bash
Start → Link A → A1 → A1a → ...
              ↓
        (backtrack)
              ↓
        Link B → B1 → ...
```


#### Example



**Code:**
```bash
Queue = [(Start, score=100)]

while Queue:
    url = Queue.pop_highest_score()
    links = crawl(url)
    for link in links:
        score = calculate_relevance(link)
        Queue.add((link, score))
```


#### Example



**Code:**
```bash
Prüfungen:
├── URL Format valide?
├── Bereits besucht? (visited Set)
├── Depth < max_depth?
├── Domain erlaubt? (same-domain / allow-list)
├── Pattern-Match? (include/exclude regex)
└── Robots.txt erlaubt?
```


#### Example



**Code:**
```bash
Aus Crawl-Result extrahieren:
├── <a href="..."> Tags
├── Canonical Links
├── Pagination Links
├── Sitemap References
└── JavaScript-rendered Links (optional)

Filtering:
├── Relative → Absolute URLs
├── Fragment-Removal (#anchor)
├── Query-Parameter Normalisierung
└── Duplicate Detection
```


#### Example



**Code:**
```bash
Tracked State:
├── visited: Set[str]        # Bereits gecrawlte URLs
├── depths: Dict[str, int]   # URL → Crawl-Depth
├── parents: Dict[str, str]  # URL → Parent URL (für Trace)
└── scores: Dict[str, float] # URL → Relevanz Score (BFF)
```


#### Example



**Code:**
```bash
results = await strategy.arun_batch(start_url, crawler, config)
# Wartet bis alle Seiten gecrawlt
# Return: List[CrawlResult]
```


#### Example



**Code:**
```bash
async for result in strategy.arun_stream(start_url, crawler, config):
    process(result)
    # Ergebnisse kommen live während des Crawls
```


#### Example



**Code:**
```bash
deep_crawl_active = ContextVar("deep_crawl_active", default=False)

def arun():
    if not deep_crawl_active.get():
        token = deep_crawl_active.set(True)
        try:
            # Deep crawl logic
        finally:
            deep_crawl_active.reset(token)
    else:
        # Normal single-page crawl
```




## Configuration



## Best Practices




## Related


---

<small>Source: `knowledge/templates/deep-crawl-strategy.md`</small>
