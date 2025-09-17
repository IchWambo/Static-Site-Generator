import sys
from textnode import TextNode
from copy_contents import copy_contents
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print("hello world")
    copy_contents("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()