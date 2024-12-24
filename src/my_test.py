from blocks import *



text = """> Hello you
> hello *too*
> Hello **THree** 

> hello you
> Hello Me"""

#print(markdown_to_html_node(text))


# Test 1: Multiple lines with inline formatting
text1 = """> This is **bold** text
> And *italic* text"""

# Test 2: Single line with a link
text2 = """> Here is a [link](https://example.com)"""

# Test 3: Empty quote
text3 = """>    """

node1 = markdown_to_html_node(text1)
node2 = markdown_to_html_node(text2)
node3 = markdown_to_html_node(text3)

nodes = [node1,node2,node3]
for node in nodes:
    print(node.to_html())
    print("\n")



#node = markdown_to_html_node(text)
#print(node)
#print(node.to_html())