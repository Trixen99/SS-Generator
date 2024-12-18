from enum import Enum
import re

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
    
    elif "*" in markdown_text or "1." in markdown_text:
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



