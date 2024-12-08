import unittest

from htmlnode import *
from textnode import *
from split_nodes import *

class TestSPLITNODE(unittest.TestCase):
    def test_eq_1(self):
        node = TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        TextType.TEXT,
        )
        expected_text = [TextNode("This is text with a ", TextType.TEXT), TextNode("rick roll", TextType.IMAGE,"https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", TextType.TEXT), TextNode("obi wan", TextType.IMAGE,"https://i.imgur.com/fJRm4Vk.jpeg"),]
        self.assertEqual(split_nodes_image([node]),expected_text)
    
    def test_eq_2(self):
        node = TextNode(
               "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT,
                )
        expected_text = [TextNode("This is text with a link ", TextType.TEXT),
                        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                        TextNode(" and ", TextType.TEXT),
                        TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),]
        self.assertEqual(split_nodes_link([node]),expected_text)



