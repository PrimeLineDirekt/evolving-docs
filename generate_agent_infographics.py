#!/usr/bin/env python3
"""Generate infographics for agents 46-56."""

import os
import sys
import json
import requests
from pathlib import Path
from datetime import datetime

try:
    import fal_client
except ImportError:
    print("Error: fal-client not installed. Install with: pip install fal-client")
    sys.exit(1)

OUTPUT_DIR = Path("/Users/neoforce/Buisiness/evolving-docs/docs/shared/assets/infographics/agents")

AGENTS = [
    {
        "name": "privacy-scanner-agent",
        "description": "Scans files for sensitive/personal content before and after template sync, ensuring no private data leaks into templates"
    },
    {
        "name": "research-analyst-agent",
        "description": "Multi-source research and validation agent with confidence scoring, synthesizing insights from multiple data sources"
    },
    {
        "name": "system-analyzer-agent",
        "description": "First agent in system-builder workflow, analyzing user requirements and matching them with appropriate blueprints"
    },
    {
        "name": "system-architect-agent",
        "description": "Creative core of system-builder, designing concrete architectures with agent roles, dependencies and knowledge injection"
    },
    {
        "name": "system-deep-research-agent",
        "description": "System analysis specialist generating persistent storage-locations.json configuration for Evolving system setup"
    },
    {
        "name": "system-generator-agent",
        "description": "Builder agent that takes architecture designs and generates all files in target directory for new systems"
    },
    {
        "name": "system-validator-agent",
        "description": "Quality gate validating generated systems for completeness, correctness and best-practice compliance"
    },
    {
        "name": "template-diff-agent",
        "description": "Intelligent diff analysis between source and target repositories, categorizing changes and identifying conflicts"
    },
    {
        "name": "template-inventory-agent",
        "description": "Analyzes Evolving-Template repository, counting components and comparing with source to identify gaps and sync needs"
    },
    {
        "name": "tool-inventory-agent",
        "description": "Inventory specialist discovering tools, finding orphaned components and generating comprehensive Tool-Map"
    },
    {
        "name": "whats-next",
        "description": "Specialized session-handoff agent running with fresh context to write handoff files for session continuity"
    }
]

def generate_image(name: str, description: str) -> dict:
    """Generate a single infographic."""
    print(f"\n📸 Generating: {name}")

    prompt = f"Modern tech infographic for {name} agent: {description}. Visual elements: agent icon, workflow arrows, data flows. Blue-purple gradient, clean minimalist style"

    try:
        result = fal_client.subscribe(
            "fal-ai/nano-banana-pro",
            arguments={
                "prompt": prompt,
                "aspect_ratio": "16:9",
                "num_images": 1
            }
        )

        if not result or "images" not in result or len(result["images"]) == 0:
            print(f"   ✗ No image returned")
            return None

        image_url = result["images"][0]["url"]
        print(f"   ✓ Generated: {image_url[:50]}...")

        # Download image
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()

        # Save PNG
        png_path = OUTPUT_DIR / f"{name}.png"
        with open(png_path, "wb") as f:
            f.write(response.content)

        # Save metadata JSON
        metadata = {
            "prompt": prompt,
            "cost_usd": 0.15,
            "aspect_ratio": "16:9",
            "url": image_url,
            "timestamp": datetime.now().isoformat(),
            "type": "generate",
            "model": "fal-ai/nano-banana-pro"
        }

        json_path = OUTPUT_DIR / f"{name}.json"
        with open(json_path, "w") as f:
            json.dump(metadata, f, indent=2)

        file_size = png_path.stat().st_size / (1024 * 1024)
        print(f"   ✅ Saved: {file_size:.2f} MB")

        return metadata

    except Exception as e:
        print(f"   ✗ Error: {e}")
        return None

def main():
    print("=" * 70)
    print("Agent Infographic Generator (46-56)")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_cost = 0.0
    successful = 0

    for agent in AGENTS:
        result = generate_image(agent["name"], agent["description"])
        if result:
            successful += 1
            total_cost += result.get("cost_usd", 0.15)

    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"✅ Generated: {successful}/{len(AGENTS)}")
    print(f"💰 Total cost: ${total_cost:.2f}")
    print(f"📁 Output: {OUTPUT_DIR}")

    return 0 if successful == len(AGENTS) else 1

if __name__ == "__main__":
    sys.exit(main())
