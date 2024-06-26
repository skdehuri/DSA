class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def recursive_insert(node, value):
    if not node:
        return Node(value)
    
    if value == node.data:
        return
    elif value < node.data:
        if node.left:
            recursive_insert(node.left, value)
        else:
            node.left = Node(value)
    else:
        if node.right:
            recursive_insert(node.right, value)
        else:
            node.right = Node(value)


def iterative_insert(node, value):
    while node:
        if value == node.data:
            return
        
        if value < node.data:
            if node.left:
                node = node.left
            else:
                node.left = Node(value)
                return
        else:
            if node.right:
                node = node.right
            else:
                node.right = Node(value)
                return
    
root_node = Node(50)

iterative_insert(root_node, 30)
iterative_insert(root_node, 60)

recursive_insert(root_node, 40)
recursive_insert(root_node, 55)

print(root_node.left.data)
print(root_node.right.data)

print(root_node.left.right.data)
print(root_node.right.left.data)