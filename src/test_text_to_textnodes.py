import unittest

from htmlnode import *
from textnode import *
from split_nodes import *

class TestTextToTextNode(unittest.TestCase):
    def test_eq_1(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]
        self.assertEqual(expected,text_to_textnodes(text))

    def test_eq_2(self):
        text = "this is ![sparta](www.sparta.com), and we will die defending it [inspiration](www.men.com) because ..."
        expected = [
            TextNode("this is ",TextType.TEXT),
            TextNode("sparta",TextType.IMAGE,"www.sparta.com"),
            TextNode(", and we will die defending it ", TextType.TEXT),
            TextNode("inspiration", TextType.LINK, "www.men.com"),
            TextNode(" because ...",TextType.TEXT)
        ]
        self.assertEqual(expected,text_to_textnodes(text))


    def test_eq_3(self):
        text = "this is ![sparta](www.sparta.com), and we will **die** *defending* it [inspiration](www.men.com) **because** ... ![god](https://upload.wikimedia.org/wikipedia/en/9/93/Buddy_christ.jpg)"
        expected = [
            TextNode("this is ",TextType.TEXT),
            TextNode("sparta",TextType.IMAGE,"www.sparta.com"),
            TextNode(", and we will ", TextType.TEXT),
            TextNode("die", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("defending", TextType.ITALIC),
            TextNode(" it ", TextType.TEXT),            
            TextNode("inspiration", TextType.LINK, "www.men.com"),
            TextNode(" ", TextType.TEXT),
            TextNode("because", TextType.BOLD),
            TextNode(" ... ",TextType.TEXT),
            TextNode("god",TextType.IMAGE,"https://upload.wikimedia.org/wikipedia/en/9/93/Buddy_christ.jpg")
        ]
        self.assertEqual(expected,text_to_textnodes(text))

    def test4_empty(self):
        text = ""
        expected = []
        self.assertEqual(expected,text_to_textnodes(text))

    def testBold(self):
        text = "**look here**"
        expected = [TextNode("look here", TextType.BOLD)]
        self.assertEqual(expected,text_to_textnodes(text))

    def testText(self):
        text = "look here"
        expected = [TextNode("look here", TextType.TEXT)]
        self.assertEqual(expected,text_to_textnodes(text))

    def testItalic(self):
        text = "*look here*"
        expected = [TextNode("look here", TextType.ITALIC)]
        self.assertEqual(expected,text_to_textnodes(text))

    def testBOLDandITALIC(self):
        text = "**look***here*"
        expected = [TextNode("look",TextType.BOLD),
                    TextNode("here",TextType.ITALIC)]
        self.assertEqual(expected,text_to_textnodes(text))




