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
                e_text = extracted_text[-1].split(f"![{image[0]}]({image[1]})")
                extracted_text.remove(extracted_text[-1])
                extracted_text.extend(e_text)
            else:
                extracted_text = extracted_text.split(f"![{image[0]}]({image[1]})")
        for number in range(len(extracted_text)):
            if (extracted_text[number]) == "":
                extracted_text.pop(number)
        image_count = 0
        for text_number in range(len(extracted_text)):
            new_nodes = TextNode(extracted_text[text_number],TextType.TEXT)
            image_node = TextNode(extracted_images[image_count][0],TextType.IMAGE,str(extracted_images[image_count][1]))
            text_nodes.append(new_nodes)
            text_nodes.append(image_node)
            image_count += 1
    return text_nodes

def split_nodes_link(old_nodes):
    text_nodes = []
    links = None
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            text_nodes.append(node)
            continue
        extracted_text = node.text
        
        for link in links:
            split_text = extracted_text.split(f"[{link[0]}]({link[1]})")
            if split_text[0] != "":
                text_nodes.append(TextNode(split_text[0],TextType.TEXT))
            text_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            extracted_text = split_text[1]
        if extracted_text != "":
            text_nodes.append(TextNode(extracted_text, TextType.TEXT))





  
        #if len(extracted_text) == len(links) + 1:
            #for number in range(len(links)):
             #   new_TEXTNode_1 = TextNode(extracted_text[number],TextType.TEXT)
             #   new_LINKNode = TextNode(links[number][0],TextType.LINK,str(links[number][1]))
             #   if number + 1 == len(links):
            #        new_TEXTNode_2 = TextNode(extracted_text[number + 1],TextType.TEXT)
           #         text_nodes.extend([new_TEXTNode_1, new_LINKNode, new_TEXTNode_2])
          #      else:
         #           text_nodes.extend([new_TEXTNode_1, new_LINKNode])

        #e#lif len(extracted_text) == len(links):
        #    link_count = 0
         #   for text_number in range(len(extracted_text)):
          #      new_nodes = TextNode(extracted_text[text_number],TextType.TEXT)
         #       link_node = TextNode(links[link_count][0],TextType.LINK,str(links[link_count][1]))
         #       text_nodes.append(new_nodes)
         #       text_nodes.append(link_node)
         #       link_count += 1
    return text_nodes
            



        #link_count = 0
        #for text_number in range(len(extracted_text)):
        #    try:
        #        new_nodes = TextNode(extracted_text[text_number],TextType.TEXT)
        #        link_node = TextNode(extracted_links[link_count][0],TextType.LINK,str(extracted_links[link_count][1]))
        #        text_nodes.append(new_nodes)
        #        text_nodes.append(link_node)
        #        link_count += 1
        #    except:
         #       new_nodes = TextNode(extracted_text[text_number],TextType.TEXT)
         #       text_nodes.append(new_nodes)
         #       link_count += 1


 


        



    #for node in old_nodes:
    #    link_url = extract_markdown_links(node.text)
    #    print(link_url)