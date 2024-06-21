class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self) -> str:
        return f" {str(self.left) if self.left else 'NULL'}-{self.data}-{str(self.right) if self.right else 'NULL'} "

    def add_node(self, node):
        if not self.left:
            self.left = node
        elif not self.right:
            self.right = node
        else:
            print('Binary Tree can have at most two nodes')

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.data)
            self.in_order_traversal(node.right)


root = Node(10)

node_20 = Node(20)
node_30 = Node(30)

root.add_node(node_20)
root.add_node(node_30)

node_20.add_node(Node(40))

node_50 = Node(50)
node_20.add_node(node_50)

node_50.add_node(Node(70))
node_50.add_node(Node(80))

node_30.right = Node(60)


print(root)
root.in_order_traversal(root)