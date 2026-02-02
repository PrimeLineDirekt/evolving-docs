---
title: crawl
type: command
tags: []
lang: en
confidence: 100
---

# crawl


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Command |
| **Purpose** | Unified interface for web crawling that intelligently routes between:
- **Firecrawl** (MCP tools): Fast, reliable, built-in features
- **Crawlee** (Python scraper): Fallback for limits/complex scenari |
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
```yaml
name: crawl
description: Unified web crawling interface (Firecrawl MCP + Crawlee fallback)
arguments:
  urls:
    type: array
    required: true
    description: URLs to crawl
  mode:
    type: string
    required: false
    default: auto
    values: [auto, firecrawl, crawlee]
    description: Routing mode
  playwright:
    type: boolean
    required: false
    default: false
    description: Use Playwright for JS rendering (Crawlee only)
  output:
    type: string
    required: false
    description: Output file path (default stdout for <100KB)
  depth:
    type: integer
    required: false
    default: 1
    description: Crawl depth for recursive crawling
  dry-run:
    type: boolean
    required: false
    default: false
    description: Show routing decision without executing
  screenshot:
    type: boolean
    required: false
    default: false
    description: Capture screenshots (Firecrawl only)
  proxy:
    type: string
    required: false
    values: [basic, stealth, auto]
    description: Proxy type (Firecrawl only)
```


#### Example



**Code:**
```bash
/crawl {urls}
    │
    ▼
Mode = auto?
    │
    ├─ YES → Dynamic Routing
    │          │
    │          ▼
    │      Check Conditions:
    │      ├─ URLs ≤ dynamic_threshold? → Firecrawl
    │      ├─ Firecrawl limits reached? → Crawlee
    │      ├─ Screenshot/PDF needed? → Firecrawl
    │      ├─ Depth > 1? → Crawlee
    │      └─ JS-heavy site? → Crawlee
    │
    └─ NO → Explicit mode (firecrawl|crawlee)
```


#### Example



**Code:**
```json
{
  "firecrawl_usage": {
    "daily_limit": 500,
    "current_count": 120,
    "dynamic_threshold": 10,
    "last_reset": "2026-02-02"
  }
}
```


#### Example



**Code:**
```bash
remaining = daily_limit - current_count
dynamic_threshold = max(5, min(50, remaining / 10))
```


#### Example



**Code:**
```bash
/crawl https://example.com
```


#### Example



**Code:**
```bash
/crawl https://site1.com https://site2.com https://site3.com
```


#### Example



**Code:**
```bash
/crawl https://example.com --mode=firecrawl
/crawl https://example.com --mode=crawlee
```


#### Example



**Code:**
```bash
/crawl https://example.com --screenshot
```


#### Example



**Code:**
```bash
/crawl https://spa-app.com --mode=crawlee --playwright
```


#### Example



**Code:**
```bash
/crawl https://example.com --depth=3
```


#### Example



**Code:**
```bash
/crawl https://example.com --dry-run
```


#### Example



**Code:**
```bash
[DRY RUN] Would use: Firecrawl
Reason: URLs (1) ≤ threshold (15), no limits
Estimated credits: 1
```


#### Example



**Code:**
```bash
/crawl https://example.com --output=results.md
```


#### Example



**Code:**
```bash
/crawl https://example.com --proxy=stealth
```


#### Example



**Code:**
```python
urls = args.urls  # Array of URLs
mode = args.mode or "auto"  # Default: auto
playwright = args.playwright or False
output = args.output or None
depth = args.depth or 1
dry_run = args.dry_run or False
screenshot = args.screenshot or False
proxy = args.proxy or None
```


#### Example



**Code:**
```python
# Read Memory
memory = Read("_memory/projects/evolving-system.json")
usage = memory["firecrawl_usage"]

# Calculate threshold
remaining = usage["daily_limit"] - usage["current_count"]
threshold = max(5, min(50, remaining // 10))

# Decision logic
if len(urls) <= threshold and usage["current_count"] < usage["daily_limit"]:
    if screenshot or proxy:
        tool = "firecrawl"  # Firecrawl-only features
    elif depth > 1:
        tool = "crawlee"  # Recursive better with Crawlee
    else:
        tool = "firecrawl"  # Default to fast option
else:
    tool = "crawlee"  # Over threshold or limits reached
```


