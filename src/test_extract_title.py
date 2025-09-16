import unittest
from extract_title import extract_title

class Test_Extract(unittest.TestCase):
    def test_h1(self):
        header_text = """
    # This is a heading

    This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

    - This is the first list item in a list block
    - This is a list item
    - This is another list item
    """
        title = extract_title(header_text)
        self.assertEqual("This is a heading", title)

    def test_h2(self):
        header_text = """
    # This is a heading
    ## This is a heading2

    This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

    - This is the first list item in a list block
    - This is a list item
    - This is another list item
    """
        title = extract_title(header_text)
        self.assertEqual("This is a heading", title)

    def test_h3(self):
        header_text = """
    # This is a heading
    ## This is a heading2
    ### This is a heading3

    This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

    - This is the first list item in a list block
    - This is a list item
    - This is another list item
    """
        title = extract_title(header_text)
        self.assertEqual("This is a heading", title)
        
if __name__ == "__main__":
    unittest.main()