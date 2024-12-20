from enum import Enum
import re
from htmlnode import *
from split_nodes import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    new_block_list = []
    block_list = markdown.split("\n\n")
    for blocknumber in range(len(block_list)):
        if block_list[blocknumber] != "":
            string = block_list[blocknumber].strip()
            new_block_list.append(string)
    return new_block_list


def block_to_block_type(markdown_text):
    if re.match(r"^\#{1,6}\ .+", markdown_text):
        return BlockType.HEADING


    elif re.match(r"^(\`\`\`(.|\n)*\`\`\`)", markdown_text):
        return BlockType.CODE
    
    elif markdown_text.startswith(">"):
        individual_lines = markdown_text.split("\n")
        for line in individual_lines:
            if re.match(r"^\>.*", line):
                pass
            else:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    elif markdown_text.startswith("*") or markdown_text.startswith("-") or markdown_text.startswith("1."):
        individual_lines = markdown_text.split("\n")
        if individual_lines[0][0] == "*" or individual_lines[0][0] == "-":
            for line in individual_lines:
                if re.match(r"^(\*\ .*|\-\ .*)",line):
                    pass
                else:
                    return BlockType.PARAGRAPH
            return BlockType.UNORDERED_LIST

        elif individual_lines[0][0:2] == "1.":
            expected_line_number = 1
            unordered = 0
            for line in individual_lines:
                if line.startswith(f"{expected_line_number}. "):
                    pass
                else:
                    unordered = 1
                expected_line_number += 1
            if unordered != 0:
                return BlockType.PARAGRAPH
            else:
                return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH






def markdown_to_html_node(markdown):
    blocks_list = markdown_to_blocks(markdown)
    for block in blocks_list:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                paragraph = text_to_textnodes(block)
                list = []
                for node in paragraph:
                    if node.text_type == TextType.BOLD:
                        list.append(LeafNode(tag="b", value=node.text))
                    elif node.text_type == TextType.ITALIC:
                        list.append(LeafNode(tag="i", value=node.text))
                    elif node.text_type == TextType.TEXT:
                        list.append(LeafNode(None,node.text))
                html = HTMLNode("p",None, list, None)
                print(html)




                #segments = block.split("\n")
                #leaf_list = []
                #for segment in segments:
                #    leaf_list.append(LeafNode(value=segment))
                #paragraph = ParentNode(tag="p",children=leaf_list)
                #print(paragraph)





                #new_html_node = HTMLNode(tag="p", value=block)

            case BlockType.HEADING:
                first_6_characters = block[:7]
                hashtag_count = 0
                for character in first_6_characters:
                    if character =="#":
                        hashtag_count += 1
                    else:
                        new_html_node = HTMLNode(tag=f"h{hashtag_count}", value=block)
                        break

            case BlockType.CODE:
                pass

            case BlockType.QUOTE:
                pass

            case BlockType.UNORDERED_LIST:
                pass

            case BlockType.ORDERED_LIST:
                pass

            case _:
                raise Exception("a non valid block type has been provided")



