#!/usr/bin/env python3
"""Main CLI script for generating Evolving system documentation."""
import argparse
import sys
from pathlib import Path
from typing import Dict

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from config import get_source_files, get_output_dir, OUTPUT_DIRS, TEMPLATE_DIR
from renderer import Renderer
from parser import parse_markdown, extract_markdown_title, extract_markdown_sections


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    return text.lower().replace(' ', '-').replace('/', '-')


def extract_simple_metadata(source_file: Path, category: str) -> Dict:
    """Extract basic metadata from a markdown file."""
    frontmatter, body = parse_markdown(source_file)

    # Extract title
    title = extract_markdown_title(body) or source_file.stem

    # Extract sections
    sections = extract_markdown_sections(body)

    # Build basic metadata with all required fields
    metadata = {
        'name': source_file.stem,
        'slug': slugify(source_file.stem),
        'title': title,
        'description': frontmatter.get('description', sections.get('Description', '')[:200]),
        'category': category,
        'type': category.rstrip('s'),  # agents -> agent
        'tags': frontmatter.get('tags', '').split(',') if frontmatter.get('tags') else [],
        'created': frontmatter.get('created', ''),
        'lang': 'en',

        # Template requires these fields (with defaults)
        'confidence': 100,
        'complexity': 'medium',
        'model': 'sonnet',

        # Extracted content
        'purpose': sections.get('Purpose', sections.get('Concept', ''))[:200] if sections.get('Purpose', sections.get('Concept', '')) else 'Component description',
        'key_features': _extract_bullets(sections.get('Features', sections.get('Key Features', ''))),
        'usage': sections.get('Usage', sections.get('How to use', '')),
        'examples': _extract_examples(body),

        # Source reference
        'source_file': str(source_file.relative_to(Path('/Users/neoforce/Buisiness/Evolving'))),
    }

    return metadata


def _extract_bullets(text: str) -> list:
    """Extract bullet points from text."""
    bullets = []
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('-') or stripped.startswith('*'):
            item = stripped.lstrip('-*').strip()
            if item:
                bullets.append(item)
    return bullets


def _extract_examples(content: str) -> list:
    """Extract code examples from content."""
    examples = []
    in_code = False
    code_lines = []
    code_lang = 'bash'

    for line in content.split('\n'):
        if line.startswith('```'):
            if not in_code:
                # Start of code block
                code_lang = line.strip('`').strip() or 'bash'
                in_code = True
            else:
                # End of code block
                if code_lines:
                    examples.append({
                        'code': '\n'.join(code_lines),
                        'code_lang': code_lang,
                        'title': 'Example'
                    })
                code_lines = []
                in_code = False
        elif in_code:
            code_lines.append(line)

    return examples


def ensure_output_dirs(language: str = "en"):
    """Create all output directories if they don't exist."""
    for category, output_dir in OUTPUT_DIRS[language].items():
        output_dir.mkdir(parents=True, exist_ok=True)
    print(f"✓ Output directories ensured")


def generate_category_docs(
    category: str,
    renderer: Renderer,
    language: str = "en",
) -> int:
    """
    Generate documentation for a single category.

    Returns:
        Number of files generated
    """
    print(f"\n{'='*60}")
    print(f"Generating {category.upper()} documentation...")
    print(f"{'='*60}")

    # Get source files
    source_files = get_source_files(category)
    if not source_files:
        print(f"⚠️  No source files found for {category}")
        return 0

    print(f"Found {len(source_files)} source file(s)")

    output_dir = get_output_dir(category, language)
    generated_count = 0
    components = []

    # Process each source file
    for source_file in source_files:
        try:
            # Extract metadata
            metadata = extract_simple_metadata(source_file, category)
            if not metadata:
                print(f"⚠️  Skipped {source_file.name} (no metadata)")
                continue

            # Render component doc (pass metadata directly, not nested)
            content = renderer.render_component("component.md.j2", metadata)

            # Write to output file
            output_file = output_dir / f"{metadata['slug']}.md"
            output_file.write_text(content)

            print(f"✓ Generated: {output_file.name}")
            generated_count += 1
            components.append(metadata)

        except Exception as e:
            print(f"❌ Error processing {source_file.name}: {e}")
            import traceback
            traceback.print_exc()
            continue

    # Generate category index
    if components:
        try:
            # Transform components to items format expected by template
            items = []
            for c in components:
                items.append({
                    "name": c.get("title", c.get("name", "")),
                    "link": f"{c.get('slug', c.get('name', '').lower())}.md",
                    "description": c.get("description", c.get("purpose", ""))[:100],
                    "type": c.get("type", category.rstrip('s')),
                })

            index_content = renderer.render_component("index.md.j2", {
                "title": f"{category.title()}",
                "lang": language,
                "description": f"Documentation for all {category} in the Evolving system.",
                "items": items,
                "item_type": category.rstrip('s').title(),
                "grouping": "alphabetical",
                "stats": [
                    {"value": str(len(components)), "label": f"Total {category.title()}"},
                ],
            })

            index_file = output_dir / "index.md"
            index_file.write_text(index_content)
            print(f"✓ Generated index: {index_file.name}")

        except Exception as e:
            print(f"❌ Error generating index for {category}: {e}")

    print(f"\n✓ {category}: {generated_count}/{len(source_files)} files generated")
    return generated_count


def update_mkdocs_counts(counts: Dict[str, int]):
    """Update mkdocs.yml with accurate component counts."""
    print(f"\n📝 Component counts for mkdocs.yml:")
    for category, count in counts.items():
        print(f"   {category}: {count}")

    print("\n⚠️  Manual update required: Update tab counts in mkdocs.yml")
    print("   Format: 'Components/Agents (X)' where X is the count")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate Evolving system documentation"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generate all categories",
    )
    parser.add_argument(
        "--category",
        choices=["agents", "commands", "skills", "rules", "patterns", "templates", "prompts", "blueprints", "hooks"],
        help="Generate specific category",
    )
    parser.add_argument(
        "--language",
        default="en",
        choices=["en", "de"],
        help="Output language (default: en)",
    )

    args = parser.parse_args()

    if not args.all and not args.category:
        parser.print_help()
        sys.exit(1)

    # Initialize renderer
    try:
        renderer = Renderer()
    except Exception as e:
        print(f"❌ Failed to initialize renderer: {e}")
        print(f"   Template directory: {TEMPLATE_DIR}")
        sys.exit(1)

    # Ensure output directories exist
    print("Setting up output directories...")
    ensure_output_dirs(args.language)

    # Categories to process
    categories = [
        "agents", "commands", "skills", "rules",
        "patterns", "templates", "prompts", "blueprints", "hooks"
    ] if args.all else [args.category]

    # Generate documentation
    counts = {}
    for category in categories:
        count = generate_category_docs(
            category,
            renderer,
            args.language,
        )
        counts[category] = count

    # Summary
    print(f"\n{'='*60}")
    print("GENERATION COMPLETE")
    print(f"{'='*60}")

    total = sum(counts.values())
    print(f"\n✓ Total files generated: {total}")
    for category, count in counts.items():
        print(f"   {category}: {count}")

    # Update mkdocs.yml
    update_mkdocs_counts(counts)

    print("\n✅ Documentation generation complete!")


if __name__ == "__main__":
    main()
