from enum import Enum


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
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
