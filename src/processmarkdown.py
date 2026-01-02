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
        elif (old_node.text.count(delimiter) % 2) != 0:
            raise Exception(
                f"Error: Invalid markdown - odd number of delimiter '{delimiter}' in node text"
            )
        else:
            pieces = old_node.text.split(delimiter)
            for index, piece in enumerate(pieces):
                if index % 2 == 0 and piece != "":
                    new_nodes.append(TextNode(piece, TextType.TEXT))
                elif index % 2 != 0 and piece != "":
                    new_nodes.append((TextNode(piece, text_type)))
    return new_nodes
