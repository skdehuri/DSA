class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def height(node):
    if not node:
        return 0
    
    left_height = height(node.left)
    right_height = height(node.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


def print_current_level_nodes(node, level):
    if not node:
        return
    
    if level == 0:
        print(node.data, end=" ")
    else:
        print_current_level_nodes(node.left, level - 1)
        print_current_level_nodes(node.right, level - 1)


################## NAIVE WAY #####################

def level_order_traversal_naive(node):
    h = height(node)

    for i in range(h):
        print_current_level_nodes(node, i)

################## USING QUEUE ####################

def level_order_traversal_queue(node):
    
    if not node:
        return
    
    queue = []

    queue.append(node)

    while len(queue) > 0:
        print(queue[0].data, end=" ")
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


root_node = Node(10)
root_node.left = Node(20)
root_node.left.left = Node(15)

root_node.right = Node(30)
root_node.right.left = Node(40)
root_node.right.right = Node(80)
root_node.right.right.right = Node(50)

level_order_traversal_naive(root_node)
print("\n")
level_order_traversal_queue(root_node)
