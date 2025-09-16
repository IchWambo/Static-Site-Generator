from extract_markdown_images import extract_markdown_images, extract_markdown_link
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            if node.text == "":
                continue
            else:
                new_nodes.append(node)
                continue
        split_image = extract_markdown_images(node.text)
        if len(split_image) < 1:
            new_text_node = TextNode(node.text, TextType.TEXT)
            new_nodes.append(new_text_node)
            continue
        remaining_text = node.text
        while len(split_image) > 0:
            current_link = split_image[0]
            split_text = remaining_text.split(f"![{current_link[0]}]({current_link[1]})", 1)
            new_text_node = TextNode(split_text[0], TextType.TEXT)
            new_link_node = TextNode(current_link[0], TextType.IMAGE, url=current_link[1]) 
            remaining_text = split_text[1]
            split_image = extract_markdown_images(remaining_text)
            if new_text_node.text != "":
                new_nodes.append(new_text_node)
            new_nodes.append(new_link_node)
        if remaining_text != "":
            new_text_node = TextNode(remaining_text, TextType.TEXT)
            new_nodes.append(new_text_node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            if node.text == "":
                continue
            else:
                new_nodes.append(node)
                continue
        split_link = extract_markdown_link(node.text)
        if len(split_link) < 1:
            new_text_node = TextNode(node.text, TextType.TEXT)
            new_nodes.append(new_text_node)
            continue
        remaining_text = node.text
        while len(split_link) > 0:
            current_link = split_link[0]
            split_text = remaining_text.split(f"[{current_link[0]}]({current_link[1]})", 1)
            new_text_node = TextNode(split_text[0], TextType.TEXT)
            new_link_node = TextNode(current_link[0], TextType.LINK, url=current_link[1]) 
            remaining_text = split_text[1]
            split_link = extract_markdown_link(remaining_text)
            if new_text_node.text != "":
                new_nodes.append(new_text_node)
            new_nodes.append(new_link_node)
        if remaining_text != "":
            new_text_node = TextNode(remaining_text, TextType.TEXT)
            new_nodes.append(new_text_node)
    return new_nodes