"""Template rendering utilities using Jinja2."""
from pathlib import Path
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader, Template, TemplateNotFound

try:
    from .config import TEMPLATE_DIR
except ImportError:
    from config import TEMPLATE_DIR


class Renderer:
    """Jinja2 template renderer."""

    def __init__(self, template_dir: Path = TEMPLATE_DIR):
        """Initialize renderer with template directory."""
        self.template_dir = template_dir

        if not template_dir.exists():
            raise ValueError(f"Template directory not found: {template_dir}")

        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render_component(self, template_name: str, context: Dict[str, Any]) -> str:
        """
        Render a component using a template.

        Args:
            template_name: Name of template file (e.g., 'agent.md.j2')
            context: Dict of variables to pass to template

        Returns:
            Rendered markdown string
        """
        try:
            template = self.env.get_template(template_name)
            return template.render(**context)
        except TemplateNotFound:
            raise ValueError(f"Template not found: {template_name}")
        except Exception as e:
            raise ValueError(f"Failed to render template {template_name}: {e}")

    def render_string(self, template_string: str, context: Dict[str, Any]) -> str:
        """
        Render a string template.

        Args:
            template_string: Template string with Jinja2 syntax
            context: Dict of variables to pass to template

        Returns:
            Rendered string
        """
        try:
            template = self.env.from_string(template_string)
            return template.render(**context)
        except Exception as e:
            raise ValueError(f"Failed to render string template: {e}")

    def list_templates(self) -> list[str]:
        """List all available templates."""
        return self.env.list_templates()


# Convenience function for one-off rendering
def render_component(template_name: str, context: Dict[str, Any]) -> str:
    """Render a component using default renderer."""
    renderer = Renderer()
    return renderer.render_component(template_name, context)
