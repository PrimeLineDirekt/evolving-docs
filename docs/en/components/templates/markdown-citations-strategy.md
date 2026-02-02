---
title: markdown-citations-strategy
type: template
tags: []
lang: en
confidence: 100
---

# markdown-citations-strategy


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
```markdown
Check out [this article](https://example.com/very/long/url/path)
and also [another resource](https://another-site.com/different/path).
```


#### Example



**Code:**
```markdown
Check out this article⟨1⟩ and also another resource⟨2⟩.

## References

⟨1⟩ https://example.com/very/long/url/path: this article
⟨2⟩ https://another-site.com/different/path: another resource
```


#### Example



**Code:**
```bash
                    ┌─────────────────┐
                    │  Raw Markdown   │
                    │  [text](url)    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Link Pattern   │
                    │  Detection      │
                    └────────┬────────┘
                             │
                             ▼
              ┌──────────────┴──────────────┐
              │        Link Map Building     │
              │   url → (number, description)│
              └──────────────┬──────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼                             ▼
    ┌─────────────────┐           ┌─────────────────┐
    │ Inline Replace  │           │ References      │
    │ text⟨N⟩        │           │ Section Build   │
    └─────────────────┘           └─────────────────┘
```


#### Example



**Code:**
```bash
!?\[([^\]]+)\]\(([^)]+?)(?:\s+"([^"]*)")?\)

Gruppen:
- Group 0: Ganzer Match (inkl. optional !)
- Group 1: Link Text
- Group 2: URL
- Group 3: Optional Title
```


#### Example



**Code:**
```bash
link_map = {
  "https://example.com": (1, ": Article Title"),
  "https://another.com": (2, ": Description - Link Text"),
  ...
}
```


#### Example



**Code:**
```bash
Priorität:
1. Title (wenn vorhanden)
2. Link Text (wenn unterschiedlich von Title)
3. Beides kombiniert: "Title - Link Text"
```


#### Example



**Code:**
```bash
base_url = "https://example.com/page/"
relative_url = "../images/photo.jpg"

resolved = "https://example.com/images/photo.jpg"
```


#### Example



**Code:**
```bash
Optimierte Fälle:
1. http:// oder https:// → direkt zurück
2. mailto: → direkt zurück
3. // → Protocol-relative, direkt
4. / → Absolute path, base + url
5. Sonst → urljoin()
```


#### Example



**Code:**
```markdown
Original:
Check out [this article](https://example.com) for more info.

Converted:
Check out this article⟨1⟩ for more info.
```


#### Example



**Code:**
```markdown
## References

⟨1⟩ https://example.com: this article
⟨2⟩ https://other.com/path: Another Resource - link text
```


#### Example



**Code:**
```markdown
See [here](https://example.com) and also [there](https://example.com).

→

See here⟨1⟩ and also there⟨1⟩.

## References

⟨1⟩ https://example.com: here - there
```


#### Example



**Code:**
```bash
HTML → html2text → Raw Markdown → Citations → Final Markdown
```


#### Example



**Code:**
```bash
                    ┌─────────────────┐
                    │   HTML Input    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │ Raw MD      │  │ MD + Cites  │  │ Fit MD      │
    │ (alles)     │  │ (mit Refs)  │  │ (gefiltert) │
    └─────────────┘  └─────────────┘  └─────────────┘
```


#### Example



**Code:**
```bash
MarkdownGenerationResult:
├── raw_markdown          # Original conversion
├── markdown_with_citations  # Mit Citation-Nummern
├── references_markdown   # ## References Section
├── fit_markdown         # Gefiltert (optional)
└── fit_html            # Gefiltertes HTML (optional)
```




## Configuration



## Best Practices




## Related



---

<small>Source: `knowledge/templates/markdown-citations-strategy.md`</small>
