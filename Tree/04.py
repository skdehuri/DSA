class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return str(self.data)


def get_nodes_at_distance(node, k):
    if not node:
        return
    
    if k == 0:
        print(node, end=" ")
    else:
        get_nodes_at_distance(node.left, k - 1)
        get_nodes_at_distance(node.right, k - 1)
    


root_node = Node(10)
root_node.left = Node(20)
root_node.left.left = Node(15)

root_node.right = Node(30)
root_node.right.left = Node(40)
root_node.right.right = Node(80)
root_node.right.right.right = Node(50)

get_nodes_at_distance(root_node, 2)
