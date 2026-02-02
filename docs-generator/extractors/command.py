"""Command extractor for parsing Claude Code slash commands."""

from pathlib import Path
from typing import Dict, Any, List
from ..parser import parse_markdown_file
from ..config import Config


class CommandExtractor:
    """Extract command documentation from markdown files with YAML frontmatter."""

    def __init__(self, config: Config):
        self.config = config
        self.source_dir = Path(config.source_root) / ".claude" / "commands"

    def extract_all(self) -> List[Dict[str, Any]]:
        """Extract all commands from source directory."""
        commands = []

        if not self.source_dir.exists():
            return commands

        for cmd_file in self.source_dir.glob("*.md"):
            try:
                cmd_data = self.extract_one(cmd_file)
                if cmd_data:
                    commands.append(cmd_data)
            except Exception as e:
                print(f"Error extracting command {cmd_file}: {e}")

        return commands

    def extract_one(self, file_path: Path) -> Dict[str, Any]:
        """Extract a single command's documentation."""
        frontmatter, content = parse_markdown_file(file_path)

        # Extract name from filename (add slash prefix)
        name = f"/{file_path.stem}"

        # Build context dict matching template requirements
        context = {
            # Basic metadata
            'name': name,
            'type': 'command',
            'tags': frontmatter.get('tags', []),
            'lang': 'en',

            # Core fields
            'description': frontmatter.get('description', ''),
            'purpose': self._extract_purpose(content),

            # Command-specific fields
            'complexity': self._infer_complexity(frontmatter, content),
            'model': frontmatter.get('model', 'claude-sonnet-4-5'),
            'category': self._infer_category(content, name),
            'created': frontmatter.get('created', ''),

            # Usage info
            'argument_hint': frontmatter.get('argument-hint', ''),

            # Feature lists
            'key_features': self._extract_key_features(content),
            'enables': self._extract_enables(content),
            'integrates_with': self._extract_integrations(content),

            # Best practices
            'dos': self._extract_dos(content),
            'donts': self._extract_donts(content),
            'tips': self._extract_tips(content),

            # Examples
            'examples': self._extract_examples(content, name),

            # Source reference
            'source_file': str(file_path.relative_to(self.config.source_root))
        }

        return context

    def _extract_purpose(self, content: str) -> str:
        """Extract purpose from content."""
        lines = content.split('\n')
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                return stripped
        return ''

    def _infer_complexity(self, frontmatter: Dict, content: str) -> str:
        """Infer complexity from frontmatter or content."""
        if 'complexity' in frontmatter:
            return frontmatter['complexity']

        # Simple heuristic: length and structure
        word_count = len(content.split())
        if word_count < 200:
            return 'low'
        elif word_count < 500:
            return 'medium'
        else:
            return 'high'

    def _infer_category(self, content: str, name: str) -> str:
        """Infer category from content and name."""
        content_lower = content.lower()
        name_lower = name.lower()

        # Category keywords
        categories = {
            'memory': ['memory', 'experience', 'learning'],
            'workflow': ['workflow', 'plan', 'task', 'todo'],
            'analysis': ['analyze', 'review', 'audit', 'explore'],
            'creation': ['create', 'generate', 'new'],
            'documentation': ['doc', 'documentation', 'handoff'],
            'debugging': ['debug', 'error', 'fix'],
        }

        for category, keywords in categories.items():
            if any(kw in name_lower or kw in content_lower for kw in keywords):
                return category

        return 'general'

    def _extract_key_features(self, content: str) -> List[str]:
        """Extract key features from various sections."""
        features = []
        features.extend(self._extract_list_from_section(content, 'Features'))
        features.extend(self._extract_list_from_section(content, 'Key Features'))
        features.extend(self._extract_list_from_section(content, 'Capabilities'))
        return features

    def _extract_enables(self, content: str) -> List[str]:
        """Extract what this command enables."""
        enables = []
        enables.extend(self._extract_list_from_section(content, 'Enables'))
        enables.extend(self._extract_list_from_section(content, 'Use Cases'))
        return enables

    def _extract_integrations(self, content: str) -> List[str]:
        """Extract integration points."""
        return self._extract_list_from_section(content, 'Integrates with')

    def _extract_dos(self, content: str) -> List[str]:
        """Extract DO items."""
        return self._extract_list_from_section(content, 'Do')

    def _extract_donts(self, content: str) -> List[str]:
        """Extract DON'T items."""
        donts = []
        donts.extend(self._extract_list_from_section(content, "Don't"))
        donts.extend(self._extract_list_from_section(content, "Avoid"))
        return donts

    def _extract_tips(self, content: str) -> List[str]:
        """Extract tips."""
        tips = []
        tips.extend(self._extract_list_from_section(content, 'Tips'))
        tips.extend(self._extract_list_from_section(content, 'Best Practices'))
        tips.extend(self._extract_list_from_section(content, 'Notes'))
        return tips

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
                    item = stripped.lstrip('-*').strip()
                    if item:
                        items.append(item)

        return items

    def _extract_examples(self, content: str, cmd_name: str) -> List[Dict[str, str]]:
        """Extract usage examples from content."""
        examples = []
        in_example = False
        current_example = None
        code_lines = []
        code_lang = ''

        for line in content.split('\n'):
            # Detect example section
            if any(marker in line for marker in ['## Example', '### Example', '## Usage', '### Usage']):
                in_example = True
                if current_example and code_lines:
                    current_example['code'] = '\n'.join(code_lines)
                    current_example['code_lang'] = code_lang
                    examples.append(current_example)

                current_example = {'title': line.strip('#').strip()}
                code_lines = []
                code_lang = ''
                continue

            # Detect code block
            if line.startswith('```'):
                if not code_lines:
                    # Start of code block
                    code_lang = line.strip('`').strip() or 'bash'
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

        # Save last example
        if current_example and code_lines:
            current_example['code'] = '\n'.join(code_lines)
            current_example['code_lang'] = code_lang
            examples.append(current_example)

        # If no examples found, create a basic one
        if not examples:
            examples.append({
                'title': 'Basic Usage',
                'code': cmd_name,
                'code_lang': 'bash'
            })

        return examples
