from __future__ import annotations
from enum import Enum


class TextType(Enum):
    PLAIN = "plain: text"
    BOLD = "bold: **Bold text**"
    ITALIC = "italic: _Italic text_"
    CODE = "code: `code text`"
    LINK = "link: [anchor text](url)"
    IMAGE = "image: ![alt text](url)"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: TextNode) -> bool:
        if not isinstance(other, TextNode):
            return False

        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
