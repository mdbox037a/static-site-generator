import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
