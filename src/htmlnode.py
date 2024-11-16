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
        if self.children == None:
            return f"tag = {convert(self.tag)}\nvalue = {convert(self.value)}\nchildren = {convert(self.children)}\nprops = {convert(self.props)}"
        else:
            new_children = ", ".join(self.children)
            return f"tag = {convert(self.tag)}\nvalue = {convert(self.value)}\nchildren = {new_children}\nprops = {convert(self.props)}"


            
        
    
