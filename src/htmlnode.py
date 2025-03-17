from textnode import TextType

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        if tag is None and value is None and children is None and props is None:
            raise ValueError("Creating an HTMLNode with all None parameters is pointless")
        self.tag = tag
        self.value = value
        self.props = props
        self.children = children
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            return " " + " ".join(['{}="{}"'.format(k, v) for k, v in self.props.items()])
        
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}, children: {self.children}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a VALUE")
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        return self.value if self.tag == None else "<{}{}>{}</{}>".format(self.tag, self.props_to_html(), self.value, self.tag)
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children=None, props=None):
        if children is None:
            raise ValueError("ParentNode requires CHILDREN")
        if tag is None:
            raise ValueError("ParentNode requires a TAG")
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.children is None:
            raise ValueError("ParentNode requires a CHILD")
        if self.tag is None:
            raise ValueError("ParentNode requires a TAG")
        return "<{}{}>{}</{}>".format(self.tag, self.props_to_html(), "".join([child.to_html() for child in self.children]), self.tag)
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", text_node.text, {"src": text_node.url})
        case _:
            raise ValueError("Unknown TextType")
        



if __name__ == "__main__":
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())