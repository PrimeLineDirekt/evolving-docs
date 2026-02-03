"""Rule extractor for Evolving documentation."""

from pathlib import Path
from typing import Any
import re


def extract(source_path: Path) -> dict[str, Any]:
    """
    Extract rule documentation from markdown files.

    Args:
        source_path: Path to the rule markdown file

    Returns:
        Dictionary with rule metadata for template rendering
    """
    content = source_path.read_text(encoding='utf-8')

    # Extract title (first # heading)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else source_path.stem

    # Extract priority
    priority_match = re.search(r'\*\*Priorität\*\*:\s*(.+?)(?:\n|$)', content)
    priority = priority_match.group(1).strip() if priority_match else "MEDIUM"

    # Extract trigger
    trigger_match = re.search(r'\*\*Trigger\*\*:\s*(.+?)(?:\n|$)', content)
    trigger = trigger_match.group(1).strip() if trigger_match else "N/A"

    # Extract first paragraph after metadata as description
    # Look for content after the metadata lines and before the first ## heading
    desc_match = re.search(
        r'(?:\*\*Trigger\*\*:.*?\n\n)(.*?)(?:\n##|\Z)',
        content,
        re.DOTALL
    )

    if desc_match:
        description = desc_match.group(1).strip()
        # Clean up markdown and limit length
        description = re.sub(r'\n+', ' ', description)
        description = re.sub(r'\s+', ' ', description)
    else:
        # Fallback: get first paragraph after title
        paragraphs = re.split(r'\n\n+', content)
        description = next(
            (p.strip() for p in paragraphs[1:] if p.strip() and not p.startswith('#')),
            "No description available"
        )

    # Extract sections for content
    sections = []
    section_pattern = re.compile(r'^##\s+(.+?)$\n(.*?)(?=^##|\Z)', re.MULTILINE | re.DOTALL)
    for match in section_pattern.finditer(content):
        section_title = match.group(1).strip()
        section_content = match.group(2).strip()
        sections.append({
            'title': section_title,
            'content': section_content
        })

    return {
        'type': 'rule',
        'title': title,
        'filename': source_path.name,
        'priority': priority,
        'trigger': trigger,
        'description': description,
        'sections': sections,
        'source_path': str(source_path)
    }
