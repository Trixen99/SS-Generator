from blocks import *



text = """* Hello
- My friend
* I **am**
- God
* Today"""



#Paragraph **with bold**"""




node = markdown_to_html_node(text)
print(node)
print(node.to_html())