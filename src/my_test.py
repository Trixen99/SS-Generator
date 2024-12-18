from blocks import *


####### Heading (7 #'s)
#Not a heading (no space after #)
#    Heading (multiple spaces)

#text = "####### Heading"
#text2 = "#Not a heading"
#text3 = "#    Heading"


#text = "####### Header" #(7 #'s)
#text2 = "# Valid header!"
#text3 = "#Invalid header" #(no space)
#print(block_to_block_type(text))
#print(block_to_block_type(text2))
#print(block_to_block_type(text3))


text1 = """#### Heading

This is a Paragraph

1. This
2. is
3. an
4. ordered
5. list


* this
* is
* an
* unordered
* list


> this is 
> a quote

```this is code```
"""
expected = [BlockType.HEADING, BlockType.PARAGRAPH, BlockType.ORDERED_LIST, BlockType.UNORDERED_LIST, BlockType.QUOTE, BlockType.CODE]

#block = markdown_to_blocks(text1)
#list = []
#for item in block:
#    list.append(block_to_block_type(item))
#print(list)


