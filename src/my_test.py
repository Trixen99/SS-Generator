from split_nodes import *
#node2 = TextNode(
#    "This is text with a link that is going to destroy the world [google](https://www.google.com) and marry my daughter[Shia LaBeouf](https://en.wikipedia.org/wiki/Shia_LaBeouf)",
#    TextType.TEXT,
#)


#node = TextNode(
#    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#    TextType.TEXT,
#)




#new_nodes = split_nodes_link([node])
#print(new_nodes)

node = TextNode(
    "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
    TextType.TEXT,
)


expected_text = [TextNode("This is text with a ", TextType.TEXT),
                 TextNode("rick roll", TextType.IMAGE,"https://i.imgur.com/aKaOqIh.gif"),
                 TextNode(" and ", TextType.TEXT),
                 TextNode("obi wan", TextType.IMAGE,"https://i.imgur.com/fJRm4Vk.jpeg"),
                ]
test = split_nodes_image([node])
print(test)
print(test==expected_text)


[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]


