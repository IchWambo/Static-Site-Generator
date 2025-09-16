import unittest
from block_to_block_type import block_to_block_type, BlockType

class Test_Block(unittest.TestCase):
    def test_block_para(self):
        markdown = "This is a Paragraph"
        blocks = block_to_block_type(markdown)
        self.assertEqual(BlockType.Paragraph, blocks)

    def test_block_head(self):
        markdown = "# This is a Heading"
        blocks = block_to_block_type(markdown)
        self.assertEqual(BlockType.Heading, blocks)

    def test_block_code(self):
        markdown = "```This is Code```"
        blocks = block_to_block_type(markdown)
        self.assertEqual(BlockType.Code, blocks)

    def test_block_quote(self):
        markdown = ">This is a Quote"
        blocks = block_to_block_type(markdown)
        self.assertEqual(BlockType.Quote, blocks)

    def test_block_unord(self):
        markdown = "- This is an unordered list"
        blocks = block_to_block_type(markdown)
        self.assertEqual(BlockType.Unordered_list, blocks)

    def test_block_ord(self):
        markdown = "1. This is an ordered list"
        blocks = block_to_block_type(markdown)
        self.assertEqual(BlockType.Ordered_list, blocks)
    
if __name__ == "__main__":
    unittest.main()