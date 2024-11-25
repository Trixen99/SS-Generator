from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_list.append(node)
            continue
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise ValueError("original text is not formatted correctly")
        count = 1
        split_nodes_list = []
        for string in split_node:
            if string == "":
              count += 1
              continue
            elif count % 2 == 0:
                split_nodes_list.append(TextNode(string,text_type))
                count += 1
                continue
            split_nodes_list.append(TextNode(string, node.text_type))
            count += 1
            continue

    final_list.extend(split_nodes_list)
    return final_list



        












    


                  


    

