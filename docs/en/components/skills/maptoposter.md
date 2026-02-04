---
title: MapToPoster
type: skill
tags: [design, maps, creative, posters, automation]
lang: en
confidence: 95
---

# MapToPoster

![MapToPoster Skill](../../shared/assets/infographics/skills/maptoposter.png)

## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Skill |
| **Purpose** | Generate minimalist city map posters with artistic themes |
| **Complexity** | Low |
| **Model** | haiku |
| **Plugin** | specialized |
| **Version** | 1.0 |
</div>

## What It Does

MapToPoster is a Python-based tool that generates minimalist city map posters for any city in the world. It uses OpenStreetMap data for roads, water, and parks, and applies one of 17 artistic themes to create high-quality (300 DPI) poster-ready outputs.

## Key Features

- **17 Artistic Themes** - From noir to neon cyberpunk to japanese ink
- **Flexible Distance** - 4km to 20km radius coverage
- **Bilingual Labels** - City + Country text overlay
- **High-Resolution** - 300 DPI output for print quality
- **OSM Integration** - Real-time map data from OpenStreetMap
- **Batch Processing** - Generate multiple themes or cities at once

## Available Themes

<div class="grid cards" markdown>

-   **Classic Styles**

    ---

    - `feature_based` - Classic black & white with road hierarchy
    - `noir` - Pure black background, white roads
    - `monochrome_blue` - Single blue color family
    - `contrast_zones` - High contrast urban density

-   **Vibrant Themes**

    ---

    - `neon_cyberpunk` - Dark with electric pink/cyan
    - `midnight_blue` - Navy background with gold roads
    - `sunset` - Warm oranges and pinks
    - `autumn` - Burnt oranges and reds

-   **Natural Tones**

    ---

    - `forest` - Deep greens and sage
    - `ocean` - Blues and teals for coastal cities
    - `terracotta` - Mediterranean warmth
    - `copper_patina` - Oxidized copper aesthetic

-   **Artistic Styles**

    ---

    - `blueprint` - Architectural blueprint aesthetic
    - `japanese_ink` - Minimalist ink wash style
    - `pastel_dream` - Soft muted pastels
    - `warm_beige` - Vintage sepia tones
    - `gradient_roads` - Smooth gradient shading

</div>

## The Process

### 1. Theme Selection

The skill asks for:
- City name
- Country name
- Desired theme
- Optional: distance (radius in meters)

### 2. Generation

Executes the poster generation:
```bash
./poster.sh -c "City" -C "Country" -t theme -d distance
```

### 3. Output

- Saves poster to `posters/{city}_{theme}_{timestamp}.png`
- Provides file path to user
- Optionally offers to generate additional themes

## Usage

```
/maptoposter
```

Or naturally trigger with phrases like:
- "Create poster for [city]"
- "Generate map of [city]"
- "Make [city] map in [theme] style"

## Distance Guidelines

Choose distance based on city size and desired detail:

| Distance | Best For | Example Cities |
|----------|----------|----------------|
| 4000-6000m | Small/dense cities | Venice, Amsterdam center |
| 8000-12000m | Medium cities, downtown focus | Paris, Barcelona |
| 15000-20000m | Large metros, full city view | Tokyo, Mumbai |

## Command Reference

### Basic Command
```bash
./poster.sh -c "Da Nang" -C "Vietnam" -t ocean -d 10000
```

### Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--city` | `-c` | City name | required |
| `--country` | `-C` | Country name | required |
| `--theme` | `-t` | Theme name | feature_based |
| `--distance` | `-d` | Radius in meters | 29000 |
| `--name` | | Display name override | |
| `--country-label` | | Display country override | |
| `--list-themes` | | Show all available themes | |
| `--all-themes` | | Generate poster for all themes | |

## Example Commands

### Iconic Grid Patterns
```bash
# New York noir style
./poster.sh -c "New York" -C "USA" -t noir -d 12000

# Barcelona vintage style
./poster.sh -c "Barcelona" -C "Spain" -t warm_beige -d 8000
```

