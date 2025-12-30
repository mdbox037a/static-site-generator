import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_empty(self):
        node = TextNode("This is a link node with no url", TextType.LINK)
        self.assertEqual(node.url, None)

    def test_eq_url_none(self):
        node1 = TextNode("This is a link node with no url", TextType.LINK)
        node2 = TextNode(
            "This is a link node with a url", TextType.LINK, "http://example.com"
        )
        self.assertNotEqual(node1, node2)

    def test_eq_type_diff(self):
        node1 = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
