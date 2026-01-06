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
