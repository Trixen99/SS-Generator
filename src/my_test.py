from blocks import *



text = """# Heading 1

## Heading 2 `code` here

### Heading 3 ![image](https://static.wikia.nocookie.net/kevinsmith/images/9/93/Buddy_christ.jpg/revision/latest?cb=20081023201520)

#### Heading 4 **bold**

##### Heading 5 *italic*

###### Heading 6 [link](www.google.com)

####### Heading 7 **bold** and *italic*

paragraph part one, **bold** and *italic* parahraph part two [link](www.google.com) ![image](https://static.wikia.nocookie.net/kevinsmith/images/9/93/Buddy_christ.jpg/revision/latest?cb=20081023201520)

```some code here
[link](www.shouldnotconvert.com)
![image](www.shouldnotconvert.com)
```

* unordered_list part 1
- unordered_list **part** *2*
* unordered_list [part 3](www.part3.com)
* unordered_list ![part 4](https://static.wikia.nocookie.net/kevinsmith/images/9/93/Buddy_christ.jpg/revision/latest?cb=20081023201520)
- unordered_list `part` 5
- unordered_list part 6

1. ordered_list part 1
2. ordered_list **part** *2*
3. ordered_list [part 3](www.part3.com)
4. ordered_list ![part 4](https://static.wikia.nocookie.net/kevinsmith/images/9/93/Buddy_christ.jpg/revision/latest?cb=20081023201520)
5. ordered_list `part` 5
6. ordered_list part 6

> quote **bold**
> quote *italic*
> quote [link](www.google.com)
> quote ![Image](https://static.wikia.nocookie.net/kevinsmith/images/9/93/Buddy_christ.jpg/revision/latest?cb=20081023201520)
> quote `code`
"""

text = """> Here's a quote with a **bold** part
1. First item with *italic*
2. Second item with `code`"""

text = """> This is a quote
> with multiple lines

1. First item
2. Second item

Regular paragraph"""


node = markdown_to_html_node(text)
#print(node)
print(node.to_html())