import unittest

from blocks import *


class TestMarkdowntoBlocks(unittest.TestCase):
    def test_eq(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        expected = ["# This is a heading","This is a paragraph of text. It has some **bold** and *italic* words inside of it.","""* This is the first list item in a list block
* This is a list item
* This is another list item"""]
        self.assertEqual(markdown_to_blocks(text), expected)
    
    def test_2(self):
        text = "Hello"
        expected = ["Hello"]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_3(self):
        text = """hello

world

my
name
is

ralph"""

        expected = ["hello","world","my\nname\nis","ralph"]
        self.assertEqual(markdown_to_blocks(text), expected)




    def test_block_to_block_type_1(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected_list = markdown_to_blocks(text)
        blocktype_list = []
        for item in expected_list:
            blocktype_list.append(block_to_block_type(item))
        expected = [BlockType.HEADING, BlockType.PARAGRAPH, BlockType.UNORDERED_LIST]
        self.assertEqual(blocktype_list, expected)
    
    def test_block_to_block_type_2(self):
        text = "Hello"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(markdown_to_blocks(text)[0]), expected)


    def test_block_to_block_type_3(self):
        text = """hello

world

my
name
is

ralph"""

        block = markdown_to_blocks(text)
        expected = [BlockType.PARAGRAPH,BlockType.PARAGRAPH,BlockType.PARAGRAPH,BlockType.PARAGRAPH]
        list = []
        for item in block:
            list.append(block_to_block_type(item))
        self.assertEqual(list, expected)

    def test_block_to_block_type_4(self):
        text = """#### Heading

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
        block = markdown_to_blocks(text)
        list = []
        for item in block:
            list.append(block_to_block_type(item))
        self.assertEqual(list, expected)

    def test_block_to_block_type_4(self):
        test1 = """> Line 1
> Line 2
>Line 3"""
        expected1 = BlockType.QUOTE
        self.assertEqual(block_to_block_type(test1), expected1)

    def test_block_to_block_type_5(self):

        test2 = """* Item 1
- Item 2
* Item 3"""
        expected2 = BlockType.UNORDERED_LIST
        self.assertEqual(block_to_block_type(test2), expected2)

    def test_block_to_block_type_6(self):
        test3 = """1. First
2. Second
4. Fourth"""
        expected3 = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(test3), expected3)

    def test_block_to_block_type_7(self):
        test4 = """1. First
2.Second (missing space)
3. Third"""
        expected4 = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(test4), expected4)

    def test_block_to_block_type_8(self):
        test5 = """### Heading
with multiple
lines"""
        expected5 = BlockType.HEADING
        self.assertEqual(block_to_block_type(test5), expected5)

    def test_block_to_block_type_9(self):
        test6 = """```python
def hello():
    print("Hi")
``"""
        expected6 = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(test6), expected6)