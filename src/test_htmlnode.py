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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
