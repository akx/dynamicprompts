from __future__ import annotations

from dynamicprompts.generators.promptgenerator import PromptGenerator


class DummyGenerator(PromptGenerator):
    """A dummy generator that returns the template as-is."""

    def generate(
        self,
        template: str,
        num_images: int = 1,
    ) -> list[str]:
        """Return the template as-is, multiple times."""
        return num_images * [template]