### Waterfront & Canals
```bash
# Venice blueprint style
./poster.sh -c "Venice" -C "Italy" -t blueprint -d 4000

# Dubai midnight blue
./poster.sh -c "Dubai" -C "UAE" -t midnight_blue -d 15000
```

### Asian Cities
```bash
# Tokyo japanese ink style
./poster.sh -c "Tokyo" -C "Japan" -t japanese_ink -d 15000

# Da Nang ocean theme
./poster.sh -c "Da Nang" -C "Vietnam" -t ocean -d 10000
```

### European Cities
```bash
# Paris pastel dream
./poster.sh -c "Paris" -C "France" -t pastel_dream -d 10000

# Berlin noir
./poster.sh -c "Berlin" -C "Germany" -t noir -d 12000
```

### Generate All Themes
```bash
# Create posters in all 17 themes
./poster.sh -c "Singapore" -C "Singapore" --all-themes
```

## Output Format

Posters are saved to:
```
/Users/neoforce/Buisiness/maptoposter/posters/{city}_{theme}_{YYYYMMDD_HHMMSS}.png
```

Files are:
- High-resolution PNG format
- 300 DPI for print quality
- Optimized for poster printing (typically 18x24" or A2)
- Include city and country labels

## Theme Selection Guide

### By City Character

**Modern Metropolis**
- `noir`, `neon_cyberpunk`, `midnight_blue`
- Best for: New York, Dubai, Singapore

**Coastal Cities**
- `ocean`, `pastel_dream`, `warm_beige`
- Best for: Da Nang, Venice, Barcelona

**Historic Cities**
- `blueprint`, `copper_patina`, `terracotta`
- Best for: Paris, Rome, Istanbul

**Nature-Integrated**
- `forest`, `autumn`, `japanese_ink`
- Best for: Portland, Vancouver, Kyoto

### By Use Case

**Home Decor**
- `pastel_dream`, `warm_beige`, `terracotta`

**Office/Professional**
- `noir`, `blueprint`, `contrast_zones`

**Gift/Special**
- `neon_cyberpunk`, `copper_patina`, `gradient_roads`

## Batch Processing

Generate multiple cities:
```bash
for city in "Tokyo" "Paris" "Berlin"; do
  ./poster.sh -c "$city" -C "auto" -t noir -d 12000
done
```

Generate multiple themes for one city:
```bash
./poster.sh -c "Amsterdam" -C "Netherlands" --all-themes
```

## Quality Checklist

Before finalizing a poster:

- [ ] City name and country are correctly spelled
- [ ] Distance captures desired area (not too zoomed in/out)
- [ ] Theme matches intended aesthetic
- [ ] Map data downloaded successfully from OSM
- [ ] Output file exists in posters/ directory
- [ ] Resolution is 300 DPI for print quality

## Workflow Integration

### Standalone Generation
```
User: "Create poster for Tokyo"
→ Theme selection
→ Distance recommendation
→ Generate poster
→ Provide file path
```

### With Etsy Integration
```
User: "Create Tokyo map poster for Etsy"
→ Generate map with maptoposter
→ Pass to etsy-poster-creator for SEO
→ Complete listing with image
```

## Meta-Instructions

When using MapToPoster:

1. **Always** work in `/Users/neoforce/Buisiness/maptoposter`
2. **Always** use `./poster.sh` (not direct Python calls)
3. **Provide** theme recommendations based on city character
4. **For unknown cities**, show `--list-themes` options first
5. **Suggest distance** based on city size and user intent

## Related Skills

- [Etsy Poster Creator](etsy-poster-creator.md) - Create Etsy listings for map posters
- [Brainstorming](brainstorming.md) - Design ideation and planning
- [Image Generation](../../workflows/image-generation.md) - General image creation workflows

---

<small>Source: `specialized:maptoposter`</small>
