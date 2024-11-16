from htmlnode import *

child1 = HTMLNode(tag="p", value="First paragraph")
child2 = HTMLNode(tag="p", value="Second paragraph")
parent = HTMLNode(
    tag="div",
    children=[child1, child2],
    props={"class": "container"}
)
print(parent)