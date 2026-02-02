---
title: schema-extraction-strategy
type: template
tags: []
lang: en
confidence: 100
---

# schema-extraction-strategy


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
                    │  JSON Schema    │
                    │  (CSS/XPath)    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   HTML Parser   │
                    │ (lxml/BS4)      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Base Selector   │
                    │ (Repeat Items)  │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
         ┌────────┐    ┌────────┐    ┌────────┐
         │ Item 1 │    │ Item 2 │    │ Item N │
         └────┬───┘    └────┬───┘    └────┬───┘
              │              │              │
              ▼              ▼              ▼
         ┌─────────────────────────────────────┐
         │       Field Extraction              │
         │  (per schema definition)            │
         └─────────────────────────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  JSON Output    │
                    │  [{...}, {...}] │
                    └─────────────────┘
```


#### Example



**Code:**
```json
{
  "name": "Schema Name",
  "baseSelector": "CSS/XPath für wiederholende Elemente",
  "baseFields": [
    // Felder vom Base-Element selbst
  ],
  "fields": [
    // Felder von Child-Elementen
  ]
}
```


#### Example



**Code:**
```json
{
  "name": "title",
  "selector": ".product-title",
  "type": "text"
}
```


#### Example



**Code:**
```json
{
  "name": "image_url",
  "selector": "img.product-image",
  "type": "attribute",
  "attribute": "src"
}
```


#### Example



**Code:**
```json
{
  "name": "price_value",
  "selector": ".price-text",
  "type": "regex",
  "pattern": "\\$([\\d,]+)"
}
```


#### Example



**Code:**
```json
{
  "name": "author",
  "type": "nested",
  "selector": ".author-info",
  "fields": [
    {"name": "name", "selector": ".author-name", "type": "text"},
    {"name": "avatar", "selector": "img", "type": "attribute", "attribute": "src"}
  ]
}
```


#### Example



**Code:**
```json
{
  "name": "comments",
  "type": "list",
  "selector": ".comment",
  "fields": [
    {"name": "user", "selector": ".user-name", "type": "text"},
    {"name": "content", "selector": ".comment-text", "type": "text"}
  ]
}
```


#### Example



**Code:**
```json
{
  "name": "location",
  "selector": ".location",
  "type": "text",
  "transform": "strip"
}
```


#### Example



**Code:**
```json
{
  "baseSelector": ".product-card",
  "fields": [
    {"name": "title", "selector": "h2.title", "type": "text"}
  ]
}
```


#### Example



**Code:**
```json
{
  "baseSelector": "//div[@class='product-card']",
  "fields": [
    {"name": "title", "selector": ".//h2[contains(@class,'title')]", "type": "text"}
  ]
}
```


#### Example



**Code:**
```html
<div class="product" data-id="123" data-category="electronics">
  <h2>Product Name</h2>
</div>
```


#### Example



**Code:**
```json
{
  "baseSelector": ".product",
  "baseFields": [
    {"name": "product_id", "type": "attribute", "attribute": "data-id"},
    {"name": "category", "type": "attribute", "attribute": "data-category"}
  ],
  "fields": [
    {"name": "name", "selector": "h2", "type": "text"}
  ]
}
```


#### Example



**Code:**
```json
{
  "name": "full_name",
  "type": "computed",
  "expression": "f'{first_name} {last_name}'"
}
```


#### Example



**Code:**
```json
{
  "name": "price_cents",
  "type": "computed",
  "function": "lambda item: int(float(item['price'].replace('$','')) * 100)"
}
```


#### Example



**Code:**
```bash
Input:
1. HTML Sample
2. Optional: Target JSON Example
3. Optional: Query/Description

Output:
Generated JSON Schema für Extraction
```


#### Example



**Code:**
```bash
SCHLECHT:
.xK7sF_container  ← Dynamisch generiert

GUT:
[data-testid='product-container']  ← Stabil
.product-card  ← Semantisch
```


#### Example



**Code:**
```json
// Statt dynamischer Klasse:
"selector": "div[class*='PlaceCard_descriptionContainer']"

// Oder Data-Attribute:
"selector": "[data-testid='description-container']"
```


#### Example



**Code:**
```json
{
  "name": "rating",
  "selector": ".rating",
  "type": "text",
  "default": "N/A"
}
```


#### Example



**Code:**
```bash
1. Selector matcht nicht → default oder null
2. Transform schlägt fehl → Original-Wert
3. Computed field error → null
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/templates/schema-extraction-strategy.md`</small>
