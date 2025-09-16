from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_node = ParentNode("div", [])
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.Paragraph:
                lines = block.splitlines()
                text = " ".join(line.strip() for line in lines if line.strip())
                text = " ".join(text.split())
                children = text_to_children(text)
                if len(children) == 1 and getattr(children[0], "tag", None) == "img":
                    html_node.children.append(children[0])
                else:
                    html_node.children.append(ParentNode("p", children))

            case BlockType.Heading:
                level = 0
                while level < len(block) and level < 6 and block[level] == "#":
                    level += 1

                if level == 0 or level > 6 or level >= len(block) or block[level] != " ":
                        raise Exception("Wrong Heading")
                
                heading = ParentNode(f"h{level}", text_to_children(block[level+1:].lstrip()))
                html_node.children.append(heading)

            case BlockType.Code:
                lines = block.splitlines()
                text = ""
                if lines and lines[0].strip() == "```" and lines[-1].strip() == ("```"):
                    text = "\n".join(lines[1:-1]) + "\n"
                else:
                    text = block
                code = ParentNode("code", [LeafNode(None, text.strip())])
                pre = ParentNode("pre", [code])
                html_node.children.append(pre)

            case BlockType.Quote:
                lines = block.splitlines()
                cleaned = []
                text = ""
                for line in lines:
                    if line.startswith("> "):
                        cleaned.append(line[2:])
                    elif line.startswith(">"):
                        cleaned.append(line[1:].lstrip())
                text = "\n".join(cleaned)
                quote = ParentNode("blockquote", text_to_children(text))
                html_node.children.append(quote)

            case BlockType.Unordered_list:
                split_block = block.split("\n")
                parent_node = ParentNode("ul", [])

                for line in split_block:
                    if line.startswith("- ") or line.startswith("* "):
                        line = line[2:]
                    elif line.startswith(""):
                        continue
                    parent_node.children.append(ParentNode("li",text_to_children(line.strip())))
                html_node.children.append(parent_node)

            case BlockType.Ordered_list:
                split_block = block.split("\n")
                parent_node = ParentNode("ol", [])

                for line in split_block:
                    text = line.split(".", 1)
                    parent_node.children.append(ParentNode("li", text_to_children(text[1].strip())))
                html_node.children.append(parent_node)

    return html_node

def text_to_children(text):
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in nodes]
