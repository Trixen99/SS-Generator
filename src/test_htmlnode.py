import unittest

from htmlnode import *


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