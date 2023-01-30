from dynamicprompts.parser.parse import Parser
from dynamicprompts.parser.random_generator import RandomActionBuilder
from dynamicprompts.wildcardmanager import WildcardManager


def test_223_part_2(wildcard_manager: WildcardManager):
    prompt = """
prefix,
({0$$a|b} {1$$c|d|e}),
suffix
    """.strip()
    parsed = Parser(builder=RandomActionBuilder(wildcard_manager=wildcard_manager)).parse(prompt)
    assert parsed.prompts() == 8
