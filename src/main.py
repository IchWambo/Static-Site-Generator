from textnode import TextNode
from copy_contents import copy_contents
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

def main():
    print("hello world")
    #text_node_1 = TextNode("anchor text", "liink", "https://www.boot.dev")
    #print(f'TextNode("{text_node_1.text}, {text_node_1.text_type}, {text_node_1.url}")')
    copy_contents("static", "public")
    generate_pages_recursive("content", "template.html", "public")
    #generate_page("content/index.md", "template.html", "public/index.html")
    #generate_page("content/blog/glorfindel/index.md", "template.html", "public/blog/glorfindel/index.html")
    #generate_page("content/blog/tom/index.md", "template.html", "public/blog/tom/index.html")
    #generate_page("content/blog/majesty/index.md", "template.html", "public/blog/majesty/index.html")
    #generate_page("content/contact/index.md", "template.html", "public/contact/index.html")

if __name__ == "__main__":
    main()