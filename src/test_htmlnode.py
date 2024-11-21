import unittest

from htmlnode import *
from textnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq_1(self):
        node = HTMLNode(props={
            "href": "https://google.com",
            "target": "_blank"
        })
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_eq_2(self):
        child1 = HTMLNode(tag="p", value="First paragraph", props={
            "tag": "p",
            "value": "First paragraph"
            })      
        self.assertEqual(child1.props_to_html(), ' tag="p" value="First paragraph"')

    def test_long_one(self):
        child2 = HTMLNode(tag="p", value="First paragraph", props={
            "my_text": "hello",
            "world": "look at the time",
            "why_are_you": "doing this",
            "my_god": "you are dead"
            })     
        self.assertNotEqual(child2.props_to_html(),' my_text="hello" world="look at the time" why are you="doing this" my god="you are dead"')

    def test_there_is_a_space(self):
        child2 = HTMLNode(tag="p", value="First paragraph", props={
            "my_text": "hello",
            "world": "look at the time",
            "why_are_you": "doing this",
            "my_god": "you are dead"
            })      
        self.assertNotEqual(child2.props_to_html(),'my_text="hello" world="look at the time" why_are_you="doing this" my_god="you are dead"')

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_LeafNode_1(self):
        test = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(test.to_html(),"<p>This is a paragraph of text.</p>")


    def test_LeafNode_2(self):
        test = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(test.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_LeafNode_3(self):
        test = LeafNode(None, None)
        self.assertRaises(ValueError, test.to_html)

    def test_LeafNode_4(self):
        test = LeafNode(None, None)
        with self.assertRaises(ValueError):
            test.to_html()

    
    def test_ParentNode_1(self):
        node = ParentNode(
            "p",
            [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_ParentNode_2(self):
        node = ParentNode(
            "p",
            [
            ParentNode("p", [LeafNode(None, "Normal text")]),
            ],)
        self.assertEqual(node.to_html(),"<p><p>Normal text</p></p>")


    def test_ParentNode_3(self):
        node = ParentNode(
            "p",
        [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        LeafNode("a", "Normal text",{"href": "https://www.google.com"}),
        ])
        self.assertEqual(node.to_html(),'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a href="https://www.google.com">Normal text</a></p>')
 
    def test_ParentNode_4(self):
        node = ParentNode(
            None,
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            ParentNode("div",[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text")],
            {"href": "https://www.google.com"})],
            {"href": "https://www.google.com"})

        with self.assertRaises(ValueError):
            node.to_html()

    def test_ParentNode_5(self):
        node = ParentNode(
            "div",
        None,
            {"href": "https://www.google.com"})

        with self.assertRaises(ValueError):
            node.to_html()

    def test_text_node_to_html_node_1(self):
        node = TextNode("hello",TextType.ITALIC,None)
        test = LeafNode("i", "hello", None)
        self.assertEqual(text_node_to_html_node(node), test)

    def test_text_node_to_html_node_2(self):
        node = TextNode("hello",TextType.LINK,"www.themain.com")
        test = LeafNode("a", "hello", {"href": "www.themain.com"})
        self.assertEqual(text_node_to_html_node(node), test)

    def test_text_node_to_html_node_3(self):
        node = TextNode("hello",TextType.BOLD)
        test = LeafNode("b", "hello")
        self.assertEqual(text_node_to_html_node(node), test)
    
    def test_text_node_to_html_node_4(self):
        node = TextNode("hello",TextType.CODE)
        test = LeafNode("code", "hello")
        self.assertEqual(text_node_to_html_node(node), test)

    def test_text_node_to_html_node_5(self):
        node = TextNode("hello",TextType.TEXT)
        test = LeafNode(None, "hello")
        self.assertEqual(text_node_to_html_node(node), test)

    def test_text_node_to_html_node_6(self):
        node = TextNode("hello",TextType.TEXT)
        test = LeafNode(None, "hello")
        self.assertEqual(text_node_to_html_node(node), test)
    
    def test_text_node_to_html_node_7(self):
        node = TextNode("hello",TextType.IMAGE, "www.themain.com")
        test = LeafNode("img","",{"src": "www.themain.com", "alt": "hello"})
        self.assertEqual(text_node_to_html_node(node), test)

    def test_text_node_to_html_node_8(self):
        node = TextNode("hello", "PROP", "www.themain.com")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)




