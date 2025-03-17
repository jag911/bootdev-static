# src/test_htmlnode.py
import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode,text_node_to_html_node
from textnode import TextNode,TextType

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.boot.dev/img/bootdev-logo-full-small.webp")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "This is an image node")
        self.assertEqual(html_node.props["src"], "https://www.boot.dev/img/bootdev-logo-full-small.webp")
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props["href"], "https://www.boot.dev")
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

if __name__ == "__main__":
    unittest.main()