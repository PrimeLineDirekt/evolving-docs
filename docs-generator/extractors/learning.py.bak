"""Learning Extractor - extracts documentation from knowledge/learnings/*.md"""

import re
from pathlib import Path
from typing import Dict, Any, Optional
import yaml


class LearningExtractor:
    """Extracts learning documentation from markdown files"""

    def __init__(self, evolving_root: Path):
        self.learnings_dir = evolving_root / "knowledge" / "learnings"

    def extract_all(self) -> list[Dict[str, Any]]:
        """Extract all learnings"""
        learnings = []

        if not self.learnings_dir.exists():
            return learnings

        for md_file in self.learnings_dir.glob("*.md"):
            if md_file.name.startswith("_"):
                continue

            learning = self._extract_learning(md_file)
            if learning:
                learnings.append(learning)

        return learnings

    def _extract_learning(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Extract learning from a single file"""
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

            # Build learning data
            learning = {
                "name": name,
                "type": "learning",
                "tags": frontmatter.get("tags", []) if frontmatter else [],
                "lang": frontmatter.get("lang", "en") if frontmatter else "en",
                "description": frontmatter.get("description", "") if frontmatter else "",
                "purpose": self._extract_purpose(content, frontmatter),
                "key_features": self._extract_key_points(content),
                "examples": self._extract_examples(content),
                "source_file": self._get_source_file(frontmatter, file_path),
                # Learning-specific fields
                "confidence": frontmatter.get("confidence") if frontmatter else None,
                "learning_type": frontmatter.get("type") if frontmatter else None,
                "date": frontmatter.get("date") if frontmatter else None,
            }

            return learning

        except Exception as e:
            print(f"Error extracting learning from {file_path}: {e}")
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

    def _extract_purpose(self, content: str, frontmatter: Optional[Dict]) -> str:
        """Extract purpose/context of the learning"""
        if frontmatter and "purpose" in frontmatter:
            return frontmatter["purpose"]

        # Look for context/why section
        pattern = r'##\s+(?:Context|Why|Purpose)\s*\n(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

        if match:
            return match.group(1).strip()[:300]  # First 300 chars

        return ""

    def _extract_key_points(self, content: str) -> list[str]:
        """Extract key learning points"""
        points = []

        # Look for common learning sections
        sections = [
            "What We Learned", "Key Takeaways", "Lessons",
            "Insights", "Findings"
        ]

        for section in sections:
            pattern = rf'##\s+{section}\s*\n(.*?)(?=\n##|\Z)'
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

            if match:
                section_content = match.group(1).strip()
                # Extract bullet points
                bullets = re.findall(r'^\s*[-*]\s+(.+)$', section_content, re.MULTILINE)
                points.extend(bullets[:3])

        return points[:5]  # Limit to 5 total

    def _extract_examples(self, content: str) -> list[str]:
        """Extract example sections or code blocks"""
        examples = []

        # Look for example/solution sections
        patterns = [
            r'##\s+(?:Example|Solution|Implementation)\s*\n(.*?)(?=\n##|\Z)',
            r'```[^\n]*\n(.*?)```'
        ]

        for pattern in patterns:
            matches = re.finditer(pattern, content, re.DOTALL | re.IGNORECASE)
            for match in matches:
                example = match.group(1).strip()
                if example and len(example) < 500:
                    examples.append(example)
                if len(examples) >= 3:
                    break

        return examples

    def _get_source_file(self, frontmatter: Optional[Dict], file_path: Path) -> str:
        """Get source file reference"""
        # Check frontmatter for Source field (common in learnings)
        if frontmatter and "source" in frontmatter:
            return frontmatter["source"]

        # Fall back to relative path
        return str(file_path.relative_to(file_path.parents[3]))
