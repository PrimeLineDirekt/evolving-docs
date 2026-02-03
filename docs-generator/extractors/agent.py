"""Agent extractor for parsing Claude Code agent definitions."""

from pathlib import Path
from typing import Dict, Any, List
from parser import parse_markdown_file
from config import Config


class AgentExtractor:
    """Extract agent documentation from markdown files with YAML frontmatter."""

    def __init__(self, config: Config):
        self.config = config
        self.source_dir = Path(config.source_root) / ".claude" / "agents"

    def extract_all(self) -> List[Dict[str, Any]]:
        """Extract all agents from source directory."""
        agents = []

        if not self.source_dir.exists():
            return agents

        for agent_file in self.source_dir.glob("*.md"):
            try:
                agent_data = self.extract_one(agent_file)
                if agent_data:
                    agents.append(agent_data)
            except Exception as e:
                print(f"Error extracting agent {agent_file}: {e}")

        return agents

    def extract_one(self, file_path: Path) -> Dict[str, Any]:
        """Extract a single agent's documentation."""
        frontmatter, content = parse_markdown_file(file_path)

        # Extract name from filename
        name = file_path.stem

        # Build context dict matching template requirements
        context = {
            # Basic metadata
            'name': name,
            'slug': file_path.stem,  # filename without extension
            'type': 'agent',
            'tags': frontmatter.get('tags', []),
            'lang': 'en',  # Default language
            'confidence': 100,  # Default confidence level

            # Core fields
            'description': frontmatter.get('description', ''),
            'purpose': self._extract_purpose(content),

            # Agent-specific fields
            'complexity': frontmatter.get('complexity', 'medium'),
            'model': frontmatter.get('model', 'claude-sonnet-4-5'),
            'category': frontmatter.get('domain', 'general'),
            'created': frontmatter.get('created', ''),

            # Feature lists
            'key_features': self._extract_kernkompetenzen(content),
            'enables': self._extract_enables(content),
            'integrates_with': self._extract_integrations(content),

            # Best practices
            'dos': self._extract_dos(content),
            'donts': self._extract_donts(content),
            'tips': self._extract_tips(content),

            # Examples
            'examples': self._extract_examples(content),

            # Source reference
            'source_file': str(file_path.relative_to(self.config.source_root))
        }

        return context

    def _extract_purpose(self, content: str) -> str:
        """Extract purpose/summary from content."""
        # Look for first paragraph after title
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith('#'):
                return line.strip()
        return ''

    def _extract_kernkompetenzen(self, content: str) -> List[str]:
        """Extract core competencies from ## Kernkompetenzen section."""
        return self._extract_list_from_section(content, 'Kernkompetenzen')

    def _extract_dos(self, content: str) -> List[str]:
        """Extract DO items from ### Do section."""
        return self._extract_list_from_section(content, 'Do')

    def _extract_donts(self, content: str) -> List[str]:
        """Extract DON'T items from ### Don't section."""
        return self._extract_list_from_section(content, "Don't")

    def _extract_tips(self, content: str) -> List[str]:
        """Extract tips from various sections."""
        tips = []
        tips.extend(self._extract_list_from_section(content, 'Tipps'))
        tips.extend(self._extract_list_from_section(content, 'Best Practices'))
        return tips

    def _extract_enables(self, content: str) -> List[str]:
        """Extract what this agent enables/provides."""
        enables = []
        enables.extend(self._extract_list_from_section(content, 'Enables'))
        enables.extend(self._extract_list_from_section(content, 'Provides'))
        return enables

    def _extract_integrations(self, content: str) -> List[str]:
        """Extract integration points."""
        return self._extract_list_from_section(content, 'Integrates with')

    def _extract_list_from_section(self, content: str, section_name: str) -> List[str]:
        """Extract bullet list items from a named section."""
        items = []
        in_section = False

        for line in content.split('\n'):
            # Check if we entered the target section
            if f'## {section_name}' in line or f'### {section_name}' in line:
                in_section = True
                continue

            # Check if we exited to another section
            if in_section and line.startswith('#'):
                break

            # Extract list items
            if in_section:
                stripped = line.strip()
                if stripped.startswith('-') or stripped.startswith('*'):
                    # Remove list marker and clean
                    item = stripped.lstrip('-*').strip()
                    if item:
                        items.append(item)

        return items

    def _extract_examples(self, content: str) -> List[Dict[str, str]]:
        """Extract code examples from content."""
        examples = []
        in_example = False
        current_example = None
        code_lines = []
        code_lang = ''

        for line in content.split('\n'):
            # Detect example section start
            if '## Beispiel' in line or '### Beispiel' in line or '## Example' in line:
                in_example = True
                if current_example:
                    # Save previous example
                    if code_lines:
                        current_example['code'] = '\n'.join(code_lines)
                        current_example['code_lang'] = code_lang
                    examples.append(current_example)

                # Start new example
                current_example = {'title': line.strip('#').strip()}
                code_lines = []
                code_lang = ''
                continue

            # Detect code block
            if in_example and line.startswith('```'):
                if not code_lines:
                    # Start of code block
                    code_lang = line.strip('`').strip() or 'text'
                else:
                    # End of code block
                    if current_example:
                        current_example['code'] = '\n'.join(code_lines)
                        current_example['code_lang'] = code_lang
                        examples.append(current_example)
                    current_example = None
                    code_lines = []
                    in_example = False
                continue

            # Collect code lines
            if in_example and code_lines is not None:
                code_lines.append(line)

        # Save last example if exists
        if current_example and code_lines:
            current_example['code'] = '\n'.join(code_lines)
            current_example['code_lang'] = code_lang
            examples.append(current_example)

        return examples
