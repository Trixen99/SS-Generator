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
    current_node_list = []
    for block in blocks_list:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                current_node_list.extend(block_type_paragraph(block))

            case BlockType.HEADING:
                current_node_list.extend(block_type_heading(block)) 

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
    return ParentNode("body", current_node_list, None)





def block_type_paragraph(block):
    paragraph = text_to_textnodes(block)
    node_list = []
    for node in paragraph:
        if node.text_type == TextType.BOLD:
            node_list.append(LeafNode(tag="b", value=node.text))
        elif node.text_type == TextType.ITALIC:
            node_list.append(LeafNode(tag="i", value=node.text))
        elif node.text_type == TextType.TEXT:
            node_list.append(LeafNode(None,node.text))
        elif node.text_type == TextType.IMAGE:
            node_list.append(LeafNode("img", node.text, {"src": f"{node.url}"}))
        elif node.text_type == TextType.CODE:
            node_list.append(LeafNode("code",node.text,None))
        elif node.text_type == TextType.LINK:
            node_list.append(LeafNode("a", node.text, {"href": f"{node.url}"}))
    return [ParentNode("p", node_list, None)]

def block_type_heading(block):
    node_list = []
    first_6_characters = block[:7]
    hashtag_count = 0
    for character in first_6_characters:
        if character =="#":
            hashtag_count += 1
        else:
            node_list.append(LeafNode(value=block.strip("#").strip()))
            break
    return [ParentNode(f"h{hashtag_count}", node_list, None)]