from typing import Text
import unittest

from processmarkdown import split_nodes_delimiter
from textnode import TextNode, TextType


class TestProcessMarkdown(unittest.TestCase):
    def test_single_text(self):
        node = TextNode("test text node", TextType.TEXT)
        old_nodes = [node]
        self.assertEqual(split_nodes_delimiter(old_nodes, "/", TextType.TEXT), [node])

    def test_multiple_text(self):
        node1 = TextNode("test text node1", TextType.TEXT)
        node2 = TextNode("test text node2", TextType.TEXT)
        old_nodes = [node1, node2]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "/", TextType.TEXT), [node1, node2]
        )

    def test_single_code(self):
        node = TextNode("`test code block`", TextType.TEXT)
        old_nodes = [node]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "`", TextType.CODE),
            [TextNode("test code block", TextType.CODE)],
        )


if __name__ == "__main__":
    unittest.main()
