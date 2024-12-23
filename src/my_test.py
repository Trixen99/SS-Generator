from blocks import *



text = """> Hello you"""

#print(markdown_to_html_node(text))





node = markdown_to_html_node(text)
#print(node)
print(node.to_html())