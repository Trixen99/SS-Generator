from blocks import *



text = """# Header

paragraph `code`"""

#print(markdown_to_html_node(text))
node = markdown_to_html_node(text)
print(node.to_html())