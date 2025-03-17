# src/test_htmlnode.py
import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()