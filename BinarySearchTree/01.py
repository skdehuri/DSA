class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f" {self.left if self.left else ''}-{self.data}-{self.right if self.right else ''} "

    def add_value(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_value(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add_value(data)
            else:
                self.right = Node(data)


root_node = Node(25)
root_node.add_value(20)
root_node.add_value(80)

root_node.add_value(30)
root_node.add_value(40)
root_node.add_value(2)
root_node.add_value(10)
root_node.add_value(9)
root_node.add_value(5)
root_node.add_value(70)

print(root_node)