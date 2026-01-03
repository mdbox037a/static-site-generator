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

    def test_typical_mix(self):
        node1 = TextNode(
            "Here is a first sample `code goes here` sample continues", TextType.TEXT
        )
        node2 = TextNode(
            "Here is a second sample **bold goes here** sample continues", TextType.TEXT
        )
        old_nodes = [node1, node2]
        self.assertEqual(
            split_nodes_delimiter(old_nodes, "`", TextType.CODE),
            [
                TextNode("Here is a first sample ", TextType.TEXT),
                TextNode("code goes here", TextType.CODE),
                TextNode(" sample continues", TextType.TEXT),
                TextNode(
                    "Here is a second sample **bold goes here** sample continues",
                    TextType.TEXT,
                ),
            ],
        )

    def test_missing_delimiter(self):
        node = TextNode("Testing missing _italic delimiter", TextType.TEXT)
        old_nodes = [node]
        with self.assertRaises(ValueError) as context_manager:
            split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            str(context_manager.exception),
            "invalid markdown, formatted section not closed",
        )


if __name__ == "__main__":
    unittest.main()
