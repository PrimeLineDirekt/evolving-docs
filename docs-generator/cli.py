#!/usr/bin/env python3
"""Main CLI script for generating Evolving system documentation."""
import argparse
import sys
from pathlib import Path
from typing import Dict

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from config import get_source_files, get_output_dir, OUTPUT_DIRS, TEMPLATE_DIR, Config, EVOLVING_ROOT, set_roots
from renderer import Renderer
from parser import parse_markdown, extract_markdown_title, extract_markdown_sections

# Import extractors dynamically to avoid import errors
try:
    from extractors.command import CommandExtractor
    from extractors.agent import AgentExtractor
    from extractors.skill import SkillExtractor
    from extractors.pattern import PatternExtractor
    from extractors.learning import LearningExtractor
    from extractors.scenario import ScenarioExtractor
    from extractors.graphics_tool import GraphicsToolExtractor
    # Function-based extractors
    from extractors import hook as hook_extractor
    from extractors import blueprint as blueprint_extractor
    from extractors import rule as rule_extractor
    EXTRACTORS_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import extractors: {e}")
    EXTRACTORS_AVAILABLE = False


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    return text.lower().replace(' ', '-').replace('/', '-')


def get_extractor_for_category(category: str, config: Config):
    """
    Get the specialized extractor for a given category.

    Args:
        category: Component category (e.g., 'commands', 'agents')
        config: Config object with source_root

    Returns:
        Extractor instance or None if no specialized extractor exists
    """
    if not EXTRACTORS_AVAILABLE:
        return None

    extractor_map = {
        'commands': CommandExtractor,
        'agents': AgentExtractor,
        'skills': SkillExtractor,
        'patterns': PatternExtractor,
        # 'rules': No class-based extractor (uses function-based)
        # 'hooks': No class-based extractor (uses function-based)
        # 'blueprints': No class-based extractor (uses function-based)
        # 'templates': No specialized extractor yet
        # 'prompts': No specialized extractor yet
    }

    extractor_class = extractor_map.get(category)
    if extractor_class:
        try:
            return extractor_class(config)
        except Exception as e:
            print(f"Warning: Could not instantiate {extractor_class.__name__}: {e}")
            return None
    return None


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
        'source_file': str(source_file.relative_to(EVOLVING_ROOT)),
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


def _normalize_hook_metadata(raw: Dict, source_file: Path) -> Dict:
    """Normalize hook extractor output to template format."""
    description = raw.get('description', 'No description available')
    # Extract first line/paragraph for short description
    short_desc = description.split('\n')[0] if description else 'Hook component'

    return {
        'name': raw.get('title', source_file.stem),
        'slug': slugify(raw.get('title', source_file.stem)),
        'description': description,  # Full description
        'category': 'hooks',
        'type': 'hook',
        'tags': [raw.get('hook_type', 'general'), raw.get('language', 'unknown')],
        'lang': 'en',
        'confidence': 100,
        'complexity': 'medium',
        'model': 'sonnet',
        'purpose': short_desc[:200],  # Short version for purpose
        'key_features': [f"Type: {raw.get('hook_type', 'general')}", f"Language: {raw.get('language', 'unknown')}"],
        'usage': f"Hook file: `{raw.get('filename', source_file.name)}`",
        'examples': [{'code': raw.get('code_snippet', ''), 'code_lang': raw.get('language', 'bash'), 'title': 'Implementation'}] if raw.get('code_snippet') else [],
        'source_file': str(source_file.relative_to(EVOLVING_ROOT)),
    }


def _normalize_blueprint_metadata(raw: Dict, source_file: Path) -> Dict:
    """Normalize blueprint extractor output to template format."""
    # TODO: Implement based on blueprint extractor output format
    return {
        'name': raw.get('title', source_file.stem),
        'slug': slugify(raw.get('title', source_file.stem)),
        'description': raw.get('description', 'No description available'),
        'category': 'blueprints',
        'type': 'blueprint',
        'tags': raw.get('tags', []),
        'lang': 'en',
        'confidence': 100,
        'complexity': 'medium',
        'model': 'sonnet',
        'purpose': raw.get('description', 'Blueprint component')[:200],
        'key_features': [],
        'usage': '',
        'examples': [],
        'source_file': str(source_file.relative_to(EVOLVING_ROOT)),
    }


def _normalize_rule_metadata(raw: Dict, source_file: Path) -> Dict:
    """Normalize rule extractor output to template format."""
    # TODO: Implement based on rule extractor output format
    return {
        'name': raw.get('title', source_file.stem),
        'slug': slugify(raw.get('title', source_file.stem)),
        'description': raw.get('description', 'No description available'),
        'category': 'rules',
        'type': 'rule',
        'tags': raw.get('tags', []),
        'lang': 'en',
        'confidence': 100,
        'complexity': 'medium',
        'model': 'sonnet',
        'purpose': raw.get('description', 'Rule component')[:200],
        'key_features': [],
        'usage': '',
        'examples': [],
        'source_file': str(source_file.relative_to(EVOLVING_ROOT)),
    }


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

    # Get appropriate extractor
    config = Config()
    extractor = get_extractor_for_category(category, config)

    # Log which extractor will be used
    if category in ['hooks', 'blueprints', 'rules']:
        print(f"✓ Using function-based extractor: {category}_extractor.extract()")
    elif extractor:
        print(f"✓ Using specialized extractor: {extractor.__class__.__name__}")
    else:
        print(f"ℹ️  Using simple metadata extractor (no specialized extractor for {category})")

    output_dir = get_output_dir(category, language)
    generated_count = 0
    components = []

    # Process each source file
    for source_file in source_files:
        try:
            # Extract metadata using specialized extractor or fallback
            # Function-based extractors (hooks, blueprints, rules)
            if category == 'hooks':
                raw_metadata = hook_extractor.extract(source_file)
                # Normalize to template format
                metadata = _normalize_hook_metadata(raw_metadata, source_file)
            elif category == 'blueprints':
                raw_metadata = blueprint_extractor.extract(source_file)
                # Normalize to template format
                metadata = _normalize_blueprint_metadata(raw_metadata, source_file)
            elif category == 'rules':
                raw_metadata = rule_extractor.extract(source_file)
                # Normalize to template format
                metadata = _normalize_rule_metadata(raw_metadata, source_file)
            elif extractor:
                # Class-based extractor
                metadata = extractor.extract_one(source_file)
            else:
                # Fallback to simple extraction
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
    parser.add_argument(
        "--source",
        help="Path to evolving source repo (default: env EVOLVING_ROOT or local)",
    )
    parser.add_argument(
        "--output",
        help="Path to docs output repo (default: env DOCS_ROOT or repo root)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force regenerate all docs (ignore cache)",
    )

    args = parser.parse_args()

    # Apply root overrides before anything else
    if args.source or args.output:
        set_roots(source=args.source, output=args.output)

    if not args.all and not args.category:
        # Default to --all when --force is used (CI workflow)
        if args.force:
            args.all = True
        else:
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
