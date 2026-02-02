---
title: fal-image-generator-agent
type: agent
tags: []
lang: en
confidence: 100
---

# fal-image-generator-agent


## Overview

<div class="component-meta" markdown>
| Attribute | Value |
|-----------|-------|
| **Type** | Agent |
| **Purpose** | Component description |
| **Complexity** | medium |
| **Model** | sonnet |
| **Category** | agents |</div>


## What It Does

"FAL.ai image generation with ICS Framework prompting"


## System Impact




## Architecture




## Usage


### Examples

#### Example



**Code:**
```python
STYLE_SIGNALS = {
    "infographic": ["erkläre", "zeige wie", "funktioniert", "prozess", "schritte", "anleitung", "workflow", "diagram"],
    "step_by_step": ["schritt für schritt", "how to", "tutorial", "anleitung", "schritte", "guide"],
    "commercial": ["poster", "werbung", "marketing", "kampagne", "ad", "flyer", "banner", "promo"],
    "editorial": ["blog", "artikel", "editorial", "magazin", "header", "thumbnail", "cover"],
    "comic": ["lustig", "witzig", "cartoon", "meme", "humor", "übertrieben", "karikatur", "funny"],
    "data_viz": ["daten", "statistik", "chart", "graph", "visualisierung", "zahlen", "prozent"],
    "product_mockup": ["etsy", "produkt", "mockup", "listing", "shop", "e-commerce", "amazon"],
    "social_media": ["instagram", "social", "post", "reels", "tiktok", "viral", "feed", "story"],
    "scientific": ["wissenschaft", "medizin", "biologie", "chemie", "anatomie", "zelle", "forschung"],
    "concept_art": ["konzept", "game", "fantasy", "world building", "character design", "creature"],
    "portrait": ["portrait", "headshot", "person", "gesicht", "charakter", "profil"],
    "landscape": ["landschaft", "natur", "outdoor", "berge", "meer", "wald", "panorama"],
    "minimalist": ["minimalistisch", "clean", "simple", "reduziert", "schlicht", "modern"],
    "retro": ["vintage", "retro", "alt", "nostalgisch", "70er", "80er", "analog", "film"],
    "3d_render": ["3d", "render", "cgi", "blender", "isometric", "geometric"],
    "icon_logo": ["icon", "logo", "symbol", "badge", "emblem", "marke", "app icon"],
    "anime": ["anime", "manga", "japan", "chibi", "kawaii", "ghibli"],
    "watercolor": ["aquarell", "watercolor", "gemalt", "künstlerisch", "soft", "traditional"],
    "cyberpunk": ["cyberpunk", "futuristic", "neon", "sci-fi", "dystopian", "tech", "cyber"],
    "food": ["essen", "food", "rezept", "kochen", "restaurant", "kulinarisch", "gericht"]
}
```


#### Example



**Code:**
```bash
User Input
    │
    ▼
┌─────────────────────┐
│ SIGNAL EXTRACTION   │
│ Keywords + Kontext  │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ STYLE MATCHING      │
│ Confidence Score    │
└─────────┬───────────┘
          │
    ┌─────┴─────┐
    ▼           ▼
 HIGH CONF   LOW CONF
    │           │
    ▼           ▼
 AUTO-APPLY  FRAGE:
 + Erklärung "Ich schlage X vor.
             Passt das?"
```


#### Example



**Code:**
```bash
SCHLECHT (Tag Soup):
"dog, park, 4k, realistic, beautiful, professional"

GUT (ICS Framework):
"[I] Product photography style shot
 [C] Golden retriever mid-leap catching a red frisbee in Central Park,
     autumn leaves scattered on grass, joggers blurred in background
 [S] Golden hour backlighting creating rim light on fur, shot with
     85mm lens at f/2.8, shallow depth of field, warm color grading"
```


#### Example



**Code:**
```bash
[Subject description with specific details] in [location/setting],
[action or pose], [time of day] lighting.
Shot with [focal length] lens at [aperture],
[depth of field], [color grading/mood].
```


