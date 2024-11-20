from textnode import *

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        list = []
        for key in self.props:
            list.append(f' {key}="{self.props[key]}"')
        return "".join(list)


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def __eq__(self, second):
        if not isinstance(second, type(self)):
            return False
        return (
            self.tag == second.tag
            and self.value == second.value
            and self.children == second.children
            and self.props == second.props
            )
        

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None ,props)


    def to_html(self):
        if self.value is None:
            raise ValueError("must have a value")
        elif self.tag is None:
            return f"{self.value}"
        elif self.props is not None:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        
        
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

            
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a 'tag' value")
        elif self.children is None:
            raise ValueError("ParentNode must have a 'children' value")
        def concatenating(f_children):
            if len(f_children) == 0:
                return ""
            current_childnode = f_children[0].to_html()
            return f"{current_childnode}{concatenating(f_children[1:])}"
        return f"<{self.tag}>{concatenating(self.children)}</{self.tag}>"  
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

        
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img","",{"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("not a valid text type")


