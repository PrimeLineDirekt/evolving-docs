---
title: browser-automation-pattern
type: pattern
tags: []
lang: en
confidence: 100
---

# browser-automation-pattern


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




## Architecture




## Usage


### Examples

#### Example



**Code:**
```bash
┌─────────────────────────────────────────────────┐
│                  ORCHESTRATOR                    │
│  (Claude Code Main Thread)                       │
└─────────────────┬───────────────────────────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
    ▼             ▼             ▼
┌───────┐   ┌───────┐   ┌───────┐
│ Tab 1 │   │ Tab 2 │   │ Tab N │
│ URL A │   │ URL B │   │ URL N │
└───┬───┘   └───┬───┘   └───┬───┘
    │           │           │
    ▼           ▼           ▼
┌───────────────────────────────┐
│     PARALLEL EXTRACTION       │
│  (JavaScript / get_page_text) │
└───────────────────────────────┘
                │
                ▼
        ┌───────────────┐
        │   AGGREGATOR   │
        │ (Results merge)│
        └───────────────┘
```


#### Example



**Code:**
```bash
# N Tabs parallel erstellen
tabs_create_mcp × N  (in einem Tool-Call Block)
```


#### Example



**Code:**
```bash
# Alle URLs gleichzeitig laden
navigate(url_1, tab_1)
navigate(url_2, tab_2)
...
navigate(url_N, tab_N)
```


#### Example



**Code:**
```bash
wait(1-2 seconds)
```


#### Example



**Code:**
```bash
# Option A: Text extrahieren
get_page_text(tab_1)
get_page_text(tab_2)
...

# Option B: Strukturierte Daten (EMPFOHLEN)
javascript_tool(extraction_script, tab_1)
javascript_tool(extraction_script, tab_2)
...
```


#### Example



**Code:**
```javascript
Array.from(document.querySelectorAll('a[href]'))
  .map(a => ({ text: a.textContent.trim(), url: a.href }))
  .filter(l => l.text && l.url)
```


#### Example



**Code:**
```javascript
Array.from(document.querySelectorAll('table'))
  .map(table => ({
    headers: Array.from(table.querySelectorAll('th')).map(th => th.textContent.trim()),
    rows: Array.from(table.querySelectorAll('tr')).slice(1).map(row =>
      Array.from(row.cells).map(cell => cell.textContent.trim())
    )
  }))
```


#### Example



**Code:**
```javascript
Array.from(document.querySelectorAll('[data-product], .product, .listing'))
  .map(el => ({
    title: el.querySelector('h1,h2,h3,.title')?.textContent?.trim(),
    price: el.querySelector('.price,[data-price]')?.textContent?.trim(),
    image: el.querySelector('img')?.src
  }))
```


#### Example



**Code:**
```javascript
({
  title: document.title,
  description: document.querySelector('meta[name="description"]')?.content,
  canonical: document.querySelector('link[rel="canonical"]')?.href,
  ogImage: document.querySelector('meta[property="og:image"]')?.content
})
```


#### Example



**Code:**
```bash
Problem erkannt
     │
     ▼
tabs_create_mcp (neuer Tab)
     │
     ▼
navigate(same_url, new_tab)
     │
     ▼
Alte Tab-ID ignorieren
```


#### Example



**Code:**
```bash
Operation blockiert
     │
     ▼
User: Dismiss Dialog manuell
     │
     ▼
Claude: "continue"
```


#### Example



**Code:**
```bash
Timeout/Error erkannt
     │
     ▼
wait(2)
     │
     ▼
navigate(url) (Retry)
```


#### Example



**Code:**
```python
# 1. Shop-Seite laden
navigate("https://etsy.com/shop/Example", tab_1)

# 2. Listing-URLs extrahieren
urls = javascript_tool("""
  Array.from(document.querySelectorAll('a[href*="/listing/"]'))
    .slice(0, 10)
    .map(a => a.href.split('?')[0])
""", tab_1)

# 3. Zusätzliche Tabs erstellen
tabs_create_mcp × 3

# 4. Parallel laden (4 Tabs, 10 URLs in Batches)
# Batch 1
navigate(urls[0], tab_1)
navigate(urls[1], tab_2)
navigate(urls[2], tab_3)
navigate(urls[3], tab_4)

# 5. Parallel extrahieren
javascript_tool(listing_details_script, tab_1)
javascript_tool(listing_details_script, tab_2)
javascript_tool(listing_details_script, tab_3)
javascript_tool(listing_details_script, tab_4)

# 6. Wiederholen für Batch 2, 3...
```


#### Example



**Code:**
```javascript
// Tab 1: Nachricht senden
const msg = { from: 'tab1', action: 'scrape_complete', data: { count: 5 } };
localStorage.setItem('cross_tab_msg', JSON.stringify(msg));

// Tab 2: Nachricht empfangen
const received = JSON.parse(localStorage.getItem('cross_tab_msg'));
```


#### Example



**Code:**
```javascript
// NICHT: alert('Debug info');  // ❌ Tab blockiert!

// STATTDESSEN:
console.log('[DEBUG] Extraction done:', result);
console.error('[ERROR] Failed:', error);

// Dann auslesen mit:
read_console_messages(tabId, pattern='DEBUG')
```


#### Example



**Code:**
```javascript
// Text/Email/Tel
form_input(ref_1, "Claude Test User")

// Radio Button (Value des gewünschten)
form_input(ref_5, "medium")

// Checkbox (Boolean)
form_input(ref_7, true)

// Time Input (Format HH:MM)
form_input(ref_11, "18:30")

// Textarea
form_input(ref_12, "Long text...")
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/patterns/browser-automation-pattern.md`</small>
