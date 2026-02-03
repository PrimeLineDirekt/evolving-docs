#!/usr/bin/env python3
"""Test script for new extractors."""

import sys
from pathlib import Path

# Add both directories to path
docs_gen_dir = Path(__file__).parent / "docs-generator"
sys.path.insert(0, str(docs_gen_dir))
sys.path.insert(0, str(docs_gen_dir.parent))

# Import directly from files to avoid __init__.py relative import issues
import importlib.util

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

skill_mod = load_module("skill", docs_gen_dir / "extractors" / "skill.py")
scenario_mod = load_module("scenario", docs_gen_dir / "extractors" / "scenario.py")
graphics_mod = load_module("graphics_tool", docs_gen_dir / "extractors" / "graphics_tool.py")
config_mod = load_module("config", docs_gen_dir / "config.py")

SkillExtractor = skill_mod.SkillExtractor
ScenarioExtractor = scenario_mod.ScenarioExtractor
GraphicsToolExtractor = graphics_mod.GraphicsToolExtractor
Config = config_mod.Config

def test_skill_extractor():
    """Test SkillExtractor."""
    print("\n=== Testing SkillExtractor ===")
    config = Config(source_root="/Users/neoforce/Buisiness/Evolving")
    extractor = SkillExtractor(config)

    skills = extractor.extract_all()
    print(f"✓ Found {len(skills)} skills")

    if skills:
        first_skill = skills[0]
        print(f"  Example: {first_skill['name']} - {first_skill.get('title', 'N/A')}")

def test_scenario_extractor():
    """Test ScenarioExtractor."""
    print("\n=== Testing ScenarioExtractor ===")
    config = Config(source_root="/Users/neoforce/Buisiness/Evolving")
    extractor = ScenarioExtractor(config)

    scenarios = extractor.extract_all()
    print(f"✓ Found {len(scenarios)} scenarios")

    if scenarios:
        first_scenario = scenarios[0]
        print(f"  Example: {first_scenario['name']} - {first_scenario.get('title', 'N/A')}")

def test_graphics_tool_extractor():
    """Test GraphicsToolExtractor."""
    print("\n=== Testing GraphicsToolExtractor ===")
    config = Config(source_root="/Users/neoforce/Buisiness/Evolving")
    extractor = GraphicsToolExtractor(config)

    tools = extractor.extract_all()
    print(f"✓ Found {len(tools)} graphics tools")

    if tools:
        first_tool = tools[0]
        print(f"  Example: {first_tool['name']} - {first_tool.get('title', 'N/A')}")

if __name__ == "__main__":
    print("Testing new extractors...")

    try:
        test_skill_extractor()
        test_scenario_extractor()
        test_graphics_tool_extractor()
        print("\n✓ All extractors working correctly!\n")
    except Exception as e:
        print(f"\n✗ Error: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)