#### Example



**Code:**
```bash
Professional woman in tailored navy blazer reviewing documents at
a modern glass desk, morning sunlight streaming through floor-to-ceiling
windows behind her. Shot with 50mm lens at f/2.0, shallow depth of field
with bokeh highlights, clean corporate aesthetic with cool blue tones.
```


#### Example



**Code:**
```bash
[Art style] illustration of [subject],
[distinctive features], [color palette],
[background treatment], [additional style notes].
```


#### Example



**Code:**
```bash
Flat vector illustration of a cozy coffee shop interior,
warm earth tones with terracotta and sage green accents,
geometric simplified shapes, subtle texture overlay,
white background with soft drop shadow.
```


#### Example



**Code:**
```bash
[Design type] featuring the text "[EXACT TEXT]" in [font style],
[text treatment], [background/context],
[additional design elements].
```


#### Example



**Code:**
```bash
Vintage-style poster featuring the text "COFFEE CLUB" in bold
serif typography with distressed texture, cream colored background
with subtle coffee stain rings, art deco border elements,
warm sepia color palette.
```


#### Example



**Code:**
```bash
[Product type] [product details] displayed on [surface/setting],
[arrangement], [lighting setup],
[style notes], [background treatment].
```


#### Example



**Code:**
```bash
Artisan ceramic mug with hand-painted blue geometric pattern
displayed on a raw wooden board, accompanied by loose coffee beans
and a small succulent, three-point softbox lighting setup,
clean white background with subtle shadows.
```


#### Example



**Code:**
```bash
[Subject] [minimal details] against [background color/treatment],
[composition notes], [single accent element if any],
intentional negative space [placement].
```


#### Example



**Code:**
```bash
Single red origami crane against pure white background,
positioned in lower right third, casting soft gray shadow to left,
intentional negative space filling upper two-thirds for text overlay.
```


#### Example



**Code:**
```bash
[Panel layout] showing [character] [action sequence],
[art style], [speech bubble content if any],
[color treatment], [panel borders/gutters].
```


#### Example



**Code:**
```bash
Four-panel comic strip showing a programmer's reaction to finding
a semicolon bug, exaggerated expressions in clean line art style,
speech bubbles with "WHY?!" and "FINALLY!", muted pastel colors,
thin black panel borders with white gutters.
```


#### Example



**Code:**
```bash
User Prompt
    │
    ▼
┌───────────────────────────┐
│ 0. CONTENT UNDERSTANDING  │
│    Signal-Keywords        │
│    Intent-Analyse         │
│    Style-Empfehlung       │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ 1. ICS STRUCTURE          │
│    + Image Type           │
│    + Content Details      │
│    + Style Aesthetics     │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ 2. PHOTOGRAPHY LAYER      │
│    + Camera/Lens          │
│    + Lighting Setup       │
│    + Composition          │
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ 3. QUALITY CHECKS         │
│    ☑ No tag soup          │
│    ☑ Narrative style      │
│    ☑ Specific details     │
└─────────────┬─────────────┘
              │
              ▼
       OPTIMIZED PROMPT
```


#### Example



**Code:**
```bash
USER: "Bild für meinen Kaffee-Blog"

ANALYSE:
- Signal: "blog" → Editorial Style
- Domain: Kaffee → Food/Lifestyle
- Use Case: Content Header

ENHANCED PROMPT:
"Editorial lifestyle photograph of an artisan latte with intricate
foam art, served in a handcrafted ceramic cup on a rustic wooden
table. Morning light streaming through a nearby window creates
soft shadows and warm highlights on the coffee surface.
Shot with 50mm lens at f/2.8, shallow depth of field with
background café ambiance softly blurred, warm and inviting
color palette with rich browns and cream tones."
```


#### Example



**Code:**
```bash
"Keep everything, but change [specific element] to [new value]"
"Same composition, add [new element]"
"Maintain the character, place in [different setting]"
"Everything is perfect except [specific issue], fix that"
```


