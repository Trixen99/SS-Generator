

def markdown_to_blocks(markdown):
    new_block_list = []
    block_list = markdown.split("\n\n")
    for blocknumber in range(len(block_list)):
        if block_list[blocknumber] != "":
            string = block_list[blocknumber].strip()
            new_block_list.append(string)
    return new_block_list

