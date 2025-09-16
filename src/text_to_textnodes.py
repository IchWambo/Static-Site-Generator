from split_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    #example_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text_node = TextNode(text, TextType.TEXT)
    nodes = [text_node]
    result_bold = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    result_italic = split_nodes_delimiter(result_bold,"_", TextType.ITALIC)
    result_code = split_nodes_delimiter(result_italic, "`", TextType.CODE)
    image_result = split_nodes_image(result_code)
    link_result = split_nodes_link(image_result)
    return link_result
    
    

#def main():
    #text_to_textnodes("text")

#if __name__ == "__main__":
    #main()