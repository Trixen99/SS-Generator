import unittest

from extract_markdown import *


class TestExtractMarkdown(unittest.TestCase):
    def test_eq(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_text = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), expected_text)

    def test_eq_2(self):
        text = text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_text = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), expected_text)

    def test_eq_3(self):
        text = text = "Hello world this is your leader talking ![leader here](https://linkgoeshere.gif) and i am here to destory you ![destory](https://mightguy.gif)"
        expected_text = [("leader here", "https://linkgoeshere.gif"), ("destory", "https://mightguy.gif")]
        self.assertEqual(extract_markdown_images(text), expected_text)


