"""Abstract base class for component extractors."""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

from .config import get_source_files


class BaseExtractor(ABC):
    """
    Abstract base class for extracting metadata from Evolving components.

    Subclasses must implement:
    - get_source_files(): Return list of files to process
    - extract_metadata(source_file): Extract metadata from a single file
    """

    def __init__(self, category: str):
        """
        Initialize extractor for a component category.

        Args:
            category: Component category (e.g., 'agents', 'commands', 'rules')
        """
        self.category = category

    @abstractmethod
    def get_source_files(self) -> List[Path]:
        """
        Get list of source files to process for this category.

        Returns:
            List of Path objects
        """
        pass

    @abstractmethod
    def extract_metadata(self, source_file: Path) -> Dict[str, Any]:
        """
        Extract metadata from a single source file.

        Args:
            source_file: Path to source file

        Returns:
            Dict with component metadata
        """
        pass

    def enrich_metadata(self, metadata: Dict[str, Any], source_file: Path) -> Dict[str, Any]:
        """
        Add common metadata fields to extracted data.

        Args:
            metadata: Metadata dict from extract_metadata()
            source_file: Original source file path

        Returns:
            Enriched metadata dict
        """
        enriched = metadata.copy()

        # Add common fields
        enriched.setdefault("category", self.category)
        enriched.setdefault("source_file", str(source_file))
        enriched.setdefault("filename", source_file.name)
        enriched.setdefault("name", source_file.stem)

        # Add timestamps if file exists
        if source_file.exists():
            stat = source_file.stat()
            enriched.setdefault("modified_date", datetime.fromtimestamp(stat.st_mtime).isoformat())
            enriched.setdefault("created_date", datetime.fromtimestamp(stat.st_ctime).isoformat())

        # Ensure required fields have defaults
        enriched.setdefault("title", enriched.get("name", "Untitled"))
        enriched.setdefault("description", "")
        enriched.setdefault("tags", [])

        return enriched

    def extract_all(self) -> List[Dict[str, Any]]:
        """
        Extract metadata from all source files.

        Returns:
            List of metadata dicts for all components
        """
        results = []

        for source_file in self.get_source_files():
            try:
                metadata = self.extract_metadata(source_file)
                enriched = self.enrich_metadata(metadata, source_file)
                results.append(enriched)
            except Exception as e:
                print(f"Warning: Failed to extract {source_file}: {e}")
                continue

        return results

    def extract_one(self, source_file: Path) -> Dict[str, Any]:
        """
        Extract metadata from a single file.

        Args:
            source_file: Path to source file

        Returns:
            Enriched metadata dict
        """
        metadata = self.extract_metadata(source_file)
        return self.enrich_metadata(metadata, source_file)
