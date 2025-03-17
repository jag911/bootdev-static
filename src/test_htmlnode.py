# src/test_htmlnode.py
import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_no_tag(self):
        node = HTMLNode(value="a_value", props={"a_prop": "a_prop_value"}, children=["a_child"])
        self.assertIs(node.tag, None, "A Tag of None will be displayed as pure TEXT")
    
    def test_no_value(self):
        node = HTMLNode(tag="a_tag", props={"a_prop": "a_prop_value"}, children=["a_child"])
        self.assertIs(node.value, None, "A Value of None is assumed to have CHILDREN")
    
    def test_no_props(self):
        node = HTMLNode(tag="a_tag", value="a_value", children=["a_child"])
        self.assertIs(node.props, None, "A Props of None is assumed to have no ATTRIBUTES")
    
    def test_no_children(self):
        node = HTMLNode(tag="a_tag", value="a_value", props={"a_prop": "a_prop_value"})
        self.assertIs(node.children, None, "A Children of None is assumed to have a VALUE")
    
    def test_all_none(self):
        with self.assertRaises(ValueError) as context:
            node = HTMLNode()  # All parameters default to None
            if node.tag is None and node.value is None and node.children is None and node.props is None:
                raise ValueError("Creating an HTMLNode with all None parameters is pointless")
        self.assertIn("pointless", str(context.exception))

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">Click me!</a>')
    def test_leaf_no_value(self):
        with self.assertRaises(ValueError) as context:
            LeafNode("a", None)  # Explicitly pass None as value
            self.assertIn("LeafNode requires a value", str(context.exception))

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