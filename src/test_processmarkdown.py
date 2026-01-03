from typing import Text
import unittest

from processmarkdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)
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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "sample 1 ![image1](test1.com) and sample 2 ![image2](test2.com)"
        )
        self.assertListEqual(
            [("image1", "test1.com"), ("image2", "test2.com")], matches
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("Sample text with [link](www.example.com)")
        self.assertListEqual([("link", "www.example.com")], matches)

    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "sample 1 [link1](test1.com) and sample 2 [link2](test2.com)"
        )
        self.assertListEqual([("link1", "test1.com"), ("link2", "test2.com")], matches)

    def test_extract_mixed_markdown(self):
        matches = extract_markdown_links(
            "sample 1 [link](test1.com) and sample 2 ![image](test2.com)"
        )
        self.assertListEqual([("link", "test1.com")], matches)


if __name__ == "__main__":
    unittest.main()
