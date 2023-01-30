from __future__ import annotations

import logging

from dynamicprompts import constants
from dynamicprompts.generators.promptgenerator import PromptGenerator

logger = logging.getLogger(__name__)


class BatchedCombinatorialPromptGenerator(PromptGenerator):
    """Calls the wrapped generator multiple times to generate more prompts."""
    def __init__(self, generator: PromptGenerator, batches: int = 1) -> None:
        self._generator = generator
        self._batches = batches

    def generate(
        self,
        template: str,
        max_prompts: int = constants.MAX_IMAGES,
    ) -> list[str]:
        """Generate prompts by calling the wrapped generator multiple times."""
        images = []

        for _ in range(self._batches):
            images.extend(self._generator.generate(template, max_prompts))
        return images
