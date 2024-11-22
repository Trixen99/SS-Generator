

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    def splitter(old_nodes, delimiter):
        text_from_node_list = old_nodes[0].text.split(delimiter)
        if len(old_nodes) <= 1:
            return text_from_node_list
        other_nodes = splitter(old_nodes[1:], delimiter)
        print(f"other_nodes\n{other_nodes}")
        text_from_node_list.extend(other_nodes)
        return text_from_node_list

    def formatter(split_text, text_type):
        
        return split_text


    split_text = splitter(old_nodes, delimiter)
    formatted_text = formatter(split_text, text_type)
    return formatted_text