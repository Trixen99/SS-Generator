from split_nodes import *

node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)

node2 = TextNode(
    "This is text with a link that is going to destroy the world [google](https://www.google.com) and marry my daughter[Shia LaBeouf](https://en.wikipedia.org/wiki/Shia_LaBeouf)",
    TextType.TEXT,
)


new_nodes = split_nodes_link([node])
print(new_nodes)

# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]


