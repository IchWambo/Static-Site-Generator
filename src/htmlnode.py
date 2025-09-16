from textnode import TextType,TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        if children == None:
            self.children = []
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string_representation = ""
        if not self.props:
            return ""
        else:
            for prop, value in self.props.items():
                string_representation += " " + prop + "=" +f'"{value}"'
            return string_representation
            

    def __repr__(self):
        tag = repr(self.tag)
        value = repr(self.value)
        children = f"[{len(self.children)} children]" if self.children else "[]"
        props = repr(self.props) if self.props else "{}"
        return f"HTMLNode:(tag={tag}, value={value}, children={children},props={props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        children = [] if children is None else children
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        VOID_TAGS = {"img", "br", "hr", "input", "meta", "link"}
        if self.tag == None:
            if self.value == None:
                raise ValueError
            return str(self.value)
        attrs = ""
        if self.props:
            parts = [f'{prop}="{value}"' for prop, value in self.props.items()]
            attrs = " " + " ".join(parts)
        if self.tag in VOID_TAGS:
            return f"<{self.tag}{attrs}>"
        if self.value is None:
            raise ValueError("LeafNode missing value")
        open_tag = f"<{self.tag}{attrs}>"
        close_tag = f"</{self.tag}>"
        content = self.value or ""
        html_tag = f"{open_tag}{content}{close_tag}"
        return html_tag

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        children = [] if children is None else children
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag error")
        elif self.children is None:
            raise ValueError("child error")
        else:
            string_text = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                string_text += child.to_html()
            string_text += f"</{self.tag}>"
            return string_text

def text_node_to_html_node(text_node):
    #if text_node.text_type not in TextType:
        #raise Exception("Text Type not found.")
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
            if not getattr(text_node, "url", None):
                raise ValueError("Link node missing href")
            return LeafNode("a", text_node.text, None,  {"href": f"{text_node.url}"})
        case TextType.IMAGE:
            if not getattr(text_node, "url", None):
                raise ValueError("Image node missing src")
            alt = text_node.text or ""  
            return LeafNode("img", None, None, {"src": text_node.url, "alt": alt})
