import unittest

from extract_markdown_images import extract_markdown_images, extract_markdown_link

class TestMark(unittest.TestCase):
    def test_image(self):
        image = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], image)
    
    def test_link(self):
        link = extract_markdown_link("This is text with a link [to boot dev](https://www.boot.dev)")
        self.assertEqual([("to boot dev", "https://www.boot.dev")], link)

if __name__ == "__main__":
    unittest.main()