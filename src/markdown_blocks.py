from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading with 1-6 leading # and a ' '"
    CODE = "code with surrounding ```"
    QUOTE = "quote with leading >"
    UNORDERED_LIST = "list with - bullets"
    ORDERED_LIST = "list with <number>. bullets"


def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Take a raw markdown string representing a full md document and return a list
    of strings, each representing one block of markdown text
    """
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks]
    for block in blocks:
        if len(block) == 0:
            blocks.remove(block)
    return blocks


def block_to_block_type(block: str) -> BlockType:
    """Accept a single block of markdown text and return its markdown BlockType"""
    if re.match(r"^#{1-6} ", block):
        return BlockType.HEADING
    elif re.match(r"^`{3}.*`{3}$", block, re.DOTALL):
        return BlockType.CODE
