from enum import Enum

class BlockType(Enum):
    Paragraph = "PARAGRAPH"
    Heading = "HEADING"
    Code = "CODE"
    Quote = "QUOTE"
    Unordered_list = "UNORDERED_LIST"
    Ordered_list = "ORDERED_LIST"

def block_to_block_type(markdown):
    if markdown.startswith("#"):
        return BlockType.Heading
    elif markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.Code
    elif markdown.startswith(">"):
        return BlockType.Quote
    elif markdown.startswith("-") and markdown[1] == " ":
        return BlockType.Unordered_list
    elif markdown[0] == "1" and markdown[1] == ".":
        return BlockType.Ordered_list
    else:
        return BlockType.Paragraph

def main():
    block_to_block_type("> Heading 1")

if __name__ == "__main__":
    main()