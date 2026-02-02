"""Content parsing utilities."""
import json
import re
from pathlib import Path
from typing import Dict, Tuple, Optional


def parse_markdown(file_path: Path) -> Tuple[Dict[str, str], str]:
    """
    Parse markdown file with optional YAML frontmatter.

    Returns:
        Tuple of (frontmatter_dict, body_string)
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        raise ValueError(f"Failed to read {file_path}: {e}")

    frontmatter = {}
    body = content

    # Check for YAML frontmatter (--- at start, --- to close)
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(frontmatter_pattern, content, re.DOTALL)

    if match:
        frontmatter_text = match.group(1)
        body = match.group(2)

        # Parse frontmatter as simple key: value pairs
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip()

    return frontmatter, body


def parse_json(file_path: Path) -> Dict:
    """
    Parse JSON file.

    Returns:
        Parsed JSON as dict
    """
    try:
        with file_path.open('r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f"Failed to parse JSON {file_path}: {e}")


def extract_code_metadata(file_path: Path) -> Dict[str, str]:
    """
    Extract metadata from Python or shell script files.

    Returns:
        Dict with 'docstring', 'shebang', and 'description'
    """
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        raise ValueError(f"Failed to read {file_path}: {e}")

    metadata = {
        "docstring": "",
        "shebang": "",
        "description": "",
    }

    lines = content.split('\n')

    # Extract shebang if present
    if lines and lines[0].startswith('#!'):
        metadata["shebang"] = lines[0]

    # Extract docstring (Python triple-quote or shell comments)
    if file_path.suffix == '.py':
        # Look for triple-quoted docstring
        docstring_pattern = r'"""(.*?)"""'
        match = re.search(docstring_pattern, content, re.DOTALL)
        if match:
            metadata["docstring"] = match.group(1).strip()
            metadata["description"] = metadata["docstring"].split('\n')[0]

    elif file_path.suffix == '.sh':
        # Extract comment block at top
        comment_lines = []
        for line in lines[1:] if metadata["shebang"] else lines:
            if line.strip().startswith('#'):
                comment_lines.append(line.strip().lstrip('#').strip())
            elif line.strip():
                break

        if comment_lines:
            metadata["description"] = comment_lines[0]
            metadata["docstring"] = '\n'.join(comment_lines)

    return metadata


def extract_markdown_title(body: str) -> Optional[str]:
    """Extract first H1 title from markdown body."""
    match = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
    return match.group(1) if match else None


def extract_markdown_sections(body: str) -> Dict[str, str]:
    """
    Extract sections from markdown body.

    Returns dict mapping section titles to their content.
    """
    sections = {}
    current_section = None
    current_content = []

    for line in body.split('\n'):
        # Check for H2 headers
        match = re.match(r'^##\s+(.+)$', line)
        if match:
            # Save previous section
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()

            # Start new section
            current_section = match.group(1)
            current_content = []
        elif current_section:
            current_content.append(line)

    # Save last section
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()

    return sections
