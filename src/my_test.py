from htmlnode import *
from textnode import *
from delimiter import *

node = TextNode("This is text with a `code block` word", TextType.TEXT)
node2 = TextNode("This is text with a `code block` word number 2", TextType.BOLD)
node3 = TextNode("This is text with a code block word number `2`", TextType.BOLD)
#new_nodes = split_nodes_delimiter([node3], "`", TextType.CODE)
new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)

print(f"node\n{node}")
print(f"new nodes\n{new_nodes}")