#### Example



**Code:**
```python
if dry_run:
    print(f"[DRY RUN] Would use: {tool}")
    print(f"Reason: {decision_reason}")
    if tool == "firecrawl":
        print(f"Estimated credits: {len(urls)}")
    return
```


#### Example



**Code:**
```python
results = []
for url in urls:
    params = {
        "url": url,
        "formats": ["markdown"]
    }

    if screenshot:
        params["formats"].append("screenshot")

    if proxy:
        params["proxy"] = proxy

    result = mcp__firecrawl__firecrawl_scrape(**params)
    results.append(result)

# Update Memory
usage["current_count"] += len(urls)
Write("_memory/projects/evolving-system.json", updated_memory)
```


#### Example



**Code:**
```python
# Build command
cmd = f"python scripts/crawlers/crawlee_template.py {' '.join(urls)}"

if playwright:
    cmd += " --playwright"

if depth > 1:
    cmd += f" --depth={depth}"

# Execute
result = Bash(cmd)
results = parse_crawlee_output(result)
```


#### Example



**Code:**
```python
# Combine results
combined = "\n\n---\n\n".join(results)

# Check size
size = len(combined.encode('utf-8'))

if output or size > 100_000:  # >100KB
    file_path = output or f"crawl-{timestamp}.md"
    Write(file_path, combined)
    print(f"✓ Saved to {file_path} ({size/1024:.1f}KB)")
else:
    print(combined)
```


#### Example



**Code:**
```bash
/crawl https://blog.example.com/post-123
```


#### Example



**Code:**
```bash
[Auto] Using Firecrawl (1 URL, threshold: 15)
✓ Crawled https://blog.example.com/post-123
[Output shown in stdout]
```


#### Example



**Code:**
```bash
/crawl https://site.com/page1 https://site.com/page2 ... (20 URLs)
```


#### Example



**Code:**
```bash
[Auto] Using Crawlee (20 URLs > threshold: 15)
✓ Crawled 20 URLs
✓ Saved to crawl-2026-02-02-143022.md (245KB)
```


#### Example



**Code:**
```bash
/crawl https://example.com --screenshot
```


#### Example



**Code:**
```bash
[Auto] Using Firecrawl (screenshot requested)
✓ Captured screenshot
✓ Saved to example-com-screenshot.png
[Content shown in stdout]
```


#### Example



**Code:**
```bash
/crawl https://docs.example.com --depth=2
```


#### Example



**Code:**
```bash
[Auto] Using Crawlee (depth > 1)
✓ Crawling depth: 2
✓ Found 45 pages
✓ Saved to crawl-2026-02-02-143045.md (1.2MB)
```


#### Example



**Code:**
```bash
/crawl https://example.com --dry-run
```


#### Example



**Code:**
```bash
[DRY RUN] Would use: Firecrawl
Reason: 1 URL ≤ threshold (15), limits OK (120/500)
Estimated credits: 1
Current threshold: 15 (380 credits remaining)
```


#### Example



**Code:**
```bash
# Force Crawlee mode
/crawl {urls} --mode=crawlee

# Or wait for daily reset (check Memory)
```


#### Example



**Code:**
```bash
cd scripts/crawlers
pip install -r requirements.txt
```


#### Example



**Code:**
```bash
# Auto-saves to file for >100KB
/crawl {urls}

# Or explicit file
/crawl {urls} --output=my-results.md
```


#### Example



**Code:**
```bash
# Use Playwright with Crawlee
/crawl {url} --mode=crawlee --playwright
```


#### Example



**Code:**
```bash
# View current usage
cat _memory/projects/evolving-system.json | grep firecrawl_usage
```


#### Example



**Code:**
```json
{
  "firecrawl_usage": {
    "current_count": 125,  // +5 from last crawl
    "last_updated": "2026-02-02T14:30:22Z"
  }
}
```


#### Example



**Code:**
```python
if today != last_reset:
    usage["current_count"] = 0
    usage["last_reset"] = today
```


#### Example



**Code:**
```python
remaining = daily_limit - current_count
new_threshold = max(5, min(50, remaining // 10))
usage["dynamic_threshold"] = new_threshold
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/commands/crawl.md`</small>
