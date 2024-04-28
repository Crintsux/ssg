class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        output = ""
        for key in self.props:
            output += f' {key}="{self.props[key]}"'
        return output
    
    def __repr__(self):
        return f"HTMLNode(Tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(Tag: {self.tag}, value: {self.value}, props: {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        super().__init__(self, tag, None, children, props)

    def to_html(self):
        if not self.children:
            raise ValueError
        