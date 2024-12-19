from blocks import *

text = """# Header

Paragraph

* List Item
* List Item 2

[link](www.google.com)

![image](www.boo.com/boo_image)

_italics_

**bold**"""



print(markdown_to_html_node(text))