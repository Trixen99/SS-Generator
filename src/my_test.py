from blocks import *



text = """* Hello
* my **man**
- hello
- Madam"""



#Paragraph **with bold**"""




node = markdown_to_html_node(text)
#print(node)
print(node.to_html())