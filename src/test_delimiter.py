import unittest

from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplit(unittest.TestCase):
    def test_bold(self):
        node1 = TextNode("text with **bold** word", TextType.TEXT)
        node_list = [node1]
        new_node = split_nodes_delimiter(node_list ,"**",TextType.BOLD)
        test_node = TextNode("text with ", TextType.TEXT)
        test_node2 = TextNode("bold", TextType.BOLD)
        test_node3 = TextNode(" word", TextType.TEXT)
        test_node_list = [test_node, test_node2, test_node3]
        self.assertEqual(new_node, test_node_list)

    def test_italic(self):
        node1 = TextNode("text with _italic_ word", TextType.TEXT)
        node_list = [node1]
        new_node = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
        test_node = TextNode("text with ", TextType.TEXT)
        test_node2 = TextNode("italic", TextType.ITALIC)
        test_node3 = TextNode(" word", TextType.TEXT)
        test_node_list = [test_node, test_node2, test_node3]
        self.assertEqual(new_node, test_node_list)

    def test_code(self):
        node1 = TextNode("text with `code` word", TextType.TEXT)
        node_list = [node1]
        new_node = split_nodes_delimiter(node_list, "`", TextType.CODE)
        test_node = TextNode("text with ", TextType.TEXT)
        test_node2 = TextNode("code", TextType.CODE)
        test_node3 = TextNode(" word", TextType.TEXT)
        test_node_list = [test_node, test_node2, test_node3]
        self.assertEqual(new_node, test_node_list)

if __name__ == "__main__":
    unittest.main()