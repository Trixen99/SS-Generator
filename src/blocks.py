from enum import Enum
import re
from htmlnode import *
from split_nodes import *
from delimiter import *

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
    #any more than 6 #, returns a paragraph
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
                current_node_list.extend(block_type_code(block)) 

            case BlockType.QUOTE:
                current_node_list.extend(block_type_quote(block)) 

            case BlockType.UNORDERED_LIST:
                current_node_list.extend(block_type_unordered_list(block)) 

            case BlockType.ORDERED_LIST:
                current_node_list.extend(block_type_ordered_list(block)) 

            case _:
                raise Exception("a non valid block type has been provided")
    return ParentNode("div", current_node_list, None)





def block_type_paragraph(block):
    paragraph = text_to_textnodes(block)
    node_list = []
    for node in paragraph:
        node_list.append(text_node_converter(node))
    return [ParentNode("p", node_list, None)]


def block_type_heading(block):
    editted_block = block.lstrip("# ")
    text_nodes = text_to_textnodes(editted_block)
    node_list = []
    hashtag_count = 0

    for character in block[0:7]:
        if character =="#":
            hashtag_count += 1
        else:
            break
    redacted_text_nodes_list = text_nodes.copy()

    for node in redacted_text_nodes_list:
        node_list.append(text_node_converter(node))
        continue
    return [ParentNode(f"h{hashtag_count}", node_list, None)]



def block_type_code(block):
    new_block = block.strip("` ")
    leaf_node = LeafNode(None,new_block,None)
    return [ParentNode("pre", [ParentNode("code", [leaf_node], None)],None)]


def block_type_quote(block):
    split_lines = block.split("\n")
    for line_number in range(len(split_lines)):
        split_lines[line_number] = split_lines[line_number].strip(">").strip()
    unsplit_lines = " ".join(split_lines)
    text_nodes = []
    text_nodes.extend(text_to_textnodes(unsplit_lines))
    leaf_nodes = []
    for node in text_nodes:
        leaf_nodes.append(text_node_converter(node))
    return [ParentNode("blockquote", leaf_nodes, None)]


def block_type_unordered_list(block):
    split_block = block.split("\n")
    parent_nodes = []
    for section in split_block:
        leaf_nodes = []
        editted_section = section.lstrip("-*").lstrip(" ")
        text_nodes = (text_to_textnodes(editted_section))
        for node in text_nodes:
            leaf_nodes.append(text_node_converter(node))
        parent_nodes.extend([ParentNode("li", leaf_nodes, None)])
    return [ParentNode("ul", parent_nodes, None)]


def block_type_ordered_list(block):
    split_block = block.split("\n")
    parent_nodes = []
    for section in split_block:
        leaf_nodes = []
        editted_section = section.lstrip("1234567890. ")
        text_nodes = (text_to_textnodes(editted_section))
        for node in text_nodes:
            leaf_nodes.append(text_node_converter(node))
        parent_nodes.extend([ParentNode("li", leaf_nodes, None)])
    return [ParentNode("ol", parent_nodes, None)]


def text_node_converter(node):
    if node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=node.text)
    elif node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=node.text)
    elif node.text_type == TextType.TEXT:
        return LeafNode(None,node.text)
    elif node.text_type == TextType.IMAGE:
        return LeafNode("img", node.text, {"src": f"{node.url}"})
    elif node.text_type == TextType.CODE:
        return LeafNode("code",node.text,None)
    elif node.text_type == TextType.LINK:
        return LeafNode("a", node.text, {"href": f"{node.url}"})