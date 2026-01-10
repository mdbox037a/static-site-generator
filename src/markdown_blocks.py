from enum import Enum
import re
from htmlnode import HTMLNode, ParentNode
from processmarkdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


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


def markdown_to_html_node(markdown: str) -> HTMLNode:
    """
    Accept a full markdown document and return a single parent HTMLNode containing
    all HTMLNode children representing its nested elements
    """
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        btype = block_to_block_type(block)
        match btype:
            case BlockType.PARAGRAPH:
                clean_block = " ".join(block.splitlines())
                child_hnodes = text_to_children(clean_block)
                block_parent_hnode = ParentNode("p", child_hnodes)
                children.append(block_parent_hnode)
            case BlockType.CODE:
                inner_text = remove_codeblock_backticks(block)
                tnode = TextNode(inner_text, TextType.CODE)
                code_hnode = text_node_to_html_node(tnode)
                pre_node = ParentNode("pre", [code_hnode])
                children.append(pre_node)
            # insert further cases here
    div_parent_hnode = ParentNode("div", children)
    return div_parent_hnode


def text_to_children(block: str) -> list[HTMLNode]:
    """Accept a text block string and return a list of HTMLNodes that represent inline markdown children"""
    child_hnodes = []
    tnodes = text_to_textnodes(block)
    for tnode in tnodes:
        child_hnodes.append(text_node_to_html_node(tnode))
    return child_hnodes


def remove_codeblock_backticks(codeblock: str) -> str:
    """Take multi-line codeblock and return it without the leading and trailing backticks"""
    lines = codeblock.splitlines()
    inner_lines = lines[1:-1]
    return "\n".join(inner_lines) + "\n"
