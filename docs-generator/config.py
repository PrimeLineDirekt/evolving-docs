"""Configuration for documentation generator."""
import os
from pathlib import Path
from typing import Dict, List

# Local development fallbacks
_DEFAULT_EVOLVING = "/Users/neoforce/Buisiness/Evolving"
_DEFAULT_DOCS = str(Path(__file__).parent.parent)  # repo root

# Root directories - configurable via env vars or set_roots()
EVOLVING_ROOT = Path(os.environ.get("EVOLVING_ROOT", _DEFAULT_EVOLVING))
DOCS_ROOT = Path(os.environ.get("DOCS_ROOT", _DEFAULT_DOCS))


def set_roots(source: str = None, output: str = None):
    """Override root directories (called from CLI args)."""
    global EVOLVING_ROOT, DOCS_ROOT, SOURCE_DIRS, OUTPUT_DIRS, TEMPLATE_DIR
    if source:
        EVOLVING_ROOT = Path(source)
    if output:
        DOCS_ROOT = Path(output)
    # Rebuild derived paths
    SOURCE_DIRS.update(_build_source_dirs(EVOLVING_ROOT))
    OUTPUT_DIRS.update(_build_output_dirs(DOCS_ROOT))
    TEMPLATE_DIR = DOCS_ROOT / "templates"


class Config:
    """Configuration object for extractors."""
    def __init__(self, source_root: str = None):
        self.source_root = Path(source_root) if source_root else EVOLVING_ROOT


def _build_source_dirs(root: Path) -> Dict[str, Path]:
    return {
        "agents": root / ".claude" / "agents",
        "commands": root / ".claude" / "commands",
        "skills": root / ".claude" / "skills",
        "rules": root / ".claude" / "rules",
        "patterns": root / "knowledge" / "patterns",
        "templates": root / "knowledge" / "templates",
        "prompts": root / "knowledge" / "prompts",
        "blueprints": root / ".claude" / "blueprints",
        "hooks": root / ".claude" / "hooks",
    }


def _build_output_dirs(root: Path) -> Dict[str, Dict[str, Path]]:
    result = {}
    for lang in ("en", "de"):
        result[lang] = {}
        for category in ("agents", "commands", "skills", "rules", "patterns", "templates", "prompts", "blueprints", "hooks"):
            result[lang][category] = root / "docs" / lang / "components" / category
    return result


# Source directories in Evolving
SOURCE_DIRS = _build_source_dirs(EVOLVING_ROOT)

# Output directories in evolving-docs
OUTPUT_DIRS = _build_output_dirs(DOCS_ROOT)

# Template directory
TEMPLATE_DIR = DOCS_ROOT / "templates"


def get_source_files(category: str) -> List[Path]:
    """Get all source files for a category."""
    source_dir = SOURCE_DIRS.get(category)
    if not source_dir or not source_dir.exists():
        return []

    files = []
    if category in ["agents", "commands", "skills", "rules", "patterns", "templates", "prompts", "blueprints"]:
        files = list(source_dir.glob("*.md"))
    elif category == "hooks":
        files = list(source_dir.glob("*.py")) + list(source_dir.glob("*.sh"))

    return sorted(files)


def get_output_dir(category: str, language: str = "en") -> Path:
    """Get output directory for a category and language."""
    return OUTPUT_DIRS[language][category]
