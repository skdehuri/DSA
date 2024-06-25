# Number of nodes in the longest path
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_size(node):
    if not node:
        return 0
    
    left_size = get_size(node.left)
    right_size = get_size(node.right)
    return left_size + right_size + 1



root_node = Node(10)
root_node.left = Node(20)
root_node.left.left = Node(15)

root_node.right = Node(30)
root_node.right.left = Node(40)
root_node.right.right = Node(80)
root_node.right.right.right = Node(50)

print(get_size(root_node))