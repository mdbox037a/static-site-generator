import re
from textnode import TextType, TextNode


def split_nodes_delimiter(
    old_nodes: list[TextNode],
    delimiter: str,
    text_type: TextType,
) -> list[TextNode]:
    """
    Return new_node: a TextType.TEXT node, potentially split into TEXT, BOLD,
    ITALIC, and CODE nodes as dictated by **, _, and ` delimiter
    """
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        pieces = old_node.text.split(delimiter)
        if len(pieces) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        else:
            for index, piece in enumerate(pieces):
                if index % 2 == 0 and piece != "":
                    new_nodes.append(TextNode(piece, TextType.TEXT))
                elif index % 2 != 0 and piece != "":
                    new_nodes.append((TextNode(piece, text_type)))
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    """
    Return a list of tuples containing the alt text and URL of any detected
    markdown image strings
    """
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    """
    Return a list of tuples containing the anchor text and URL of any detected
    markdown link strings
    """
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    """Return a list of text and image TextNodes; parse nodes in old_nodes for image strings"""

    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.IMAGE or old_node.text_type == TextType.LINK:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        next_temp = old_node.text
        if images:
            for image in images:
                sections = next_temp.split(f"![{image[0]}]({image[1]})", 1)
                text_temp = sections[0]
                next_temp = sections[1] if sections[1] else ""
                if text_temp != "":
                    new_nodes.append(TextNode(text_temp, TextType.TEXT))
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            if next_temp != "":
                new_nodes.append(TextNode(next_temp, TextType.TEXT))
        else:
            new_nodes.append(old_node)
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    """Return a list of text and link TextNodes; parse nodes in old_nodes for link strings"""
    pass
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.IMAGE or old_node.text_type == TextType.LINK:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        next_temp = old_node.text
        if links:
            for link in links:
                sections = next_temp.split(f"[{link[0]}]({link[1]})", 1)
                text_temp = sections[0]
                next_temp = sections[1] if sections[1] else ""
                if text_temp != "":
                    new_nodes.append(TextNode(text_temp, TextType.TEXT))
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            if next_temp != "":
                new_nodes.append(TextNode(next_temp, TextType.TEXT))
        else:
            new_nodes.append(old_node)
    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    """
    Return a list of TextNodes that is a combination of all TextType splitters
    above for complete node representation of a string of markdown
    """
    combined_nodes = [TextNode(text, TextType.TEXT)]
    delimiters = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}
    for d in delimiters:
        combined_nodes = split_nodes_delimiter(combined_nodes, d, delimiters[d])
    combined_nodes = split_nodes_image(combined_nodes)
    combined_nodes = split_nodes_link(combined_nodes)
    return combined_nodes


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
