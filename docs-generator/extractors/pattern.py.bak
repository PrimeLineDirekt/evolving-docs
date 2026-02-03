"""Pattern Extractor - extracts documentation from knowledge/patterns/*.md"""

import re
from pathlib import Path
from typing import Dict, Any, Optional
import yaml


class PatternExtractor:
    """Extracts pattern documentation from markdown files"""

    def __init__(self, evolving_root: Path):
        self.patterns_dir = evolving_root / "knowledge" / "patterns"

    def extract_all(self) -> list[Dict[str, Any]]:
        """Extract all patterns"""
        patterns = []

        if not self.patterns_dir.exists():
            return patterns

        for md_file in self.patterns_dir.glob("*.md"):
            if md_file.name.startswith("_"):
                continue

            pattern = self._extract_pattern(md_file)
            if pattern:
                patterns.append(pattern)

        return patterns

    def _extract_pattern(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Extract pattern from a single file"""
        try:
            content = file_path.read_text(encoding="utf-8")

            # Try to parse YAML frontmatter
            frontmatter = self._parse_frontmatter(content)

            # Extract title from heading if no frontmatter name
            if not frontmatter or "name" not in frontmatter:
                title = self._extract_title(content)
                if not title:
                    return None
                name = title
            else:
                name = frontmatter.get("name")

            # Build pattern data
            pattern = {
                "name": name,
                "type": "pattern",
                "tags": frontmatter.get("tags", []) if frontmatter else [],
                "lang": frontmatter.get("lang", "en") if frontmatter else "en",
                "description": frontmatter.get("description", "") if frontmatter else "",
                "purpose": frontmatter.get("purpose", "") if frontmatter else "",
                "key_features": self._extract_key_features(content),
                "examples": self._extract_examples(content),
                "source_file": str(file_path.relative_to(file_path.parents[3]))
            }

            return pattern

        except Exception as e:
            print(f"Error extracting pattern from {file_path}: {e}")
            return None

    def _parse_frontmatter(self, content: str) -> Optional[Dict[str, Any]]:
        """Parse YAML frontmatter if present"""
        if not content.startswith("---"):
            return None

        parts = content.split("---", 2)
        if len(parts) < 3:
            return None

        try:
            return yaml.safe_load(parts[1])
        except yaml.YAMLError:
            return None

    def _extract_title(self, content: str) -> Optional[str]:
        """Extract title from first # heading"""
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        return match.group(1).strip() if match else None

    def _extract_key_features(self, content: str) -> list[str]:
        """Extract key features from pattern"""
        features = []

        # Look for common pattern sections
        sections = [
            "Benefits", "Key Features", "Advantages",
            "When to Use", "Use Cases"
        ]

        for section in sections:
            pattern = rf'##\s+{section}\s*\n(.*?)(?=\n##|\Z)'
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

            if match:
                section_content = match.group(1).strip()
                # Extract bullet points
                bullets = re.findall(r'^\s*[-*]\s+(.+)$', section_content, re.MULTILINE)
                features.extend(bullets[:3])  # Limit to 3 per section

        return features[:5]  # Total limit of 5 features

    def _extract_examples(self, content: str) -> list[str]:
        """Extract example sections"""
        examples = []

        # Look for example/usage sections
        patterns = [
            r'##\s+Example[s]?\s*\n(.*?)(?=\n##|\Z)',
            r'##\s+Usage\s*\n(.*?)(?=\n##|\Z)',
            r'```[^\n]*\n(.*?)```'
        ]

        for pattern in patterns:
            matches = re.finditer(pattern, content, re.DOTALL | re.IGNORECASE)
            for match in matches:
                example = match.group(1).strip()
                if example and len(example) < 500:  # Reasonable length
                    examples.append(example)
                if len(examples) >= 3:
                    break

        return examples
