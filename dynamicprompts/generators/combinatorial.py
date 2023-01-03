from __future__ import annotations

import logging

from dynamicprompts.wildcardmanager import WildcardManager
from dynamicprompts import constants
from dynamicprompts.parser.combinatorial_generator import CombinatorialGenerator
from . import PromptGenerator

logger = logging.getLogger(__name__)


class CombinatorialPromptGenerator(PromptGenerator):
    def __init__(self, wildcard_manager: WildcardManager, template):
        self._wildcard_manager = wildcard_manager
        self._template = template
        self._generator = CombinatorialGenerator(wildcard_manager)

    def generate(self, max_prompts=constants.MAX_IMAGES) -> list[str]:
        if self._template is None or len(self._template) == 0:
            return [""]
        prompts = self._generator.generate_prompts(self._template, max_prompts)
        prompts = list(prompts)

        return prompts
