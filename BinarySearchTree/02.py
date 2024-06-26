class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_data(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_data(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add_data(data)
            else:
                self.right = Node(data)


def search(node, value):
    if not node:
        return False
        
    if node.data == value:
        return True
    
    elif value < node.data:
        return search(node.left, value)

    elif value > node.data:
        return search(node.right, value)
        

root_node = Node(25)
root_node.add_data(20)
root_node.add_data(80)

root_node.add_data(30)
root_node.add_data(40)
root_node.add_data(2)
root_node.add_data(10)
root_node.add_data(9)
root_node.add_data(5)
root_node.add_data(70)

print(search(root_node, 9))



