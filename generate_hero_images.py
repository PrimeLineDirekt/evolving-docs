#!/usr/bin/env python3
"""
Generate hero/infographic images for Evolving documentation using Fal.ai API.
"""

import os
import sys
import json
import requests
from pathlib import Path
from datetime import datetime

# Try to import fal_client
try:
    import fal_client
except ImportError:
    print("Error: fal-client not installed. Install with: pip install fal-client")
    sys.exit(1)

# Configuration
OUTPUT_DIR = Path("/Users/neoforce/Buisiness/evolving-docs/docs/shared/assets/images")
IMAGES_TO_CREATE = [
    {
        "name": "hero-system.png",
        "prompt": "Futuristic AI knowledge system visualization, interconnected glowing nodes forming a network, dark background, purple and orange accents, abstract tech art, clean minimal style, high quality"
    },
    {
        "name": "hero-agents.png",
        "prompt": "Multiple AI agents collaborating together, holographic displays showing data flows, neural network patterns, dark tech aesthetic, purple blue orange glow, futuristic, high quality"
    },
    {
        "name": "hero-commands.png",
        "prompt": "Terminal interface with flowing data streams, CLI aesthetic, dark mode, syntax highlighting colors, abstract tech visualization, command prompt lines, high quality"
    },
    {
        "name": "hero-memory.png",
        "prompt": "Digital brain with persistent memory storage, data crystals and nodes, neural pathways glowing, futuristic dark theme, purple and blue accents, abstract, high quality"
    }
]

def generate_image(prompt: str, filename: str) -> bool:
    """Generate a single image using Fal.ai API."""
    print(f"\n📸 Generating: {filename}")
    print(f"   Prompt: {prompt[:60]}...")

    try:
        # Call Fal.ai API
        result = fal_client.subscribe(
            "fal-ai/flux/schnell",
            arguments={
                "prompt": prompt,
                "image_size": "landscape_16_9",
                "num_images": 1,
                "enable_safety_checker": False
            }
        )

        # Get image URL
        if not result or "images" not in result or len(result["images"]) == 0:
            print(f"   ✗ No image returned from API")
            return False

        image_url = result["images"][0]["url"]
        print(f"   ✓ Image URL received: {image_url[:50]}...")

        # Download image
        output_path = OUTPUT_DIR / filename
        print(f"   ⬇ Downloading to: {output_path}")

        response = requests.get(image_url, timeout=30)
        response.raise_for_status()

        # Save image
        with open(output_path, "wb") as f:
            f.write(response.content)

        file_size = output_path.stat().st_size / (1024 * 1024)  # Size in MB
        print(f"   ✅ Saved: {filename} ({file_size:.2f} MB)")

        return True

    except Exception as e:
        print(f"   ✗ Error: {str(e)}")
        return False

def main():
    """Main execution function."""
    print("=" * 70)
    print("Evolving Documentation Hero Image Generator")
    print("=" * 70)

    # Verify output directory
    if not OUTPUT_DIR.exists():
        print(f"✗ Output directory not found: {OUTPUT_DIR}")
        sys.exit(1)

    print(f"\n📁 Output directory: {OUTPUT_DIR}")
    print(f"📊 Images to generate: {len(IMAGES_TO_CREATE)}")

    # Generate images
    successful = 0
    failed = 0
    results = []

    for image_config in IMAGES_TO_CREATE:
        success = generate_image(
            prompt=image_config["prompt"],
            filename=image_config["name"]
        )

        if success:
            successful += 1
            results.append({
                "filename": image_config["name"],
                "status": "success",
                "path": str(OUTPUT_DIR / image_config["name"]),
                "timestamp": datetime.now().isoformat()
            })
        else:
            failed += 1
            results.append({
                "filename": image_config["name"],
                "status": "failed",
                "timestamp": datetime.now().isoformat()
            })

    # Summary
    print("\n" + "=" * 70)
    print("Generation Summary")
    print("=" * 70)
    print(f"✅ Successful: {successful}/{len(IMAGES_TO_CREATE)}")
    print(f"✗ Failed: {failed}/{len(IMAGES_TO_CREATE)}")

    if successful > 0:
        print("\n📸 Generated Images:")
        for result in results:
            if result["status"] == "success":
                print(f"   • {result['filename']}")
                print(f"     Path: {result['path']}")

    # Save results to JSON
    results_file = OUTPUT_DIR.parent / "image-generation-results.json"
    with open(results_file, "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "successful": successful,
            "failed": failed,
            "results": results
        }, f, indent=2)

    print(f"\n📋 Results saved to: {results_file}")

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
