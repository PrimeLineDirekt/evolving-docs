"""Configuration for documentation generator."""
from pathlib import Path
from typing import Dict, List


class Config:
    """Configuration object for extractors."""
    def __init__(self, source_root: str = "/Users/neoforce/Buisiness/Evolving"):
        self.source_root = Path(source_root)


# Root directories
EVOLVING_ROOT = Path("/Users/neoforce/Buisiness/Evolving")
DOCS_ROOT = Path("/Users/neoforce/Buisiness/evolving-docs")

# Source directories in Evolving
SOURCE_DIRS = {
    "agents": EVOLVING_ROOT / ".claude" / "agents",
    "commands": EVOLVING_ROOT / ".claude" / "commands",
    "skills": EVOLVING_ROOT / ".claude" / "skills",
    "rules": EVOLVING_ROOT / ".claude" / "rules",
    "patterns": EVOLVING_ROOT / "knowledge" / "patterns",
    "templates": EVOLVING_ROOT / "knowledge" / "templates",
    "prompts": EVOLVING_ROOT / "knowledge" / "prompts",
    "blueprints": EVOLVING_ROOT / ".claude" / "blueprints",
    "hooks": EVOLVING_ROOT / ".claude" / "hooks",
}

# Output directories in evolving-docs
OUTPUT_DIRS = {
    "en": {
        "agents": DOCS_ROOT / "docs" / "en" / "components" / "agents",
        "commands": DOCS_ROOT / "docs" / "en" / "components" / "commands",
        "skills": DOCS_ROOT / "docs" / "en" / "components" / "skills",
        "rules": DOCS_ROOT / "docs" / "en" / "components" / "rules",
        "patterns": DOCS_ROOT / "docs" / "en" / "components" / "patterns",
        "templates": DOCS_ROOT / "docs" / "en" / "components" / "templates",
        "prompts": DOCS_ROOT / "docs" / "en" / "components" / "prompts",
        "blueprints": DOCS_ROOT / "docs" / "en" / "components" / "blueprints",
        "hooks": DOCS_ROOT / "docs" / "en" / "components" / "hooks",
    },
    "de": {
        "agents": DOCS_ROOT / "docs" / "de" / "components" / "agents",
        "commands": DOCS_ROOT / "docs" / "de" / "components" / "commands",
        "skills": DOCS_ROOT / "docs" / "de" / "components" / "skills",
        "rules": DOCS_ROOT / "docs" / "de" / "components" / "rules",
        "patterns": DOCS_ROOT / "docs" / "de" / "components" / "patterns",
        "templates": DOCS_ROOT / "docs" / "de" / "components" / "templates",
        "prompts": DOCS_ROOT / "docs" / "de" / "components" / "prompts",
        "blueprints": DOCS_ROOT / "docs" / "de" / "components" / "blueprints",
        "hooks": DOCS_ROOT / "docs" / "de" / "components" / "hooks",
    },
}

# Template directory
TEMPLATE_DIR = DOCS_ROOT / "templates"


def get_source_files(category: str) -> List[Path]:
    """Get all source files for a category."""
    source_dir = SOURCE_DIRS.get(category)
    if not source_dir or not source_dir.exists():
        return []

    # Get all markdown, Python, and shell files
    files = []
    if category in ["agents", "commands", "skills", "rules", "patterns", "templates", "prompts", "blueprints"]:
        files = list(source_dir.glob("*.md"))
    elif category == "hooks":
        files = list(source_dir.glob("*.py")) + list(source_dir.glob("*.sh"))

    return sorted(files)


def get_output_dir(category: str, language: str = "en") -> Path:
    """Get output directory for a category and language."""
    return OUTPUT_DIRS[language][category]
