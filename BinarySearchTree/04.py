class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.left if self.left else ''} {self.data} {self.right if self.right else ''}"

    
    def add_node(self, value):
        if value == self.data:
            return None
        
        if value < self.data:
            if self.left:
                self.left.add_node(value)
            else:
                self.left = Node(value)

        else:
            if self.right:
                self.right.add_node(value)
            else:
                self.right = Node(value)

    def delete_node(self, value):
        if not self.data:
            return
        
        if value < self.data:
            self.left = self.left.delete_node(value)
        elif value > self.data:
            self.right = self.right.delete_node(value)
        else:
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                temp_node = self.right

                while not temp_node.left:
                    temp_node = temp_node.left
                
                self.data = temp_node.data
                self.right = self.right.delete_node(temp_node.data)

                



root_node = Node(25)
root_node.add_node(20)
root_node.add_node(80)
root_node.add_node(30)
root_node.add_node(40)
root_node.add_node(2)
root_node.add_node(10)
root_node.add_node(9)
root_node.add_node(5)
root_node.add_node(70)

root_node.delete_node(20)
root_node.delete_node(25)

print(root_node)
