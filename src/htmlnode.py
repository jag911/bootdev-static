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

    def __str__(self):
        if self.children is None:
            return "<{}{}>".format(self.tag, self._attributes())
        else:
            return "<{}{}>{}</{}>".format(self.tag, self._attributes(), self._children(), self.tag)

    def _attributes(self):
        if self.attributes is None:
            return ""
        else:
            return " " + " ".join(['{}="{}"'.format(k, v) for k, v in self.attributes.items()])

    def _children(self):
        if self.children is None:
            return ""
        else:
            return "".join([str(child) for child in self.children])

    def add_child(self, child):
        if self.children is None:
            self.children = []
        self.children.append(child)

    def add_attribute(self, key, value):
        if self.attributes is None:
            self.attributes = {}
        self.attributes[key] = value