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
