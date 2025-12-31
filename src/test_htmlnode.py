import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_tags(self):
        node = HTMLNode("p", "sample text")
        node2 = HTMLNode("h1", "sample text")
        self.assertNotEqual(node.tag, node2.tag)

    def test_text(self):
        node = HTMLNode("p", "sample text")
        node2 = HTMLNode("h1", "sample text")
        self.assertEqual(node.value, node2.value)

    def test_props(self):
        node = HTMLNode(None, None, None, {"key1": "value1", "key2": "value2"})
        self.assertEqual(node.props_to_html(), ' key1="value1" key2="value2"')


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.example.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.example.com">Click me!</a>'
        )

    def test_leaf_to_html_aa(self):
        node = LeafNode(
            "a", "Click me!", {"href": "https://www.example.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.example.com" target="_blank">Click me!</a>',
        )


if __name__ == "__main__":
    unittest.main()
