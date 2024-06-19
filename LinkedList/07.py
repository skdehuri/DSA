class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"[{self.value}|{'NODE' if self.next else 'NULL'}]"
    
class LinkedList:
    def __init__(self):
        self.head = None

    def add_values(self, values):

        def add(value):
            if not self.head:
                self.head = Node(value)
                return
            
            current_node = self.head

            while current_node.next:
                current_node = current_node.next
            
            current_node.next = Node(value)
        
        for value in values:
            add(value)
        
    def print(self):

        if not self.head:
            print("Linkedlist is empty")
            return
        
        current_node = self.head
        ll_str = ''

        while current_node:
            ll_str += str(current_node) + ' ----> '
            current_node = current_node.next
        
        print(ll_str)

    def rotate_right(self):
        
        if not self.head:
            print("Linkedlist is empty")
            return
        
        current_node = self.head
        prev_node = None

        while current_node.next:
            prev_node = current_node
            current_node = current_node.next

        prev_node.next = None
        current_node.next = self.head
        self.head = current_node


ll = LinkedList()
ll.add_values([1, 2, 3, 4, 5, 6, 7, 8])
ll.print()

ll.rotate_right()
ll.print()