from htmlnode import *
from textnode import *

node = TextNode("hello",TextType.ITALIC,None)


#print(node)
node_2 = text_node_to_html_node(node)
print(node_2)