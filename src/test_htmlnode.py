import unittest

from htmlnode import HTMLNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_ul(self):
        node = HTMLNode("ul", "text", HTMLNode("li"))
        node.props_to_html()
    def test_p(self):
        node = HTMLNode("p", "text")
        node.props_to_html
    def test_h(self):
        node = HTMLNode("a", "link","",{"href": "https://www.google.com"})
        node.props_to_html
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()