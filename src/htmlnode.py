class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        list = []
        for key in self.props:
            list.append(f' {key}="{self.props[key]}"')
        return "".join(list)


    def __repr__(self):
        convert = lambda input: f'"{input}"' if input != None else None
        dict_convert = lambda input: input if input != None else None
        if self.children == None:
            return f"tag = {convert(self.tag)}, value = {convert(self.value)}, children = {convert(self.children)}, props = {dict_convert(self.props)}"
        else:
            children_list = []
            for child in self.children:
                children_list.append(f"{str(child)}()")
            new_children = "".join(str(children_list)).replace("()", "\n")
            return f"tag = {convert(self.tag)}, value = {convert(self.value)}, \nchildren = {new_children},\nprops = {dict_convert(self.props)}"


            
        
    
