class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_node(self, node):
        node.parent = self
        self.children.append(node)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent

        return level

    def __repr__(self):
        spaces = ' ' * self.get_level() * 4
        tree_str = f"{spaces if self.parent else ''}|--{self.data}"
        
        for child in self.children:
            tree_str += '\n' + str(child)

        return tree_str

root_node = Node("Vegetables")

greens = Node("Greens")
pulses = Node("Pulses")
roots = Node("Roots")
tubers = Node("Tubers")

root_node.add_node(greens)
root_node.add_node(pulses)
root_node.add_node(roots)
root_node.add_node(tubers)

greens.add_node(Node("Cabbage"))
greens.add_node(Node("Spinach"))

pulses.add_node(Node("Peas"))
pulses.add_node(Node("Beans"))

roots.add_node(Node("Carrots"))
roots.add_node(Node("Turnips"))

tubers.add_node(Node("Potatos"))
tubers.add_node(Node("Yams"))

print(root_node)
    
