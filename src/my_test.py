from split_nodes import *


node = TextNode(
               "Hello my dear friends this is [text to link](www.google.com) and i am [deadly](www.spooky.com). Kill all [fiends](www.zombie.com) hey",
                TextType.TEXT,
                )

expected_text = [TextNode("Hello my dear friends this is ", TextType.TEXT, None),
                        TextNode("text to link", TextType.LINK, "www.google.com"),
                        TextNode(" and i am ", TextType.TEXT, None),
                        TextNode("deadly", TextType.LINK, "www.spooky.com"),
                        TextNode(". Kill all ", TextType.TEXT, None),
                        TextNode("fiends", TextType.LINK, "www.zombie.com"),
                        TextNode(" hey", TextType.TEXT, None),
        ]

test = split_nodes_link([node])
print(test)
print(test==expected_text)


[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]