#### Example



**Code:**
```bash
1. Initial: "Product shot of a leather journal on marble surface"
   → Generiert

2. Refine: "Keep everything, but add a vintage fountain pen next to it"
   → Editiert

3. Refine: "Same setup, change marble to dark walnut wood"
   → Editiert

4. Final: "Perfect, now make the lighting warmer, golden hour feel"
   → Final Version
```


#### Example



**Code:**
```python
import fal_client
import os
from dotenv import load_dotenv

load_dotenv()

def generate_image(
    prompt: str,
    aspect_ratio: str = "1:1",
    output_format: str = "png",
    safety_tolerance: int = 2
) -> str:
    """Generate image with Nano Banana Pro."""

    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro",
        arguments={
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "output_format": output_format,
            "safety_tolerance": safety_tolerance
        }
    )

    return result["images"][0]["url"]


def edit_image(
    prompt: str,
    image_url: str,
    aspect_ratio: str = "1:1"
) -> str:
    """Edit existing image with Nano Banana Pro."""

    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro/edit",
        arguments={
            "prompt": prompt,
            "image_url": image_url,
            "aspect_ratio": aspect_ratio
        }
    )

    return result["images"][0]["url"]
```


#### Example



**Code:**
```typescript
import { fal } from "@fal-ai/client";

interface GenerateOptions {
  prompt: string;
  aspectRatio?: string;
  outputFormat?: "png" | "jpeg";
  safetyTolerance?: number;
}

async function generateImage(options: GenerateOptions): Promise<string> {
  const result = await fal.subscribe("fal-ai/nano-banana-pro", {
    input: {
      prompt: options.prompt,
      aspect_ratio: options.aspectRatio || "1:1",
      output_format: options.outputFormat || "png",
      safety_tolerance: options.safetyTolerance || 2
    }
  });

  return result.data.images[0].url;
}
```


#### Example



**Code:**
```bash
1. ANALYSE: Produkt-Typ, Zielgruppe, Etsy-Trends
2. STYLE: Product Mockup Template
3. SETTINGS:
   - Aspect: 4:5 (Etsy optimal)
   - Background: Clean, lifestyle oder transparent
   - Lighting: Soft, professional
4. GENERATE: Main Image + Lifestyle Shots
5. REFINE: A/B Test Varianten
```


#### Example



**Code:**
```bash
1. ANALYSE: Platform, Content-Type, Brand Style
2. STYLE: Social Media Ready Template
3. SETTINGS:
   - Aspect: 1:1 (Feed) oder 9:16 (Stories/Reels)
   - Bold, scroll-stopping elements
   - Text overlay space beachten
4. GENERATE: Multiple Varianten
5. REFINE: CTA-optimiert
```


#### Example



**Code:**
```bash
1. ANALYSE: Kampagnen-Ziel, Brand Guidelines
2. STYLE: Commercial Template
3. SETTINGS:
   - Aspect: Verschiedene für verschiedene Placements
   - On-brand Colors
   - Text-Integration berücksichtigen
4. GENERATE: Hero Image + Supporting
5. REFINE: Format-Anpassungen
```


#### Example



**Code:**
```bash
SCHLECHT:
"cat, cute, 4k, realistic, beautiful, professional, amazing, stunning,
 masterpiece, highly detailed, award winning"

→ Keine Struktur, vage, redundant
```


#### Example



**Code:**
```bash
SCHLECHT:
"A nice picture of a coffee shop"

→ Was genau? Welcher Stil? Welche Stimmung?
```


#### Example



**Code:**
```bash
SCHLECHT:
"Minimalist design with lots of detailed ornaments"

→ Widerspruch in sich
```


#### Example



**Code:**
```bash
SCHLECHT:
"[500 Wörter mit jedem erdenklichen Detail]"

→ Fokus geht verloren, Modell verwirrt
```




## Configuration



## Best Practices




## Related



---

<small>Source: `.claude/agents/fal-image-generator-agent.md`</small>
