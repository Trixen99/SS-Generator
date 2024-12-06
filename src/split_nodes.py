from textnode import *
from extract_markdown import *


def split_nodes_image(old_nodes):
    text_nodes = []
    extracted_images = None
    for node in old_nodes:
        extracted_images = extract_markdown_images(node.text)
        if len(extracted_images) == 0:
            return node
        extracted_text = node.text
        
        for image in extracted_images:
            if isinstance(extracted_text,list):
                e_text = extracted_text[-1].split(f"[{image[0]}]({image[1]})")
                extracted_text.remove(extracted_text[-1])
                extracted_text.extend(e_text)
            else:
                extracted_text = extracted_text.split(f"[{image[0]}]({image[1]})")
        for number in range(len(extracted_text)):
            if (extracted_text[number]) == "":
                extracted_text.pop(number)
        image_count = 0
        for text_number in range(len(extracted_text)):
            new_nodes = TextNode(extracted_text[text_number],TextType.TEXT)
            link_node = TextNode(extracted_images[image_count][0],TextType.LINK,f'"{extracted_images[image_count][1]}"')
            text_nodes.append(new_nodes)
            text_nodes.append(link_node)
            image_count += 1
    return text_nodes

def split_nodes_link(old_nodes):
    text_nodes = []
    extracted_links = None
    for node in old_nodes:
        extracted_links = extract_markdown_links(node.text)
        if len(extracted_links) == 0:
            return node
        extracted_text = node.text
        
        for link in extracted_links:
            if isinstance(extracted_text,list):
                e_text = extracted_text[-1].split(f"[{link[0]}]({link[1]})")
                extracted_text.remove(extracted_text[-1])
                extracted_text.extend(e_text)
            else:
                extracted_text = extracted_text.split(f"[{link[0]}]({link[1]})")
        for number in range(len(extracted_text)):
            if (extracted_text[number]) == "":
                extracted_text.pop(number)
        link_count = 0
        for text_number in range(len(extracted_text)):
            new_nodes = TextNode(extracted_text[text_number],TextType.TEXT)
            link_node = TextNode(extracted_links[link_count][0],TextType.LINK,f'"{extracted_links[link_count][1]}"')
            text_nodes.append(new_nodes)
            text_nodes.append(link_node)
            link_count += 1
    return text_nodes


        



    #for node in old_nodes:
    #    link_url = extract_markdown_links(node.text)
    #    print(link_url)