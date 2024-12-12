from textnode import *
from extract_markdown import *


def split_nodes_image(old_nodes):
    text_nodes = []
    images = None
    split = "IMAGE"
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            text_nodes.append(node)
            continue
        extracted_text = node.text
        text_nodes.extend(split_part_two(extracted_text, images, split))
    return text_nodes


def split_nodes_link(old_nodes):
    text_nodes = []
    split = "LINK"
    links = None
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            text_nodes.append(node)
            continue
        extracted_text = node.text
        text_nodes.extend(split_part_two(extracted_text, links, split))
    return text_nodes
        


def split_part_two(extracted_text, iterables, split):
        node_list = []
        for iterable in iterables:
            split_text = None
            new_text_type = None
            if split == "IMAGE":
                    split_text = extracted_text.split(f"![{iterable[0]}]({iterable[1]})")
                    new_text_type = TextType.IMAGE
            else:
                    split_text = extracted_text.split(f"[{iterable[0]}]({iterable[1]})")
                    new_text_type = TextType.LINK

            if split_text[0] != "":
                node_list.append(TextNode(split_text[0],TextType.TEXT))
            node_list.append(TextNode(iterable[0], new_text_type, iterable[1]))
            extracted_text = split_text[1]
        if extracted_text != "":
            node_list.append(TextNode(extracted_text, TextType.TEXT))
        return(node_list)
