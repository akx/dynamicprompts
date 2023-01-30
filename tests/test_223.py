from pprint import pprint

from dynamicprompts.commands import SequenceCommand
from dynamicprompts.parser.parse import parse
from dynamicprompts.parser.random_generator import RandomGenerator
from dynamicprompts.wildcardmanager import WildcardManager


def test_223_part_2(wildcard_manager: WildcardManager):
    prompt = """
prefix,
({0$$a|b} {1$$c|d|e}),
suffix
    """.strip()
    parsed = parse(prompt)
    pprint(parsed, width=120)  # noqa: T203
    assert isinstance(parsed, SequenceCommand)
    rg = RandomGenerator(wildcard_manager=wildcard_manager, ignore_whitespace=True)
    list(rg.generate_prompts(parsed, 1))
