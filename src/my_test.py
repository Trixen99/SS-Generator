from blocks import *

text = """# Header

Paragraph
Paragraph2
Paragraph3
Paragraph4

* List Item
* List Item 2

[link](www.google.com)

![image](www.boo.com/boo_image)

_italics_

**bold**"""
text = """
Paragraph
Paragraph2
Paragraph3
Paragraph4
**ps1**
*ps2*
"""


#print(markdown_to_html_node(text))
markdown_to_html_node(text)