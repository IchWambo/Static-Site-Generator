import unittest

from htmlnode import ParentNode, LeafNode

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

    def test_multiple_children(self):
        child1 = LeafNode("b", "Bold")
        child2 = LeafNode(None, "Normal text")  
        child3 = LeafNode("i", "Italic")
        parent = ParentNode("p", [child1, child2, child3])
        expected = "<p><b>Bold</b>Normal text<i>Italic</i></p>"
        self.assertEqual(parent.to_html(), expected)

    def test_parent_with_props(self):
        child = LeafNode("span", "content")
        parent = ParentNode("div", [child], {"class": "container", "id": "main"})
        expected = '<div class="container" id="main"><span>content</span></div>'
        self.assertEqual(parent.to_html(), expected)
    
    def test_nested_parent_nodes(self):
        inner_child = LeafNode("b", "bold text")
        inner_parent = ParentNode("p", [inner_child])
        outer_parent = ParentNode("div", [inner_parent]) 
        expected = "<div><p><b>bold text</b></p></div>"
        self.assertEqual(outer_parent.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
