"""Hook extractor for Evolving documentation."""

from pathlib import Path
from typing import Any
import re


def extract(source_path: Path) -> dict[str, Any]:
    """
    Extract hook documentation from Python and Shell files.

    Args:
        source_path: Path to the hook file (.py or .sh)

    Returns:
        Dictionary with hook metadata for template rendering
    """
    content = source_path.read_text(encoding='utf-8')

    title = source_path.stem.replace('-', ' ').replace('_', ' ').title()
    description = "No description available"
    code_snippet = ""

    if source_path.suffix == '.py':
        # Extract module docstring
        docstring_match = re.search(
            r'^"""(.*?)"""',
            content,
            re.MULTILINE | re.DOTALL
        )
        if docstring_match:
            description = docstring_match.group(1).strip()
            # Clean up multi-line docstrings
            description = re.sub(r'\n\s+', ' ', description)

        # Extract first function/class as example
        code_match = re.search(
            r'((?:def|class)\s+\w+.*?(?:\n    .*?)*)',
            content,
            re.MULTILINE
        )
        if code_match:
            code_snippet = code_match.group(1).strip()

    elif source_path.suffix == '.sh':
        # Extract header comments after shebang
        lines = content.split('\n')
        comment_lines = []
        started = False

        for line in lines:
            if line.startswith('#!'):
                continue
            if line.startswith('#'):
                started = True
                # Remove leading # and whitespace
                comment_lines.append(line.lstrip('#').strip())
            elif started and line.strip():
                # Stop at first non-comment, non-empty line
                break

        if comment_lines:
            description = ' '.join(comment_lines)

        # Extract first meaningful function or logic block as example
        # Look for first function definition or significant logic
        function_match = re.search(
            r'((?:function\s+\w+|^\w+\(\))\s*{.*?^})',
            content,
            re.MULTILINE | re.DOTALL
        )
        if function_match:
            code_snippet = function_match.group(1).strip()
        else:
            # Fallback: get first 20 lines after comments
            non_comment_lines = [
                line for line in lines
                if not line.startswith('#') and line.strip()
            ]
            code_snippet = '\n'.join(non_comment_lines[:20])

    # Determine hook type from filename patterns
    hook_type = "general"
    if 'check' in source_path.stem:
        hook_type = "validation"
    elif 'enforce' in source_path.stem:
        hook_type = "enforcement"
    elif 'sync' in source_path.stem or 'update' in source_path.stem:
        hook_type = "synchronization"
    elif 'detect' in source_path.stem:
        hook_type = "detection"

    return {
        'type': 'hook',
        'title': title,
        'filename': source_path.name,
        'language': 'python' if source_path.suffix == '.py' else 'bash',
        'hook_type': hook_type,
        'description': description,
        'code_snippet': code_snippet,
        'source_path': str(source_path)
    }
