#!/usr/bin/env python3
"""
Content Enrichment Script for Evolving Documentation.

Enriches generated docs with:
1. Translation DE → EN
2. AI-generated content for empty sections
3. Expanded examples
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional
import anthropic

# Configuration - uses env vars with local fallbacks
DOCS_ROOT = Path(os.environ.get("DOCS_ROOT", str(Path(__file__).parent.parent))) / "docs" / "en" / "components"
SOURCE_ROOT = Path(os.environ.get("EVOLVING_ROOT", "/Users/neoforce/Buisiness/Evolving"))

# Categories and their source directories
CATEGORIES = {
    "commands": SOURCE_ROOT / ".claude" / "commands",
    "agents": SOURCE_ROOT / ".claude" / "agents",
    "rules": SOURCE_ROOT / ".claude" / "rules",
    "hooks": SOURCE_ROOT / ".claude" / "hooks",
    "patterns": SOURCE_ROOT / "knowledge" / "patterns",
    "skills": SOURCE_ROOT / ".claude" / "skills",
}

# Sections that need enrichment
SECTIONS_TO_ENRICH = [
    "System Impact",
    "Architecture",
    "Configuration",
    "Best Practices",
]


def load_doc(doc_path: Path) -> str:
    """Load a documentation file."""
    return doc_path.read_text()


def load_source(category: str, name: str) -> Optional[str]:
    """Load the source file for a component."""
    source_dir = CATEGORIES.get(category)
    if not source_dir:
        return None

    # Try different extensions
    for ext in [".md", ".py", ".sh"]:
        source_path = source_dir / f"{name}{ext}"
        if source_path.exists():
            return source_path.read_text()

    return None


def extract_section(content: str, section_name: str) -> str:
    """Extract content of a specific section."""
    pattern = rf"## {re.escape(section_name)}\s*\n(.*?)(?=\n## |\n---|\Z)"
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ""


def is_section_empty(content: str, section_name: str) -> bool:
    """Check if a section has no meaningful content."""
    section_content = extract_section(content, section_name)
    # Strip whitespace and check if empty
    stripped = section_content.strip()
    return len(stripped) < 10


def create_enrichment_prompt(
    doc_content: str,
    source_content: str,
    component_name: str,
    component_type: str,
    empty_sections: List[str]
) -> str:
    """Create prompt for AI enrichment."""

    sections_list = "\n".join(f"- {s}" for s in empty_sections)

    return f"""You are enriching documentation for an AI-powered development system component.

COMPONENT: {component_name}
TYPE: {component_type}

CURRENT DOCUMENTATION (may have German text that needs translation):
```markdown
{doc_content}
```

SOURCE FILE (original implementation):
```
{source_content[:3000] if source_content else "Not available"}
```

TASK:
1. Translate any German text to English (keep technical terms like "Agent", "Hook", "Pattern" in English)
2. Generate meaningful content for these empty sections:
{sections_list}

GUIDELINES for each section:
- **System Impact**: How does this component affect the overall system? What does it enable? (2-3 bullet points)
- **Architecture**: Key dependencies, data flow, integration points (2-3 bullet points)
- **Configuration**: Available options, environment variables, defaults (list format)
- **Best Practices**: Do's and Don'ts for using this component (2-3 items each)

OUTPUT FORMAT:
Return ONLY the enriched markdown content. Keep the existing structure but with filled sections.
Do NOT include ```markdown markers. Return clean markdown."""


def enrich_with_claude(prompt: str, client: anthropic.Anthropic) -> str:
    """Call Claude API for enrichment."""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


def process_doc(
    doc_path: Path,
    category: str,
    client: anthropic.Anthropic,
    dry_run: bool = False
) -> Dict:
    """Process a single documentation file."""
    name = doc_path.stem
    doc_content = load_doc(doc_path)
    source_content = load_source(category, name)

    # Check which sections are empty
    empty_sections = [s for s in SECTIONS_TO_ENRICH if is_section_empty(doc_content, s)]

    # Check for German content (simple heuristic)
    has_german = any(word in doc_content.lower() for word in [
        " du ", " ist ", " wird ", " eine ", " für ", " mit ", " wenn ",
        " oder ", " nicht ", " kann ", " diese ", " werden "
    ])

    needs_enrichment = empty_sections or has_german

    if not needs_enrichment:
        return {
            "name": name,
            "status": "skipped",
            "reason": "Already enriched"
        }

    # Create enrichment prompt
    prompt = create_enrichment_prompt(
        doc_content,
        source_content,
        name,
        category.rstrip("s"),
        empty_sections
    )

    if dry_run:
        return {
            "name": name,
            "status": "dry_run",
            "empty_sections": empty_sections,
            "has_german": has_german
        }

    # Call Claude for enrichment
    try:
        enriched_content = enrich_with_claude(prompt, client)

        # Write back
        doc_path.write_text(enriched_content)

        return {
            "name": name,
            "status": "enriched",
            "empty_sections": empty_sections,
            "has_german": has_german
        }
    except Exception as e:
        return {
            "name": name,
            "status": "error",
            "error": str(e)
        }


def process_category(
    category: str,
    client: anthropic.Anthropic,
    dry_run: bool = False,
    limit: int = None
) -> List[Dict]:
    """Process all docs in a category."""
    category_dir = DOCS_ROOT / category
    if not category_dir.exists():
        print(f"Category directory not found: {category_dir}")
        return []

    docs = list(category_dir.glob("*.md"))
    # Exclude index.md
    docs = [d for d in docs if d.name != "index.md"]

    if limit:
        docs = docs[:limit]

    results = []
    for i, doc_path in enumerate(docs):
        print(f"  [{i+1}/{len(docs)}] Processing {doc_path.name}...")
        result = process_doc(doc_path, category, client, dry_run)
        results.append(result)
        print(f"    → {result['status']}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Enrich documentation with AI-generated content")
    parser.add_argument("--category", choices=list(CATEGORIES.keys()), help="Process specific category")
    parser.add_argument("--all", action="store_true", help="Process all categories")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be enriched without making changes")
    parser.add_argument("--limit", type=int, help="Limit number of docs per category")

    args = parser.parse_args()

    if not args.category and not args.all:
        parser.print_help()
        sys.exit(1)

    # Initialize Claude client
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key and not args.dry_run:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key) if api_key else None

    categories = list(CATEGORIES.keys()) if args.all else [args.category]

    all_results = {}
    for category in categories:
        print(f"\n{'='*60}")
        print(f"Processing {category.upper()}")
        print(f"{'='*60}")

        results = process_category(category, client, args.dry_run, args.limit)
        all_results[category] = results

        # Summary
        enriched = sum(1 for r in results if r["status"] == "enriched")
        skipped = sum(1 for r in results if r["status"] == "skipped")
        errors = sum(1 for r in results if r["status"] == "error")

        print(f"\n{category}: {enriched} enriched, {skipped} skipped, {errors} errors")

    # Overall summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    for category, results in all_results.items():
        enriched = sum(1 for r in results if r["status"] == "enriched")
        total = len(results)
        print(f"  {category}: {enriched}/{total} enriched")


if __name__ == "__main__":
    main()
