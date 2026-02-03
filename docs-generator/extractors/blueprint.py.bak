"""Blueprint extractor for Evolving documentation."""

from pathlib import Path
from typing import Any
import json


def extract(source_path: Path) -> dict[str, Any]:
    """
    Extract blueprint documentation from JSON files.

    Args:
        source_path: Path to the blueprint JSON file

    Returns:
        Dictionary with blueprint metadata for template rendering
    """
    with open(source_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract basic metadata
    name = data.get('name', source_path.stem)
    description = data.get('description', 'No description available')
    blueprint_type = data.get('type', 'general')
    category = data.get('category', 'uncategorized')

    # Extract agents and their roles
    agents = data.get('agents', [])
    agent_list = []
    for agent in agents:
        if isinstance(agent, dict):
            agent_list.append({
                'name': agent.get('name', 'Unknown'),
                'role': agent.get('role', 'N/A')
            })
        else:
            # If agents is just a list of strings
            agent_list.append({
                'name': str(agent),
                'role': 'Agent'
            })

    # Key features are derived from agent roles
    key_features = [agent['role'] for agent in agent_list if agent['role'] != 'N/A']

    # Extract workflow/phases if available
    workflow = data.get('workflow', [])
    phases = data.get('phases', [])

    # Combine workflow and phases for structured overview
    structure = []
    if workflow:
        structure.extend([{'type': 'workflow', 'content': w} for w in workflow])
    if phases:
        structure.extend([{'type': 'phase', 'content': p} for p in phases])

    # Extract use cases or examples
    use_cases = data.get('use_cases', [])
    examples = data.get('examples', [])

    return {
        'type': 'blueprint',
        'title': name,
        'filename': source_path.name,
        'description': description,
        'blueprint_type': blueprint_type,
        'category': category,
        'agents': agent_list,
        'agent_count': len(agent_list),
        'key_features': key_features,
        'structure': structure,
        'use_cases': use_cases,
        'examples': examples,
        'raw_data': data,  # Include full data for advanced templates
        'source_path': str(source_path)
    }
